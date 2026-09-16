from run import W,D,run
import time,json
while not (D/'focal-leg1-judge/ne-focal-judge.md').exists():time.sleep(2)
v=(W/'focal-leg1/ne-focal-judge.md').read_text();assert 'FOCAL_MISMATCH' in v.split('## needs_revision_count')[0]
triggers=['ne-focal-judge.md','ne-focal-judge-prior.md','ne-evidence-review.md','ne-humanizing-flags.md']
removed=[]
for x in triggers:
 p=W/'focal-leg1'/x
 if p.exists():p.unlink();removed.append(x)
(D/'focal-reopen.json').write_text(json.dumps({'focal_reopen_count':1,'phase':'1.75','candidate_from_judge':'Onboarding speed predicts renewal and preliminary modeling favors option(c).','forced_fixture_choice':'Retention metrics held steady in Q3.','focal_origin':'user-selected-after-reset','note':'Simulated deliberate user choice required by scenario; neither actual user endorsement nor evaluator instruction.','removed_triggers':removed},indent=2)+'\n')
run('builder','focal-leg2','focal-leg2-build')
run('focal-fidelity-judge','focal-leg2','focal-leg2-judge')
