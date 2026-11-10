"""Prepare ONE three-view test asset and material-only style reference.
python3 packet.py --guides DIR --style IMAGE --patches JSON --out DIR
guides must contain facade.png, side.png, diagonal.png on identical canvases.
patches JSON: {"label":[left,top,right,bottom],...}, normalized 0..1.
No generated artwork is modified. This prepares reference inputs only.
"""
import argparse
import json
from pathlib import Path

from PIL import Image


def main():
    parser=argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--guides',type=Path,required=True)
    parser.add_argument('--style',type=Path,required=True)
    parser.add_argument('--patches',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    a=parser.parse_args()
    names=('facade','side','diagonal')
    images=[Image.open(a.guides/(name+'.png')).convert('RGBA') for name in names]
    assert len({im.size for im in images})==1, 'Guide canvases must match'
    bounds=[im.getchannel('A').getbbox() for im in images]
    assert all(bounds), 'Empty guide'
    w,h=images[0].size
    crop=(max(0,min(b[0] for b in bounds)-20),max(0,min(b[1] for b in bounds)-20),
          min(w,max(b[2] for b in bounds)+20),min(h,max(b[3] for b in bounds)+20))
    # Same crop and scale for all views, retaining their true relative sizes.
    factor=min(464/(crop[2]-crop[0]),640/(crop[3]-crop[1]))
    size=(round((crop[2]-crop[0])*factor),round((crop[3]-crop[1])*factor))
    board=Image.new('RGBA',(1536,768),(0,0,0,0))
    for i,im in enumerate(images):
        tile=im.crop(crop).resize(size,Image.Resampling.LANCZOS)
        board.alpha_composite(tile,(i*512+(512-size[0])//2,(768-size[1])//2))
    style=Image.open(a.style).convert('RGBA')
    boxes=json.loads(a.patches.read_text())
    assert 1 <= len(boxes) <= 6
    swatches=Image.new('RGB',(512,256*((len(boxes)+1)//2)), '#c8c4bd')
    records=[]
    for i,(label,box) in enumerate(boxes.items()):
        left,top,right,bottom=box
        assert 0<=left<right<=1 and 0<=top<bottom<=1
        rect=(round(left*style.width),round(top*style.height),round(right*style.width),round(bottom*style.height))
        tile=style.crop(rect)
        tile.thumbnail((240,240),Image.Resampling.LANCZOS)
        x=(i%2)*256+(256-tile.width)//2
        y=(i//2)*256+(256-tile.height)//2
        swatches.paste(tile,(x,y),tile)
        records.append({'label':label,'normalized_crop':box,'source_pixel_crop':rect})
    a.out.mkdir(parents=True,exist_ok=True)
    board.save(a.out/'geometry-three-views.png')
    swatches.save(a.out/'style-surfaces.png')
    manifest={'mode':'single_house_turnaround_experiment','geometry_input':str((a.out/'geometry-three-views.png').resolve()),
              'style_input':str((a.out/'style-surfaces.png').resolve()),
              'style_source':str(a.style.resolve()),'style_patches':records,
              'view_order':list(names),'guide_canvas':list(images[0].size),'common_crop':crop,'common_scale':factor,
              'output_asset':'One three-view turnaround PNG; no claim that panels are separate ready-to-use assets',
              'initial_imagegen_calls':1,'automatic_retries':0,
              'limits':'Joint views/material crops are a hypothesis, not validated geometry conditioning.'}
    (a.out/'packet.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'view_count':3,'style_patches':len(records),'imagegen_calls_planned':1}))


if __name__=='__main__':main()
