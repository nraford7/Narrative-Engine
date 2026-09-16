import concurrent.futures, hashlib, json, os, pathlib, random, re, subprocess, sys, time
ROOT=pathlib.Path(os.environ.get('NE_ACCEPTANCE_SCRATCH','/Users/noahraford/Documents/Codex/2026-09-16/i-d-x20/work/acceptance-ablation')).resolve()
REPO=pathlib.Path(os.environ.get('NE_ACCEPTANCE_REPO','/Users/noahraford/Dropbox/Noah_Remote_Shared/claude-brain/skills/Narrative-Engine')).resolve()
BASE=pathlib.Path(os.environ.get('NE_ACCEPTANCE_BASELINES','/Users/noahraford/Projects/family-office/agent-studio-out/ablation')).resolve()
if ROOT.is_relative_to(REPO): raise ValueError('Private scratch must be outside the repository')
ROOT.mkdir(parents=True,exist_ok=True)
OUT=REPO/'docs/superpowers/runs/acceptance/ablation'
OUT.mkdir(parents=True,exist_ok=True)
def dump(p,d): p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def parse(text):
 text=text.strip()
 if text.startswith('```'): text=re.sub(r'^```(?:json)?\s*|\s*```$','',text)
 return json.loads(text)
def extract():
 records={}
 for name in ['astra','lease','launch','churn']:
  t=(BASE/f'ne-ablation-judge-{name}.md').read_text()
  source=(t.split('=== SOURCE MATERIAL ===\n\n',1)[1].split('\n=== DECK 1 ===',1)[0].rstrip() if name=='astra' else re.search(r'THE SOURCE:\s*<<<\n(.*?)\n>>>',t,re.S).group(1))
  audience=re.search(r'^AUDIENCE: (.*)$',t,re.M).group(1)
  ask=re.search(r'^ASK: (.*)$',t,re.M).group(1)
  records[name]={'source':source,'audience':audience,'ask':ask}
 dump(ROOT/'sources-private.json',records)
 dump(OUT/'source-manifest.json',{k:{'sha256':hashlib.sha256(v['source'].encode()).hexdigest(),'characters':len(v['source']),'audience':v['audience'],'ask':v['ask']} for k,v in records.items()})
 files=['SKILL.md','framework-selection.md','prose-craft.md','prose-craft-constructions.md','deck-title-craft.md','humanizing-pass.md','prompts/builder.md','prompts/focal-fidelity-judge.md','prompts/evidence-reviewer.md','prompts/reviewer.md','prompts/stress-tester.md']
 runtime='\n\n'.join('=== RUNTIME FILE '+f+' ===\n'+(REPO/f).read_text() for f in files)
 (ROOT/'runtime-private.txt').write_text(runtime)
 dump(OUT/'runtime-manifest.json',{f:hashlib.sha256((REPO/f).read_bytes()).hexdigest() for f in files})
 for name,format in [('astra','boardroom'),('lease','boardroom'),('launch','boardroom'),('churn','boardroom'),('astra','prose'),('launch','keynote')]:
  d=records[name]; key=name+'-'+format
  prompt='''You are generating one deliverable for a controlled acceptance experiment. No browsing, tools, file reads, delegation, or external research. The source and runtime below are your entire input. Do not seek other outputs or baselines. Run the rebuilt Narrative Engine in FAST mode, SOLO-SIMULATED in this single response, as the historical old-engine arm was simulated. Infer choices, surface the 2-3 focal candidates in your audit, select one, compile the brief, build using only the builder-permitted instructions, then simulate focal, humanizing and evidence checks and targeted reviewer/stress tests if required. Respect repair caps; do not optimize indefinitely. This solo simulation is not true blind internal judging; record this limitation. No need to ask permission or confirmation: this bounded generation is authorized.
Return ONLY valid JSON with these keys:
"punchline": string (decks only; empty for prose),
"titles": array of exact slide titles (empty for prose),
"deck_markdown": string (deck BODY ONLY, same historical contract: Punchline line, Title sequence numbered list, then every slide heading with slide content; keynote includes spoken narration per slide),
"prose_markdown": string (prose BODY ONLY, otherwise empty),
"audit": {"focal_candidates": [strings], "selected_focal": string, "material_read": string, "argument_outline": [strings], "shape": string, "build_brief": string, "initial_evidence_findings": [strings], "repairs": [strings], "final_evidence_verdict": string, "simulated_focal_verdict": string, "reviewer_and_stress_notes": [strings], "source_trace": [strings], "limitations": [strings]}.
Content-driven length, no padding. Preserve qualifications and exact source support. Do not insert evaluation commentary in deliverable body.
'''+f'\nOUTPUT: {format}\nAUDIENCE: {d["audience"]}\nASK: {d["ask"]}\n\nSOURCE:\n<<<\n{d["source"]}\n>>>\n\n'+runtime
  (ROOT/f'writer-{key}.txt').write_text(prompt)
