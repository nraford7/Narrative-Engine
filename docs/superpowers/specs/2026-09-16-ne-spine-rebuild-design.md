# Spec: Narrative-Engine spine rebuild

Date: 2026-09-16 · Status: draft · Scope: this repo only (keynote-create explicitly untouched)

## Problem statement

Two blind multi-agent audits (39 findings each; 16 verified clusters standalone) and a 4-source × 4-arm blind ablation established:

1. **The generation-side machinery does not help and actively hurts.** Full NE matched a ~300-word minimal spine on hook/chain/payoff but collapsed on fidelity (4.5 vs 7.3) and naturalness (5.8 vs 8.3), judged blind by gpt-6-astra. The spine won all 4 sources; full NE lost to a bare one-line prompt on 3 of 4. Mechanism, named blind: ornament quotas and arc anchor beats fabricate drama ("invents drama the source carefully avoids", "turns possibilities into diagnoses").
2. **The hook has no method, no quality bar, and no escape hatch** (5/5 auditors). Focal chosen before audience, silently in Fast mode, skippable, never re-derivable; no gate can return "wrong focal".
3. **Gate 2 cannot fail**: the builder prints the Focal Statement and Killer Line in the header of the file the "cold" judge reads first (3/5 auditors).
4. **Contradictory rule systems**: builder forbidden from catalogs it is later told to apply (5/5); legacy headline rules vs embedded title-craft (3/5); exemplars teach the construction the Filter bans at zero (2/5); Tier-2 humanizing has two owners (2/5).
5. **Fidelity leaks in every arm, including the winner** — no generation-side prompt fixes it; a separate evidence gate holding the source is required.

## Success criteria (measurable)

1. **Ablation re-run (binding acceptance test):** rebuilt NE (arm A′), run on the same 4 saved sources with the same output contract and blind astra judging against the SAVED old-A and B decks per source: A′ outranks old-A on all 4 sources; A′ mean fidelity ≥ 7.0 and mean natural ≥ 7.5; A′ ranks at or above B on ≥ 2 of 4 sources. **Register/format coverage:** the re-run additionally produces one PROSE output and one Keynote-register deck through the rebuilt pipeline (astra-scored on the same dimensions, threshold: fidelity ≥ 7 and natural ≥ 7.5 each) so the changed workflow is exercised beyond Boardroom decks.
1b. **Protocol regression scenarios (binding):** two scripted end-to-end scenarios with expected artifacts and verdicts: (i) *focal-mismatch path* — a source whose most consequential audience-relevant claim is deliberately excluded from the brief's focal → the judge must emit FOCAL_MISMATCH citing the passage, P1.75 reopens once, and a second pass may not reopen again; (ii) *evidence-repair path* — a draft with a planted causation-overclaim → P4.8 flags it into `ne-evidence-review.md`, the builder revision resolves it, the evidence re-check and judge re-read run clean, trigger files are cleaned up. Scenario transcripts must show the judge read a body-only file (no focal/killer metadata present in its input).
2. **Traceability:** every one of the 16 verified audit clusters maps to a change in this rebuild or a recorded deferral with reason (table in the plan).
3. **Mechanical gates:** `scripts/check-sync.sh` passes; grep gates pass — builder output template contains no `Focal Statement:`/`Killer Line:` metadata; no file instructs the builder to open a profile catalog; no unconditional ornament mandate ("must contain a killer line" phrasing class) survives in builder-facing files; `attention-loop.md` no longer states the stale one-per-piece cap.
4. **No regression in what the audits marked well-designed:** RUN_DIR handoff architecture, cold-read-before-brief protocol shape, verdict taxonomy + careful-editor test, content-driven length, prose-craft Tier-1 floor, chain/antecedent/stranger/flat test battery all survive.

## Proposed approach

### Architecture: generation minimal, judgment rich

The build core becomes the ablation-winning spine. The catalogs are retained but re-homed as judge/orchestrator reference. All rigor points at the two decisions the audits showed are made on vibes — what the claim is, and whether the material supports the shape — plus a new post-build evidence gate.

### Phase changes (SKILL.md rewrite)

