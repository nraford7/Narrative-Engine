# Narrative Engine spine rebuild — acceptance record

16 September 2026. Continuation from `9fa82c1`, preserving the original rebuild commits and `pre-spine-rebuild` rollback tag. Scope: Narrative Engine only. After acceptance, the user explicitly authorized updating its GitHub repository.

**Acceptance criteria met**, with one permitted prose repair/retest. The measurements below are model-judged comparisons, not proof of consistent performance across future Claude runs.

## Required outcomes

| Requirement | Result |
|---|---|
| Rebuilt output outranks saved old-A on all four sources | PASS — 4/4 |
| Mean boardroom fidelity ≥7 | PASS — 10.00 |
| Mean boardroom naturalness ≥7.5 | PASS — 8.25 |
| Rebuilt output ranks at/above saved minimal spine B on ≥2 sources | PASS — 3/4 |
| Astra prose fidelity ≥7 and naturalness ≥7.5 | PASS after one repair — 9.5 / 8.0; initial naturalness 7.0 failed |
| Launch Keynote register fidelity ≥7 and naturalness ≥7.5 | PASS — 9.5 / 8.5 |
| Focal-mismatch scenario, both legs | PASS — first reset; forced second weak focal advisory, no second reset |
| Evidence-repair scenario | PASS — FINDINGS → actual builder repair → CLEAN → fresh focal PASS → cleanup |
| Source/brief isolation in judge transcripts | PASS — all four protocol judge transcripts preserve body → cold-read write → source → brief order; no sidecar reads |
| Mechanical and embed checks | PASS — 13 rebuild gates, 3 canonical sync checks, 3 sync regression tests |
| Audit-cluster traceability | PASS — all 16 mapped in the implementation plan |
| Keynote-create unchanged | PASS — all 46 installed-file hashes match the continuation baseline |

## Comparative results

Ranks are among the saved old engine, saved minimal spine and rebuilt output, judged together in anonymized order. Lower rank is better.

| Source | Old engine rank | Minimal spine rank | Rebuilt rank | Rebuilt fidelity | Rebuilt naturalness |
|---|---:|---:|---:|---:|---:|
| Astra briefing | 3 | 1 | 2 | 10 | 7.5 |
| Lease decision | 3 | 2 | 1 | 10 | 8.5 |
| Launch review | 3 | 2 | 1 | 10 | 8 |
| Retention review | 3 | 2 | 1 | 10 | 9 |

| Mean dimension | Saved old engine | Saved minimal spine | Rebuilt |
|---|---:|---:|---:|
| Hook | 8.375 | 8.25 | 7.25 |
| Argument chain | 8.00 | 8.00 | 8.625 |
| Fidelity to supplied source | 4.25 | 6.75 | 10.00 |
| Payoff | 7.875 | 9.00 | 8.75 |
| Naturalness | 5.375 | 7.625 | 8.25 |

The improvement is strongest in source fidelity, coherence and naturalness. Hook scores are lower, and the minimal spine still outranks the rebuilt Astra deck. The results do not justify claiming that every opening is more engaging. Service-first introductions and technical qualifications remain areas for editorial judgment.

The initial Astra prose had excessive reader-facing references to the source and repeated caveats. The single repair removed backstage commentary and redundant qualifications while retaining material limitations beside the relevant claims. An independent evidence recheck returned CLEAN, and a body-only reader recovered the governing claim and consultation ask. The final blind score raised naturalness from 7 to 8 while fidelity stayed at 9.5. Initial output and failed scores remain preserved; no other slice was regenerated in response to scores.

## What the continuation repaired

The main build was already committed. Fresh review exposed gaps not covered by its initial nine checks:

- The focal judge still directed a PASS straight to Phase 5. It now explicitly routes through Phases 4.7 and 4.8 before delivery.
- Required embedded prose guidance restored mandatory figured anchors, developed-sentence quotas and catalog loading. Seven finite Narrative Engine adaptations remove those conflicts while preserving the Floor/Filter and optional Ceiling. Exact canonical anchors are checked; unexpected drift fails sync.
- Escalation cleanup could delete the reports the user needed to inspect. Unresolved reports and sidecar now survive escalation.
- An authorized framework restart could retain a stale verdict and misroute the new builder. Fresh-draft restart archives and clears triggers, resets draft evidence counts and preserves the run-level focal-reset limit.
- A first evidence audit after an earlier gate's repair could inspect only changed sections. The first audit now covers the full draft; subsequent audits use changed sections and unresolved findings, with count/report history independent of trigger-file presence.

The reference README and progress checklist now describe actual implemented behavior. The 16-cluster traceability table is in the [plan](../plans/2026-09-16-ne-spine-rebuild.md).

## Method and limits

Generation used fresh `gpt-5.6-sol` sessions at medium reasoning because the Claude limit remained active. The exact historical generator version is not recorded in the baseline package. The saved old-A/B bodies were reused unchanged. External scores came from fresh, blind `gpt-6-astra` medium sessions receiving only the source, audience, ask and anonymized bodies—not arm names, runtime instructions, prior scores, generation self-checks or acceptance thresholds.

There is one final generation per source/format, plus the single allowed failed-prose repair and rescore. Two preliminary pre-fix generations were preserved unjudged and excluded before the final runtime snapshot. These small, model-confounded comparisons support the observed outcomes; they do not isolate the skill's causal effect or replace a later same-model Claude check.

Comparative generation solo-simulated internal gates, matching the historical arm's simulation boundary. It does not establish internal review blindness. Separate protocol scenarios used genuinely isolated roles and retained raw read/write transcripts. Those scenarios were manually orchestrated using the recorded commands and transition artifacts; the consolidated replay wrapper was syntax/overwrite-guard checked, not re-executed as one whole run. Escalation and framework restart received contract review and mechanical checks rather than live model scenarios.

The plan predicted the first focal judge would quote the 2.3× discount finding. It instead quoted the consequential 96%/71% onboarding and preliminary 3–4× modeling passages. That satisfies the binding spec's quoted consequential-evidence requirement; the narrower expected-phrase deviation is retained explicitly. The deliberately weak second memo received NEEDS_REVISION plus an advisory, not a fictitious delivery PASS.

The detailed plan's sidecar-until-delivery contract governs over the earlier spec's broad end-loop deletion sentence. Confidential Astra source and full derivatives remain outside this repository; retained public records contain hashes and numeric results. Synthetic scenario sources and raw protocol transcripts are included.

## Evidence and recovery

- [Protocol results and transcripts](acceptance/protocol/README.md)
- [Initial comparative results, including the failed prose score](acceptance/ablation/results.json)
- [Final comparative results](acceptance/ablation/results-final.json)
- [Mechanical checks](acceptance/mechanical-checks.txt), [sync checks](acceptance/sync-checks.txt), [sync regression tests](acceptance/sync-regression-tests.txt)
- [Independent review](acceptance/independent-review.md)

All changes are reversible local files. `pre-spine-rebuild` identifies the original pre-rebuild state; `9fa82c1` identifies the continuation base. Revert the continuation commit to undo only this completion work. Testing made no publication or changes to keynote-create. Publication of this verified rebuild is now user-authorized.

Final independent acceptance review: READY for integration, with no unresolved material findings. Runtime hashes match the tested files. Local commit and authorized publication follow this recorded review.
