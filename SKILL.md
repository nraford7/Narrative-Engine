---
name: narrative-engine
description: "Requires an explicit Fast or Deep choice before work. Transform any content into narrative-driven presentations OR prose through a minimal build spine wrapped in rich judgment — a blind focal judge, a source-holding evidence gate, and content-driven length. Use when converting content to presentations, restructuring existing decks, writing long-form pieces, or optimizing for specific audiences."
---

# Narrative Engine

## Start here — mode gate

For a new piece, first check whether the user explicitly selected **Fast** or **Deep**. If neither was selected, the next response is only the mode question with a brief explanation of the two choices. Stop there: no source analysis, brief, outline, writing or agent dispatch. Do not treat “quick”, “just write it”, or “no questions” as selecting a mode. Asking the mode is part of invoking this skill, not optional discovery. Use this first-response form:

> Choose **Fast** (I infer the framing and show a brief for approval) or **Deep** (we work through the framing together). Neither is selected by default.

If the user explicitly selected a mode for this piece, continue to Phase 1.5. If they explicitly decline this workflow itself, explain that the work would be outside Narrative Engine rather than claiming its process was followed.


Transform content into compelling narratives — as presentations or prose. Content determines length — no padding, no artificial minimums. The architecture: **generation minimal, judgment rich.** The builder gets a small, compiled contract and a short spine; the heavy machinery (catalogs, matrices, cold reads, source audits) lives with the orchestrator and the judges.

## Workflow Overview

```
Import → mandatory Fast / Deep choice
  → Purpose + success → Audience starting position → Format, use, limits
  → Material Read: support, relevance, limits and unknowns
  → Content type + writing treatment → Provisional points
  → Compare reasoning + direct explanation + supported arcs (Gate 1)
  → Approve point and structure together → Compile and check brief
  → Writer: body + private metadata
  → Blind focal/purpose review (Gate 2) → Writing check (Gate 3)
  → Source evidence review (Gate 4) → Targeted review / optional stress test
  → Deliver written prose/presentation; compression and change log on request
```

**Four structural gates protect the work:**

- **Gate 1 (Phase 3)** stops a wrong shape from being chosen. The default is a plain argument outline delivered answer-first; a dramatic shape is admitted only when the material licenses it — a withheld reveal requires a genuine surprise in the Material Read, and a named arc requires every essential beat matched to a quoted source passage plus a passing skeleton stamp test.
- **Gate 2 (Phase 4.6)** catches drift between intent and execution — a blind judge cold-reads the body-only output before ever seeing the brief, names the One Thing, checks the source for a more consequential claim, and compares. Four verdicts: PASS, NEEDS_REVISION, FRAMEWORK_MISMATCH, FOCAL_MISMATCH. For decks, the judge runs the title-chain tests (spoken-prose + antecedent, register-appropriate) as part of its cold read.
- **Gate 3 (Phase 4.7)** catches AI-slop the first two miss — a discourse-level structural-delta check grounded in the narrative-structure research corpus. The evidence: a classifier still detects AI from *structure* at 93.9% after surface lexical cleanup. The orchestrator flags only; repairs go through the builder. See [`humanizing-pass.md`](humanizing-pass.md).
- **Gate 4 (Phase 4.8)** holds the source. An evidence reviewer with the original material open checks that the piece claims only what the source supports — unsupported claims, stripped hedges, hardened correlations, cut reasoning steps, overreaching asks, and mis-tagged provenance. Style is out of its scope; fidelity to the source is its only axis.

**Sentence discipline is always on.** Every prose paragraph and every deck title is built through the **embedded prose-craft discipline** ([`prose-craft.md`](prose-craft.md) + [`prose-craft-constructions.md`](prose-craft-constructions.md)) during the build (Tier 1 of the humanizing pass). It is *embedded, not invoked* — the build subagent reads these files directly, so Narrative Engine runs once with no dependency on a separate skill.

**The builder's reading list is deliberately short.** The brief (the sole rule source — a rule that is not in the brief does not exist for the build), the source content, and exactly four craft files: `prose-craft.md`, `prose-craft-constructions.md`, `deck-title-craft.md` (presentation only), and the Tier-2 checklist in `humanizing-pass.md`. The framework, voice, audience, emotional-arc, opening/closing, and rhetorical-figure catalogs are **orchestrator/judge reference — never builder input**. Anything from them that matters is compiled into the Build Brief. Ornament is licensed by the material, never required: a plain, well-supported sentence passes unchanged, and no killer line is ever pre-drafted.

---

## Subagent Architecture

Phases 1–3.5 run in the main conversation using the selected interaction mode. Phases 4, 4.6, 4.8, 5, and 5.5 run as subagents using fresh isolated agents (Claude Code Task or the host equivalent). Do not fork the conversation into the builder or blind judge. If isolation is unavailable, disclose the limitation and offer a draft; never describe a same-context reread as blind. Phase 4.7 runs in the orchestrator (flag-only).

### Handoff Files

All handoff files live in a per-run directory the orchestrator creates at the end of Phase 3.5: `RUN_DIR = mkdtemp("ne-<topic>-")` (a unique temporary directory). Every dispatch prompt must state the RUN_DIR; the templates refer to files by name and resolve them inside it. Concurrent runs never collide, and deleting the directory cleans up the whole run.

