#!/usr/bin/env python3
"""Read-only sprite containment audit and four-background contact sheets."""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageDraw


def audit(source, frames, edge_limit):
    results = []
    for name, rect in frames:
        x, y, w, h = rect
        if min(x, y) < 0 or min(w, h) < 1 or x+w > source.width or y+h > source.height:
            raise ValueError(f'{name}: frame outside sheet: {rect}')
        a = source.crop((x, y, x+w, y+h)).getchannel('A')
        strips = [(0, 0, w, 1), (0, h-1, w, h), (0, 0, 1, h), (w-1, 0, w, h)]
        edge = max(a.crop(r).getextrema()[1] for r in strips)
        bounds = a.point(lambda v: 255 if v >= 200 else 0).getbbox()
        status = 'fail' if edge > edge_limit else 'pass'
        results.append({'name': name, 'rect': rect, 'edgeAlphaMax': edge,
                        'opaqueBoundsLocal': bounds, 'empty': a.getbbox() is None,
                        'status': status})
    return results


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('sheet', type=Path)
    p.add_argument('--metadata', type=Path)
    p.add_argument('--cols', type=int, default=1)
    p.add_argument('--rows', type=int, default=1)
    p.add_argument('--edge-alpha-max', type=int, default=8)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    if not 0 <= args.edge_alpha_max <= 255:
        p.error('--edge-alpha-max must be 0..255')
    original = Image.open(args.sheet)
    if 'A' not in original.getbands() and 'transparency' not in original.info:
        p.error('Source has no alpha; this audit is for transparent sprites, not ground textures')
    source = original.convert('RGBA')
    if args.metadata:
        data = json.loads(args.metadata.read_text())['frames']
        entries = list(data.items()) if isinstance(data, dict) else [(v.get('filename', str(i)), v) for i, v in enumerate(data)]
        frames = [(n, tuple(v['frame'][k] for k in ('x', 'y', 'w', 'h'))) for n, v in entries]
    else:
        if args.cols < 1 or args.rows < 1 or source.width % args.cols or source.height % args.rows:
            p.error('Positive grid must divide image dimensions exactly')
        w, h = source.width // args.cols, source.height // args.rows
        frames = [(str(i), (i % args.cols*w, i // args.cols*h, w, h)) for i in range(args.cols*args.rows)]
    if not frames:
        p.error('No frames')
    report = audit(source, frames, args.edge_alpha_max)
    args.out.mkdir(parents=True, exist_ok=True)
    payload = {'source': str(args.sheet.resolve()), 'size': source.size,
               'sourceBytes': args.sheet.stat().st_size,
               'decodedRGBABytes': source.width*source.height*4,
               'edgeAlphaLimit': args.edge_alpha_max, 'frames': report}
    (args.out / 'report.json').write_text(json.dumps(payload, indent=2))
    columns = min(4, len(frames))
    width = 256
    for label, background in [('dark', '#0d1725'), ('white', '#ffffff'), ('gray', '#777777'), ('magenta', '#ff00ff')]:
        contact = Image.new('RGBA', (columns*width, ((len(frames)+columns-1)//columns)*280), background)
        draw = ImageDraw.Draw(contact)
        for i, (name, (x, y, w, h)) in enumerate(frames):
            tile = source.crop((x, y, x+w, y+h))
            tile.thumbnail((240, 240), Image.Resampling.LANCZOS)
            left, top = i % columns*width, i//columns*280
            contact.alpha_composite(tile, (left+(width-tile.width)//2, top+(240-tile.height)//2+8))
            draw.text((left+8, top+252), name[:36], fill='#222222' if label=='white' else '#ffffff')
        contact.convert('RGB').save(args.out / f'contact-{label}.png')
    failures = sum(r['status'] == 'fail' or r['empty'] for r in report)
    print(f'{len(report)} frames, {failures} containment/empty failures; {args.out / "report.json"}')
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
