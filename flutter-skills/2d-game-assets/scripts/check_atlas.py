#!/usr/bin/env python3
"""Read-only validation of JSON hash/array sprite frames referencing a PNG.

Checks metadata geometry, not decoded pixels or compatibility with a game loader.
Exit 0: valid metadata, 1: validation errors, 2: unreadable/invalid input.
"""
import argparse
import json
import math
from pathlib import Path
import struct
import sys
import zlib


class InputError(ValueError):
    """Input cannot be interpreted safely as the supported format."""


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise InputError(f'Duplicate JSON key: {key}')
        result[key] = value
    return result


def reject_constant(value):
    raise InputError(f'Non-finite JSON value: {value}')


def png_size(path):
    with path.open('rb') as stream:
        header = stream.read(33)
    if len(header) != 33 or header[:8] != b'\x89PNG\r\n\x1a\n':
        raise InputError(f'{path}: missing PNG signature/IHDR')
    if header[8:16] != b'\x00\x00\x00\rIHDR':
        raise InputError(f'{path}: invalid IHDR chunk')
    if zlib.crc32(header[12:29]) & 0xffffffff != struct.unpack('>I', header[29:33])[0]:
        raise InputError(f'{path}: invalid IHDR checksum')
    width, height = struct.unpack('>II', header[16:24])
    if not (0 < width < 2**31 and 0 < height < 2**31):
        raise InputError(f'{path}: invalid PNG dimensions')
    return width, height


def integer(value):
    return isinstance(value, int) and not isinstance(value, bool)


def rect(value):
    return (isinstance(value, dict)
            and all(integer(value.get(k)) for k in ('x', 'y', 'w', 'h'))
            and value['x'] >= 0 and value['y'] >= 0
            and value['w'] > 0 and value['h'] > 0)


def size(value):
    return (isinstance(value, dict)
            and all(integer(value.get(k)) and value[k] > 0 for k in ('w', 'h')))


