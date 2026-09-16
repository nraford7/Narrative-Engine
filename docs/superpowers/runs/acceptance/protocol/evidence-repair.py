from run import W,D,run
import time,shutil,json
while not (D/'evidence-first-review/ne-evidence-review.md').exists():time.sleep(2)
p=W/'evidence'
assert '\nFINDINGS\n' in (p/'ne-evidence-review.md').read_text()
run('builder','evidence','evidence-builder-revision')
run('evidence-reviewer','evidence','evidence-recheck')
v=(p/'ne-evidence-review.md').read_text()
assert '\nCLEAN\n' in v,v
(p/'ne-evidence-review.md').unlink()
run('focal-fidelity-judge','evidence','evidence-final-judge')
v=(p/'ne-focal-judge.md').read_text()
assert '\nPASS\n' in v or 'Verdict: PASS' in v,v
removed=[]
for n in ['ne-focal-judge.md','ne-focal-judge-prior.md','ne-evidence-review.md','ne-humanizing-flags.md']:
 f=p/n
 if f.exists():f.unlink();removed.append(n)
(D/'evidence-cleanup.json').write_text(json.dumps({'evidence_review_count':2,'focal_reread_reason':'Repair changed the close','final_evidence_verdict':'CLEAN','final_focal_verdict':'PASS','removed_at_end':removed,'evidence_trigger_removed_after_recheck':True,'remaining_triggers':[],'sidecar':'Retained to delivery per plan RUN_DIR contract.'},indent=2)+'\n')
z=D/'evidence-final';z.mkdir(exist_ok=True)
for f in p.glob('ne-*.md'):shutil.copy2(f,z/f.name)
