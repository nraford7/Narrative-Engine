from run import D,W
from pathlib import Path
import hashlib,json,shutil,re
verdict=lambda p: re.search(r'## Verdict\s+(?:Verdict:\s*)?(PASS|NEEDS_REVISION|FRAMEWORK_MISMATCH|FOCAL_MISMATCH|CLEAN|FINDINGS)',p.read_text()).group(1)
a=verdict(D/'focal-leg1-judge/ne-focal-judge.md');b=verdict(D/'focal-leg2-judge/ne-focal-judge.md');c=verdict(D/'evidence-first-review/ne-evidence-review.md');d=verdict(D/'evidence-recheck/ne-evidence-review.md');e=verdict(D/'evidence-final-judge/ne-focal-judge.md')
assert a=='FOCAL_MISMATCH';assert b!='FOCAL_MISMATCH';assert 'ADVISORY' in (D/'focal-leg2-judge/ne-focal-judge.md').read_text();assert (c,d,e)==('FINDINGS','CLEAN','PASS')
assert (D/'evidence-build/ne-output.md').read_bytes()==(D/'evidence-builder-revision/ne-output.md').read_bytes()
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
hash0=h(Path('/tmp/ne-accept-s1/ne-source-content.md'))
assert all(h(p)==hash0 for p in D.glob('*/ne-source-content.md'))
triggers=['ne-focal-judge.md','ne-focal-judge-prior.md','ne-evidence-review.md','ne-humanizing-flags.md']
assert not any((W/'evidence'/n).exists() for n in triggers)
(D/'focal-no-second-reset.json').write_text(json.dumps({'focal_reopen_count':1,'leg2_verdict':b,'advisory_present':True,'second_reopen':False,'unresolved_piece_findings':'Retained for visibility; deliberately weak-focal fixture is not a delivery candidate.'},indent=2)+'\n')
text=f'''# Protocol acceptance — 2026-09-16

Spec-level verdict: READY for Task10 steps1–2. Both protocol scenarios demonstrated using fresh `gpt-6-astra`, medium reasoning, independent CLI contexts. No runtime edits, commits, pushes, or keynote-create changes were made by this harness.

## Results

| Scenario | Observed result | Evidence |
|---|---|---|
| First inferred weak focal | {a}; automatic first reopen | focal-leg1-judge/ne-focal-judge.md |
| Forced weak focal selected after reset | {b}, with ADVISORY; no second reopen | focal-leg2-judge/ne-focal-judge.md; focal-no-second-reset.json |
| Genuine initial evidence draft | Initial focal PASS | evidence-initial-judge/ne-focal-judge.md |
| One planted causation overclaim | {c}; 2 BLOCKING findings: causation and resulting provenance-tag failure | evidence-first-review/ne-evidence-review.md |
| Actual builder revision | Only planted sentence deleted; body restored exactly to genuine initial draft; sidecar updated | evidence-repair.diff; evidence-builder-revision/ne-output-meta.md |
| Second evidence review | {d}; changed closing section and both prior findings checked | evidence-recheck/ne-evidence-review.md |
| Fresh judge reread after closing repair | {e} | evidence-final-judge/ne-focal-judge.md |
| End-loop cleanup | All four trigger/prior files absent; sidecar retained to delivery | evidence-cleanup.json; evidence-final/ |

## Protocol integrity and source preservation

Every role invocation starts a fresh `codex exec --ephemeral`; no resume, fork, prior authoring conversation or verdict expectation enters evaluator dispatch. Each exact dispatch is retained as `*.prompt.txt`, and raw tool transcripts as `*.jsonl`. `judge-input-verification.json` records all judge read orders, cold-read write before source, source-check write before brief, body-only input and absence of sidecar reads. Judges receive the same audience/ask as the brief, no focal in dispatch. The transcript later contains focal metadata only when the contract permits reading the brief at Phase B.

The source is an exact copy of `/tmp/ne-accept-s1/ne-source-content.md` (SHA256 `{hash0}`); every archived source matches. All prior `/tmp/ne-accept-s1` artifacts were left untouched. The deliberate weak briefs and the single inserted sentence are documented in `manifest.json` and `intentional-error.json`. Reopen is a harness orchestration action; the deliberately repeated weak focal is a simulated user choice required by the scenario, not a real user endorsement.

## Precise plan deviation

The first judge quoted the source's 96%/71% onboarding renewal gap and preliminary 3–4× per-dirham passage, rather than the plan's expected 2.3× discount sentence. Both quoted claims are consequential to the exact requested option(c) budget decision. Binding spec1b requires a consequential source quote, which this satisfies. The narrow plan-level quote oracle does not match; no source, ask, or evaluator instruction was altered to force it. Parent explicitly accepted this interpretation. The second weak memo's {b} is preserved as an actual quality finding; the tested guard is advisory/no-reset, not a requirement that a deliberately bad focal produce a deliverable memo.

## Timing and integration limits

The parent revised runtime lifecycle instructions while initial builds/judges were in flight. Each raw transcript preserves the actual contract read. First evidence review ran all five checks across the entire draft; its dispatch predates the explicit count field but the report documents full first-run scope. Second evidence dispatch explicitly gives review count2 and the archived first report path under the corrected current contract. Sidecar retention follows the approved plan's detailed RUN_DIR contract and current runtime; an earlier broad spec sentence says delete it at loop end.

These are prose scenarios; Boardroom/Keynote register coverage belongs to the separate ablation acceptance. The harness executes routing and cleanup explicitly; it does not prove every surrounding interactive Phase1.75/P3 UI path. Escalation/cap breach and authorized framework restart are separate lifecycle paths handled by parent review/mechanical gates, not exercised here.

Risk: low, reversible local artifacts only. No external publication. Recovery: remove only this acceptance archive and scratch run directories to discard test artifacts; original source and runtime remain unchanged by this agent. Do not delete the forced leg2 NEEDS_REVISION report merely to make cleanup appear green; it is preserved as unresolved fixture output and only the evidence scenario has completed repair cleanup.

Test surface: `prompts/builder.md`, `prompts/focal-fidelity-judge.md`, `prompts/evidence-reviewer.md`, and `SKILL.md` reset/repair/cleanup routing. Raw transcripts, paired snapshots and the body diff support the claimed behavior. Hidden scope is limited to evaluator stochasticity and the manual harness orchestration boundary described above.
'''
(D/'README.md').write_text(text)
for n in ['run.py','verify.py','focal-next.py','evidence-next.py','evidence-repair.py','report.py']:
 shutil.copy2(W/n,D/n)
print(text[:1600])
