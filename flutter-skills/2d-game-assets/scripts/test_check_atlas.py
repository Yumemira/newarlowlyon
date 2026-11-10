"""Behavior tests with disposable PNG/JSON fixtures; no third-party dependencies."""
import copy
import json
from pathlib import Path
import struct
import subprocess
import sys
import tempfile
import unittest
import zlib

from check_atlas import png_size, validate


def chunk(kind, payload):
    return struct.pack('>I', len(payload)) + kind + payload + struct.pack('>I', zlib.crc32(kind + payload) & 0xffffffff)


def png(width=16, height=16):
    raw = (b'\x00' + b'\x00\x00\x00\xff' * width) * height
    return (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0))
            + chunk(b'IDAT', zlib.compress(raw)) + chunk(b'IEND', b''))


def atlas():
    return {'meta': {'image': 'sheet.png', 'size': {'w': 16, 'h': 16},
                     'frameTags': [{'name': 'idle', 'from': 0, 'to': 0}]},
            'frames': {'idle': {'frame': {'x': 0, 'y': 0, 'w': 8, 'h': 8}, 'duration': 100}}}


class AtlasTests(unittest.TestCase):
    def test_valid_hash_and_array(self):
        data = atlas()
        self.assertEqual(validate(data, 16, 16)[0], [])
        self.assertEqual(validate(data, 16, 16)[2], 1)
        record = data['frames']['idle']
        data['frames'] = [dict(record, filename='idle')]
        self.assertEqual(validate(data, 16, 16)[0], [])
        self.assertEqual(validate(data, 16, 16)[2], 1)

    def test_out_of_bounds(self):
        data = atlas(); data['frames']['idle']['frame']['x'] = 12
        self.assertTrue(any('exceeds PNG' in e for e in validate(data, 16, 16)[0]))

    def test_boolean_coordinates_rejected(self):
        data = atlas(); data['frames']['idle']['frame']['x'] = True
        self.assertTrue(validate(data, 16, 16)[0])

    def test_negative_and_zero_dimensions(self):
        for key, value in [('x', -1), ('w', 0), ('h', -2)]:
            data = atlas(); data['frames']['idle']['frame'][key] = value
            self.assertTrue(validate(data, 16, 16)[0])

    def test_bad_durations(self):
        for value in [0, -1, True, '100', float('inf')]:
            data = atlas(); data['frames']['idle']['duration'] = value
            self.assertTrue(any('duration' in e for e in validate(data, 16, 16)[0]))

    def test_duplicate_array_names(self):
        data = atlas(); record = dict(data['frames']['idle'], filename='idle')
        data['frames'] = [record, copy.deepcopy(record)]
        self.assertTrue(any('duplicate frame' in e for e in validate(data, 16, 16)[0]))

    def test_tag_range(self):
        data = atlas(); data['meta']['frameTags'][0]['to'] = 1
        self.assertTrue(any('range' in e for e in validate(data, 16, 16)[0]))

    def test_trimmed_geometry(self):
        data = atlas(); record = data['frames']['idle']; record['trimmed'] = True
        self.assertTrue(validate(data, 16, 16)[0])
        record.update(sourceSize={'w': 12, 'h': 12}, spriteSourceSize={'x': 2, 'y': 2, 'w': 8, 'h': 8})
        self.assertFalse(validate(data, 16, 16)[0])
        record['spriteSourceSize']['x'] = 8
        self.assertTrue(any('exceeds original' in e for e in validate(data, 16, 16)[0]))

    def test_rotated_dimensions_and_warning(self):
        data = atlas(); record = data['frames']['idle']; record['frame']['w'] = 4
        record.update(rotated=True, sourceSize={'w': 8, 'h': 4}, spriteSourceSize={'x': 0, 'y': 0, 'w': 8, 'h': 4})
        errors, warnings, _ = validate(data, 16, 16)
        self.assertFalse(errors); self.assertTrue(warnings)

    def test_empty_or_malformed(self):
        for frames in [[], {}, None, [None]]:
            data = atlas(); data['frames'] = frames
            self.assertTrue(validate(data, 16, 16)[0])

    def test_meta_size_mismatch(self):
        data = atlas(); data['meta']['size']['w'] = 32
        self.assertTrue(validate(data, 16, 16)[0])

    def test_untrimmed_source_size_mismatch(self):
        data = atlas(); record = data['frames']['idle']
        record.update(trimmed=False, sourceSize={'w': 4, 'h': 4})
        self.assertTrue(any('untrimmed' in e for e in validate(data, 16, 16)[0]))

    def test_untrimmed_offset_rejected(self):
        data = atlas(); record = data['frames']['idle']
        record.update(trimmed=False, sourceSize={'w': 16, 'h': 16},
                      spriteSourceSize={'x': 2, 'y': 2, 'w': 8, 'h': 8})
        self.assertTrue(any('untrimmed' in e for e in validate(data, 16, 16)[0]))

    def test_valid_untrimmed_rotated(self):
        data = atlas(); record = data['frames']['idle']; record['frame']['w'] = 4
        record.update(trimmed=False, rotated=True, sourceSize={'w': 8, 'h': 4},
                      spriteSourceSize={'x': 0, 'y': 0, 'w': 8, 'h': 4})
        self.assertFalse(validate(data, 16, 16)[0])

    def test_multipage_and_scale_are_warnings(self):
        data = atlas(); data['meta'].update(related_multi_packs=['other.json'], scale='0.5')
        errors, warnings, _ = validate(data, 16, 16)
        self.assertFalse(errors)
        self.assertTrue(any('multipage' in w for w in warnings))
        self.assertTrue(any('scale' in w for w in warnings))

    def test_hash_tag_order_warning(self):
        self.assertTrue(any('order' in w for w in validate(atlas(), 16, 16)[1]))

    def test_invalid_trim_flag_still_rejected(self):
        data = atlas(); data['frames']['idle']['trimmed'] = 'false'
        self.assertTrue(any('boolean' in e for e in validate(data, 16, 16)[0]))

    def cli(self, text=None, image=None, extra=()):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); source = root/'atlas.json'; texture = root/'sheet.png'
            source.write_text(text if text is not None else json.dumps(atlas()))
            texture.write_bytes(png() if image is None else image)
            before = (source.read_bytes(), texture.read_bytes())
            result = subprocess.run([sys.executable, str(Path(__file__).with_name('check_atlas.py')), str(source), *extra], capture_output=True, text=True)
            self.assertEqual(before, (source.read_bytes(), texture.read_bytes()))
            return result.returncode, json.loads(result.stdout)

    def test_cli_valid_and_read_only(self):
        code, report = self.cli(); self.assertEqual(code, 0); self.assertTrue(report['valid'])

    def test_cli_invalid_json(self):
        self.assertEqual(self.cli('{oops')[0], 2)

    def test_cli_duplicate_keys(self):
        code, report = self.cli('{"frames":{},"frames":{}}')
        self.assertEqual(code, 2); self.assertIn('Duplicate', report['errors'][0])

    def test_cli_invalid_png(self):
        self.assertEqual(self.cli(image=b'not png')[0], 2)

    def test_cli_missing_image(self):
        data = atlas(); data['meta']['image'] = 'missing.png'
        self.assertEqual(self.cli(json.dumps(data))[0], 2)

    def test_cli_validation_exit(self):
        data = atlas(); data['frames']['idle']['frame']['w'] = 100
        self.assertEqual(self.cli(json.dumps(data))[0], 1)

    def test_png_crc(self):
        bad = bytearray(png()); bad[29] ^= 1
        self.assertEqual(self.cli(image=bytes(bad))[0], 2)

    def test_reused_rectangles_valid(self):
        data = atlas(); data['frames']['other'] = copy.deepcopy(data['frames']['idle'])
        self.assertFalse(validate(data, 16, 16)[0])


if __name__ == '__main__':
    unittest.main()
