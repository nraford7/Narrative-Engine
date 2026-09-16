from pathlib import Path
import json,re,hashlib
from run import D
rows=[]
for f in sorted(D.glob('*judge.jsonl')):
 ev=[json.loads(l) for l in f.read_text().splitlines()]
 commands=[e['item'] for e in ev if e['type']=='item.completed' and e.get('item',{}).get('type')=='command_execution']
 reads=[]
 for i,c in enumerate(commands):
  s=c['command'];out=c.get('aggregated_output','')
  if re.search(r'(?:cat|sed|read_text|readFile)',s):
   for name in ['ne-output.md','ne-source-content.md','ne-build-brief.md','ne-output-meta.md']:
    if name in s:reads.append((i,name))
  if 'ne-output.md' in s and re.search(r'\bcat\b',s): assert not re.search(r'Focal Statement:|Killer Line:|focal_origin:',out),f
 assert not any(n=='ne-output-meta.md' for i,n in reads),(f,reads)
 first={n:next(i for i,k in reads if k==n) for n in ['ne-output.md','ne-source-content.md','ne-build-brief.md']}
 assert first['ne-output.md']<first['ne-source-content.md']<first['ne-build-brief.md'],(f,reads)
 writes=[i for i,c in enumerate(commands) if 'ne-cold-read.md' in c['command'] and ('cat >' in c['command'] or 'write_text' in c['command'])]
 assert len(writes)>=2 and first['ne-output.md']<writes[0]<first['ne-source-content.md']<writes[1]<first['ne-build-brief.md'],(f,writes)
 rows.append({'cold_read_written_before_source':True,'source_check_written_before_brief':True,'transcript':f.name,'read_order':reads,'body_only':True,'no_sidecar_read':True,'completed':ev[-1]['type']=='turn.completed'})
print(json.dumps(rows,indent=2))
(D/'judge-input-verification.json').write_text(json.dumps(rows,indent=2)+'\n')
