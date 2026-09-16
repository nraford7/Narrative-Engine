from run import W,D,run
import shutil,json
p=W/'evidence'
v=(p/'ne-focal-judge.md').read_text()
assert '\nPASS\n' in v,v
(p/'ne-focal-judge.md').unlink()
f=p/'ne-output.md';s=f.read_text();old='That estimate remains preliminary. Approve the AED 1.8M reallocation'
assert old in s
s=s.replace(old,'That estimate remains preliminary. Discounts caused the churn. Approve the AED 1.8M reallocation')
f.write_text(s)
z=D/'evidence-planted';z.mkdir(exist_ok=True)
for x in p.glob('ne-*.md'):shutil.copy2(x,z/x.name)
(D/'intentional-error.json').write_text(json.dumps({'file':'ne-output.md','section':'closing section, paragraph 1','insertion':'Discounts caused the churn.','other_edits':'none','reason':'Causation overclaim planted into genuine builder draft; close is changed to trigger judge reread after repair.'},indent=2))
run('evidence-reviewer','evidence','evidence-first-review')