def call(key,kind,model,effort):
 prompt=ROOT/f'{kind}-{key}.txt'; final=ROOT/f'{kind}-{key}-response.txt'; log=ROOT/f'{kind}-{key}-events.jsonl'
 args=['codex','exec','--ephemeral','--ignore-user-config','--skip-git-repo-check','-s','read-only','-m',model,'-c',f'model_reasoning_effort="{effort}"','--json','-o',str(final),'-']
 start=time.time()
 with prompt.open() as inp,log.open('w') as logs:
  proc=subprocess.run(args,stdin=inp,stdout=logs,stderr=subprocess.STDOUT,cwd=ROOT)
 meta={'model':model,'reasoning_effort':effort,'elapsed_seconds':round(time.time()-start,1),'exit_code':proc.returncode,'input_sha256':hashlib.sha256(prompt.read_bytes()).hexdigest()}
 if proc.returncode: dump(OUT/f'{kind}-{key}-status.json',meta); return key,meta
 try:
  result=parse(final.read_text()); destination=ROOT if key.startswith('astra-') else OUT
  if key.startswith('astra-') and kind=='judge':
   destination=OUT
   dump(ROOT/f'{kind}-{key}-private.json',result)
   for row in result['decks']: row['verdict']='Private qualitative verdict retained in local scratch; numeric scores preserved verbatim.'
  dump(destination/f'{kind}-{key}.json',result)
  if kind=='writer': (destination/f'{key}.md').write_text(result['prose_markdown'] if 'prose' in key.split('-') else result['deck_markdown'])
 except Exception as e: meta['parse_error']=str(e)
 dump(OUT/f'{kind}-{key}-status.json',meta)
 return key,meta
def write_all():
 keys=['astra-boardroom','lease-boardroom','launch-boardroom','churn-boardroom','astra-prose','launch-keynote']
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
  jobs=[pool.submit(call,k,'writer','gpt-5.6-sol','medium') for k in keys]
  for f in concurrent.futures.as_completed(jobs): print(f.result(),flush=True)
def prepare_judges():
 sources=json.loads((ROOT/'sources-private.json').read_text())
 original=json.loads((BASE/'full-results.json').read_text())['result']['perSource']
 rubric=(BASE/'ne-ablation-judge-churn.md').read_text().split('\n\nTHE SOURCE:')[0].replace('four','three')
 mappings={}
 for record in original:
  name=record['source']; key=name+'-boardroom'; d=sources[name]
  t=(BASE/f'ne-ablation-judge-{name}.md').read_text()
  parts=re.split(r'=== DECK \d+ ===\s*',t)[1:]
  decks={arm:parts[i].strip() for i,arm in enumerate(record['perm']) if arm in ['A','B']}
  loc=ROOT if name=='astra' else OUT
  decks['rebuilt']=(loc/f'{key}.md').read_text().strip()
  order=['A','B','rebuilt']; random.Random('ne-acceptance-2026-09-16-'+name).shuffle(order)
  mappings[key]={str(i+1):arm for i,arm in enumerate(order)}
  prompt=rubric+'\n\nJudge only the supplied content, independently. Do not use tools, external context, or infer provenance. Scores can use decimals. Overall ranks must be distinct 1, 2, 3.\n\n'+f'THE SOURCE:\n<<<\n{d["source"]}\n>>>\n\nAUDIENCE: {d["audience"]}\nASK: {d["ask"]}\n\n'+'\n\n'.join(f'=== DECK {i+1} ===\n{decks[arm]}' for i,arm in enumerate(order))
  (ROOT/f'judge-{key}.txt').write_text(prompt)
 for key in ['astra-prose','launch-keynote']:
  name,fmt=key.split('-'); d=sources[name]; loc=ROOT if name=='astra' else OUT
  r=rubric.replace('three presentation decks','one '+('prose piece' if fmt=='prose' else 'keynote-register presentation')).replace('For each deck','For this piece').replace('Then rank the three decks overall, 1 = best.','Use rank 1 for this single piece.').replace('slide 2','the next section' if fmt=='prose' else 'the next beat')
  r=r.replace('read the slide titles in order as one paragraph — do they form one coherent spoken argument','read the section openings in order — do they form one coherent argument' if fmt=='prose' else 'read each slide beat with its narration in sequence — do they form one coherent spoken argument; fragments are appropriate to keynote register')
  prompt=r+'\n\nJudge only supplied content, independently. No tools or provenance inference. Scores can use decimals.\n\n'+f'THE SOURCE:\n<<<\n{d["source"]}\n>>>\n\nAUDIENCE: {d["audience"]}\nASK: {d["ask"]}\n\n=== DECK 1 ===\n'+(loc/f'{key}.md').read_text()
  (ROOT/f'judge-{key}.txt').write_text(prompt)
 dump(ROOT/'blind-map.json',mappings)