| File | Written by | Read by |
|------|-----------|---------|
| `ne-build-brief.md` | orchestrator (P3.5) | builder, judge (Phase B only), evidence reviewer, reviewers, stress-testers |
| `ne-source-content.md` | orchestrator | builder, judge (Phase A2 only), evidence reviewer, reviewers, stress-testers |
| `ne-output.md` (BODY ONLY) | builder | everyone |
| `ne-output-meta.md` (sidecar: focal statement, shape + register, argument outline, sourcing summary + per-section tags, revision notes) | builder | evidence reviewer, orchestrator — NEVER the focal judge |
| `ne-cold-read.md` | judge Phase A | judge Phase B, builder (revision), evidence reviewer |
| `ne-focal-judge.md` | judge Phase B | orchestrator, builder (revision trigger #1) |
| `ne-focal-judge-prior.md` | orchestrator rotation | judge (pattern detection) |
| `ne-evidence-review.md` | evidence reviewer | orchestrator, builder (revision trigger #2), evidence reviewer (2nd run reads its prior report first) |
| `ne-humanizing-flags.md` | orchestrator (P4.7, flag-only) | builder (revision trigger #3) |

**Builder revision-mode trigger priority:** `ne-focal-judge.md` > `ne-evidence-review.md` > `ne-humanizing-flags.md`. The builder self-routes on file presence — any trigger present means Revision Mode against the highest-priority file.

**The sidecar rule.** `ne-output.md` is the deliverable body and nothing else; all metadata (focal statement, shape, argument outline, sourcing tags, revision notes) lives in `ne-output-meta.md`. The focal judge NEVER receives the sidecar — it would contaminate the cold read. The evidence reviewer DOES receive it and spot-checks its sourcing tags against the source.

### Portable role dispatch

Set `NE_ROOT` to this skill installation’s absolute directory and include it with `RUN_DIR` in every role dispatch. Resolve `NE_ROOT/...` before reading. Use the host’s isolated-agent tool for Task calls; role inputs, read order and review limits remain the same. The original source stays intact in the run directory. For Both, use a separate child run directory per output so verdicts and triggers never cross formats.

### Prompt Templates

| Template | Phase | Dispatch |
|----------|-------|----------|
| [`prompts/builder.md`](prompts/builder.md) | 4 (initial), repair loop (revision) | 1 agent, serial. Self-detects mode via trigger-file presence |
| [`prompts/focal-fidelity-judge.md`](prompts/focal-fidelity-judge.md) | 4.6 | 1 agent, serial. Blind cold read; dispatch message carries audience/ask/register only |
| [`prompts/evidence-reviewer.md`](prompts/evidence-reviewer.md) | 4.8 | 1 agent, serial. Holds the source; two runs max per draft |
| [`prompts/reviewer.md`](prompts/reviewer.md) | 5 | 2 agents, parallel (roles named in dispatch from the Phase 5 table) |
| [`prompts/stress-tester.md`](prompts/stress-tester.md) | 5.5 | 3 agents, parallel (personas named in dispatch from the Phase 5.5 table) |

### File Hygiene

1. **Judge rotation:** before re-dispatching the Focal Judge for a later pass, copy `RUN_DIR/ne-focal-judge.md` → `RUN_DIR/ne-focal-judge-prior.md` so the next pass can do pattern detection and carry the `needs_revision_count` counter forward.
2. **Trigger lifecycle:** a trigger file (`ne-focal-judge.md`, `ne-evidence-review.md`, `ne-humanizing-flags.md`) left in place is the builder's signal to enter Revision Mode. The orchestrator deletes a trigger file when its findings are resolved.
3. **End-of-loop cleanup:** after all gates pass, delete all three trigger files and `ne-focal-judge-prior.md`. Preserve unresolved reports and the sidecar on escalation; attach or link them before ending the run. The sidecar `ne-output-meta.md` is kept until delivery.

---

## PHASE 1: Content Import

Accept content in any form:
- Pasted prose, articles, or reports
- Outlines or bullet points
- Research notes or data
- Existing presentation text
- URLs (fetch and extract)

If user pastes content without instructions, acknowledge receipt and proceed to Mode.

---

## PHASE 1.25: Mode

A mode choice is mandatory for each new piece. Before discovery, outlining or drafting, ask and wait unless the user already explicitly chose a mode for this piece. Revisions retain that choice.

> **How do you want to work?**
> 1. **Fast** — I work through the same analysis, infer missing answers, and show the assumptions, candidate points and structure comparison in one brief for correction or approval.
> 2. **Deep** — we work through unresolved framing questions, then choose the point and how it unfolds together.

**No default mode. Never select Fast automatically.** Urgency, clear instructions, "quick pass", "just write it", "no questions" and permission to proceed are not choices. Ask Fast or Deep and stop until answered. Silence is not a choice. The former name Guided means Deep.

Both modes perform Phases 1.5–3.5 in the same order. Fast infers missing answers and labels assumptions, especially `[INFERRED — LOW CONFIDENCE]`; it never presents assumptions about an audience as known facts. Deep asks one unresolved question at a time, offering the relevant menu and accepting free text; confirm supplied information instead of asking twice. Fast surfaces 2–3 provisional focal candidates unless a supplied point makes alternatives unnecessary, relevant evidence limits, and direct explanation alongside any eligible arc. Neither mode bypasses final brief approval or the review gates.

---

## PHASE 1.5: Assignment — Purpose, Audience, Format and Use

Record these before the Material Read. A quick source inspection to understand the assignment is allowed; do not select a focal or structure yet. User-supplied points are retained as user-owned constraints to test, not replaced by inferred alternatives.

### Purpose and success condition

> **What should this piece accomplish?**

| Purpose | What the source analysis must look for |
|---|---|
| Persuade to act | Reasons for action, alternatives, objections and support sufficient for the proposed action. |
| Inform / Educate | Concepts, mechanisms, misconceptions and examples needed for understanding. |
| Inspire / Motivate | Credible possibilities, meaningful stakes and reasons to engage. |
| Align / Build consensus | Shared facts, differing assumptions, agreements and unresolved disagreements. |
| Report / Update | Changes, results, exceptions, current status and implications. |
| Defend / Justify | The challenged position, objections and evidence addressing them. |
| Entertain / Engage | Interesting observations, scenes, questions or discoveries genuinely present in the material. |

Then establish a concrete success condition: what should the reader understand, be able to explain, decide, feel or do afterward? Choose a primary purpose when purposes compete; record a secondary one only when useful. An action is optional. Keep the internal `Ask` field for compatibility: for education or reflection it means the intended change in understanding, not a forced call to action.

### Audience and starting position

> **Who is this for?** Executive / Board; Technical / Engineering; Sales / Marketing; Investors / VCs; General Public; Skeptics / Resisters; Mixed / Cross-functional; Academic / Research; or a description in your own words.

Establish the relevant existing knowledge, beliefs, concerns and likely objections. Ask only what is unresolved and consequential. Record unknowns as unknown; in Fast, label hypotheses as inferred. The category is a starting point, not evidence about particular people. Do not infer their beliefs from their job title alone.

### Format, intended use and limits

> **What format do you need?** Presentation / Prose / Both.

- **Prose:** establish intended use (article, essay, briefing, report or other), whether it must stand alone, and target length: Short (~500–800 words), Medium (~1,000–1,500), Long (~2,000–3,000), or content-determined. These are targets, not padding quotas; an explicit user limit takes precedence.
- **Presentation:** establish intended use (live talk, workshop, read-ahead or standalone), any speaking-time or slide limit, and whether written narration is needed. Every visible slide counts. This skill produces the written narrative and notes; visual rendering is outside its required workflow.
- **Both:** confirm which format is primary: Prose → Presentation or Presentation → Prose. Approve the shared argument once; adapt it and review each format's actual output. Never assume the first version's verdict certifies the second.

Record required inclusions, exclusions and evidence standards. Capture explicit style preferences now, but resolve detailed treatment in Phase 2. Source material and audience facts may expose an infeasible objective: surface it rather than silently changing the assignment.

---

## PHASE 1.75: Material Read

Read the complete supplied source against the assignment. Record:

- **Supported findings:** claims with quoted or pinpointed source passages.
- **Purpose relevance:** which findings help fulfill the success condition and how.
- **Audience relevance:** which knowledge gap, belief, concern or objection each important finding addresses. Make the connection visible: "Because the audience believes/needs X, passage Y matters because Z." Distinguish user-supplied facts from inferred audience hypotheses.
- **Stake and tension:** what matters and what question is genuinely unresolved; either can be modest. Do not invent conflict.
- **Genuine surprise:** what would be unexpected for this audience, with source support; otherwise "none — never manufacture one". When audience knowledge is unknown, mark surprise as uncertain rather than licensing a reveal on a guess.
- **Strongest existing passages/examples:** 2–3 quoted or pinpointed passages where available; fewer is valid for a short source.
- **What changes:** the supported change in understanding, decision or action.
- **Limits and contrary evidence:** qualifications, alternative explanations, contradictions and scope.
- **Missing information:** what the source cannot establish, including support missing for the user's desired conclusion.

Separate "the user wants to argue X" from "the source establishes X." Do not silently discard contrary evidence. If the assignment requires unsupported claims, explain the gap and offer a narrower claim, more source material, or an explicitly conditional treatment. Do not invent evidence or initiate unrequested research.

Paste this Material Read into the final brief. No focal is locked at this phase.

---

## PHASE 2: Content Type, Writing Treatment and Provisional Points

### Content type

Suggest the best-fitting type from the material; invite correction in Deep or surface it in Fast:

Counterintuitive research findings; Strategic plan / transformation roadmap; Scenario planning / decision fork; Paradigm shift / new mental model; Company/product origin story; Post-mortem / retrospective; Sales pitch; Investor pitch / fundraising; Product launch; Case study; Policy recommendation; Vision/inspiration piece. Accept an unlisted type.

Content type helps choose review expertise and candidate structures. It never selects an arc by itself or changes what the evidence supports. Review dispatch uses the Phase 5 table.

### Writing treatment

Resolve these independently; they are not competing packages:

| Dimension | Choices | Consequence |
|---|---|---|
| Detail | Concise / Standard / Detailed | How much supporting explanation is visible. Never cuts an essential reasoning step or qualification. |
| Assumed knowledge | Non-specialist / Informed / Specialist | What must be defined and how much context is needed. |
| Rhythm | Compressed / Conversational / Expansive | Sentence/paragraph pace and space between ideas, within the length limit. |
| Tone | Authoritative / Provocative / Warm / Urgent / Balanced / Visionary / Playful | Expression and relationship to the reader; never a license to distort evidence. |

For presentations also resolve **register**: Boardroom (sentence-led titles) or Keynote (fragment-led beats with written narration). Here Keynote is a writing register, not a dependency on another skill. If the user expresses no preference, recommend sentence-led Boardroom and surface the choice. For fragment-led work, compile the actual spoken narration requirement into the brief. Prose does not need a presentation register.

Legacy density labels remain accepted as suggestions: High-Impact/Punchy → concise detail, compressed rhythm; Narrative/Flowing → standard detail, conversational or expansive rhythm; Evidence/Dense → detailed support; ELI5 → non-specialist knowledge and plain language, with detail resolved separately. Keynote/sparse means sparse visible support and fragment-led presentation, not permission to omit reasoning or evidence. Store the explicit dimensions; retain `Density` only as a compatibility summary when useful.

Suggest a voice from [`voice-profiles.md`](voice-profiles.md)'s audience-plus-tone matrix; show its effect in plain language and permit override or a blend. Compile only relevant recommendations from the audience/voice profiles. Evidence, user instructions, purpose, approved outline and practical limits outrank profile defaults. No rhetorical quotas, mandatory emotion, invented examples, or caps on necessary qualifications.

### Provisional focal candidates

Now propose 2–3 distinct claims, recommendations, insights or organizing questions. One is sufficient when the user already supplies a clear point; do not fabricate alternatives to satisfy a count. An organizing question must have a bounded supported takeaway or explicitly unresolved outcome, not be a vague topic.

For each candidate show:
- The point, speakable in one breath.
- Strongest source support and important limitation.
- Relevance to this audience and purpose.
- What understanding or action it enables.

Do not ask for final commitment yet. A user-supplied point stays valid as their intent; offer sharpening without replacing it. If unsupported, preserve its origin while requiring an evidence-safe treatment before writing. Candidate exploration cannot authorize false claims.

---

## PHASE 3: Compare Reasoning and Narrative Structures (Gate 1)

For the promising point(s), write a short **Argument Outline**: what this audience needs to understand, in what order, what each section establishes, which source evidence supports it, and where the intended outcome lands. Test the transitions without framework labels or dramatic vocabulary. A broken inference returns to the candidate or source analysis before style work.

Make structure comparison visible. Offer:
1. **Direct explanation:** answer-first is the normal baseline, with grouped reasons and a clear close; no named framework is a complete result.
2. **Best supported narrative arc**, when eligible.
3. **A second arc**, only when it provides a genuinely different useful route.

Each option shows **opening, reader's question, progression, payoff, source support and trade-offs** (time, complexity, delayed explanation). Describe the experience in plain language alongside the arc's name. Do not require users to know arc terminology. Do not force alternatives where none are supported.

Use [`framework-selection.md`](framework-selection.md) for candidate selection and [`narrative-arcs.md`](narrative-arcs.md) for the ten arcs. The Material Read's real surprise gates delayed-reveal choices. Match the kind of takeaway; quote source support for every essential/anchor beat; reject an arc with an unsupported essential beat. Optional/nonessential beats can be omitted. Run the skeleton stamp test: payoff delivers the provisional point, close fulfills the intended outcome, progression carries the reasoning. A withheld-reveal route requires a supported genuine surprise even without a named arc.

No compulsory mid-piece turn, emotional reversal, minimum length or prewritten killer line. Purpose and source support decide whether the added structure earns its complexity. Communication-framework overlays may clarify delivery after this comparison, but must not add a second competing sequence. Emotional pacing is a suggestion derived from supported events, never a demand to manufacture feelings.

If no arc passes, show direct explanation and briefly explain the relevant rejection. Do not widen the search indefinitely. Source facts remain facts; forecasts stay conditional, scenarios stay scenarios.

For investor pitches, sales pitches, strategic plans, policy recommendations and multi-stakeholder/controversial material, run Audience Advocate and Comms Specialist on the proposed reasoning before final approval. Their advice informs the choice; they do not choose a different user-owned point. Create a unique run directory if needed; save the original source as `ne-source-content.md` and the assignment, Material Read, candidates and structure comparison as `ne-prebuild-review.md`. Dispatch `prompts/reviewer.md` with `review_stage: prebuild`, the two named roles and their Phase 5 reference files. This mode reads the working packet and source, not a nonexistent draft or approved brief. Keep this run directory for Phase 4. Resolve critical support/logic issues before presenting final approval.

---

## PHASE 3.5: Final Choice, Compiled Brief and Pre-Build Check

Choose the **point and how it unfolds together**, as the last major framing decision. In Deep, present the tested options and resolve the user's selection; in Fast, mark the proposed combination and expose the alternatives in the consolidated brief. Ask for correction or approval before drafting. An explicit approval of this concrete brief counts; a generic earlier "go ahead" does not approve unseen inferred decisions.

Record `focal_origin`: `user-stated` if supplied by the user; `user-selected` if they selected/edited a proposed point; `inferred` only if the model chose it and the user merely approved the overall brief; `user-selected-after-reset` after an eligible focal reopen. Generic approval never downgrades a user-stated focal or conceals an inferred one.

### Build Brief — compile actual instructions, not profile labels

- **Purpose + success condition:** primary/secondary purpose, what success looks like; `Ask` may be understanding rather than action.
- **Audience + starting position:** relevant knowledge, beliefs, concerns, objections; distinguish known, inferred and unknown.
- **Format + intended use + limits:** Prose / Presentation / Both, primary format when Both, length/time, standalone or spoken context, inclusions/exclusions and evidence standards.
- **Focal Statement:** One Thing (claim/insight or question with supported takeaway), Ask, Through-Line; `focal_origin`.
- **Material Read:** the full source analysis from Phase 1.75, including evidence passages, relevance links, contrary evidence, uncertainty and missing information.
- **Argument Outline:** each section's job, support and reasoning transition; no unexplained jump between finding and recommendation.
- **Shape + Register:** `answer-first` / `withheld-reveal` / named arc; `prose` / `boardroom` / `keynote`. Paste the selected supported beat skeleton and pacing instructions in full, identify essential beats, list omitted optional beats, and retain a brief reason for the selection over alternatives.
- **Writing treatment:** detail, assumed knowledge, rhythm, tone, operative voice and audience instructions; optional legacy Density summary. Specify narration when needed.
- **Opening opportunity:** a supported question, finding, passage or example and why it matters here; direct statement of the answer is valid. No compulsory hook device or prewritten killer line.
- **Evidence boundaries:** claims that cannot be made, qualifications to retain, no invented essential beats or examples.
- **Success checks:** observable tests tied to purpose—for education, can a reader explain the mechanism/distinction; for persuasion, can they assess the supported action and principal objection; for reporting, can they identify changes and uncertainty? Adapt to the actual purpose.

The brief is the builder's sole assignment rule source. The writer also reads the source and craft files; it does not inherit this conversation or browse the profile catalogs. Include the operative instruction wherever a label alone would lose a decision.

### Pre-build consistency check

Before dispatch, verify:
1. Purpose, success condition and Ask agree; no forced action for an educational or reflective piece.
2. Audience needs map to evidence and section jobs; unknown audience facts are not treated as known.
3. Every essential claim/arc beat has support; contrary evidence and necessary qualifications survive.
4. Outline transitions work and the chosen point fits the evidence and length budget.
5. Format, use, detail, knowledge level, rhythm and tone are mutually feasible.
6. Profile defaults do not contradict evidence, purpose or the approved outline.
7. The approved point, structure and constraints all appear in the brief.

Fix compilation omissions before presenting the final brief. If a substantive choice must change, return it to the user (or mark it as an unresolved proposal in Fast); do not silently substitute. Approval closes the framing stage. Then write and run all gates. No mandatory external rendering skill is part of completion.

---

## PHASE 4: Build (Subagent)

The build runs as a subagent executing **THE SPINE** — the nine-step procedure in [`prompts/builder.md`](prompts/builder.md): material anchor, claim, shape, titles/sections as a chain, test-then-revise-once, bans, licensed ornament, craft floor, content-driven length.

### Content-Driven Length

The builder determines length from the source content, not from any template. Named arcs preserve every essential/anchor beat. Unsupported essential beats reject an arc; unsupported nonessential beats are omitted at brief compilation. A strong 8-slide deck beats a padded 20-slide deck.

### Pre-Build: Write Handoff Files

Before dispatching:
1. Create a new unique temporary run directory (`mkdtemp`), or retain the unique directory already created for prebuild review
2. Write the confirmed Build Brief to `RUN_DIR/ne-build-brief.md`
3. Write the user's source content to `RUN_DIR/ne-source-content.md`
4. State the RUN_DIR path explicitly in every subagent dispatch message

### Dispatch

Create one Task:
- **subagent_type:** `general-purpose`
- **Prompt:** Read and execute [`prompts/builder.md`](prompts/builder.md)
- The subagent reads ONLY: the compiled Build Brief, the source content, and exactly four craft files — [`prose-craft.md`](prose-craft.md) + [`prose-craft-constructions.md`](prose-craft-constructions.md) (Tier-1 sentence discipline), [`deck-title-craft.md`](deck-title-craft.md) (presentation path only), and the Tier-2 checklist in [`humanizing-pass.md`](humanizing-pass.md) (self-check, flag-and-fix once). No catalogs; the brief is the contract.
- **Trace-to-source rule:** every claim-bearing title and paragraph traces to a passage in the source. Evidentiary qualifications the source carries (may / estimated / preliminary / correlational) are preserved — stripping one is an evidence-review failure, not a style win.
- **Output:** `RUN_DIR/ne-output.md` (deliverable body ONLY) + `RUN_DIR/ne-output-meta.md` (sidecar: focal statement, shape + register, argument outline as executed, sourcing summary with per-section tags, revision notes).

### Content Sourcing Tags (sidecar only)

The builder tags every section/slide in `ne-output-meta.md` — never in the body:

| Tag | Meaning |
|-----|---------|
| `[DIRECT]` | Quoted or nearly verbatim from source |
| `[PARAPHRASE]` | User's ideas restated |
| `[ELABORATED]` | User's concept expanded |
| `[GENERATED]` | Connective content with no source passage |

The evidence reviewer (Phase 4.8) spot-checks these tags against the source.

### Post-Build

1. If the writer returns a brief-gap report or produces no valid body/sidecar, return to Phase 3.5 and resolve it before running gates. Otherwise read `RUN_DIR/ne-output.md` (the orchestrator may read the sidecar too; the focal judge never does)
2. Do NOT present the output yet — run the gates in order: **Phase 4.6 → 4.7 → 4.8**
3. Present the output only after all three pass, then proceed to Phase 5

> Full output format templates (Presentation, Prose, sidecar) are in [`prompts/builder.md`](prompts/builder.md).

---

## PHASE 4.6: Focal Fidelity Gate (Gate 2)

A blind judge checks **what the piece communicates and whether it fulfills the approved purpose**. Purpose and success criteria are inspected only after the cold read, when the brief is opened. Phase 5 reviewers focus on prose quality, audience fit, and persuasion — without Gate 2, focal drift slips past them because the piece reads internally coherent.

### Why a blind gate, not just another reviewer

A chosen shape has gravity: the build naturally serves the shape, and the shape serves *its* payload, which may not be the focal payload. The judge breaks that gravity by reading the body-only output *before* the brief and reporting what it actually communicates. It then reads the source (still before the brief) and checks whether the material contains a claim more consequential for this audience than the piece's apparent One Thing.

### The dispatch contract (strict)

- **subagent_type:** `general-purpose`
- **Prompt:** Read and execute [`prompts/focal-fidelity-judge.md`](prompts/focal-fidelity-judge.md)
- **The dispatch message carries the audience, the ask, and the register (Boardroom/Keynote, decks) — verbatim from the brief — and NEVER the focal statement, any focal candidate, or any quotable line from the draft.** The judge must extract the One Thing cold.
- **Inputs read by judge (its own protocol order):** `ne-output.md` (Phase A cold read — for decks, the concatenated title sequence first, with the register-appropriate chain tests), `ne-source-content.md` (Phase A2 source check), `ne-focal-judge-prior.md` if present (Phase C), `ne-build-brief.md` LAST (Phase B). The judge never receives `ne-output-meta.md`.
- **Outputs:** `ne-cold-read.md`, `ne-focal-judge.md` (verdict + `needs_revision_count`).

Do NOT parallelize the judge — its protocol depends on a deterministic file-reading order.

### Verdict routing (all four)

1. **PASS** → delete `ne-focal-judge.md` and `ne-focal-judge-prior.md` immediately (a stale verdict file would misroute the builder into Revision Mode if a later gate triggers a repair), then proceed to Phase 4.7. Show the user a short summary: cold-read One Thing, Brief One Thing, judge's confidence. If the verdict carries a FOCAL_MISMATCH **advisory** (see below), surface the quoted passage to the user alongside the summary.
2. **NEEDS_REVISION** → shared repair loop with `ne-focal-judge.md` as the trigger. Rotate the prior verdict file first. The judge's `needs_revision_count` field is the counter; at 3 with no convergence the judge itself escalates to FRAMEWORK_MISMATCH. Loop automatically — don't ask the user; they can interrupt.
   > "Pass [N] focal drift detected: [judge's drift summary]. Dispatching builder in revision mode."
3. **FRAMEWORK_MISMATCH** → the shape cannot structurally land the focal; editing will not fix it. Escalate to the user:
   > "The selected shape cannot structurally land your focal. The judge diagnosed: [diagnosis]. Options: (1) restart Phase 3 with a different shape, (2) revise the Focal Statement, (3) accept the current draft as-is. Which do you prefer?"
   Do not silently restart Phase 3 — the user owns that decision.
   - **Fresh-draft restart:** after the user authorizes a new shape or focal, archive the current reports, then clear all trigger files and `ne-focal-judge-prior.md` before the new builder dispatch. Reset the evidence review count for the new draft. Preserve the run-level focal-reopen count; a shape restart does not grant another automatic focal reset.
4. **FOCAL_MISMATCH** → the judge's source check found an audience-relevant, source-supported claim more consequential than the brief's focal. The piece is not badly built — it is built on the wrong One Thing.
   - **Automatic reset (once per run):** ONLY when the brief marks `focal_origin: inferred` (Fast mode, user never touched the focal line) and no reset has happened this run. Before re-entering the pipeline: delete ALL trigger files (`ne-focal-judge.md`, `ne-focal-judge-prior.md`, `ne-evidence-review.md`, `ne-humanizing-flags.md`) so the reset build starts clean in Initial Build Mode with a fresh `needs_revision_count`; the evidence reviewer's two-run cap also resets with the new draft. Then revisit Phase 1.75 with the judge's quoted passage, regenerate provisional candidates in Phase 2, and compare them in Phase 3; the user's new choice is marked `focal_origin: user-selected-after-reset`; then re-run Phases 3 → 3.5 → 4.
   - **Advisory (every other case):** for `user-selected`, `user-stated`, or `user-selected-after-reset` origins — and for ANY second mismatch in a run regardless of origin — the judge downgrades to an advisory inside the verdict it otherwise issues. The orchestrator surfaces the quoted passage and the audience-relevance argument to the user, never resets on its own.

### Cleanup

After the gate resolves: delete `ne-focal-judge.md` once its findings are closed (per the shared repair loop) and `ne-focal-judge-prior.md` at end-of-loop, so a future build does not accidentally enter revision mode.

### What Phase 4.6 does NOT do

- It does not coach prose style (Phase 5), replace specialist persuasion/originality review (Phase 5/5.5), or replace the evidence audit (Phase 4.8). After the cold read it does check the approved purpose and observable success condition.
- It does not receive the focal, the sidecar, or any draft line in its dispatch — blindness is the mechanism.
- Its cold read checks a reason to continue and whether the close fulfills the opening's promise. A direct answer can establish relevance without suspense or a literal question. A failed purpose or broken promise blocks PASS even on a semantic match. For decks, a broken title chain forces NEEDS_REVISION regardless of focal match.

---

## The Shared Repair Loop (one contract for Gates 2–4)

Every post-build revision — whichever gate triggered it — runs the same loop:

1. Leave (or write) the trigger file in RUN_DIR; dispatch the builder, which self-routes into Revision Mode against the highest-priority trigger present (`ne-focal-judge.md` > `ne-evidence-review.md` > `ne-humanizing-flags.md`) and makes the smallest edits that close the findings.
2. **(a)** The builder re-runs Tier-1 prose-craft + the bans on every edited section (its own contract).
3. **(b)** The first evidence review of a draft always audits the entire draft, even when a focal or humanizing repair caused its dispatch. Later reviews audit changed sections plus every unresolved prior finding. Keep an evidence review count and archived last report in the run record, independent of trigger-file presence; pass the count and last report path in the reviewer dispatch. A clean report may be removed as a trigger without erasing this history. Every dispatch counts toward the two-run cap. When Phase 4.8 is reached with an unchanged draft already audited CLEAN, reuse that result; do not spend a redundant review.
4. **(c)** Judge revalidation: when the FOCAL JUDGE originated the repair, the orchestrator ALWAYS re-dispatches the judge on the revised draft — the gate that found the problem confirms its fix, whatever was edited. When another gate originated the repair, one judge re-read is triggered only if the revision touched the governing claim, the ask, the climax, or the close.
5. **(d)** A trigger file is deleted when its findings are resolved; successful end-of-loop cleanup deletes all three triggers plus `ne-focal-judge-prior.md`. Archive each report before removing its trigger. Preserve unresolved reports and the sidecar on escalation. The sidecar is kept until delivery.
6. **(e)** Caps: evidence reviewer 2 runs total per draft; judge NEEDS_REVISION capped at 3 via its `needs_revision_count` counter. Any cap breach escalates to the user with the findings files.

---

## PHASE 4.7: Humanizing Check (Gate 3 — flag-only)

After focal fidelity passes, the orchestrator runs the Tier-2 discourse-level structural-delta check from [`humanizing-pass.md`](humanizing-pass.md) against the draft. **Tier 2 runs INSIDE the build as the builder's self-check; Phase 4.7 verifies and flags only — repairs go through the builder's revision route.** The orchestrator never edits the draft itself.

**Why a separate check from prose-craft.** prose-craft (Tier 1, run in the build) cleans the *sentence*. But the research corpus shows a classifier still detects AI from *structure* at 93.9% macro-F1 after that lexical cleanup. The AI signature lives in the discourse, not the words.

**The deltas checked** (full definitions and carve-outs in `humanizing-pass.md`): theme-statement budget (mid-piece restatements only — the answer-first opening and title chains are exempt), tolerated asymmetry / open threads, temporal complexity preserved, discourse redundancy, idiosyncrasy as a conditional detector (a plain, well-supported section is NOT a failure; no un-templatable moment may be manufactured).

**The cardinal rule, non-negotiable:** these are **gates and drift detectors, never optimization objectives**. Do not loop a generator against them — optimizing the metric manufactures the slop the check removes.

**Disposition:**
- No drift → note it briefly, proceed to Phase 4.8.
- Drift → write the specific flags to `RUN_DIR/ne-humanizing-flags.md` (flag-only: delta name, location, quoted evidence — no rewrites) and enter the shared repair loop with it as the trigger.

---

## PHASE 4.8: Evidence Review (Gate 4 — blocking)

The final gate before anything reaches the user: a subagent holding the source audits every claim.

### Dispatch

- **subagent_type:** `general-purpose`
- **Prompt:** Read and execute [`prompts/evidence-reviewer.md`](prompts/evidence-reviewer.md)
- **Inputs:** `ne-output.md`, `ne-output-meta.md` (the sidecar — the reviewer is the sidecar's auditor), `ne-source-content.md`, `ne-build-brief.md`, `ne-cold-read.md` if present (peak-impact moments are priority audit targets).
- **Output:** `RUN_DIR/ne-evidence-review.md` — verdict **CLEAN | FINDINGS**, numbered findings (severity BLOCKING/MINOR, location, source passage vs output claim, required fix), spot-check record.

### The five checks

Unsupported claims · altered qualifications (correlation→causation, hedge-stripping, "may"→"will", subgroup→universal) · missing reasoning steps · ask overreach (with the supportable ask proposed) · sourcing-tag spot-check (≥3 [DIRECT]/[PARAPHRASE] tags verified verbatim against the source). Style and taste are explicitly out of its scope.

### Routing

- **CLEAN** → gate passes. Delete any resolved trigger files; present the output; proceed to Phase 5.
- **FINDINGS with any BLOCKING entry** → shared repair loop with `ne-evidence-review.md` as the trigger. The builder never fixes an unsupported claim by inventing support — it cuts or scales the claim to what the source states.
- **FINDINGS with only MINOR entries** → the gate passes with notes: delete the trigger file, surface the findings to the user alongside the deliverable as evidence notes, and offer the repair in one line ("want the minor evidence findings fixed? one builder pass"). No automatic repair dispatch — MINOR means the claim is defensible.
- **Two-run cap:** the reviewer runs at most twice per draft (the second run re-checks changed sections + prior findings only). Findings still unresolved after the second run → escalate to the user with `ne-evidence-review.md` attached; the user decides.

After the applicable reviews pass, deliver the written prose or presentation narrative. Rendering is a separate optional downstream task, not required for standalone completion.

---

## PHASE 5: Targeted Review (2 Parallel Subagents)

### When to Run

Auto-run the panel only for high-stakes content types (the same list as Phase 3's early review: investor pitch, sales pitch, strategic plan / transformation, policy recommendation, multi-stakeholder / controversial). For everything else, offer it in one line after Gate 4 passes — "Want the two-reviewer pass? Optional for a piece like this; the four gates have already run." — and proceed without it if declined. The gates assess focal/purpose fidelity, writing drift, and source fidelity; the panel adds audience and persuasion depth that low-stakes pieces can skip.

Two specialist agents review the output simultaneously via the Task tool, selected by content type to focus on the dimensions that matter most for this piece.

```
                    ┌─────────────────────────────────────┐
                    │            DIRECTOR                 │
                    │  Synthesizes, resolves conflicts    │
                    │        (main conversation)          │
                    └─────────────────────────────────────┘
                                     ▲
                          ┌──────────┼──────────┐
                          ▼                     ▼
                    REVIEWER 1             REVIEWER 2
               (content-type selected, parallel subagents)
```

### Why 2, Not 6

The builder already runs compression and the craft floor internally, and the gates cover focal, structure, and sourcing. Adding 6 independent reviewers fragments the unified voice the builder produced. Two focused reviewers catch the highest-value issues without overwhelming the piece with competing rewrites.

### Reviewer Selection by Content Type (single source — `prompts/reviewer.md` points here)

The Audience Advocate is always one reviewer — "does this land for the audience?" is the universal review question. The second reviewer is selected by the highest-risk dimension for this content type. Name both roles in the dispatch message; the reviewer prompt carries no table of its own.

| Content Type | Reviewer 1 (always) | Reviewer 2 (selected) | Why this pairing |
|-------------|---------------------|----------------------|-----------------|
| Investor pitch / fundraising | Audience Advocate | Comms Specialist | Messaging tightness is make-or-break for pitches |
| Sales pitch | Audience Advocate | Comms Specialist | Persuasion must be airtight |
| Strategic plan / transformation | Audience Advocate | Content Expert | Claims must survive scrutiny |
| Post-mortem / retrospective | Audience Advocate | Content Expert | Technical accuracy is non-negotiable |
| Counterintuitive research | Audience Advocate | Content Expert | Evidence must be bulletproof |
| Keynote / thought leadership | Audience Advocate | Originality Agent | Distinctiveness matters most here |
| Vision / inspiration piece | Audience Advocate | Originality Agent | Must not feel generic |
| Paradigm shift / new model | Audience Advocate | Originality Agent | Fresh framing is the whole point |
| Company/product origin story | Audience Advocate | Originality Agent | The story must feel like no one else's |
| Scenario planning | Audience Advocate | Comms Specialist | Fork framing must be tight |
| Case study | Audience Advocate | Content Expert | Facts drive the credibility |
| Product launch | Audience Advocate | Comms Specialist | Messaging clarity is key |
| Policy recommendation | Audience Advocate | Content Expert | Evidence and accuracy critical |

### Dispatch

Create 2 Tasks simultaneously using [`prompts/reviewer.md`](prompts/reviewer.md), naming the selected roles in each dispatch message.

Each subagent:
- **subagent_type:** `general-purpose`
- Reads `RUN_DIR/ne-output.md`, `RUN_DIR/ne-build-brief.md`, and `RUN_DIR/ne-source-content.md` (spot-check claims against the source — a verdict on sourcing you did not check is a guess), plus its reference file
- Returns findings as task result (not written to file)

**Judge hygiene.** The reviewers (and the Phase 4.6 / 5.5 judges) are LLM-as-judge, which carries verbosity, position, and self-preference bias. Instruct each to score against the Build Brief and the Content-Driven Length principle — a tight piece is not worse than a padded one — and treat confidence scores as advisory, not as a gate. See [`humanizing-pass.md`](humanizing-pass.md) → *Judge hygiene*.

See [`prompts/reviewer.md`](prompts/reviewer.md) for full role descriptions and dispatch configurations.

### Director Synthesis (Main Conversation)

After both complete, synthesize into focused recommendations:

1. **Agreement** — Both agents flag the same issue → high-confidence fix
2. **Complementary** — Each catches different issues → present both
3. **Conflict** — Escalate to user for decision

**Output format:**

```markdown
## Review Summary

### Strengths
- [What's working] — *Agent attribution*

### Recommended Changes
1. **[Change]** — *Agent attribution*
   [Specific recommendation]

### Points Requiring Your Decision (if any)
> [Agent A] says X, [Agent B] says Y — which approach?

### Overall Assessment
**Ready?** [Yes / Yes with edits / Needs revision]
**Most important change:** [One sentence]
```

---

## PHASE 5.5: Stress Test Panel (High-Stakes Content Only)

The stress test is reserved for content types where the stakes justify additional scrutiny. **Do not auto-offer for every piece.**

### When to Offer

Offer the stress test only for these content types:
- Investor pitch / fundraising
- Sales pitch
- Policy recommendation
- Strategic plan / transformation (when presented to decision-makers)

For all other content types, skip Phase 5.5 unless the user explicitly requests it.

> "This is a [content type] — want me to stress test it? I'd test against: **[Persona 1]**, **[Persona 2]**, **[Persona 3]**.
>
> You can also swap in: Engineer, Skeptic, Risk Officer, CFO, Lawyer, Conservative, COO."

### Persona Selection by Content Type (single source — `prompts/stress-tester.md` points here)

Always 3 personas per run. Name them in the dispatch messages; the stress-tester prompt carries no table of its own.

| Content Type | Auto-Selected |
|--------------|---------------|
| Investor pitch | CFO, COO, Skeptic |
| Sales pitch | Skeptic, COO, Engineer |
| Strategic plan | COO, Conservative, Risk Officer |
| Policy recommendation | Lawyer, Risk Officer, Conservative |

### Dispatch

Create 3 Tasks simultaneously using [`prompts/stress-tester.md`](prompts/stress-tester.md), naming each persona in its dispatch message. Each subagent:
- **subagent_type:** `general-purpose`
- Reads `RUN_DIR/ne-output.md`, `RUN_DIR/ne-build-brief.md`, and `RUN_DIR/ne-source-content.md` (spot-check claims against the source)
- Returns PASSED/FLAGGED/FAILED verdict with findings as task result

See [`prompts/stress-tester.md`](prompts/stress-tester.md) for full persona descriptions and configurations.

### Director Triage (Main Conversation)

After personas review, Director categorizes:

```markdown
## Stress Test Results

### [Persona] — [PASSED / FLAGGED / FAILED]
**Concerns:**
1. [Concern]

---

## Director Triage

### Must Fix (will undermine piece if ignored)
1. **[Issue]** ([Persona]) — [Why it matters and how to fix]

### Should Fix (strengthens meaningfully)
1. **[Issue]** ([Persona]) — [Recommendation]

### Could Fix (nice-to-have)
1. **[Issue]** ([Persona]) — [Optional improvement]

### Director's Recommendation
[1-2 sentences on what to prioritize]
```

---

## ON-DEMAND: "Tighter"

User can request compression passes anytime after delivery.

When user says "tighter":

1. **Focal check** — Has the point drifted? Re-confirm.
2. **Section pass** — Any sections that could merge or be cut?
3. **Unit pass** — Four-lens compression on every slide/paragraph.
4. **Re-run prose-craft + the humanizing check** — compression tends to flatten sentence-length variance (a Reinhart AI-tell) and to re-introduce theme-restatement; re-check both Tier 1 and Tier 2 after cutting. For decks, re-run the title-chain tests (spoken-prose + antecedent, register-appropriate). If the compression touched the governing claim, the ask, the climax, or the close, or touched any sourced claim, re-run the affected gates per the shared repair loop.
5. **Output** — Tighter version with change summary.

Repeatable until user is satisfied.

---

## ON-DEMAND: Change Log Export

After final delivery (or after any revision pass), offer to export a Change Log:

> "Want me to export a Change Log? This documents what changed from your original content and why — useful for collaborators, future reference, or understanding the transformation."

See [`checklists.md`](checklists.md) for the Change Log template and Metric Menu.

---

## Reference Files

| File | Contains |
|------|----------|
| [`prose-craft.md`](prose-craft.md) + [`prose-craft-constructions.md`](prose-craft-constructions.md) | Embedded sentence-level discipline (Floor/Filter/Ceiling + construction catalog). Tier 1 of the humanizing pass. **Builder input** — applied directly by the builder, not a separate skill call. |
| [`deck-title-craft.md`](deck-title-craft.md) | Local title guide — action titles, title-chain tests (spoken-prose + antecedent), register variants and rewrite examples. **Builder input** (presentation path) and the judge's deck-branch test source. |
| [`humanizing-pass.md`](humanizing-pass.md) | The de-slop layer — Tier 1 (prose-craft) + Tier 2 (discourse structural-delta checklist), judge hygiene, the gate-not-objective rule. **Builder input** (Tier-2 checklist as self-check); Phase 4.7 verifies and flags only. |
| [`framework-selection.md`](framework-selection.md) | The Phase 3 shape-selection protocol — reveal gate, payload match (Focal Fit Definition table), beat-support audit, skeleton stamp test. Orchestrator/judge reference — never builder input. |
| [`narrative-arcs.md`](narrative-arcs.md) | 10 narrative arc structures with beats. Orchestrator/judge reference — never builder input. |
| [`communication-frameworks.md`](communication-frameworks.md) | Efficiency frameworks (Pyramid, AIDA, PAS, etc.). Orchestrator/judge reference — never builder input. |
| [`audience-profiles.md`](audience-profiles.md) | Deep audience profiles — compiled into the brief's Audience essentials. Orchestrator/judge reference — never builder input. |
| [`voice-profiles.md`](voice-profiles.md) | 7 voice profiles with auto-derive mapping — compiled into the brief's Voice essentials. Orchestrator/judge reference — never builder input. |
| [`emotional-arcs.md`](emotional-arcs.md) | Framework emotional textures + audience calibration. Orchestrator/judge reference — never builder input. |
| [`opening-closing-strategies.md`](opening-closing-strategies.md) | Opening/closing strategy libraries. Orchestrator/judge reference — never builder input; the brief carries at most a pointer to a source passage, never a strategy type. |
| [`rhetorical-figures.md`](rhetorical-figures.md) | High-style figure catalog (surprise + repetition families). Orchestrator/judge reference — never builder input; the builder's licensed-ornament step needs no catalog. |
| [`attention-loop.md`](attention-loop.md) | The per-section engagement engine (Stakes → Big Question → Head Fake → Re-hook). Orchestrator/judge reference — informs the outline and the judge's engagement questions; never builder input. |
| [`checklists.md`](checklists.md) | Quality checklists (headlines, CTAs, pricing, compression) + Change Log template. Orchestrator/judge reference — never builder input. |
| [`agent-reference-persuasion.md`](agent-reference-persuasion.md) | Comms agent deep reference (Phase 5) |
| [`agent-reference-visual.md`](agent-reference-visual.md) | Visual agent deep reference (Phase 5) |
| [`agent-reference-verification.md`](agent-reference-verification.md) | Content expert deep reference (Phase 5) |
| [`prompts/builder.md`](prompts/builder.md) | Build subagent — THE SPINE, initial + revision modes, body/sidecar output contract |
| [`prompts/focal-fidelity-judge.md`](prompts/focal-fidelity-judge.md) | Blind cold-read judge — Gate 2, four verdicts incl. FOCAL_MISMATCH, `needs_revision_count` counter |
| [`prompts/evidence-reviewer.md`](prompts/evidence-reviewer.md) | Evidence reviewer — Gate 4, the five source-fidelity checks, CLEAN/FINDINGS, two-run cap |
| [`prompts/reviewer.md`](prompts/reviewer.md) | Targeted review subagents (Phase 5) — roles named in dispatch from the Phase 5 table |
| [`prompts/stress-tester.md`](prompts/stress-tester.md) | Stress test panel (Phase 5.5) — personas named in dispatch from the Phase 5.5 table |
| [`examples/`](examples/) | Full workflow examples |

---

## Quick Start

1. Import source; require explicit Fast or Deep.
2. Purpose/success, audience starting position, format/use/limits (Phase 1.5).
3. Read source for evidence, relevance and limits (Phase 1.75).
4. Resolve treatment and propose provisional points (Phase 2).
5. Compare plain reasoning and supported arcs (Phase 3; Gate 1).
6. Approve point and structure together; compile and check brief (Phase 3.5).
7. Dispatch isolated writer with brief, source and craft only (Phase 4).
8. Run blind focal/purpose, humanizing and evidence gates with the shared repair loop (Phases 4.6–4.8). A focal PASS does not authorize delivery.
9. Run applicable specialist reviews and any chosen stress test. Route changes through affected gates.
10. Deliver prose/presentation text; offer compression or a change log as appropriate.
