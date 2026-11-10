"""Optional description of profile similarities; no diversity score or acceptance threshold."""
import argparse,itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def compare(a,b):
 keys=sorted((set(a)|set(b))-{'palette','motion_ids'})
 return {'shared':{k:a[k] for k in keys if k in a and k in b and a[k]==b[k]},'different':{k:{'a':a.get(k),'b':b.get(k)} for k in keys if k in a and k in b and a[k]!=b[k]},'unspecified':[k for k in keys if k not in a or k not in b]}
def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('proposals',type=Path);parser.add_argument('--history',type=Path);args=parser.parse_args()
 proposed=json.loads(args.proposals.read_text())
 history_path = args.history or ROOT / 'usage.json'
 try:
  history = json.loads(history_path.read_text())
 except FileNotFoundError:
  if args.history is not None:
   raise
  history = []
 pairs=list(itertools.combinations(proposed,2))+[(a,b) for a in proposed for b in history if a['project_slug']!=b['project_slug']]
 print(json.dumps({'comparisons':[{'a':a['project_slug'],'b':b['project_slug'],**compare(a.get('profile',{}),b.get('profile',{}))} for a,b in pairs],'note':'Optional observations only. No required axes, score, threshold, or automatic design rejection.'},ensure_ascii=False,indent=2))
 return 0
if __name__=='__main__':raise SystemExit(main())
