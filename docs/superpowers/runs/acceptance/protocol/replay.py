"""Full protocol recipe. Replays into NEW directories; never overwrites the archived run."""
from pathlib import Path
import argparse,os,sys,runpy,json
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--work',required=True,help='New scratch directory; must not exist')
p.add_argument('--archive',required=True,help='New results directory; must not exist')
p.add_argument('--source',default=str(Path(__file__).parent/'evidence-build/ne-source-content.md'))
a=p.parse_args()
for target in [a.work,a.archive]:
 if Path(target).exists():p.error('Refusing to overwrite existing directory: '+target)
source=Path(a.source).resolve();assert source.is_file(),source
os.environ.update(NE_PROTOCOL_WORK=str(Path(a.work).resolve()),NE_PROTOCOL_ARCHIVE=str(Path(a.archive).resolve()),NE_PROTOCOL_SOURCE=str(source))
from run import run,D
# Focal path: one automatic reopen, then a forced after-reset weak focal.
run('builder','focal-leg1','focal-leg1-build')
run('focal-fidelity-judge','focal-leg1','focal-leg1-judge')
runpy.run_path(str(Path(__file__).parent/'focal-next.py'),run_name='__main__')
leg2=(D/'focal-leg2-judge/ne-focal-judge.md').read_text()
verdict_block=leg2.split('## Verdict',1)[1].split('## needs_revision_count',1)[0]
assert 'FOCAL_MISMATCH' not in verdict_block and 'ADVISORY' in leg2
(D/'focal-no-second-reset.json').write_text(json.dumps({'focal_reopen_count':1,'second_reopen':False,'advisory_present':True,'leg2_verdict_block':verdict_block.strip()},indent=2)+'\n')
# Evidence path: genuine draft and initial gate, one planted error, first full audit,
# actual builder revision, explicit second-review count+archive dispatch,
# fresh judge after the closing repair, then trigger cleanup.
run('builder','evidence','evidence-build')
run('focal-fidelity-judge','evidence','evidence-initial-judge')
runpy.run_path(str(Path(__file__).parent/'evidence-next.py'),run_name='__main__')
runpy.run_path(str(Path(__file__).parent/'evidence-repair.py'),run_name='__main__')
runpy.run_path(str(Path(__file__).parent/'verify.py'),run_name='__main__')
(D/'replay-complete.json').write_text(json.dumps({'note':'Full sequence completed; assess actual archived verdicts. Unchanged original acceptance artifacts remain untouched.'},indent=2)+'\n')
print('Replay results:',D)
