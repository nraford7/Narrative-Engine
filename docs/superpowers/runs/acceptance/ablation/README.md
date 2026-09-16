# Rebuilt Narrative Engine: comparative acceptance

**Final numerical acceptance: PASS after one targeted prose repair. Initial acceptance: FAIL on prose naturalness alone.** This is a model-confounded comparison, not an exact reproduction with the historical generator. All original and rerun scores are retained.

## Results

| Source / format | Rebuilt rank | Old A rank | Spine B rank | Rebuilt hook | Chain | Fidelity | Payoff | Natural |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Astra / boardroom | 2 | 3 | 1 | 6.5 | 7.5 | 10 | 8 | 7.5 |
| Lease / boardroom | 1 | 3 | 2 | 8 | 9.5 | 10 | 9.5 | 8.5 |
| Launch / boardroom | 1 | 3 | 2 | 6.5 | 8.5 | 10 | 8.5 | 8 |
| Churn / boardroom | 1 | 3 | 2 | 8 | 9 | 10 | 9 | 9 |
| Astra / prose, initial | — | — | — | 7.5 | 8.5 | 9.5 | 8.5 | **7 (FAIL)** |
| Astra / prose, sole repair | — | — | — | 7.5 | 8.5 | 9.5 | 8.5 | **8 (PASS)** |
| Launch / keynote | — | — | — | 7.5 | 9 | 9.5 | 9 | 8.5 |

Rebuilt beats saved old A on **4/4** sources and ranks above saved spine B on **3/4**. Boardroom mean fidelity **10.0 ≥ 7.0**, mean naturalness **8.25 ≥ 7.5**. Final prose and keynote each clear fidelity ≥7 and naturalness ≥7.5.

The same blind judges rescored the saved baselines in this comparison. Their boardroom means were:

| Arm | Hook | Chain | Fidelity | Payoff | Natural |
|---|---:|---:|---:|---:|---:|
| Saved old A | 8.375 | 8.000 | 4.250 | 7.875 | 5.375 |
| Saved spine B | 8.250 | 8.000 | 6.750 | 9.000 | 7.625 |
| Rebuilt | 7.250 | 8.625 | 10.000 | 8.750 | 8.250 |

Rebuilt gains **5.75 fidelity points** and **2.875 naturalness points** over old A, while hook falls **1.125 points**. It gains fidelity and naturalness over B but loses hook and 0.25 payoff points. Overall ranking is the judge's holistic ranking, not an invented weighted composite. Astra boardroom remains behind B; the fidelity win does not eliminate the engagement tradeoff.

## Method and run accounting

- Six final-generation samples: four boardroom decks, one Astra prose piece, one launch keynote deck. Generator: **gpt-5.6-sol, medium** via fresh ephemeral Codex CLI contexts. Writers received only the saved source, audience/ask, output contract, and one hashed rebuilt-runtime snapshot; no old outputs, scores, identity maps, or acceptance thresholds.
- The original Claude generator was checked once and returned its session-limit error. The saved baseline report does not record its exact generation model/version. The change of generator is a material confound: these results establish observed output quality, not that the skill alone caused the difference.
- Rebuilt generation was **solo-simulated**, matching the historical arm's solo-simulation limitation. Its initial internal gates are self-checks, not independently blind subagents. This experiment does not prove the orchestrated file-state protocol; the separate protocol scenarios cover that requirement.
- Six independent initial **gpt-6-astra, medium** scoring contexts used the saved five-dimension rubric: hook, chain, fidelity, payoff, naturalness. Four comparisons presented exact saved old-A and B bodies alongside rebuilt bodies, with deterministic shuffled anonymous numbers. Judges saw only source, audience/ask and bodies, and had no runtime, prior scores, thresholds or identity map. The prose chain test uses section openings; keynote uses beat plus narration.
- One permitted failed-slice revision and one independent blind score rerun followed. All four boardroom outputs and the keynote remained unchanged. Seven acceptance scoring calls total; no score rerolls, averaging of retries, or hidden second repair.
- Two preliminary pre-fix generation samples finished before the parent finalized runtime repairs. They were never judged, were not used to optimize final outputs, and are preserved privately under `pre-fix-unjudged/`. All six measured initial samples use the same final snapshot. No runtime change was made for the prose retry.