- **P1.75 Focal Discovery →** audience + ask first (one line, skip only if stated); then a written **Material Read** (stake · tension · genuine-surprise-or-"none — do not manufacture one" · strongest existing passages · what changes); then 2-3 focal candidates, each committing to a different stance, each passing the quality bar (one breath; claim/recommendation/reframing, never a topic; specific; answers a question this audience cares about). **Candidates are always surfaced, Fast mode included.** A user-stated point is tested against the bar, never silently accepted.
- **P3 Framework Recommendation → P3 Argument Outline + conditional shape.** First a plain-language argument outline: what this audience needs to understand, in what order, what each section adds (the sequence must make sense with no framework labels). Then shape: **answer-first is the default**; a named arc may be layered on only when the Material Read shows the material fills that arc's essential beats — each anchor beat cited to a quoted source passage, or the arc is rejected; **"no named framework — direct explanation" is an explicit, legitimate outcome.** The payload-kind table and skeleton stamp test survive as the fit test; the category matrices become tie-breakers only; the 1-5 double scoring sweep is deleted.
- **P3.5 Build Brief** — compiled as before, now also carrying: the argument outline, the deck register (Boardroom sentence-titles vs Keynote fragments — one new question, NE-side only), and each kept beat's pacing notes pasted verbatim (no one-line shape strings).
- **P4 Build →** `prompts/builder.md` rewritten around the spine plus the craft floor: prose-craft Tier-1 pass, ban list, chain/antecedent/stranger tests, trace-to-source rule (every claim-bearing title/paragraph traces to a source passage), content-driven length. **Ornament becomes licensed, never mandated**: figures, killer lines, register shifts, metaphor families are permitted only when the source yields them; a plain well-supported sentence passes unchanged. No pre-drafted killer line; no grammar-variety rotation; no metaphor-family requirement. **All metadata moves to a sidecar** `RUN_DIR/ne-output-meta.md`; `ne-output.md` is body-only. Revision mode re-runs the Tier-1 pass and the bans on every edited section.
- **P4.6 Gate 2 →** judge reads the body-only file (blind restored); cold read gains one engagement question that feeds the verdict ("what question does the opening raise; where does interest drop; does the ending answer the opening"); **Phase A2**: after the cold read, judge reads the source and answers whether it contains a claim more consequential *for the brief's stated audience and ask* than the brief's One Thing — yes, with the source passage quoted and the audience-relevance argued, triggers the new **FOCAL_MISMATCH** verdict, which reopens P1.75 (distinct from FRAMEWORK_MISMATCH → P3). Guards: (a) automatic reset applies ONLY to a silently inferred focal (`focal_origin: inferred` — Fast mode with the focal line never touched by the user); if the user explicitly stated, selected, or edited the focal, FOCAL_MISMATCH is downgraded to an advisory surfaced with the quoted passage — never an automatic reset; (b) one reopen per run — a focal chosen after a FOCAL_MISMATCH reset cannot be reopened again (the second occurrence surfaces as advisory). Deck branch: concatenated-titles cold read with the titles-only test (Boardroom register) or beat+narration read (Keynote register). Protocol order fixed (read prior judgment before writing the verdict); running NEEDS_REVISION counter carried in each verdict.
- **P4.7 Tier-2 humanizing →** single owner: the builder runs Tier 2 during the build; P4.7 is strictly flag-only — it never edits. Flags are written to `RUN_DIR/ne-humanizing-flags.md` and repaired through the standard revision route (below). **Theme-budget carve-outs:** the answer-first opening statement in prose AND the deck title chain are protected — the budget governs mid-piece restatements only, never the opening a shape requires or the close.
- **NEW P4.8 Evidence Review →** a comparison reviewer receives **the draft (`ne-output.md`) + the sidecar metadata (`ne-output-meta.md`) + source + brief + the judge's cold read**; checks: unsupported claims, altered qualifications (correlation→causation, hedge-stripping), missing reasoning, whether the ask exceeds what the argument supports; spot-checks sourcing tags against the source. Blocking gate on the default path. Findings written to `RUN_DIR/ne-evidence-review.md`.
- **Repair contract (single revision route for all post-build gates):** the builder's revision mode generalizes from one trigger file to a priority-ordered set — `ne-focal-judge.md` (focal drift) > `ne-evidence-review.md` (evidence findings) > `ne-humanizing-flags.md` (Tier-2 drift). Presence of any triggers targeted-edit revision against that file's findings; the orchestrator deletes each trigger file once its findings are resolved and re-runs the gates the edit implicates: any revision re-runs the evidence review on changed sections; a revision touching the climax or close also triggers one judge re-read. Caps: evidence review runs at most twice per draft (initial + one re-check); unresolved findings after the cap escalate to the user with the findings file. End-of-loop cleanup deletes all three trigger files plus the sidecar.
- **P5/5.5 →** reviewers and stress-testers get `ne-source-content.md` in their input lists; dispatch tables deduplicated to SKILL.md as single source; origin-story row added.

### Reference-layer repairs

- Catalog files get a one-line header: reference for orchestrator/judges — never builder input. All builder.md references to catalogs deleted (legacy fallback clause removed with the template that needed it).
- Exemplar sweep: Filter-illegal exemplars (negative parallelism in voice-profiles Provocateur, checklists killer-line examples, opening-closing Contradiction exemplar) rewritten Filter-legal; `attention-loop.md:31` corrected to the zero ban.
- `examples/remote-work-example.md`: the slide-1/slide-4 reveal-theater fixed (answer-first opening keeps the recommendation; the Turn carries the mechanism instead) or the example replaced with the ablation-winning deck as the worked example.

## Alternatives considered

- **Surgical patches only (keep the sweep + quotas, fix wiring):** rejected — the ablation shows the machinery itself, not its wiring, produces the fidelity/naturalness collapse; patched wiring would faithfully deliver the same fabrication.
- **Delete the catalogs entirely:** rejected — audits marked the payload table, skeleton stamp, title-test battery, and Tier-1/Tier-2 material well-designed; judges and the brief compiler use them; deletion loses judge vocabulary for zero gain.
- **Add a hook panel (3 lenses) at P1.75:** rejected — empirically refuted (arm D: fidelity 3.3, worst of four; stance-committed lenses dramatized hooks).
- **Fold the evidence review into the focal judge:** rejected — different question (fidelity to source vs fidelity to intent), different inputs, and single-obsession judges were the audit's praised design.

## Blast radius / rollback

This repo only. No keynote-create edits; no orchestration-contract changes visible to other skills (skill name, invocation, RUN_DIR layout survive; one new sidecar file + one new phase). Rollback: `git tag pre-spine-rebuild` before first change; `git revert` or reset to tag restores old behavior entirely.

## Open questions

- None blocking. Push-to-master requires explicit user confirmation at Step 5 (recorded in manifest).
