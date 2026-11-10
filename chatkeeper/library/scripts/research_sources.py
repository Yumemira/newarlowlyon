"""Fetch public design sources; record evidence, not a claim of human review."""
import concurrent.futures as cf
import hashlib, html, json, re, time, urllib.request, urllib.parse
from html.parser import HTMLParser
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self):
  super().__init__();self.skip=0;self.title=False;self.titles=[];self.parts=[];self.links=[];self.in_p=False;self.p=[];self.paragraphs=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag in ('script','style','svg','noscript'): self.skip+=1
  if tag=='p':self.in_p=True;self.p=[]
  if tag=='title':self.title=True
  if tag=='a' and d.get('href'):self.links.append(d['href'])
 def handle_endtag(self,tag):
  if tag in ('script','style','svg','noscript') and self.skip:self.skip-=1
  if tag=='p' and self.in_p:
   self.paragraphs.append(' '.join(self.p));self.in_p=False
  if tag=='title':self.title=False
 def handle_data(self,data):
  if self.title:self.titles.append(data)
  if not self.skip and data.strip():
   self.parts.append(data.strip())
   if self.in_p:self.p.append(data.strip())
def fetch(item):
 url=item['url'];out={**item,'checked':'2026-10-15','status':'unavailable'}
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (compatible; DesignResearch/1.0)'})
  with urllib.request.urlopen(req,timeout=18) as r:
   out['http_status']=r.status;out['final_url']=r.url;typ=r.headers.get('Content-Type','');raw=r.read(2500000)
  if 'html' not in typ:out['reason']='non-html';return out
  page=Page();page.feed(raw.decode('utf-8','replace'))
  text=' '.join(page.parts);out['page_title']=' '.join(page.titles).strip();out['text_chars']=len(text)
  if len(text)<900 or re.search(r'^(Just a moment|Access Denied|Blocked)',out['page_title'],re.I):out['reason']='insufficient content';return out
  body=' '.join(x for x in page.paragraphs if len(x)>70) or text
  sentences=re.split(r'(?<=[.!?])\s+',body)
  keys=r'animat|motion|transition|navigation|typograph|interact|color|colour|gesture|layout|onboard|accessib|microinteract|usability|design system'
  relevant=[s for s in sentences if re.search(keys,s,re.I) and 40<len(s)<1800]
  # Store at most 25 source words, not full articles.
  out['evidence']=' '.join(' '.join(relevant[:6]).split()[:25])
  out['content_hash']=hashlib.sha256(text.encode()).hexdigest()
  out['status']='fetched' if out['evidence'] else 'irrelevant'
  out['links']=[urllib.parse.urljoin(out.get('final_url',url),x).split('#')[0] for x in page.links]
  out['topics']=[k for k in ['animation','motion','navigation','typography','color','interaction','onboarding','accessibility','layout','gesture'] if k in text.lower()]
 except Exception as e:out['reason']=str(e)[:150]
 return out
if __name__=='__main__':
 items=json.loads((ROOT/'research/candidates.json').read_text())
 hubs=['https://tympanus.net/codrops/category/tutorials/','https://www.smashingmagazine.com/category/animation/','https://www.smashingmagazine.com/category/user-experience/','https://www.smashingmagazine.com/category/design/','https://www.joshwcomeau.com/','https://ishadeed.com/articles/','https://www.sarasoueidan.com/blog/','https://emilkowal.ski/','https://www.nngroup.com/articles/','https://blog.maximeheckel.com/','https://www.nngroup.com/topic/interaction-design/']
 seen={x['url'] for x in items}
 for url in hubs:
  if url not in seen:items.append({'url':url,'title':'discovery hub'});seen.add(url)
 results=[]
 with cf.ThreadPoolExecutor(max_workers=10) as pool:
  for n,r in enumerate(pool.map(fetch,items),1):
   results.append(r)
   if n%40==0: print('fetched',n,flush=True)
 (ROOT/'research/fetch-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
 print('results',len(results),'readable',sum(x['status']=='fetched' for x in results),flush=True)
 # Discover concrete articles, avoiding tag/search indexes and irrelevant sites.
 more=[]
 for r in results:
  host=urllib.parse.urlsplit(r['url']).netloc
  if host not in ['tympanus.net','www.smashingmagazine.com','www.joshwcomeau.com','ishadeed.com','www.sarasoueidan.com','emilkowal.ski','www.nngroup.com','blog.maximeheckel.com']:continue
  added=0
  for u in r.get('links',[]):
   if urllib.parse.urlsplit(u).netloc!=host or u in seen:continue
   if not re.search(r'animat|motion|transition|interact|navigation|typograph|color|colour|layout|onboard|accessib|design|gesture|scroll|hover|menu|grid|card',u,re.I):continue
   if re.search(r'/tag/|/category/|/author/|/page/|\.(png|jpg|gif|zip|svg)|#|\?',u):continue
   seen.add(u);more.append({'url':u,'title':u.rsplit('/',2)[-2],'discovered_from':r['url']});added+=1
   if added>=20:break
 print('additional candidates',len(more),flush=True)
 with cf.ThreadPoolExecutor(max_workers=8) as pool:
  for n,r in enumerate(pool.map(fetch,more[:450]),1):
   results.append(r)
   if n%40==0: print('additional fetched',n,flush=True)
 (ROOT/'research/fetch-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
 print('FINAL',len(results),'readable',sum(x['status']=='fetched' for x in results),flush=True)
