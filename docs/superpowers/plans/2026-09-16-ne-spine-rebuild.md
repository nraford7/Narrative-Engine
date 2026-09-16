# Narrative-Engine Spine Rebuild Implementation Plan

> **For agentic workers:** This run executes under /do-it — Agency execution, chunk-boundary reviews. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Rebuild Narrative-Engine so the ablation-winning minimal spine is the build core, catalogs become judge/orchestrator reference, Gate 2 reads blind, and a new evidence gate holds the source.

**Architecture:** Generation minimal, judgment rich. Three agent contracts (builder / focal judge / evidence reviewer) exchange RUN_DIR files; SKILL.md orchestrates; catalogs feed the brief compiler and judges only. All artifacts are markdown; verification is grep gates + check-sync + two protocol scenarios + the ablation re-run.

**Tech Stack:** Markdown skill files; bash grep gates; `scripts/check-sync.sh`; Workflow-based scenario runs judged by gpt-6-astra (medium) via codex CLI.

**Spec:** `docs/superpowers/specs/2026-09-16-ne-spine-rebuild-design.md`

## Global Constraints

- keynote-create is OUT of scope and must not be touched (`~/.claude/skills/keynote-create/**` — zero edits; `deck-title-craft.md` embed content unchanged except the one-word re-sync noted in Task 3.4).
- Must survive intact: RUN_DIR handoff architecture, cold-read-before-brief protocol shape, verdict taxonomy + careful-editor test, content-driven length ("menu, not a checklist"), prose-craft Tier-1 floor, chain/antecedent/stranger/flat test battery.
- No unconditional ornament mandates anywhere in builder-facing files; ornament is licensed by the source, never required.
- Every claim-bearing output element traces to a source passage (trace-to-source rule appears in builder and evidence-reviewer contracts).
- `ne-output.md` is body-only; all metadata lives in `ne-output-meta.md`. The focal judge NEVER receives the sidecar; the evidence reviewer DOES.

## RUN_DIR file contract (single source of truth for all tasks)