def judge_all():
 keys=['astra-boardroom','lease-boardroom','launch-boardroom','churn-boardroom','astra-prose','launch-keynote']
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
  jobs=[pool.submit(call,k,'judge','gpt-6-astra','medium') for k in keys]
  for f in concurrent.futures.as_completed(jobs): print(f.result(),flush=True)
def summarize():
 mappings=json.loads((ROOT/'blind-map.json').read_text()); dimensions=['hook','chain','fidelity','payoff','natural']; rows=[];extras=[]
 for key, mapping in mappings.items():
  data=json.loads((OUT/f'judge-{key}.json').read_text())['decks']
  assert len(data)==3 and sorted(x['rank'] for x in data)==[1,2,3],key
  assert sorted(x['deck'] for x in data)==[1,2,3],key
  arms={mapping[str(x['deck'])]:x for x in data}
  for arm,x in arms.items():
   assert all(isinstance(x[d],(int,float)) and 1<=x[d]<=10 for d in dimensions),(key,arm)
  rows.append({'source':key.split('-')[0],'arms':arms,'rebuilt_beats_old_A':arms['rebuilt']['rank']<arms['A']['rank'],'rebuilt_at_or_above_B':arms['rebuilt']['rank']<=arms['B']['rank']})
 for key in ['astra-prose','launch-keynote']:
  data=json.loads((OUT/f'judge-{key}.json').read_text())['decks'];assert len(data)==1
  x=data[0];assert all(isinstance(x[d],(int,float)) and 1<=x[d]<=10 for d in dimensions)
  extras.append({'slice':key,**x,'passes':x['fidelity']>=7 and x['natural']>=7.5})
 means={arm:{d:sum(r['arms'][arm][d] for r in rows)/4 for d in dimensions} for arm in ['A','B','rebuilt']}
 checks={'beats_old_A_4_of_4':sum(r['rebuilt_beats_old_A'] for r in rows)==4,'mean_fidelity_at_least_7':means['rebuilt']['fidelity']>=7,'mean_natural_at_least_7_5':means['rebuilt']['natural']>=7.5,'at_or_above_B_at_least_2':sum(r['rebuilt_at_or_above_B'] for r in rows)>=2,'prose_and_keynote_thresholds':all(x['passes'] for x in extras)}
 summary={'method':'Saved A and B compared with fresh gpt-5.6-sol medium SOLO-simulated rebuilt outputs. Independent blind gpt-6-astra medium judging. Model-confounded; not an exact original-generator reproduction.','initial_acceptance_pass':all(checks.values()),'checks':checks,'means':means,'comparisons':rows,'extra_formats':extras,'blind_map':mappings}
 dump(OUT/'results.json',summary);print(json.dumps(summary,indent=2))
if __name__=='__main__':
 if sys.argv[1]=='prepare': extract()
 elif sys.argv[1]=='write': write_all()
 elif sys.argv[1]=='prepare-judges': prepare_judges()
 elif sys.argv[1]=='judge': judge_all()
 elif sys.argv[1]=='summarize': summarize()