## Diagnosis and targeted repair

The initial prose judge found strong fidelity but repeated source-process references and duplicated qualifications that made the writing sound adapted from a briefing. The immediate service introduction also reduced curiosity. The first generation's source-conscious self-check did not catch that it was exposing the production process to the reader.

The sole revision removed backstage references, shortened duplicate research-note caveats while retaining the material limits beside their claims, and replaced the early branded service reference with the audience-relevant invitation. Other sections and the closing ask were preserved. The private draft changed from 1,360 to 1,301 words. The original draft, exact diff, flag input, dispatch and every score are retained.

The repair writer's self-check was advisory. An independent Astra evidence recheck compared the exact diff and dependencies with the full source: **CLEAN**, zero findings, five provenance spot-checks. A separate body-only Astra reread inferred the intended claim and ask and confirmed that the ending answers the opening. It still identified slower evidence/administrative passages; those observations were retained without another edit. The resolved humanizing trigger was archived. The final independent acceptance score raised naturalness from 7 to 8 with fidelity unchanged at 9.5.

## Assessment and limits

- **Evidence reviewer perspective — agreement:** independent scoring consistently rewards preserved scope, estimates and causal qualifications. Source fidelity is not external verification that every source claim is true.
- **Narrative editor perspective — qualified agreement:** less manufactured drama improves naturalness; answer-first openings lose some curiosity, and Astra boardroom still loses to B. A further hook-focused experiment would be separate work, not an extra acceptance rerun.
- **Decision-owner perspective — agreement after repair:** every fixed numerical threshold now passes; the initial prose failure remains explicitly recorded.
- **Methodologist perspective — limitation:** four sources, one sample per arm, one judge model, a generator change, and solo internal simulations limit causal and generalization claims. These are assessment lenses applied to the independent results, not claims of additional independent panels.

No new Agency primitives were generated. No runtime skill, keynote-create file, git commit, or push was performed by this evaluation task. All artifact changes are reversible. Integration still needs the parent's combined acceptance record and review of the separate protocol scenarios.

## Artifacts and reproduction

- `results.json`: immutable initial failure record. `results-final.json`: initial plus final outcome.
- `judge-*.json`: exact numeric scores; Astra qualitative verdicts stay private. Status files record model, effort, elapsed time, prompt hash, and exit code.
- `source-manifest.json`, `runtime-manifest.json`, `private-artifact-manifest.json`: source/runtime and private-output hashes. `harness-verification.json`: exact baseline mapping/body checks, runtime consistency and privacy check.
- `prose-repair-verification.json`: sanitized repair gate evidence. Public synthetic deliverables and audits are included here; no full Astra source, brief, output, diff or judge prompt is included.
- `reproduce.py`: harness. Set `NE_ACCEPTANCE_SCRATCH` to a private directory outside the repo, `NE_ACCEPTANCE_REPO` to the skill checkout, and `NE_ACCEPTANCE_BASELINES` to the saved baseline directory. Commands `prepare`, `write`, `prepare-judges`, `judge`, `summarize` reproduce the initial experiment with fresh samples. They make model calls and overwrite their own generated paths; use a new private scratch directory and separate checkout for a new experiment. The targeted repair is a recorded one-off acceptance action, not an automatic retry loop.

Final private prose: `/Users/noahraford/Documents/Codex/2026-09-16/i-d-x20/work/acceptance-ablation/astra-prose-rerun.md`. Other confidential artifacts and raw transcripts remain in that private scratch directory; the parent may deliver the prose separately.
