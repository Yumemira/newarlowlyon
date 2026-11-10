"""Diagnostic views only; never scores art. Pillow required.

Input: {"root":"/absolute/project", "items":[{"label":"...","path":"relative.png"}]}.
Each asset is independently fitted into probe boxes. This is NOT world-scale proof.
"""
import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest')
    parser.add_argument('--out',required=True)
    args = parser.parse_args()
    data = json.loads(Path(args.manifest).read_text())
    root = Path(data['root']).resolve()
    out = Path(args.out).resolve()
    out.mkdir(parents=True,exist_ok=True)
    fontfile = Path('/System/Library/Fonts/Helvetica.ttc')
    font = ImageFont.truetype(str(fontfile),16) if fontfile.exists() else ImageFont.load_default()
    modes = [('color256',256),('color128',128),('color64',64),('gray128',128),('silhouette128',128)]
    positions = [0,280,440,540,700]
    report = {'status':'human-review-required','world_scale_verified':False,
              'note':'Independently fitted exploratory probes; silhouette uses alpha >=16. No material/camera score.',
              'items':[]}
    for start in range(0,len(data['items']),3):
        subset = data['items'][start:start+3]
        board = Image.new('RGB',(860,60+len(subset)*310),(58,66,72))
        draw = ImageDraw.Draw(board)
        draw.text((8,6),'Exploratory sizes; not confirmed gameplay scale',font=font,fill='white')
        for pos,(mode,_) in zip(positions,modes):
            draw.text((pos+8,30),mode,font=font,fill='white')
        for row,item in enumerate(subset):
            p = (root/item['path']).resolve()
            if not p.is_relative_to(root):
                raise ValueError('Image path must remain inside root')
            with Image.open(p) as original:
                im = original.convert('RGBA')
            alpha = im.getchannel('A')
            bbox = alpha.point(lambda a:255 if a>=16 else 0).getbbox()
            if bbox is None:
                raise ValueError('No visible subject: '+str(p))
            cropped = im.crop(bbox)
            y = 60+row*310
            draw.text((8,y+5),item['label'],font=font,fill='white')
            for pos,(mode,size) in zip(positions,modes):
                sample = cropped.copy()
                if mode.startswith('gray'):
                    sample = ImageOps.grayscale(sample).convert('RGBA')
                    sample.putalpha(cropped.getchannel('A'))
                elif mode.startswith('silhouette'):
                    sample = Image.new('RGBA',cropped.size,(22,24,27,255))
                    sample.putalpha(cropped.getchannel('A').point(lambda a:255 if a>=16 else 0))
                sample.thumbnail((size,size),Image.Resampling.LANCZOS)
                box = Image.new('RGBA',(size,size),(171,179,181,255))
                box.alpha_composite(sample,((size-sample.width)//2,(size-sample.height)//2))
                board.paste(box.convert('RGB'),(pos+8,y+30))
                sample.save(out/f'asset-{start+row}-{mode}.png')
            report['items'].append({'label':item['label'],'path':str(p),
                'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'alpha_bbox16':bbox,
                'crop_size':list(cropped.size)})
        board.save(out/f'probes-{start//3+1}.png')
    (out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(f'{len(report["items"])} assets, five diagnostic views each; no automatic art verdict')


if __name__ == '__main__':
    main()
