"""Read-only review boards with ONE resize factor for all source canvases.

Manifest: {"root":"/abs/project", "families":[{"label":"...",
"views":{"source":"relative.png","horizontal":"...","vertical":"..."}}]}.
Pillow required. Missing views are shown, not silently substituted.
This tool measures files and presents evidence; it cannot approve a camera.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest')
    parser.add_argument('--out',required=True)
    parser.add_argument('--factor',type=float,default=.22)
    args = parser.parse_args()
    if not 0 < args.factor <= 1:
        parser.error('factor must be >0 and <=1')
    manifest = json.loads(Path(args.manifest).read_text())
    root = Path(manifest['root']).resolve()
    out = Path(args.out).resolve()
    out.mkdir(parents=True,exist_ok=True)
    entries = []
    views = ('source','horizontal','vertical')
    maxw,maxh = 1,1
    for family in manifest['families']:
        row = {'label':family['label'],'views':{}}
        for view in views:
            rel = family['views'].get(view)
            if not rel:
                row['views'][view] = {'status':'missing'}
                continue
            p = (root/rel).resolve()
            if not p.is_relative_to(root):
                raise ValueError('Manifest path must remain within root')
            if not p.exists():
                row['views'][view] = {'status':'missing','path':str(p)}
                continue
            with Image.open(p) as im:
                rgba = im.convert('RGBA')
                alpha = rgba.getchannel('A')
                hist = alpha.histogram()
                n = im.width*im.height
                bbox = alpha.point(lambda a:255 if a>=16 else 0).getbbox()
                row['views'][view] = {
                    'status':'review-required','path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                    'size':list(im.size),'mode':im.mode,'alpha_extrema':list(alpha.getextrema()),
                    'transparent_fraction':sum(hist[:16])/n,
                    'soft_alpha_fraction':sum(hist[16:240])/n,'alpha_bbox_threshold16':bbox,
                    'note':'Alpha presence does not prove a clean cutout; camera/identity require visual review'}
                maxw = max(maxw,math.ceil(im.width*args.factor))
                maxh = max(maxh,math.ceil(im.height*args.factor))
        entries.append(row)
    fontfile = Path('/System/Library/Fonts/Helvetica.ttc')
    font = ImageFont.truetype(str(fontfile),17) if fontfile.exists() else ImageFont.load_default()
    cw,ch = maxw+24,maxh+85
    for page,start in enumerate(range(0,len(entries),3),1):
        subset = entries[start:start+3]
        board = Image.new('RGB',(cw*3,ch*len(subset)+55),(40,47,54))
        draw = ImageDraw.Draw(board)
        draw.text((12,8),f'Common image factor {args.factor}; world scale UNVERIFIED',font=font,fill='white')
        for row_i,row in enumerate(subset):
            for col,view in enumerate(views):
                x,y = col*cw,55+row_i*ch
                draw.text((x+10,y+3),row['label']+' / '+view,font=font,fill='white')
                data = row['views'][view]
                if data['status']=='missing':
                    draw.text((x+10,y+45),'MISSING',font=font,fill='orange')
                    continue
                tile = Image.new('RGBA',(maxw,maxh))
                td = ImageDraw.Draw(tile)
                for xx in range(0,maxw,16):
                    for yy in range(0,maxh,16):
                        c = 124 if (xx//16+yy//16)%2 else 167
                        td.rectangle((xx,yy,xx+15,yy+15),fill=(c,c,c,255))
                with Image.open(data['path']) as im:
                    im = im.convert('RGBA').resize((round(im.width*args.factor),round(im.height*args.factor)),Image.Resampling.LANCZOS)
                    tile.alpha_composite(im,((maxw-im.width)//2,maxh-im.height))
                board.paste(tile.convert('RGB'),(x+12,y+30))
                draw.text((x+12,y+maxh+35),str(data['size'])+' alpha '+str(data['alpha_extrema']),font=font,fill='white')
        board.save(out/f'review-{page}.png')
    (out/'report.json').write_text(json.dumps({'status':'review-required','factor':args.factor,
        'world_scale_verified':False,'families':entries},ensure_ascii=False,indent=2))
    print(f'{len(entries)} families; {len(range(0,len(entries),3))} boards; camera and identity need visual review')


if __name__ == '__main__':
    main()