| File | Written by | Read by |
|---|---|---|
| `ne-build-brief.md` | orchestrator (P3.5) | builder, judge (Phase B only), evidence reviewer, reviewers |
| `ne-source-content.md` | orchestrator | builder, judge (Phase A2 only), evidence reviewer, reviewers, stress-testers |
| `ne-output.md` (BODY ONLY) | builder | everyone |
| `ne-output-meta.md` (sidecar: focal statement, shape + register, argument outline, sourcing summary + per-section tags, revision notes) | builder | evidence reviewer, orchestrator — NEVER the focal judge |
| `ne-cold-read.md` | judge Phase A | judge Phase B, builder (revision) |
| `ne-focal-judge.md` | judge Phase B | orchestrator, builder (revision trigger #1) |
| `ne-focal-judge-prior.md` | orchestrator rotation | judge (pattern detection) |
| `ne-evidence-review.md` | evidence reviewer | orchestrator, builder (revision trigger #2) |
| `ne-humanizing-flags.md` | orchestrator (P4.7, flag-only) | builder (revision trigger #3) |

Builder revision-mode trigger priority: `ne-focal-judge.md` > `ne-evidence-review.md` > `ne-humanizing-flags.md`. Orchestrator deletes a trigger file when its findings are resolved; end-of-loop cleanup deletes all three triggers + prior + sidecar is kept until delivery.

---

## Chunk 1 — Agent contracts (prompts/)

### Task 1: Rewrite `prompts/builder.md` around the spine

**Files:**
- Modify: `prompts/builder.md` (full rewrite, ~180 lines replacing 452)

**Interfaces:**
- Consumes: `ne-build-brief.md` (carries: focal statement, audience + ask, argument outline, shape [answer-first | withheld-reveal | named-arc-with-cited-beats], deck register [boardroom | keynote] when presentation, density, voice essentials, kept-beat pacing notes pasted verbatim).
- Produces: `ne-output.md` body-only; `ne-output-meta.md` sidecar (exact section list below). Revision mode honors the trigger priority in the RUN_DIR contract.

- [x] **Step 1: Replace the file with the new contract.** Structure (write in full):

1. *Mode detection* — keep the current file-presence self-routing, generalized: check for `ne-focal-judge.md`, then `ne-evidence-review.md`, then `ne-humanizing-flags.md`; any present → Revision Mode against that file's findings (highest priority wins); none → Initial Build.
2. *Inputs* — brief (primary, the sole rule source: "a rule that is not in the brief does not exist for this build" — NO catalog references anywhere, NO legacy fallback), source content, and exactly four craft files: `prose-craft.md`, `prose-craft-constructions.md`, `deck-title-craft.md` (presentation only), `humanizing-pass.md` (Tier 2 checklist only).
3. *THE SPINE* (the build procedure — copy verbatim):

```
1. MATERIAL ANCHOR. Re-read the brief's Material Read and argument outline. Your job is to
   execute THAT argument for THAT audience — not to decorate it.
2. CLAIM. The brief's focal statement is the governing claim. Every section serves it.
3. SHAPE. Follow the brief's shape. ANSWER-FIRST: the claim lands by slide/section 2; the
   middle defends it in the outline's grouped reasons; the close returns to the ask.
   WITHHELD-REVEAL (only if the brief says so): stakes first, the reveal at its natural
   midpoint, consequences after. NAMED ARC (only if the brief says so): follow the pasted
   beat skeleton and its pacing notes; beats without cited source support were already cut.
4. TITLES/SECTIONS AS A CHAIN. Each title (deck) or section opening (prose) is a short
   complete sentence delivering one beat, carrying its setup or resolving the prior thread.
   Keynote register: fragments are the register; complete sentences are rationed for the
   3-4 lines meant to land; the chain test applies to the beat + narration read instead.
5. TEST, THEN REVISE ONCE. Titles-only/spoken-prose test + antecedent test + stranger test
   (per deck-title-craft.md; register-appropriate variant). For prose: read section openings
   in sequence as one paragraph — same chain standard. One revision pass.
6. BANS. No label titles. No reflex rhetorical hedging the source does not require ("may
   potentially", "could arguably", "appears to" as filler) — but evidentiary qualifications
   the SOURCE carries (may / estimated / preliminary / correlational) are PRESERVED; stripping
   one is an evidence-review failure, not a style win. No "Not X, but Y" scaffolds. No
   manufactured surprise or performed emotion. No invented facts, examples, or drama: every
   claim-bearing title and paragraph must trace to a passage in the source. No jargon the
   audience lacks.
7. LICENSED ORNAMENT (never required). If — and only if — the source or your draft yields a
   genuinely quotable line, a real reversal, or a natural register shift, you may place it at
   an anchor moment (opening, turn, close). A plain, well-supported sentence passes unchanged.
   Never pre-draft a "killer line"; never impose a metaphor family; never rotate grammatical
   forms for variety.
8. CRAFT FLOOR. Run the prose-craft Tier-1 pass (Ceiling/Filter/Floor) on prose paragraphs, or
   on titles only for decks. Then run the Tier-2 structural-delta checklist from
   humanizing-pass.md as a self-check — flag-and-fix once, never optimize against it.
   Carve-outs: the answer-first opening statement (prose) and the title chain (decks) are
   protected from the theme-statement budget; it governs mid-piece restatements only.
9. LENGTH. Content-driven. Count the source's substantive points; a strong 8-slide deck beats
   a padded 20-slide deck; skip outline sections the source cannot fill.
```

4. *Output* — `ne-output.md`: ONLY the deliverable body (deck: punchline line + title-sequence list + slides; prose: title + sections). `ne-output-meta.md`: `## Focal Statement`, `## Shape & Register`, `## Argument Outline (as executed)`, `## Sourcing Summary` (per-section [DIRECT]/[PARAPHRASE]/[ELABORATED]/[GENERATED] tags by section/slide number + originality %), `## Revision Notes` (appended per revision pass — never in ne-output.md).
5. *Revision Mode* — read trigger file + `ne-output.md` + brief (+ `ne-cold-read.md` if present); smallest edits that close the findings; re-run Step 8 (Tier-1 + bans) on every edited section; update sidecar Revision Notes; never strip sourcing tags.

- [x] **Step 2: Verify with grep gates.**

Run: `grep -n "Focal Statement:" prompts/builder.md | grep -v meta` → no hits placing focal in ne-output.md; `grep -n "voice-profiles\|audience-profiles\|emotional-arcs\|opening-closing\|narrative-arcs" prompts/builder.md` → zero hits; `grep -in "must contain\|at least one candidate\|2-3 times\|metaphor family" prompts/builder.md` → zero ornament mandates; `grep -n "Not X, but Y" prompts/builder.md` → 1 hit (the ban itself).

### Task 2: Rewrite `prompts/focal-fidelity-judge.md`

**Files:**
- Modify: `prompts/focal-fidelity-judge.md` (~230 lines replacing 195)

**Interfaces:**
- Consumes: `ne-output.md` (body-only), `ne-build-brief.md` (Phase B), `ne-source-content.md` (Phase A2), `ne-focal-judge-prior.md` (Phase C).
- Produces: `ne-cold-read.md`, `ne-focal-judge.md` with verdict ∈ {PASS, NEEDS_REVISION, FRAMEWORK_MISMATCH, FOCAL_MISMATCH} + `needs_revision_count` field.

- [x] **Step 1: Rewrite with these protocol changes** (keep the cold-read-before-brief shape, the verdict criteria style, the careful-editor test, and the anti-patterns section):
  - Phase order: **A** cold read (body-only file; add to the cold-read template: "What question does the opening raise?", "Where does interest drop?", "Does the ending answer the opening?") → **A2** read `ne-source-content.md`; answer: "Does the source contain a claim more consequential FOR THE AUDIENCE AND ASK STATED IN YOUR DISPATCH MESSAGE than the piece's apparent One Thing? Quote the passage and argue the audience relevance, or state none." **The orchestrator's dispatch message supplies audience, ask, and register — never the focal** (Task 5 specifies this dispatch contract) → **C** read prior judgment if present (BEFORE writing any verdict) → **B** read brief, compare, write verdict.
  - Verdicts: keep PASS/NEEDS_REVISION/FRAMEWORK_MISMATCH criteria; add **FOCAL_MISMATCH**: A2 found an audience-relevant, source-supported more-consequential claim → verdict routes the orchestrator to reopen P1.75. Guards (verbatim): "FOCAL_MISMATCH triggers an automatic reset ONLY when the brief marks `focal_origin: inferred` (Fast mode, user never touched the focal line). For `user-selected`, `user-stated`, or `user-selected-after-reset`, downgrade to an ADVISORY inside your verdict file — surface the quoted passage, never reset. One automatic reopen per run; any second mismatch is advisory regardless of origin."
  - Engagement feeds the verdict: a piece whose opening raises no question or whose ending ignores the opening cannot PASS on semantics alone → NEEDS_REVISION with the specific gap.
  - Deck branch: "If the output is a deck: your Phase A cold read is the concatenated title sequence FIRST (run the spoken-prose + antecedent tests from `deck-title-craft.md`; Boardroom register) or the beat + narration read (Keynote register, per the brief's register — you receive register in the dispatch message, not the sidecar); a broken chain forces NEEDS_REVISION regardless of focal match."
  - Verdict file carries `needs_revision_count: N` (prior count + 1 on each NEEDS_REVISION); escalation rule keyed to the counter, not free-text memory.
- [x] **Step 2: Verify.** `grep -n "ne-output-meta" prompts/focal-fidelity-judge.md` → zero hits; `grep -c "FOCAL_MISMATCH" prompts/focal-fidelity-judge.md` → ≥3; `grep -n "titles-only\|spoken-prose" prompts/focal-fidelity-judge.md` → ≥1 hit.

### Task 3: Create `prompts/evidence-reviewer.md`

**Files:**
- Create: `prompts/evidence-reviewer.md` (~90 lines)

**Interfaces:**
- Consumes: `ne-output.md`, `ne-output-meta.md`, `ne-source-content.md`, `ne-build-brief.md`, `ne-cold-read.md`.
- Produces: `ne-evidence-review.md` with verdict CLEAN | FINDINGS and a numbered findings list (severity, location, the source passage vs the output claim, required fix).

- [x] **Step 1: Write the contract.** Single obsession: "Does the piece claim only what the source supports?" Checks (each with a one-line method): unsupported claims (claim-bearing sentence/title with no traceable source passage); altered qualifications (correlation→causation, hedge-stripping, "may"→"will", subgroup→universal); missing reasoning (conclusion whose supporting step was cut); ask overreach (the ask exceeds what the argument establishes — flag, propose the supportable ask); sourcing-tag spot-check (sample ≥3 [DIRECT]/[PARAPHRASE] tags against the source verbatim). Style/taste explicitly out of scope. Verdict criteria + the two-run cap note ("your second run re-checks changed sections only").
- [x] **Step 2: Verify.** `grep -n "correlation\|qualification" prompts/evidence-reviewer.md` → ≥2 hits; file referenced by SKILL.md after Task 5.

### Task 4: Patch `prompts/reviewer.md` + `prompts/stress-tester.md` inputs

**Files:**
- Modify: `prompts/reviewer.md` (input list section), `prompts/stress-tester.md` (input list + delete its auto-selection table)

- [x] **Step 1:** Add `RUN_DIR/ne-source-content.md` to both prompts' inputs with: "Spot-check claims against the source; a verdict on sourcing you did not check is a guess." In `stress-tester.md`, delete the persona auto-selection table and replace with: "Personas are named in your dispatch message; the selection table lives in SKILL.md Phase 5.5 (single source)." In `reviewer.md`, delete its Content-Type → Reviewer mapping table the same way: "Reviewer roles are named in your dispatch message; the mapping table lives in SKILL.md Phase 5 (single source)."
- [x] **Step 2: Verify.** `grep -n "ne-source-content" prompts/reviewer.md prompts/stress-tester.md` → ≥1 hit each; `grep -c "Investor pitch" prompts/stress-tester.md` → 0; `grep -c "Investor pitch" prompts/reviewer.md` → 0.

**Chunk 1 review gate (medium):** Stage 1 ∥ Stage 2 on the combined prompts/ diff, then commit `feat: rebuild agent contracts — spine builder, blind judge with FOCAL_MISMATCH, evidence reviewer`.

---

## Chunk 2 — Orchestrator (SKILL.md + framework-selection.md)

### Task 5: Rewrite `SKILL.md`

**Files:**
- Modify: `SKILL.md` (full rewrite of phase sections; keep frontmatter description updated in place, subagent-architecture table updated to the RUN_DIR contract above)

**Interfaces:**
- Consumes: contracts from Tasks 1-3. Produces: the orchestration every prompt relies on.

- [x] **Step 1: Rewrite phases** (workflow overview diagram, phase sections, quick start — all consistent):
  - P1 import, P1.25 Fast/Guided (unchanged mechanics; Fast ALWAYS surfaces focal candidates — see P1.75), P1.5 format (+ **register question when Presentation**: Boardroom sentence-titles / Keynote fragments, default Boardroom, inferred in Fast and surfaced).
  - P1.75: audience + ask first (one line; skip only if stated) → Material Read (stake · tension · genuine-surprise-or-"none — never manufacture one" · strongest existing passages · what changes) → 2-3 stance-committing candidates, each passing the quality bar (one breath; claim/recommendation/reframing never a topic; specific; answers a question this audience cares about). User-stated points are tested against the bar; sharpened versions offered alongside, original always valid. **Fast mode: candidates appear in the consolidated brief, one line each, chosen one marked.** Brief records `focal_origin: inferred | user-selected | user-stated | user-selected-after-reset` (inferred = Fast mode with the focal line never touched by the user; user-selected = user picked or edited a candidate; only `inferred` is eligible for automatic FOCAL_MISMATCH reset).
  - P2 trimmed discovery (audience skip-if-answered; purpose; content type; tone), P2.5 density (unchanged).
  - P3 **Argument Outline** (replaces framework sweep as the primary step): a plain-language account — what this audience needs to understand, in what order, what each section adds; "the sequence must make sense with no framework labels and no dramatic vocabulary." Then **conditional shape**: answer-first default; withheld-reveal only when the Material Read named a genuine surprise; a named arc from `framework-selection.md`'s payload table only when every essential beat is matched to a QUOTED source passage (unmatched → arc rejected, note in brief); "no named framework — direct explanation" is a first-class outcome. Skeleton stamp test retained for any named arc.
  - P3.5 Build Brief: **the template is REPLACED, not extended.** Removed outright: the "Killer Line Target" section (pre-drafting is forbidden — ornament is licensed in the builder's spine only), and matrix-driven opening/closing strategy selection. New template sections: Focal Statement + `focal_origin`; Material Read (pasted in full — the builder's Step 1 anchor); Argument Outline; Shape + Register; Density; Voice essentials; Audience essentials; kept-beat pacing notes pasted verbatim when a named arc was chosen (never one-line shape strings); optional Opening/Closing note ONLY as a pointer to a specific strongest passage from the Material Read ("open on the 9:14 scene"), never a strategy-type from the catalog matrix.
  - P4 dispatch: builder per Task 1; handoff table = RUN_DIR contract; **judge dispatch message contract: carries audience, ask, and register verbatim — never the focal or killer-line text.**
  - P4.6: judge per Task 2; orchestrator routing for all four verdicts (FOCAL_MISMATCH → reopen P1.75 once when `focal_origin: inferred`, mark `user-selected-after-reset` on the new choice; advisory handling otherwise); rotation + counter mechanics; cleanup rules per contract.
  - P4.7: flag-only Tier-2 check → `ne-humanizing-flags.md` → the shared repair loop.
  - P4.8: evidence reviewer per Task 3; blocking; two-run cap; unresolved → escalate to user with the findings file.
  - **Shared repair loop (one contract for ALL post-build revisions, any trigger):** after any builder revision pass — regardless of which trigger file caused it — (a) the builder has re-run Tier-1 + bans on edited sections (Task 1); (b) the orchestrator ALWAYS re-runs the evidence reviewer on the changed sections (counts against its two-run cap); (c) the orchestrator triggers one judge re-read whenever the revision touched the governing claim, the ask, the climax, or the close — whichever gate originated the revision; (d) resolved trigger files are deleted; (e) caps: evidence reviewer 2 runs total, judge NEEDS_REVISION counter per its existing 3-cap — any cap breach escalates to the user with the findings files.
  - P5/5.5: reviewers get source; **single-source dispatch tables live here** (add "Company/product origin story → Audience Advocate + Originality Agent" row); stress-test table restored to the four high-stakes types + 3-persona rule.
  - Reference-files table updated: catalogs labeled "orchestrator/judge reference — never builder input"; `prompts/evidence-reviewer.md` row added.
- [x] **Step 2: Verify.** `grep -n "Score all 10\|full sweep\|Full Sweep" SKILL.md` → 0; `grep -c "ne-output-meta" SKILL.md` → ≥2; `grep -n "FOCAL_MISMATCH" SKILL.md` → ≥2; `grep -n "argument outline" SKILL.md -i` → ≥3; `grep -n "keynote-create" SKILL.md` → references remain descriptive only (render stage), no Stage 1-2 suppression clause.

### Task 6: Rewrite `framework-selection.md`

**Files:**
- Modify: `framework-selection.md` (protocol section replaced; matrices demoted)

- [x] **Step 1:** Replace the Selection Protocol with: Step 0 reveal gate (Material Read's surprise line gates engagement arcs; "never invent a surprise to unlock an arc"); Step 1 payload match via the existing Focal Fit Definition table (2-4 candidates max); Step 2 **beat-support audit** (for each candidate: every essential/anchor beat matched to a quoted source passage; any unmatched beat rejects the arc — no [GENERATED] backfill); Step 3 skeleton stamp test — **the stamp conditions and three Y/N pass criteria kept verbatim, but candidate selection and failure routing REWRITTEN for the new flow**: candidates come from Steps 0-2 (never "by Total score"), and when no candidate passes, the routing is "widen to adjacent payload kinds once, else fall back to no-framework direct explanation" (never "re-weight Focal Fit"); Step 4 recommend with a trace-to-material line per candidate + the explicit no-framework option. Delete the 1-5 dual-scoring sweep and its blank table. Mark everything below the protocol: "Reference matrices — tie-breakers only; never generate candidates from them."
- [x] **Step 2: Verify.** `grep -n "Context Fit" framework-selection.md | head -3` → appears only in reference/tie-breaker prose, not as a scored dimension; `grep -c "quoted source passage" framework-selection.md` → ≥2; Focal Fit Definition table intact (`grep -n "kind of payload" framework-selection.md` → ≥1).

**Chunk 2 review gate (medium):** Stage 1 ∥ Stage 2 on the combined diff, commit `feat: content-first orchestration — argument outline, conditional shape, blind-gate routing, evidence gate`.

---

## Chunk 3 — Reference sweep

### Task 7: Catalog headers + exemplar legality

**Files:**
- Modify: `narrative-arcs.md`, `voice-profiles.md`, `audience-profiles.md`, `emotional-arcs.md`, `opening-closing-strategies.md`, `communication-frameworks.md`, `rhetorical-figures.md` (header note each); `voice-profiles.md`, `checklists.md`, `opening-closing-strategies.md` (exemplar rewrites); `attention-loop.md` (line 31); `humanizing-pass.md` (single-owner + carve-outs); `checklists.md` (killer-line section)

- [x] **Step 1: Header note** (verbatim, top of each catalog under the title): `> **Reference layer.** Read by the orchestrator (brief compilation, shape selection) and by judges/reviewers. Never read by the build subagent — a rule that matters is compiled into the Build Brief.`
- [x] **Step 2: Exemplar sweep.** Rewrite Filter-illegal exemplars (the negative-parallelism constructions banned at zero by `prose-craft.md`): `voice-profiles.md` Provocateur Inversion signature + TED close example; `checklists.md` Strong Killer Line examples (replace the three negative-parallelism ones with Filter-legal lines of equal force); `opening-closing-strategies.md` Contradiction opening exemplar. Each rewrite keeps the strategy, changes only the construction.
- [x] **Step 3:** `attention-loop.md` line 31: "caps at one per piece" → "bans outright (zero per piece)". `humanizing-pass.md`: ownership line → "Tier 2 runs INSIDE the build (builder self-check); Phase 4.7 verifies and flags only — repairs go through the builder's revision route"; add the carve-out sentence (answer-first opening + title chains exempt from the theme budget; mid-piece restatements only); **rewrite Tier-2 delta #5 (idiosyncrasy) from a production quota to a conditional detector**: "flag templated sameness where it appears; when the source offers a concrete particular, prefer it over an abstraction — but a plain, well-supported section is NOT a failure, and no 'un-templatable moment' may be manufactured to satisfy this check." `checklists.md` killer-line section: reframe from mandate to license ("A piece MAY carry a killer line when the material yields one — harvested from the draft or the source, never pre-drafted; absence is not a failure").
- [x] **Step 4: Verify.** `grep -L "Reference layer" narrative-arcs.md voice-profiles.md audience-profiles.md emotional-arcs.md opening-closing-strategies.md communication-frameworks.md rhetorical-figures.md` → empty; `grep -n "one per piece" attention-loop.md` → 0; `grep -in "problem isn't\|isn't that\|question isn't" voice-profiles.md checklists.md opening-closing-strategies.md` → 0 in exemplar positions.

### Task 8: Fix the worked example + SYNC note

**Files:**
- Modify: `examples/remote-work-example.md` (slides 1 + 4), `deck-title-craft.md` (one word), `SYNC.md` (date)

- [x] **Step 1:** Rework the example so slide 1 and the Turn carry different payloads: slide 1 keeps the answer-first recommendation ("Fully remote outperformed hybrid by 23% — rebuild the team model around it"); slide 4's Turn reveals the MECHANISM (belonging predicted retention better than compensation), deleting "The data surprised us." Sweep the example for the removed machinery (killer-line mandate references, metaphor-family notes) and align its intro text with the spine flow.
- [x] **Step 2:** `deck-title-craft.md` §5: "earn attention" → "hold attention" (re-sync to canonical; embed banner re-synced date updated); `SYNC.md` Last synced column updated.
- [x] **Step 3: Verify.** `grep -n "data surprised us" examples/remote-work-example.md` → 0; `bash scripts/check-sync.sh` → deck-title-craft pair OK.

**Chunk 3 review gate (medium):** Stage 1 ∥ Stage 2 on combined diff, commit `fix: reference layer — catalog banners, Filter-legal exemplars, single-owner Tier 2, licensed killer lines, example de-theatered`.

---

## Chunk 4 — Verification & acceptance

### Task 9: Grep-gate script

**Files:**
- Create: `scripts/check-rebuild.sh` (the spec's mechanical gates as one script)

- [x] **Step 1:** Write the script: the Task 1-8 grep gates above, exit 1 on any failure, `OK`/`FAIL` per line. Include: no builder-facing catalog references; body-only output template; no unconditional ornament mandates; attention-loop fixed; headers present; stress-tester table single-sourced.
- [x] **Step 2:** Run: `bash scripts/check-rebuild.sh` → exit 0. Commit `test: add rebuild grep gates`.

### Task 10: Protocol scenarios + ablation re-run (binding acceptance)

**Files:**
- Create: `docs/superpowers/runs/2026-09-16-ne-spine-rebuild-acceptance.md` (results record)

- [x] **Step 1: Scenario (i) focal-mismatch path — both legs mandatory.** Fixture files first: write `docs/superpowers/fixtures/focal-mismatch-brief.md` (weak focal "retention metrics held steady in Q3", `focal_origin: inferred`, audience "the executive team at the budget offsite", ask "choose option (c)") and reuse the saved churn source verbatim. Leg 1: run the rebuilt pipeline from that brief. Expected: judge Phase A2 quotes the 2.3×-discount passage, emits FOCAL_MISMATCH; P1.75 reopens once. Leg 2 (**forced, never conditional**): after the reopen, deliberately select a second focal that still excludes the discount finding, marked `user-selected-after-reset`; re-run the judge. Expected: ADVISORY inside the verdict, verdict itself is NOT FOCAL_MISMATCH-reset — no second reopen. Record both verdict files next to the fixture.
- [x] **Step 2: Scenario (ii) evidence-repair path.** Run the rebuilt builder on the churn source, then plant one causation overclaim into the draft ("discounts caused the churn"); dispatch the evidence reviewer. Expected: FINDINGS names the altered qualification with both passages; builder revision resolves; evidence re-check CLEAN; judge re-read clean; trigger files cleaned up. Verify the judge's input transcript contains no focal metadata.
- [x] **Step 3: Ablation re-run.** Arm A′ = rebuilt pipeline (solo-simulated exactly like old-A was) on the 4 saved sources + one prose output (Astra source) + one Keynote-register deck (launch source). Blind astra judging (same protocol/criteria, decks shuffled) of A′ vs SAVED old-A and B decks per source. Acceptance: A′ > old-A on 4/4; A′ mean fidelity ≥ 7.0, mean natural ≥ 7.5; A′ ≥ B on ≥2 sources; prose + keynote outputs each fidelity ≥ 7, natural ≥ 7.5.
- [x] **Step 4:** Record all results in the acceptance file; if any criterion fails → fix, re-run the failed slice once; a second failure escalates to the user with the numbers. Commit `test: acceptance — protocol scenarios + ablation re-run results`.

**Chunk 4 gate:** results reviewed (Stage 1 on the acceptance record), then final commit; push per Step 5 rules (master push requires explicit user confirmation).

---

## Self-review notes

- Spec coverage: P1.75/P3/P3.5/P4/P4.6/P4.7/P4.8/P5 changes → Tasks 1-6; reference repairs → Tasks 7-8; success criteria 1/1b/3 → Tasks 9-10; criterion 2 (traceability) → the audit-cluster mapping is embedded per-task above (clusters 1→T5, 2→T1+T7, 3→T1+T2, 4→T6, 5→T7, 6→T1+T5, 7→T1, 8→T1(carve-outs)+T7, 9→T2, 10→T2+T5, 11→T1(revision re-runs Tier-1), 12→T4, 13→T1(instruction-load cut), 14→T4+T5(tables), 15→T2(order+counter), 16→T8).
- Deferred (recorded, out of scope): keynote-create-side handoff modernization (mode/spine contract) — separate future run; the builder instruction-load tiering beyond the rewrite itself (the rewrite cuts builder-required reading from ~110KB to ~60KB: brief + 4 craft files).
- Type consistency: file names and verdict strings match across Tasks 1/2/3/5 (checked against the RUN_DIR contract table).

## Verified audit-cluster traceability

| Cluster | Implemented change | Primary locations |
|---|---|---|
| 1. Hook discovery and escape route | Audience/ask before Material Read; surfaced candidates; guarded focal reset | SKILL P1.75/P4.6; focal judge |
| 2. Compulsory ornament | Licensed ornament; embedded craft quotas removed; source-supported plain writing valid | builder spine; prose-craft; humanizing-pass; checklists |
| 3. Contaminated cold read | Body-only output; separate metadata; ordered cold-read protocol | builder output; focal judge Phase A |
| 4. Framework selection and fabricated anchors | Argument first; conditional shape; source-supported beats | SKILL P3; framework-selection |
| 5. Contradictory exemplars | Filter-legal examples and corrected attention-loop cap | voice-profiles; opening-closing-strategies; checklists; attention-loop |
| 6. Half-migrated builder contract | Compiled brief and closed reading list; exact embedded adaptations remove indirect catalog loading | SKILL P3.5; builder inputs; prose-craft |
| 7. Competing title systems | Register captured; source-led title chain takes priority over ornament/variety | SKILL P1.5/P3.5; builder spine |
| 8. Humanizing ownership and post-approval edits | Builder owns edits; flag-only gate; shared repair and revalidation | SKILL P4.7/shared loop; humanizing-pass |
| 9. Engagement review absent | Opening question, attention drop and closing payoff feed verdict | focal judge Phase A/verdict |
| 10. Deck gate unowned | Judge owns register-specific sequence test | focal judge Phase A; SKILL dispatch |
| 11. Revision craft omissions | Recheck Tier 1 and bans on edited sections | builder R4 |
| 12. Reviewers lack source | Source included in specialist and evidence review inputs | reviewer; stress-tester; evidence-reviewer |
| 13. Instruction overload | Short build spine; catalogs moved to orchestrator/reviewer reference | builder; catalog banners; compiled brief |
| 14. Dispatch table drift | Tables single-sourced and origin-story row added | SKILL P5/P5.5; reviewer; stress-tester |
| 15. Prior-judgment order and counter | Prior read before verdict; explicit counter and bounded reset history | focal judge C/B; SKILL hygiene/restart |
| 16. Reveal already revealed in example | Answer-first recommendation with a distinct later mechanism | examples/remote-work-example.md |

Continuation also repaired escalation report retention, full first evidence coverage, independent evidence-count history, and stale-trigger cleanup on an authorized framework restart. These close integration gaps in the approved repair contract. No keynote-create-side work is included.

Acceptance completed in the linked acceptance record. The first prose score failed; one permitted repair/retest passed. The user explicitly authorized updating GitHub after verification.
