---
name: Narrative-Engine
description: "Transform any content into narrative-driven presentations OR prose through a minimal build spine wrapped in rich judgment — a blind focal judge, a source-holding evidence gate, and content-driven length. Use when converting content to presentations, restructuring existing decks, writing long-form pieces, or optimizing for specific audiences."
---

# Narrative Engine

Transform content into compelling narratives — as presentations or prose. Content determines length — no padding, no artificial minimums. The architecture: **generation minimal, judgment rich.** The builder gets a small, compiled contract and a short spine; the heavy machinery (catalogs, matrices, cold reads, source audits) lives with the orchestrator and the judges.

## Workflow Overview

```
PHASE 1     Content Import
    ↓
PHASE 1.25  Mode — FAST (infer everything, one consolidated confirmation)
                 / GUIDED (step-by-step discovery)
    ↓
PHASE 1.5   Output Format — Presentation / Prose / Both
            (Presentation → register question: Boardroom sentence-titles / Keynote fragments)
    ↓
PHASE 1.75  Audience + Ask → Material Read → Focal candidates
            ⇒ Focal Statement + focal_origin (the north star; for decks, the punchline)
    ↓
PHASE 2     Discovery — audience (skip if answered), purpose, content type, tone
    ↓
PHASE 2.5   Density Mode — varies by output format
    ↓
PHASE 3     Argument Outline + Conditional Shape
            ★ GATE 1: beat-support audit + skeleton stamp test (named arcs only) ★
    ↓
PHASE 3.5   Build Brief — compiles everything the builder is allowed to know
    ↓
    ══════ HANDOFF: create RUN_DIR, write Build Brief + Source into it ══════
    ↓
PHASE 4     Build — SUBAGENT runs THE SPINE (prompts/builder.md)
            writes ne-output.md (BODY ONLY) + ne-output-meta.md (sidecar)
    ↓
PHASE 4.6   ★ GATE 2: Focal Fidelity — blind cold-read judge SUBAGENT ★
            PASS / NEEDS_REVISION / FRAMEWORK_MISMATCH / FOCAL_MISMATCH
    ↓
PHASE 4.7   ★ GATE 3: Humanizing check — orchestrator, flag-only ★
            drift → ne-humanizing-flags.md → builder revision
    ↓
PHASE 4.8   ★ GATE 4: Evidence Review — SUBAGENT holding the source ★
            CLEAN / FINDINGS (BLOCKING findings loop to the builder)
    ↓
    (Gates 2-4 all repair through ONE shared repair loop — see below)
    ↓
PHASE 5     Targeted Review — 2 SUBAGENTS + Director synthesis
            (auto for high-stakes content; offered for everything else)
    ↓
PHASE 5.5   Stress Test — 3 SUBAGENTS + Director triage (high-stakes content only)
    ↓
ON-DEMAND   "Tighter" — compression passes anytime (re-runs prose-craft + humanizing)
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

Phases 1–3.5 run interactively in the main conversation. Phases 4, 4.6, 4.8, 5, and 5.5 run as subagents via the Task tool, reducing context window pressure and enabling parallel execution. Phase 4.7 runs in the orchestrator (flag-only).

### Handoff Files

All handoff files live in a per-run directory the orchestrator creates at the end of Phase 3.5: `RUN_DIR = /tmp/ne-<yymmdd>-<slug>/` (slug from the focal topic). Every dispatch prompt must state the RUN_DIR; the templates refer to files by name and resolve them inside it. Concurrent runs never collide, and deleting the directory cleans up the whole run.

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

Ask once, before any other question:

> **How do you want to work?**
> 1. **Fast** — I read your content, infer every discovery answer (format, register, audience, ask, focal point, purpose, content type, tone, density, shape), and present one pre-filled Build Brief for you to correct or approve. One confirmation, then build.
> 2. **Guided** — full step-by-step discovery: each question in turn.

**Fast mode mechanics:**
- Run Phases 1.5–3.5 internally, without asking questions. Infer each answer from the content and conversation context; where genuinely ambiguous, make the best call and mark it `[INFERRED — LOW CONFIDENCE]` in the brief.
- **Fast mode ALWAYS surfaces the focal candidates.** The 2-3 stance-committing candidates from Phase 1.75 appear in the consolidated brief, one line each, with the chosen one marked. `focal_origin` is honest about who chose: if the user's request itself stated the point, record `user-stated` — Fast mode never downgrades an explicitly supplied focal to `inferred`. Record `inferred` only when the skill picked the focal with no user input on it; the user editing the focal line in the brief flips it to `user-selected`.
- The Argument Outline and the chosen shape (with its trace-to-material justification) surface in the consolidated brief. A beat-support-audit or skeleton-stamp failure on a named arc still escalates to the user, in either mode.
- The deck register (Boardroom / Keynote) is inferred and surfaced in the brief.
- Present ONE consolidated message: the inferred discovery answers as a compact table, then the compiled Build Brief. The user corrects any line or says go.
- Gates 2–4, the review panel, and the stress test behave identically in both modes.

**Default:** if the request already implies speed ("just write it", "quick pass") or the content arrived with clear instructions, default to Fast and say so — the user can switch. Otherwise ask.

---

## PHASE 1.5: Output Format

*Guided mode only — Fast mode infers this and surfaces it in the consolidated brief.*

Ask before proceeding to focal discovery:

> **What format do you need?**
> 1. **Presentation** — Slide deck with headlines, spotlights, and design notes
> 2. **Prose** — Long-form document with sections, transitions, and flow
> 3. **Both** — Build one, derive the other (specify which first)

### If Presentation selected: ask the register

> **What register should the deck speak in?**
> 1. **Boardroom** — every slide title is a short complete sentence delivering one story beat; read top-to-bottom, the titles tell the whole narrative. *(default)*
> 2. **Keynote** — fragments are the register; complete sentences are rationed for the 3-4 lines meant to land; the chain lives in the beat + narration read.

Default to Boardroom if the user has no preference. In Fast mode, infer the register and surface it in the consolidated brief.

### If Prose selected:

Ask for target length:

> **Target length?**
> 1. **Short** (~500-800 words) — Tight, punchy, every sentence pulls its weight
> 2. **Medium** (~1,000-1,500 words) — Room to develop ideas, standard article length
> 3. **Long** (~2,000-3,000 words) — Comprehensive, detailed, thought leadership depth
> 4. **Let content determine** — No artificial target

### If Both selected:

> **Which format first?**
> 1. **Prose → Presentation** — Write the full narrative, then compress to slides
> 2. **Presentation → Prose** — Build the deck structure, then expand to prose

**Note:** The shapes (answer-first, withheld-reveal, named arcs) are *narrative structures* — they work for both formats. The divergence happens at the Build phase.

### Presentation path: embedded deck craft + a render stage

The deck craft is embedded, not invoked. The build subagent reads [`deck-title-craft.md`](deck-title-craft.md) (a verbatim embed of keynote-create's title guide) and applies it directly — titles as story beats, the spoken-prose and antecedent tests, register variants. The Focal Statement doubles as the deck's punchline line. Only the **render stage** legitimately calls keynote-create: after the gates pass, the orchestrator runs keynote-create's Stage 4 render (`keynote-render.mjs` → `/impeccable` layout promotion → PDF) in the main conversation, since that is main-conversation work, not a subagent.

---

## PHASE 1.75: Focal Discovery

**Purpose:** establish who the piece is for, what it asks of them, and the single point — before anything else.

**Step 1 — Audience + Ask first (one line; skip only if already stated).** Before proposing any focal, pin down in one line each: who reads/hears this, and what they should do, decide, or believe afterward. Every focal candidate is judged against these two lines.

**Step 2 — Material Read.** Read the source and record, in plain language:
- **Stake** — what is at risk or in play for this audience
- **Tension** — the unresolved question or conflict the material carries
- **Genuine surprise** — a finding that would surprise this audience, or **"none — never manufacture one"**
- **Strongest existing passages** — the 2-3 passages already carrying the most force, quoted or pinpointed
- **What changes** — what the reader knows, decides, or does differently after

The Material Read is pasted in full into the Build Brief — it is the builder's Step 1 anchor and the raw material for shape selection.

**Step 3 — Focal candidates.** Propose 2-3 stance-committing candidates. Each must pass the quality bar:
- Speakable in one breath
- A claim, recommendation, or reframing — never a topic
- Specific — names the mechanism, the number, or the decision
- Answers a question this audience actually cares about, given the Ask

> "Based on your material, I see these possible points:
> 1. **[Candidate A]** — [why this is the most consequential claim for this audience]
> 2. **[Candidate B]** — [...]
>
> Which should we optimize for? Or is there a different point you want to land?"

**User-stated points** are tested against the same bar; offer a sharpened version alongside, but the original stays valid — the user owns the focal.

**Fast mode:** the candidates appear in the consolidated brief, one line each, the chosen one marked.

**Output:** a Focal Statement (1-2 sentences) that becomes the north star, with three components:
- **The One Thing:** single idea the piece must land
- **The Ask:** action or shift being driven toward
- **The Through-Line:** logical/emotional thread connecting everything

**The brief records `focal_origin`:** `inferred` (Fast mode, focal line never touched by the user) | `user-selected` (user picked or edited a candidate) | `user-stated` (user supplied the point) | `user-selected-after-reset` (chosen after a FOCAL_MISMATCH reopen). Only `inferred` is eligible for the automatic FOCAL_MISMATCH reset in Phase 4.6.

---

## PHASE 2: Discovery Questions

*Guided mode only — Fast mode infers these and surfaces them in the consolidated brief.*

Ask one question at a time. Wait for the user to answer before asking the next question. User can respond with numbers or their own words. **Skip the audience question if Phase 1.75 Step 1 already answered it.**

### Question 1: Audience (skip if answered)

> **Who is your audience?**
> 1. Executive / Board (time-constrained decision-makers)
> 2. Technical / Engineering (methodology-focused, skeptical)
> 3. Sales / Marketing (action-oriented, competitive)
> 4. Investors / VCs (seeking growth story + traction)
> 5. General Public / Keynote (broad, need accessibility)
> 6. Skeptics / Resisters (need to be won over)
> 7. Mixed / Cross-functional (varied expertise levels)
> 8. Academic / Research (evidence-focused)

### Question 2: Purpose

> **What are you trying to accomplish?**
> 1. Persuade to act (get approval, close a deal)
> 2. Inform / Educate (transfer knowledge)
> 3. Inspire / Motivate (energize, create vision)
> 4. Align / Build consensus (get buy-in)
> 5. Report / Update (share status, results)
> 6. Defend / Justify (support a position)
> 7. Entertain / Engage (keynote, thought leadership)

### Question 3: Content Type

> **What type of content is this?**
> 1. Counterintuitive research findings
> 2. Strategic plan / transformation roadmap
> 3. Scenario planning / decision fork
> 4. Paradigm shift / new mental model
> 5. Company/product origin story
> 6. Post-mortem / retrospective
> 7. Sales pitch
> 8. Investor pitch / fundraising
> 9. Product launch
> 10. Case study
> 11. Policy recommendation
> 12. Vision/inspiration piece

### Question 4: Tone

> **What tone or attitude do you want?**
> 1. Authoritative / Expert
> 2. Provocative / Challenging
> 3. Warm / Relatable
> 4. Urgent / Action-oriented
> 5. Balanced / Objective
> 6. Visionary / Aspirational
> 7. Playful / Creative

---

## PHASE 2.5: Density Mode Selection

*Guided mode only — Fast mode infers this and surfaces it in the consolidated brief.*

### For Presentations:

> **How concentrated should this deck be?**
>
> 1. **High-Impact** — Maximum compression. One punch per slide. Headlines do heavy lifting. For pitches and time-constrained execs.
>
> 2. **Narrative** — Room to breathe. Story beats get space to land. Emotional builds allowed. For thought leadership and teaching.
>
> 3. **Evidence** — Denser supporting material. Multiple proof points per section. For skeptics, technical audiences, due diligence.
>
> 4. **ELI5** — Explain Like I'm 5. Maximum accessibility. Simple words, concrete analogies, zero jargon. For non-experts, broad audiences, or when clarity trumps sophistication.

### For Prose:

> **How should this piece read?**
>
> 1. **Punchy** — Short paragraphs. High signal density. Every sentence pulls its weight. Hemingway, not Faulkner.
>
> 2. **Flowing** — Room to breathe. Narrative builds allowed. Transitions smooth the ride. Story beats get space to land.
>
> 3. **Dense** — Detailed and thorough. Evidence-heavy. Multiple proof points per section. For readers who want depth.
>
> 4. **ELI5** — Explain Like I'm 5. Simple words, everyday analogies, short sentences. No jargon, no abstractions. Like explaining to a curious child or smart non-expert.

**Key principle:** No minimum word/slide counts. Content determines length.

---

### ELI5 Mode Guidelines

When ELI5 is selected, apply these rules throughout:

**Language Rules:**
- Use common words (≤2 syllables when possible)
- Replace jargon with plain language or define it immediately
- Prefer active voice: "X does Y" not "Y is done by X"
- Maximum sentence length: ~15 words
- One idea per sentence

**Analogy Requirements:**
- Use a concrete analogy when it explains an abstract concept more clearly
- Draw from everyday experience: kitchen, playground, family, sports, weather
- Use the source's concrete examples where they suffice; no analogy quota applies
- Test: Would a smart 10-year-old understand this?

**Structure Rules:**
- Shorter paragraphs (2-3 sentences max)
- More frequent section breaks
- Use questions as headers when helpful ("So what does that mean?")
- Build from familiar → unfamiliar

**What to Avoid:**
- Industry jargon (or define immediately if unavoidable)
- Acronyms without expansion
- Abstract nouns (transformation → change, optimization → making better)
- Passive constructions
- Compound sentences with multiple clauses
- Assuming prior knowledge

**Examples:**

| Instead of... | Write... |
|---------------|----------|
| "Leverage synergies across verticals" | "Use what works in one area to help another" |
| "The algorithm optimizes for engagement" | "The system figures out what keeps people interested" |
| "Market volatility impacts portfolio allocation" | "When prices jump around, you might want to spread your money differently" |
| "Stakeholder alignment is critical" | "Everyone involved needs to agree on what we're doing" |

**Shape Adjustment:**
In ELI5 mode, prefer the simplest shapes: answer-first keeps people oriented; a familiar named arc (Hero's Journey) only if its beats are fully source-supported. Avoid withheld reveals and multi-perspective structures — they demand patience ELI5 audiences shouldn't need.

---

## PHASE 3: Argument Outline + Conditional Shape (Gate 1)

The primary step is not framework selection. It is the **Argument Outline** — a plain-language account of the argument:

- What does this audience need to understand, and in what order?
- What does each section add to the case for the focal claim?
- Where does the Ask land?

**The test:** the sequence must make sense with no framework labels and no dramatic vocabulary. If the outline only holds together when you name an arc, the outline is not done.

### Conditional shape

With the Argument Outline in hand, choose the shape — in this order of preference:

1. **Answer-first (the default).** The claim lands by slide/section 2; the middle defends it in the outline's grouped reasons; the close returns to the Ask. This is the shape unless the material licenses something else. **"No named framework — direct explanation" is a first-class outcome**, not a fallback.
2. **Withheld-reveal (conditional).** Only when the Material Read named a **genuine surprise** — never manufacture one. Stakes first, the reveal at its natural midpoint, consequences after.
3. **Named arc (conditional, audited).** A named arc from [`framework-selection.md`](framework-selection.md)'s payload table, only when it survives the selection protocol there:
   - **Reveal gate:** engagement arcs are gated on the Material Read's surprise line.
   - **Payload match:** 2-4 candidates whose climax payload kind matches the focal's payload kind (Focal Fit Definition table).
   - **Beat-support audit:** every essential/anchor beat matched to a **QUOTED source passage**. Any unmatched beat rejects the arc — no [GENERATED] backfill. Note rejections in the brief.
   - **Skeleton stamp test:** stamp the surviving candidate's beat structure onto the Focal Statement and verify: (a) the climax/payoff beat structurally delivers the One Thing, (b) the closing beat structurally delivers the Ask, (c) the Through-Line is carried by the arc's natural emotional shape. All three must be Y.

*Fast mode: the outline and shape selection run silently; the chosen shape, its trace-to-material line, and any rejected-arc notes surface in the consolidated brief. An audit or stamp failure still escalates to the user.*

If a named arc was wanted but no candidate passes, do NOT force one. Widen to adjacent payload kinds once; otherwise fall back to answer-first direct explanation and say so:

> "No named arc structurally lands your focal with full source support — the candidates either pull toward [X] or need beats the source can't fill. I recommend direct answer-first explanation; the argument outline already carries the piece."

See [`framework-selection.md`](framework-selection.md) for the full selection protocol and the Focal Fit Definition table. See [`narrative-arcs.md`](narrative-arcs.md) and [`communication-frameworks.md`](communication-frameworks.md) for arc/framework details, [`emotional-arcs.md`](emotional-arcs.md) for emotional textures — all orchestrator/judge reference, never builder input.

### High-Stakes Content: Early Agent Review

For these content types, run Audience Advocate and Comms Specialist during shape recommendation:
- Investor pitch / fundraising
- Sales pitch
- Multi-stakeholder / controversial topic
- Policy recommendation
- Strategic plan / transformation

---

## PHASE 3.5: Build Brief

**Purpose:** compile everything the builder is allowed to know into one self-contained artifact. This is the bridge between "what did the user say" and "how should this be written." Present the Build Brief to the user for confirmation before building.

**The brief is a compiled artifact and the builder's sole rule source.** Paste the operative rules in; a rule left un-compiled does not exist for the builder. The builder reads the brief, the source, and exactly four craft files — it does **not** open `narrative-arcs.md`, `voice-profiles.md`, `audience-profiles.md`, `emotional-arcs.md`, `opening-closing-strategies.md`, `communication-frameworks.md`, or `rhetorical-figures.md`.

Generate a Build Brief in this format:

---

### Build Brief

**Focal Statement:** [from Phase 1.75]
- **The One Thing:** [single idea the piece must land]
- **The Ask:** [action or shift being driven toward]
- **The Through-Line:** [logical/emotional thread connecting everything]
- `focal_origin:` [inferred | user-selected | user-stated | user-selected-after-reset]

**Audience + Ask:** [the two one-liners from Phase 1.75 Step 1]

**Material Read:** [pasted IN FULL from Phase 1.75 Step 2 — stake, tension, genuine surprise or "none", strongest existing passages, what changes. This is the builder's Step 1 anchor.]

**Argument Outline:** [from Phase 3 — what this audience needs to understand, in what order, what each section adds, where the Ask lands]

**Shape + Register:** [`answer-first` | `withheld-reveal` | named arc: <name>] · [`boardroom` | `keynote` | prose]
- [Named arc only: the kept-beat skeleton and its pacing notes pasted VERBATIM — never a one-line shape string. Beats the source could not support were already cut; list them so the builder does not resurrect them.]

**Density:** [from Phase 2.5]

**Voice essentials:** [the operative rules compiled from `voice-profiles.md`: sentence structure, vocabulary register, paragraph rhythm, signature moves]

**Audience essentials:** [compiled from `audience-profiles.md`]
- Trust signals to hit: [2-3]
- Resistance triggers to avoid: [2-3]
- Evidence style: [type]
- Headline style: [specific to this audience]

**Opening/Closing note (optional):** [ONLY a pointer to a specific strongest passage from the Material Read — e.g., "open on the 9:14 scene". Never a strategy type from a catalog matrix. Omit if the Material Read offers no standout passage.]

---

> "Here's the Build Brief I'll use to guide the output. Anything you'd change before I build?"

The user can adjust any element. Once confirmed, the Build Brief becomes the binding reference for Phase 4. There is no Killer Line section and no opening/closing strategy matrix: ornament is licensed inside the builder's spine when the material yields it, never pre-drafted here.

---

## PHASE 4: Build (Subagent)

The build runs as a subagent executing **THE SPINE** — the nine-step procedure in [`prompts/builder.md`](prompts/builder.md): material anchor, claim, shape, titles/sections as a chain, test-then-revise-once, bans, licensed ornament, craft floor, content-driven length.

### Content-Driven Length

The builder determines length from the source content, not from any template. Named-arc beat structures are a **menu, not a checklist** — beats the source could not fill were already cut at brief compilation. A strong 8-slide deck beats a padded 20-slide deck.

### Pre-Build: Write Handoff Files

Before dispatching:
1. Create the run directory: `RUN_DIR = /tmp/ne-<yymmdd>-<slug>/`
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

1. Read `RUN_DIR/ne-output.md` (the orchestrator may read the sidecar too; the focal judge never does)
2. Do NOT present the output yet — run the gates in order: **Phase 4.6 → 4.7 → 4.8**
3. Present the output only after all three pass, then proceed to Phase 5

> Full output format templates (Presentation, Prose, sidecar) are in [`prompts/builder.md`](prompts/builder.md).

---

## PHASE 4.6: Focal Fidelity Gate (Gate 2)

A single-purpose blind judge whose only obsession is: **does this piece land The One Thing?** Phase 5 reviewers focus on prose quality, audience fit, and persuasion — without Gate 2, focal drift slips past them because the piece reads internally coherent.

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
   - **Automatic reset (once per run):** ONLY when the brief marks `focal_origin: inferred` (Fast mode, user never touched the focal line) and no reset has happened this run. Before re-entering the pipeline: delete ALL trigger files (`ne-focal-judge.md`, `ne-focal-judge-prior.md`, `ne-evidence-review.md`, `ne-humanizing-flags.md`) so the reset build starts clean in Initial Build Mode with a fresh `needs_revision_count`; the evidence reviewer's two-run cap also resets with the new draft. Then reopen Phase 1.75 with the judge's quoted passage as a new candidate; the user's new choice is marked `focal_origin: user-selected-after-reset`; then re-run Phases 3 → 3.5 → 4.
   - **Advisory (every other case):** for `user-selected`, `user-stated`, or `user-selected-after-reset` origins — and for ANY second mismatch in a run regardless of origin — the judge downgrades to an advisory inside the verdict it otherwise issues. The orchestrator surfaces the quoted passage and the audience-relevance argument to the user, never resets on its own.

### Cleanup

After the gate resolves: delete `ne-focal-judge.md` once its findings are closed (per the shared repair loop) and `ne-focal-judge-prior.md` at end-of-loop, so a future build does not accidentally enter revision mode.

### What Phase 4.6 does NOT do

- It does not coach prose quality (Phase 5), check persuasion or originality (Phase 5/5.5), or audit sourcing (Phase 4.8).
- It does not receive the focal, the sidecar, or any draft line in its dispatch — blindness is the mechanism.
- Its cold read DOES check engagement: an opening that raises no question, or an ending that ignores the opening, blocks PASS even on a semantic match. For decks, a broken title chain forces NEEDS_REVISION regardless of focal match.

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

For decks: after this gate passes (and Phase 5 if run), the orchestrator runs the render stage — keynote-create Stage 4 (`keynote-render.mjs` → `/impeccable` → PDF).

---

## PHASE 5: Targeted Review (2 Parallel Subagents)

### When to Run

Auto-run the panel only for high-stakes content types (the same list as Phase 3's early review: investor pitch, sales pitch, strategic plan / transformation, policy recommendation, multi-stakeholder / controversial). For everything else, offer it in one line after Gate 4 passes — "Want the two-reviewer pass? Optional for a piece like this; the four gates have already run." — and proceed without it if declined. The gates already guarantee focal fidelity, de-slop, and source fidelity; the panel adds audience and persuasion depth that low-stakes pieces can skip.

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
| [`deck-title-craft.md`](deck-title-craft.md) | Embedded keynote-create title guide — action titles, the title-chain tests (spoken-prose + antecedent), register variants, rewrite examples. **Builder input** (presentation path) and the judge's deck-branch test source. |
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

1. User provides content
2. **Ask mode: Fast or Guided.** Fast infers steps 3–8 from the content and presents one consolidated brief (focal candidates always visible, `focal_origin: inferred`); Guided walks them one at a time.
3. Ask output format (Presentation / Prose / Both). **If Presentation → ask the register: Boardroom sentence-titles or Keynote fragments (default Boardroom).** *(Guided; inferred + surfaced in Fast)*
4. **Pin audience + ask** (one line each; skip only if stated), then do the **Material Read** (stake, tension, genuine surprise or "none", strongest passages, what changes)
5. **Propose 2-3 stance-committing focal candidates** → user confirms → Focal Statement (One Thing / Ask / Through-Line) + `focal_origin` recorded. For decks this is the punchline.
6. Ask remaining discovery (purpose, content type, tone), then density mode *(Guided; inferred in Fast)*
7. **Write the Argument Outline**, then choose the shape conditionally (**Gate 1**): answer-first default; withheld-reveal only on a genuine surprise; named arc only after the beat-support audit (quoted passages) + skeleton stamp test in `framework-selection.md`
8. **Compile the Build Brief** (focal + origin, audience/ask, Material Read in full, argument outline, shape + register, density, voice + audience essentials, optional passage-pointer for open/close) → user confirms
9. **Create RUN_DIR** (`/tmp/ne-<yymmdd>-<slug>/`), write Build Brief and source content into it
10. **Dispatch build subagent** — runs THE SPINE, writes `ne-output.md` (body only) + `ne-output-meta.md` (sidecar)
11. **Gate 2** — dispatch the blind focal judge (dispatch message: audience, ask, register — never the focal). Route the verdict:
    - PASS → step 12
    - NEEDS_REVISION → shared repair loop (counter-capped at 3)
    - FRAMEWORK_MISMATCH → escalate to user; consider Phase 3 reset
    - FOCAL_MISMATCH → reopen Phase 1.75 once if `focal_origin: inferred`; otherwise surface as advisory
12. **Gate 3** — Tier-2 humanizing check, flag-only; drift → `ne-humanizing-flags.md` → shared repair loop
13. **Gate 4** — dispatch the evidence reviewer; BLOCKING findings → shared repair loop; minor-only findings pass with notes; two-run cap; then present the output. For decks, render (→ `/impeccable` → PDF) after step 14 when the review runs, immediately otherwise.
14. **Targeted review** — auto-dispatch 2 parallel subagents for high-stakes content; offer in one line otherwise (roles from the Phase 5 table, named in dispatch)
15. **Director synthesis**; for high-stakes content offer the Stress Test Panel (3 subagents, personas from the Phase 5.5 table); "tighter" and Change Log export on demand


