# Protocol acceptance — 2026-09-16

Spec-level verdict: READY for Task10 steps1–2. Both protocol scenarios demonstrated using fresh `gpt-6-astra`, medium reasoning, independent CLI contexts. No runtime edits, commits, pushes, or keynote-create changes were made by this harness.

## Results

| Scenario | Observed result | Evidence |
|---|---|---|
| First inferred weak focal | FOCAL_MISMATCH; automatic first reopen | focal-leg1-judge/ne-focal-judge.md |
| Forced weak focal selected after reset | NEEDS_REVISION, with ADVISORY; no second reopen | focal-leg2-judge/ne-focal-judge.md; focal-no-second-reset.json |
| Genuine initial evidence draft | Initial focal PASS | evidence-initial-judge/ne-focal-judge.md |
| One planted causation overclaim | FINDINGS; 2 BLOCKING findings: causation and resulting provenance-tag failure | evidence-first-review/ne-evidence-review.md |
| Actual builder revision | Only planted sentence deleted; body restored exactly to genuine initial draft; sidecar updated | evidence-repair.diff; evidence-builder-revision/ne-output-meta.md |
| Second evidence review | CLEAN; changed closing section and both prior findings checked | evidence-recheck/ne-evidence-review.md |
| Fresh judge reread after closing repair | PASS | evidence-final-judge/ne-focal-judge.md |
| End-loop cleanup | All four trigger/prior files absent; sidecar retained to delivery | evidence-cleanup.json; evidence-final/ |

## Protocol integrity and source preservation

Every role invocation starts a fresh `codex exec --ephemeral`; no resume, fork, prior authoring conversation or verdict expectation enters evaluator dispatch. Each exact dispatch is retained as `*.prompt.txt`, and raw tool transcripts as `*.jsonl`. `judge-input-verification.json` records all judge read orders, cold-read write before source, source-check write before brief, body-only input and absence of sidecar reads. Judges receive the same audience/ask as the brief, no focal in dispatch. The transcript later contains focal metadata only when the contract permits reading the brief at Phase B.

The source is an exact copy of `/tmp/ne-accept-s1/ne-source-content.md` (SHA256 `e40ab925effcc67a9db48d7d29a2fbc93d2993fa58a6623e74deb3a7d764c63c`); every archived source matches. All prior `/tmp/ne-accept-s1` artifacts were left untouched. The deliberate weak briefs and the single inserted sentence are documented in `manifest.json` and `intentional-error.json`. Reopen is a harness orchestration action; the deliberately repeated weak focal is a simulated user choice required by the scenario, not a real user endorsement.

## Precise plan deviation

The first judge quoted the source's 96%/71% onboarding renewal gap and preliminary 3–4× per-dirham passage, rather than the plan's expected 2.3× discount sentence. Both quoted claims are consequential to the exact requested option(c) budget decision. Binding spec1b requires a consequential source quote, which this satisfies. The narrow plan-level quote oracle does not match; no source, ask, or evaluator instruction was altered to force it. Parent explicitly accepted this interpretation. The second weak memo's NEEDS_REVISION is preserved as an actual quality finding; the tested guard is advisory/no-reset, not a requirement that a deliberately bad focal produce a deliverable memo.

## Timing and integration limits

The parent revised runtime lifecycle instructions while initial builds/judges were in flight. Each raw transcript preserves the actual contract read. First evidence review ran all five checks across the entire draft; its dispatch predates the explicit count field but the report documents full first-run scope. Second evidence dispatch explicitly gives review count2 and the archived first report path under the corrected current contract. Sidecar retention follows the approved plan's detailed RUN_DIR contract and current runtime; an earlier broad spec sentence says delete it at loop end.

These are prose scenarios; Boardroom/Keynote register coverage belongs to the separate ablation acceptance. The harness executes routing and cleanup explicitly; it does not prove every surrounding interactive Phase1.75/P3 UI path. Escalation/cap breach and authorized framework restart are separate lifecycle paths handled by parent review/mechanical gates, not exercised here.

Risk: low, reversible local artifacts only. No external publication. Recovery: remove only this acceptance archive and scratch run directories to discard test artifacts; original source and runtime remain unchanged by this agent. Do not delete the forced leg2 NEEDS_REVISION report merely to make cleanup appear green; it is preserved as unresolved fixture output and only the evidence scenario has completed repair cleanup.

Test surface: `prompts/builder.md`, `prompts/focal-fidelity-judge.md`, `prompts/evidence-reviewer.md`, and `SKILL.md` reset/repair/cleanup routing. Raw transcripts, paired snapshots and the body diff support the claimed behavior. Hidden scope is limited to evaluator stochasticity and the manual harness orchestration boundary described above.

## Executed orchestration and replay recipe

`run.py` is a role runner, not the full orchestrator. The executed initial build/judge calls were followed by `focal-next.py` (assert first mismatch, archive/clear triggers, record one reopen, force after-reset fixture, build and judge) and `evidence-next.py` (assert initial PASS, clear judge trigger, plant one sentence, archive, first full evidence review), then `evidence-repair.py` (actual builder revision, explicit review count2 and archived-report dispatch, CLEAN assertion, remove evidence trigger, fresh judge, PASS assertion, end-loop cleanup). These exact transition records are preserved in `focal-reopen.json`, `intentional-error.json`, and `evidence-cleanup.json`; every actual role dispatch has a paired raw JSONL.

`replay.py` now joins that same complete sequence, with new-directory guards and source preservation. It has been syntax-checked and its argument/overwrite guard checked; the newly consolidated wrapper has not itself been executed end-to-end because the underlying original scenario runs are already complete and should not be rerun to chase judgments. Fresh model results may vary.

To replay, run `python3 replay.py --work /absolute/new/scratch-path --archive /absolute/new/result-path` from this archive. Both destinations must not already exist. The source defaults to the archived genuine build source; `--source` can select an explicit exact source copy. The role runner now accepts these isolated paths from the wrapper. The second evidence dispatch supplies `Evidence review count: 2 (second and final run for this draft)` and the new archive's `evidence-first-review/ne-evidence-review.md` path. The initial dispatch now also explicitly supplies count1 and entire-draft scope. This initial-count clarification was added after the recorded first review, whose full coverage is independently documented in the original raw report.
