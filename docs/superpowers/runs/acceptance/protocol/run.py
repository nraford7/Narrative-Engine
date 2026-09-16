from pathlib import Path
import subprocess,shutil,json,hashlib,os
R=Path('/Users/noahraford/Dropbox/Noah_Remote_Shared/claude-brain/skills/Narrative-Engine')
W=Path(os.environ.get('NE_PROTOCOL_WORK','/Users/noahraford/Documents/Codex/2026-09-16/i-d-x20/work/acceptance-protocol')); W.mkdir(parents=True,exist_ok=True)
D=Path(os.environ.get('NE_PROTOCOL_ARCHIVE',str(R/'docs/superpowers/runs/acceptance/protocol'))); D.mkdir(parents=True,exist_ok=True)
source=Path(os.environ.get('NE_PROTOCOL_SOURCE','/tmp/ne-accept-s1/ne-source-content.md')).read_text()
for n in ['focal-leg1','focal-leg2','evidence']:
 p=W/n;p.mkdir(exist_ok=True);(p/'ne-source-content.md').write_text(source)
weak='''# Build Brief
## Focal Statement
One Thing: Retention metrics held steady in Q3.
Ask: Choose option (c): reallocate AED 1.8M to guided onboarding.
Through-Line: Review Q3 metrics, operating continuity, and the offsite decision.
focal_origin: ORIGIN
## Material Read
Stake: The executive team is setting the Q4 retention budget.
Tension: Competitive pressure and longer procurement decisions persist.
Genuine surprise: none within this selected focal.
Strongest existing passages: "Renewal cohort performance was within range across segments." "Operational updates: the CS reorganization completed in August; average ticket response is at 4.1 hours; the new health-score dashboard is live for enterprise accounts. Headcount is flat."
What changes: Choose option (c) at the offsite.
## Argument Outline
1. Report quarterly and segment retention figures, keeping the 1.1pp fall explicit.
2. Report operating continuity and completed CS changes.
3. Present option (c) as the offsite choice. Keep the deliberately narrow metrics focal; the cohort discount and onboarding analysis are outside this selected argument.
## Shape
answer-first; concise executive prose memo, 3 sections, content-driven length.
## Audience
The executive team at the budget offsite. Familiar with GRR and renewal metrics.
## Voice
Plain, precise executive prose. Preserve source qualifications.
## Density
narrative
'''
(W/'focal-leg1/ne-build-brief.md').write_text(weak.replace('ORIGIN','inferred'))
(W/'focal-leg2/ne-build-brief.md').write_text(weak.replace('ORIGIN','user-selected-after-reset'))
(W/'evidence/ne-build-brief.md').write_text('''# Build Brief
## Focal Statement
One Thing: Reallocate AED 1.8M of the retention-discount pool to guided onboarding, because the cohort evidence and preliminary modeling favor it.
Ask: Choose option (c) at the budget offsite.
Through-Line: The discount association and onboarding renewal gap support a shift in retention spending, with modeling uncertainty preserved.
focal_origin: user-selected
## Material Read
Stake: Q4 retention allocation.
Tension: Sales seeks expanded discounts, while discounted accounts churn more.
Genuine surprise: Discounted accounts churned at 2.3x the rate, and speed to first saved report predicts renewal.
Strongest existing passages: "accounts that received a retention discount churned at 2.3x the rate of undiscounted accounts within 18 months of the concession"; "accounts that built and saved a report within 14 days renewed at 96%, versus 71% for accounts that took longer than 45 days"; "Preliminary modeling suggests option (c) affects 18-month retention 3-4x more per dirham than discounting"
What changes: Select the source's option (c), recognizing tougher sales conversations.
## Argument Outline
1. Recommend the source's allocation and introduce why the discount pool needs scrutiny.
2. Explain the observational 2.3x discount association and onboarding renewal gap without causation; cohort covers 1,240 accounts over 24 months.
3. Close with option (c), its scope (all new mid-market and SMB accounts), preliminary model and Q4 sales tradeoff.
## Shape
answer-first; concise executive prose memo, content-driven length.
## Audience
The executive team at the budget offsite; familiar with retention metrics.
## Voice
Plain executive prose, precise qualifications.
## Density
narrative
''')
def run(role,n,label):
 p=W/n
 prompt=f'RUN_DIR: {p}\nRead and execute {R}/prompts/{role}.md. '
 if role=='evidence-reviewer':
  if label=='evidence-recheck': prompt+=f'Evidence review count: 2 (second and final run for this draft). Archived last report: {D}/evidence-first-review/ne-evidence-review.md. '
  else: prompt+='Evidence review count: 1 (first run for this draft); no prior evidence report. Audit the entire draft. '
 if role=='focal-fidelity-judge': prompt+='Audience: the executive team at the budget offsite. Ask: choose option (c), reallocate AED 1.8M to guided onboarding. Output is prose. Read only your contracted inputs, strictly in phase order, and write each intermediate artifact before advancing. '
 prompt+='This is a fresh isolated role context. Do not read other run directories or repository history. Execute the contract and write the required files; do not modify runtime skill files.'
 (D/f'{label}.prompt.txt').write_text(prompt)
 with (D/f'{label}.jsonl').open('w') as out, (D/f'{label}.stderr.txt').open('w') as err:
  r=subprocess.run(['codex','exec','--ignore-user-config','--ignore-rules','--ephemeral','--skip-git-repo-check','-C',str(p),'-m','gpt-6-astra','-c','model_reasoning_effort="medium"','-s','danger-full-access','--json',prompt],stdout=out,stderr=err)
 if r.returncode: raise RuntimeError(f'{label} exit {r.returncode}')
 dest=D/label;dest.mkdir(exist_ok=True)
 for f in p.glob('ne-*.md'):shutil.copy2(f,dest/f.name)
 print(label,flush=True)
if __name__=='__main__':
 import sys
 role,n,label=sys.argv[1:];run(role,n,label)