def validate(data, width, height):
    errors, warnings = [], []
    if not isinstance(data, dict):
        return ['Root must be a JSON object'], [], 0
    meta = data.get('meta', {})
    if not isinstance(meta, dict):
        errors.append('meta must be an object')
        meta = {}
    if 'size' in meta and (not size(meta['size']) or
                           (meta['size']['w'], meta['size']['h']) != (width, height)):
        errors.append('meta.size does not match PNG dimensions')
    if meta.get('related_multi_packs'):
        warnings.append('multipage atlas: only this image is checked; verify other pages and loader support')
    if 'scale' in meta and str(meta['scale']) not in ('1', '1.0'):
        warnings.append('meta.scale is non-unit or nonstandard; verify logical size conversion in the loader')
    frames = data.get('frames')
    if isinstance(frames, dict):
        entries = list(frames.items())
        if meta.get('frameTags'):
            warnings.append('indexed tags on hash frames: preserve exporter order; do not alphabetically sort names')
    elif isinstance(frames, list):
        entries = [(f.get('filename') if isinstance(f, dict) else None, f) for f in frames]
    else:
        return errors + ['frames must be a hash object or an array'], warnings, 0
    if not entries:
        errors.append('frames must not be empty')
    names = set()
    for index, (name, record) in enumerate(entries):
        label = f'frame[{index}] ({name!r})'
        if not isinstance(name, str) or not name.strip():
            errors.append(f'{label}: nonempty frame name required')
        elif name in names:
            errors.append(f'{label}: duplicate frame name')
        else:
            names.add(name)
        if not isinstance(record, dict):
            errors.append(f'{label}: record must be an object')
            continue
        frame = record.get('frame')
        if not rect(frame):
            errors.append(f'{label}: frame needs integer x/y >= 0 and w/h > 0')
            continue
        if frame['x'] + frame['w'] > width or frame['y'] + frame['h'] > height:
            errors.append(f'{label}: rectangle {frame} exceeds PNG {width}x{height}')
        for flag in ('rotated', 'trimmed'):
            if flag in record and not isinstance(record[flag], bool):
                errors.append(f'{label}: {flag} must be boolean')
        rotated = record.get('rotated') is True
        if rotated:
            warnings.append(f'{label}: packed rotation requires compatible loader handling')
        if 'duration' in record:
            duration = record['duration']
            if (isinstance(duration, bool) or not isinstance(duration, (int, float))
                    or not math.isfinite(duration) or duration <= 0):
                errors.append(f'{label}: duration must be a finite positive number')
        source = record.get('sourceSize')
        sprite = record.get('spriteSourceSize')
        if record.get('trimmed') is True and (source is None or sprite is None):
            errors.append(f'{label}: trimmed frame needs sourceSize and spriteSourceSize')
        if 'sourceSize' in record and not size(source):
            errors.append(f'{label}: invalid sourceSize')
        if 'spriteSourceSize' in record:
            if not rect(sprite):
                errors.append(f'{label}: invalid spriteSourceSize')
            else:
                logical = (frame['h'], frame['w']) if rotated else (frame['w'], frame['h'])
                if (sprite['w'], sprite['h']) != logical:
                    errors.append(f'{label}: trim rectangle size disagrees with packed frame')
                if size(source) and (sprite['x'] + sprite['w'] > source['w'] or
                                     sprite['y'] + sprite['h'] > source['h']):
                    errors.append(f'{label}: trim rectangle exceeds original sourceSize')
        if record.get('trimmed') is False:
            logical = (frame['h'], frame['w']) if rotated else (frame['w'], frame['h'])
            if size(source) and (source['w'], source['h']) != logical:
                errors.append(f'{label}: untrimmed sourceSize must match logical frame dimensions')
            if rect(sprite) and (sprite['x'] != 0 or sprite['y'] != 0):
                errors.append(f'{label}: untrimmed spriteSourceSize must have zero offset')
    tags = meta.get('frameTags', [])
    if not isinstance(tags, list):
        errors.append('meta.frameTags must be an array')
    else:
        tag_names = set()
        for index, tag in enumerate(tags):
            label = f'frameTags[{index}]'
            if not isinstance(tag, dict):
                errors.append(f'{label}: tag must be an object')
                continue
            name = tag.get('name')
            if not isinstance(name, str) or not name.strip():
                errors.append(f'{label}: nonempty name required')
            elif name in tag_names:
                errors.append(f'{label}: duplicate tag name {name!r}')
            else:
                tag_names.add(name)
            start, end = tag.get('from'), tag.get('to')
            if not (integer(start) and integer(end) and 0 <= start <= end < len(entries)):
                errors.append(f'{label}: range must be within 0..{len(entries)-1}')
    return errors, warnings, len(entries)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('atlas', type=Path, help='Aseprite/TexturePacker JSON hash or array')
    parser.add_argument('--image', type=Path, help='Override meta.image (relative to current directory)')
    args = parser.parse_args(argv)
    report = {'atlas': str(args.atlas.resolve()), 'scope': 'PNG header and JSON metadata only'}
    try:
        data = json.loads(args.atlas.read_text(encoding='utf-8'),
                          object_pairs_hook=unique_object, parse_constant=reject_constant)
        if not isinstance(data, dict):
            raise InputError('Root must be a JSON object')
        image = args.image
        if image is None:
            meta = data.get('meta')
            name = meta.get('image') if isinstance(meta, dict) else None
            if not isinstance(name, str) or not name.strip():
                raise InputError('Provide meta.image or --image')
            image = args.atlas.parent / name
        width, height = png_size(image)
        errors, warnings, count = validate(data, width, height)
        report.update(image=str(image.resolve()), width=width, height=height,
                      frames=count, errors=errors, warnings=warnings)
        code = 1 if errors else 0
    except (OSError, UnicodeError, ValueError, OverflowError) as exc:
        report.update(errors=[str(exc)], warnings=[])
        code = 2
    report['valid'] = code == 0
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return code


if __name__ == '__main__':
    sys.exit(main())
