"""One shared-scale board. Usage: python3 board.py /absolute/output-folder"""
import json
from pathlib import Path
import sys
from PIL import Image, ImageDraw, ImageFont

if len(sys.argv) != 2 or sys.argv[1] in ('--help', '-h'):
    print(__doc__)
    raise SystemExit(0 if len(sys.argv) == 2 else 2)

root = Path(sys.argv[1]).resolve()
report = json.loads((root/'report.json').read_text())
rows = report['buildings']
columns = len(report['yaws'])
cell, label = 256, 30
board = Image.new('RGB',(columns*cell,len(rows)*(cell+label)), '#323a45')
draw = ImageDraw.Draw(board)
font = ImageFont.load_default(size=14)
for row, building in enumerate(rows):
    for column, frame in enumerate(building['frames']):
        # Resize complete equal-sized canvases by the same factor; no per-view fit.
        im = Image.open(root/frame['image']).convert('RGBA')
        im.thumbnail((cell,cell),Image.Resampling.LANCZOS)
        x,y = column*cell,row*(cell+label)
        board.paste(im,(x+(cell-im.width)//2,y+label+(cell-im.height)//2),im)
        draw.text((x+8,y+7),building['id']+' / '+frame['view'],font=font,fill='white')
board.save(root/'board.png')
print(str(root/'board.png'))
