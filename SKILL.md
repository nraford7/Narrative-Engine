---
name: Narrative-Engine
description: "Transform any content into narrative-driven presentations OR prose using proven storytelling frameworks. Content-driven length, integrated compression, optional stress testing. Use when converting content to presentations, restructuring existing decks, writing long-form pieces, or optimizing for specific audiences."
---

# Narrative Engine

Transform content into compelling narratives — as presentations or prose. Content determines length — no padding, no artificial minimums.

## Workflow Overview

```
PHASE 1     Content Import
    ↓
PHASE 1.5   Output Format — Presentation / Prose / Both
            ⇒ Presentation selected → BUILD ON THE keynote-create MODEL (titles-as-beats + render)
    ↓
PHASE 1.75  Focal Discovery — "What's the ONE point?"  (= keynote-create punchline)
    ↓
PHASE 2     Discovery Questions — Audience, purpose, content type, tone
    ↓
PHASE 2.5   Density Mode — Varies by output format
    ↓
PHASE 3     Framework Recommendation — Full sweep + dark horse
            ★ GATE 1: Focal Fidelity Scoring + Skeleton Stamp Test ★
    ↓
PHASE 3.5   Build Brief — Translates ALL discovery into concrete writing instructions
    ↓
    ══════ HANDOFF: Write Build Brief + Source to /tmp/ ══════
    ↓
PHASE 4     Build — SUBAGENT (Content Length Assessment + Originality Check)
            • Prose path → build, then Tier-1 prose-craft pass on every paragraph
            • Presentation path → keynote-create Stage 3 (titles-as-beats, titles-only test,
              prose-craft on titles) then Stage 4 render → /impeccable → PDF
    ↓
    ══════ HANDOFF: Output written to /tmp/ ══════
    ↓
PHASE 4.6   ★ GATE 2: Focal Fidelity Loop ★
            Cold-Read Judge SUBAGENT → PASS / NEEDS_REVISION / FRAMEWORK_MISMATCH
            (decks: the keynote-create titles-only test IS this gate)
            • PASS → continue to Phase 4.7
            • NEEDS_REVISION → re-dispatch builder in revision mode (max 3 passes)
            • FRAMEWORK_MISMATCH → escape valve back to Phase 3
    ↓
PHASE 4.7   ★ GATE 3: Humanizing Pass ★  (evidence-grounded de-slop)
            Tier 2 discourse-level structural-delta gate — see humanizing-pass.md
    ↓
PHASE 5     Targeted Review — 2 SUBAGENTS (content-type selected) + Director synthesis
    ↓
PHASE 5.5   Stress Test — 3 SUBAGENTS + Director triage (high-stakes content only)
    ↓
ON-DEMAND   "Tighter" — Compression passes anytime (re-runs prose-craft + humanizing)
```

**Three structural gates protect the work:**

- **Gate 1 (Phase 3)** stops a Wrong Framework from being chosen — frameworks are scored on focal fidelity and must pass the skeleton stamp test before they can be a Top Pick.
- **Gate 2 (Phase 4.6)** catches drift between intent and execution — a cold-read judge reads the output before the brief, names the One Thing, and compares. If revision can close the gap it loops; if it can't, it escapes back to Phase 3 with a framework-mismatch diagnosis. For decks, the keynote-create **titles-only test** is this gate.
- **Gate 3 (Phase 4.7)** catches AI-slop the first two miss — a discourse-level humanizing pass grounded in the narrative-structure research corpus. The evidence: a classifier still detects AI from *structure* at 93.9% after surface lexical cleanup, so sentence-polishing alone cannot de-slop a draft. See [`humanizing-pass.md`](humanizing-pass.md).

**Sentence discipline is always on.** Every prose paragraph and every deck title is built through the **embedded prose-craft discipline** ([`prose-craft.md`](prose-craft.md) + [`prose-craft-constructions.md`](prose-craft-constructions.md)) during the build (Tier 1 of the humanizing pass). It is *embedded, not invoked* — the build subagent reads these files directly, so Narrative Engine runs once with no dependency on a separate skill. This is non-optional and replaces the old qualitative "AI Test" with a named discipline.

---

## Subagent Architecture

Phases 1–3.5 run interactively in the main conversation. Phases 4, 4.6, 5, and 5.5 run as subagents via the Task tool, reducing context window pressure and enabling parallel execution.

### Handoff Files

| File | Written by | Read by |
|------|-----------|---------|
| `/tmp/ne-build-brief.md` | Main (end of Phase 3.5) | Build, Focal Judge, Reviewers, Stress Testers |
| `/tmp/ne-source-content.md` | Main (end of Phase 3.5) | Build subagent |
| `/tmp/ne-output.md` | Build subagent | Main, Focal Judge, Reviewers, Stress Testers |
| `/tmp/ne-cold-read.md` | Focal Judge (Phase A) | Focal Judge (Phase B), Build (revision mode) |
| `/tmp/ne-focal-judge.md` | Focal Judge (Phase B) | Main, Build (revision mode) |
| `/tmp/ne-focal-judge-prior.md` | Main (between Phase 4.6 passes) | Focal Judge (pattern detection) |

### Prompt Templates

| Template | Phase | Dispatch |
|----------|-------|----------|
| [`prompts/builder.md`](prompts/builder.md) | 4 (initial), 4.6 (revision) | 1 agent, serial. Self-detects mode via `/tmp/ne-focal-judge.md` |
| [`prompts/focal-fidelity-judge.md`](prompts/focal-fidelity-judge.md) | 4.6 | 1 agent, serial. Single obsession: does the piece land The One Thing? |
| [`prompts/reviewer.md`](prompts/reviewer.md) | 5 | 2 agents, parallel (content-type selected) |
| [`prompts/stress-tester.md`](prompts/stress-tester.md) | 5.5 | 3 agents, parallel (high-stakes only) |

### Pre-Phase-4.6 File Hygiene

Between focal-fidelity passes, the orchestrator must rotate judge artifacts so the next pass can do pattern detection:

1. Before re-dispatching the Focal Judge for pass N+1, copy `/tmp/ne-focal-judge.md` → `/tmp/ne-focal-judge-prior.md`.
2. Before re-dispatching the Builder in revision mode, leave `/tmp/ne-focal-judge.md` in place — that file is the Builder's signal to enter Revision Mode.
3. After the loop exits (PASS, FRAMEWORK_MISMATCH, or cap reached), delete `/tmp/ne-focal-judge.md` and `/tmp/ne-focal-judge-prior.md` so a future build does not accidentally enter revision mode.

---

## PHASE 1: Content Import

Accept content in any form:
- Pasted prose, articles, or reports
- Outlines or bullet points
- Research notes or data
- Existing presentation text
- URLs (fetch and extract)

If user pastes content without instructions, acknowledge receipt and proceed to Output Format.

---

## PHASE 1.5: Output Format

Ask before proceeding to focal discovery:

> **What format do you need?**
> 1. **Presentation** — Slide deck with headlines, spotlights, and design notes
> 2. **Prose** — Long-form document with sections, transitions, and flow
> 3. **Both** — Build one, derive the other (specify which first)

### If Prose selected:

Ask for target length:

> **Target length?**
> 1. **Short** (~500-800 words) — Tight, punchy, every sentence earns its place
> 2. **Medium** (~1,000-1,500 words) — Room to develop ideas, standard article length
> 3. **Long** (~2,000-3,000 words) — Comprehensive, detailed, thought leadership depth
> 4. **Let content determine** — No artificial target

### If Both selected:

> **Which format first?**
> 1. **Prose → Presentation** — Write the full narrative, then compress to slides
> 2. **Presentation → Prose** — Build the deck structure, then expand to prose

**Note:** The frameworks (Trojan Horse, Heist, Time Machine, etc.) are *narrative structures* — they work for both formats. The divergence happens at the Build phase.

### If Presentation (or Both, presentation half) selected: build on the keynote-create model

Narrative Engine owns the *intelligence* a deck needs that keynote-create lacks — full framework
sweep, focal-fidelity scoring, audience profiling, the review panel. keynote-create owns the *deck
craft* Narrative Engine lacks — titles-as-story-beats, the titles-only test, five-act compression by
length, and an actual render pipeline to HTML + PDF. **For any presentation, use both: Narrative
Engine's discovery and gates wrap around a keynote-create build.**

The handoff maps cleanly because the two skills already share a spine:

| Narrative Engine | keynote-create equivalent |
|---|---|
| Focal Statement (Phase 1.75) | **Punchline** — the deck's one-line spine |
| Density Mode (Phase 2.5) | **Density** — identical four modes (High-Impact / Narrative / Evidence / ELI5) |
| Chosen arc + skeleton (Phase 3) | The **five-act arc**, with the chosen NE arc supplying the dramatic shape |
| Build (Phase 4) | keynote-create **Stage 3** (title sequence) + **Stage 4** (render → /impeccable → PDF) |
| Focal Fidelity Loop (Phase 4.6) | The **titles-only test** (spoken-prose + antecedent checks) |

Because the Focal Statement *is* the punchline and the density modes are identical, do **not**
re-ask keynote-create's Stage 1–2 questions. Run Narrative Engine's discovery once, then enter
keynote-create at its Stage 3. The defining keynote-create constraint carries through: **every slide
title is a short complete sentence that delivers one story beat; read top-to-bottom, the titles tell
the whole narrative with no bodies needed.**

**The title-craft is embedded, not invoked.** The build subagent reads
[`deck-title-craft.md`](deck-title-craft.md) (a verbatim embed of keynote-create's title guide) and
applies it directly — Narrative Engine runs once, with no dependency on a separate skill for the title
build. Only the **render stage** (Stage 4 — `keynote-render.mjs` → `/impeccable` → PDF) runs in the
orchestrator after the gates pass and legitimately calls keynote-create, since that is main-conversation
work, not a subagent.

---

## PHASE 1.75: Focal Discovery

**Purpose:** Establish the single point before anything else.

Read the content and propose 2-3 possible focal points:

> "Based on your material, I see these possible angles:
> 1. **[Angle A]** — [Why this could be the point]
> 2. **[Angle B]** — [Why this could be the point]
> 3. **[Angle C]** — [Why this could be the point]
>
> Which direction should we optimize for? Or is there a different point you want to land?"

**Skip if:** User already explicitly stated their point.

**Output:** A Focal Statement (1-2 sentences) that becomes the north star.

The Focal Statement has three components:
- **The One Thing:** Single idea the piece must land
- **The Ask:** Action or shift being driven toward
- **The Through-Line:** Logical/emotional thread connecting everything

---

## PHASE 2: Discovery Questions

Ask one question at a time. Wait for the user to answer before asking the next question. User can respond with numbers or their own words.

### Question 1: Audience

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
> 1. **Punchy** — Short paragraphs. High signal density. Every sentence earns its place. Hemingway, not Faulkner.
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
- Every abstract concept gets a concrete analogy
- Draw from everyday experience: kitchen, playground, family, sports, weather
- "It's like..." should appear frequently
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

**Framework Adjustment:**
In ELI5 mode, simpler narrative arcs work better:
- **Hero's Journey** — natural story shape everyone recognizes
- **Columbo** — answer-first keeps people oriented
- **Trojan Horse** — start where they are, guide to insight
- Avoid: Mystery Box (requires patience), Rashomon (requires holding multiple views)

---

## PHASE 3: Framework Recommendation (Gate 1)

Based on discovery answers, recommend frameworks using the Full Sweep Protocol. **Gate 1 — focal fidelity scoring + skeleton stamp test — is non-optional and lives inside this phase.**

**REQUIRED:** Before recommending, complete the framework scoring sweep in [`framework-selection.md`](framework-selection.md). This means:
1. Score all 10 narrative arcs on TWO dimensions (1-5 each): **Context Fit** (audience/purpose/content/tone) and **Focal Fit** (does the arc's climax beat structurally deliver The One Thing?). Combined Total = max 10.
2. Score the top 5 communication frameworks on the same two dimensions.
3. **Run the Skeleton Stamp Test on the top 2 candidates by Total score.** Stamp each candidate's beat structure onto the Focal Statement and verify three conditions: (a) the climax/payoff beat structurally delivers the One Thing, (b) the closing beat structurally delivers the Ask, (c) the Through-Line is carried by the arc's natural emotional shape. **All three must be Y to pass.** A candidate that fails the skeleton stamp test cannot be Top Pick or Strong Alternative regardless of its scores.
4. Present the top 2 arc + framework pairings (skeleton-stamp-passing only) with the stamped skeleton, tradeoffs, and emotional preview.
5. Present 1 Dark Horse — an unexpected option scoring 3+ on Focal Fit specifically (Context Fit may be lower) that would land the focal in an unexpected way. Dark Horses are exempt from passing the skeleton stamp on first run, but flag the structural risk if selected.
6. Include a Rejection Log — 1-2 sentences calling out (a) arcs that scored well on Context Fit but failed Focal Fit, and (b) low-Total arcs that don't fit this content.

If neither top candidate passes the skeleton stamp test, do NOT recommend a workaround. Escalate to the user with a clear diagnosis:

> "None of the top frameworks structurally land your focal — the strongest candidates pull the piece toward [X] instead of [Focal]. Possible options: (1) reframe the focal, (2) accept a Dark Horse with lower context fit but better focal fit, (3) split into two pieces."

For each recommendation:
1. **Name the framework** and category
2. **Show the stamped skeleton** — beat-by-beat, with explicit notes on what each beat carries of the focal, and whether the climax delivers the One Thing
3. **Explain fit** in 2-3 sentences specific to their situation
4. **Flag tradeoffs** — what this framework does well vs. potential drawbacks (including any focal-fidelity risks)
5. **Emotional preview** — what the audience will *feel* at the key moments (reference [`emotional-arcs.md`](emotional-arcs.md))

See [`framework-selection.md`](framework-selection.md) for the full sweep protocol, scoring matrices, and the Focal Fit Definition table mapping payload kinds to high-fit arcs.
See [`narrative-arcs.md`](narrative-arcs.md) for arc details including emotional textures.
See [`communication-frameworks.md`](communication-frameworks.md) for framework details.

### High-Stakes Content: Early Agent Review

For these content types, run Audience Advocate and Comms Specialist during framework recommendation:
- Investor pitch / fundraising
- Sales pitch
- Multi-stakeholder / controversial topic
- Policy recommendation
- Strategic plan / transformation

---

## PHASE 3.5: Build Brief

**Purpose:** Translate ALL discovery answers into concrete writing instructions. This is the bridge between "what did the user say" and "how should this be written." Present the Build Brief to the user for confirmation before building.

Generate a Build Brief in this format:

---

### Build Brief

**Focal Statement:** [from Phase 1.75]
**Framework:** [selected in Phase 3] + [communication framework overlay]
**Density:** [from Phase 2.5]

**Voice Profile:** [Auto-derived from audience + tone, or user override]
- See [`voice-profiles.md`](voice-profiles.md) for full profile
- Key instruction: [2-3 sentence summary of the voice's rules]

**Audience Profile:** [from Phase 2]
- See [`audience-profiles.md`](audience-profiles.md) for full profile
- Trust signals to hit: [list 2-3]
- Resistance triggers to avoid: [list 2-3]
- Evidence style: [type]
- Headline style: [specific to this audience]

**Emotional Arc:** [from emotional-arcs.md]
- Shape: [e.g., "comfort → unease → snap → reorientation → urgency"]
- Intensity dial: [1-5, calibrated to audience]
- Key emotional moment: [which beat, how to handle it]

**Persuasion Strategy:** [2-3 principles from Cialdini or Buyer Psychology, prioritized for this audience]
- Primary: [principle] — apply by [specific instruction]
- Secondary: [principle] — apply by [specific instruction]
- Buyer psychology lens: [1 relevant model, e.g., "Confirmation Bias — align with audience's existing belief that X"]
- See [`agent-reference-persuasion.md`](agent-reference-persuasion.md) §13-14 for full model catalog

**Opening Strategy:** [selected from opening-closing-strategies.md]
- Type: [e.g., Cold Open Scene]
- Combined with framework beat: [e.g., "The Prestige's Pledge beat, delivered as a Cold Open Scene"]

**Closing Strategy:** [selected from opening-closing-strategies.md]
- Type: [e.g., The Simple Truth]
- Combined with framework beat: [e.g., "The Prestige's Callback beat, delivered as The Simple Truth"]

**Killer Line Target:** [Draft 2-3 candidate killer lines based on the focal statement. Refine during build.]

**Anti-Sameness Notes:** [Any specific instructions to avoid generic patterns — e.g., "This audience has seen 100 'digital transformation' decks. Find a fresh angle on slide structure or metaphor."]

---

> "Here's the Build Brief I'll use to guide the output. Anything you'd change before I build?"

The user can adjust any element. Once confirmed, the Build Brief becomes the binding reference for Phase 4.

---

## PHASE 4: Build (Subagent)

The build phase runs as a subagent via the Task tool, offloading the heaviest generation work from the main conversation. The build includes a Content Length Assessment (Step 0) and Originality Check (Phase 4.5), both folded into the subagent.

### Content-Driven Length

The builder determines length from the source content, not from the arc template. Arc beat structures are a **menu, not a checklist** — the builder skips or combines beats that lack enough content to justify their own slide or section. A strong 8-slide deck beats a padded 20-slide deck.

### Pre-Build: Write Handoff Files

Before dispatching:
1. Write the confirmed Build Brief to `/tmp/ne-build-brief.md`
2. Write the user's source content to `/tmp/ne-source-content.md`

### Dispatch

Create one Task:
- **subagent_type:** `general-purpose`
- **Prompt:** Read and execute [`prompts/builder.md`](prompts/builder.md)
- The subagent first runs a Content Length Assessment (Step 0) to count substantive points and set a target length
- The subagent reads all reference files specified in the Build Brief (arc, voice, audience, emotional texture, strategies, checklists)
- **Prose path:** build the draft, then apply the **embedded prose-craft discipline** ([`prose-craft.md`](prose-craft.md)) to every paragraph as the sentence-level pass (Tier 1 of the humanizing pass — register-matched to the Density Mode; see [`humanizing-pass.md`](humanizing-pass.md))
- **Presentation path:** execute keynote-create Stage 3 — draft the title sequence as story beats, run the cold-read self-check and the **titles-only test**, then apply the **embedded prose-craft discipline to the titles only** (bodies stay as terse bullets). Stage 4 render → `/impeccable` layout promotion → PDF happens after the gates pass.
- The subagent runs the Originality & Anti-Sameness Checklist before finalizing (Phase 4.5 folded in)
- Output written to `/tmp/ne-output.md`

### Post-Build

1. Read `/tmp/ne-output.md`
2. Do NOT present the output yet — first run **Phase 4.6 (Focal Fidelity Loop)**
3. After Phase 4.6 returns PASS, run **Phase 4.7 (Humanizing Pass)**, then present the output and proceed to Phase 5

### Content Sourcing Tags

| Tag | Meaning |
|-----|---------|
| `[DIRECT]` | Quoted or nearly verbatim from source |
| `[PARAPHRASE]` | User's ideas restated |
| `[ELABORATED]` | User's concept expanded |
| `[GENERATED]` | New content for narrative flow |

> Full output format templates (Presentation, Prose, Converting Between Formats) are in [`prompts/builder.md`](prompts/builder.md).

---

## PHASE 4.6: Focal Fidelity Loop (Gate 2)

Between Build (Phase 4) and Targeted Review (Phase 5), the output passes through a single-purpose judge whose only obsession is: **does this piece land The One Thing?** Phase 5 reviewers focus on prose quality, audience fit, and persuasion — they have access to the Build Brief but their key questions are not about focal fidelity. Without Gate 2, focal drift slips past Phase 5 because the piece reads internally coherent.

### Why a separate gate, not just another reviewer

The framework's beat structure has gravity. Once an arc is selected, the build naturally serves the arc — and the arc serves *its* climax payload, which may not be the focal payload. Specialist reviewers compound the problem: they evaluate craft against the Build Brief without re-deriving the One Thing from the output itself. A cold-read judge breaks that gravity by reading the output *before* the brief and reporting what it actually communicates.

### Pass Cap

**Maximum 3 builder passes per loop** (initial build + 2 revisions). Empirically, drift that does not converge in 3 passes is structural — editing cannot close it, only changing the framework can.

### Loop Logic

```
Pass 1:  Builder (initial) → Output v1
         ↓
         Focal Judge (cold-read v1) → Verdict v1
         ↓
         ├─ PASS                  → Exit loop, proceed to Phase 5
         ├─ NEEDS_REVISION        → Pass 2
         └─ FRAMEWORK_MISMATCH    → Escape to Phase 3 with diagnosis

Pass 2:  Rotate ne-focal-judge.md → ne-focal-judge-prior.md
         Builder (revision mode reads judge findings) → Output v2
         ↓
         Focal Judge (cold-read v2, pattern-checks against prior) → Verdict v2
         ↓
         ├─ PASS                  → Exit loop, proceed to Phase 5
         ├─ NEEDS_REVISION        → Pass 3
         └─ FRAMEWORK_MISMATCH    → Escape to Phase 3 with diagnosis

Pass 3:  Rotate ne-focal-judge.md → ne-focal-judge-prior.md
         Builder (revision mode) → Output v3
         ↓
         Focal Judge (cold-read v3, pattern-checks) → Verdict v3
         ↓
         ├─ PASS                  → Exit loop, proceed to Phase 5
         └─ NEEDS_REVISION OR     → CAP REACHED → Escalate to user with
            FRAMEWORK_MISMATCH       diagnosis. The judge will typically
                                     auto-escalate NEEDS_REVISION to
                                     FRAMEWORK_MISMATCH at this point.
```

### Dispatch (each pass)

The Focal Judge runs as a single-agent serial dispatch. Do NOT parallelize — its cold-read protocol depends on a deterministic file-reading order.

- **subagent_type:** `general-purpose`
- **Prompt:** Read and execute [`prompts/focal-fidelity-judge.md`](prompts/focal-fidelity-judge.md)
- **Inputs read by judge:** `/tmp/ne-output.md`, `/tmp/ne-build-brief.md`, `/tmp/ne-focal-judge-prior.md` (if exists)
- **Outputs written by judge:** `/tmp/ne-cold-read.md`, `/tmp/ne-focal-judge.md`

After dispatch, the orchestrator (main conversation):

1. Reads `/tmp/ne-focal-judge.md` to get the verdict.
2. Routes based on verdict (see Loop Logic above).
3. **Before re-dispatching** for a revision pass: copy `/tmp/ne-focal-judge.md` → `/tmp/ne-focal-judge-prior.md` so the next judge run can detect convergence patterns.
4. **After loop exit** (any cause): delete both judge files so the next build starts clean.

### Builder Revision Mode

The Builder prompt detects revision mode automatically: if `/tmp/ne-focal-judge.md` exists when the Builder dispatches, it reads the judge findings and the prior `/tmp/ne-output.md` and applies *targeted edits* rather than a full rebuild. See [`prompts/builder.md`](prompts/builder.md) "Revision Mode Workflow" for details.

The orchestrator does NOT need to send different prompts for initial vs. revision dispatch — the Builder self-routes on file presence.

### Verdict Handling

**On PASS:**
> "Focal fidelity confirmed — the cold-read of the output matches the Focal Statement. Proceeding to specialist review (Phase 5)."

Show the user a short summary: cold-read One Thing, Brief One Thing, and the judge's confidence/notes. Then continue.

**On NEEDS_REVISION (within cap):**
> "Pass [N] focal drift detected: [judge's specific drift summary]. Dispatching builder in revision mode to address [specific edits]."

Don't ask the user — loop automatically until PASS or cap. The user can interrupt, but the default is to drive to PASS.

**On FRAMEWORK_MISMATCH (any pass) OR cap reached:**
> "The selected framework cannot structurally land your focal. The judge diagnosed: [diagnosis]. Recommended Phase 3 alternatives: [list]. Options: (1) restart Phase 3 with a different framework, (2) revise the Focal Statement, (3) accept the current draft as-is and move on. Which do you prefer?"

Do not silently restart Phase 3 — the user owns the decision because reframing the focal vs. switching frameworks vs. accepting drift is a judgment call about the work, not a mechanical step.

### What Phase 4.6 does NOT do

- It does not coach prose quality. That is Phase 5's job.
- It does not check audience fit, persuasion, factual accuracy, or originality. Those are Phase 5 / 5.5.
- It does not re-derive the focal — the focal is established in Phase 1.75 and is binding through Phase 4.6. If the user wants to change the focal, that is a Phase 1.75 reset, which restarts Phase 3 → 4 → 4.6.

The narrow scope is the point. A single-question gate is sharper than a multi-dimensional reviewer for this specific failure mode.

---

## PHASE 4.7: Humanizing Pass (Gate 3)

After focal fidelity passes and before the review panel, the draft passes through the humanizing
pass — the de-slopping layer. Full protocol and the cardinal rules in [`humanizing-pass.md`](humanizing-pass.md); the essentials:

**Why a separate gate from prose-craft.** prose-craft (Tier 1, run in the build) cleans the
*sentence* — lexical tells, monotone cadence. But the research corpus shows a classifier still
detects AI from *structure* at 93.9% macro-F1 after that lexical cleanup. The AI signature lives in
the discourse, not the words. Tier 2 is the only gate that reaches it.

**The check (Tier 2 — discourse level).** Run the structural-delta checklist against the draft:

1. **Theme-statement budget** — humans state the theme 52% of the time, AI 77%. Cut redundant body
   restatements; keep the explicit statement only at the climax and close. *(Note the irony: the
   Focal Statement and Killer Line push toward over-statement — this gate is the counterweight.)*
2. **Tolerate asymmetry / open threads** — resist resolving and moralizing every beat; leave honestly-open questions open.
3. **Preserve temporal complexity** — verify intended non-linearity wasn't flattened to chronology.
4. **Discourse redundancy** — kill runs of paragraphs that make the identical move; no fractal summary.
5. **Restore idiosyncrasy** — one concrete particular per section; one un-templatable moment in the piece.

**The cardinal rule, non-negotiable:** these are **gates and drift detectors, never optimization
objectives**. The figures are fiction-derived and directional. Do not loop a generator against them —
optimizing the metric manufactures the slop the pass removes. Flag drift, then fix by hand.

**Disposition:**
- If the draft passes, note it briefly and proceed to Phase 5.
- If it drifts on one or more deltas, apply targeted edits in place (this is an edit pass, not a rebuild), then re-check and proceed.

---

## PHASE 5: Targeted Review (2 Parallel Subagents)

Two specialist agents review the output simultaneously via the Task tool. The agents are selected based on content type to focus on the dimensions that matter most for this specific piece.

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

The builder already runs compression (Three-Level Clarity System) and originality checking (Phase 4.5) internally. Adding 6 independent reviewers fragments the unified voice and emotional arc that the builder produced. Two focused reviewers catch the highest-value issues without overwhelming the piece with competing rewrites.

### Reviewer Selection by Content Type

The Audience Advocate is always one reviewer — "does this land for the audience?" is the universal review question. The second reviewer is selected based on the highest-risk dimension for this content type.

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
| Scenario planning | Audience Advocate | Comms Specialist | Fork framing must be tight |
| Case study | Audience Advocate | Content Expert | Facts drive the credibility |
| Product launch | Audience Advocate | Comms Specialist | Messaging clarity is key |
| Policy recommendation | Audience Advocate | Content Expert | Evidence and accuracy critical |

### Dispatch

Create 2 Tasks simultaneously using [`prompts/reviewer.md`](prompts/reviewer.md) with the content-type-selected parameters.

Each subagent:
- **subagent_type:** `general-purpose`
- Reads `/tmp/ne-output.md` and `/tmp/ne-build-brief.md` plus its reference file
- Returns findings as task result (not written to file)

**Judge hygiene.** The reviewers (and the Phase 4.6 / 5.5 judges) are LLM-as-judge, which carries
verbosity, position, and self-preference bias. Instruct each to score against the Build Brief and the
Content-Driven Length principle — a tight piece is not worse than a padded one — and treat confidence
scores as advisory, not as a gate. See [`humanizing-pass.md`](humanizing-pass.md) → *Judge hygiene*.

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

### Auto-Selection by Content Type

| Content Type | Auto-Selected |
|--------------|---------------|
| Investor pitch | CFO, COO, Skeptic |
| Sales pitch | Skeptic, COO, Engineer |
| Strategic plan | COO, Conservative, Risk Officer |
| Policy recommendation | Lawyer, Risk Officer, Conservative |

### Dispatch

Create 3 Tasks simultaneously using [`prompts/stress-tester.md`](prompts/stress-tester.md) with the auto-selected persona parameters. Each subagent:
- **subagent_type:** `general-purpose`
- Reads `/tmp/ne-output.md` and `/tmp/ne-build-brief.md`
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
4. **Re-run prose-craft + the humanizing pass** — compression tends to flatten sentence-length variance (a Reinhart AI-tell) and to re-introduce theme-restatement; re-check both Tier 1 and Tier 2 after cutting. For decks, re-run the titles-only test.
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
| [`humanizing-pass.md`](humanizing-pass.md) | The de-slop layer — Tier 1 (prose-craft) + Tier 2 (discourse structural-delta checklist), judge hygiene, and the gate-not-objective rule. Grounded in the narrative-structure research corpus. |
| [`prose-craft.md`](prose-craft.md) + [`prose-craft-constructions.md`](prose-craft-constructions.md) | Embedded sentence-level discipline (Floor/Filter/Ceiling + construction catalog). Tier 1 of the humanizing pass. Applied directly by the builder — not a separate skill call. |
| [`deck-title-craft.md`](deck-title-craft.md) | Embedded keynote-create title guide — action titles, the titles-only test, antecedent test, rewrite examples. Used by the presentation build path. |
| [`checklists.md`](checklists.md) | All quality checklists (headlines, CTAs, pricing, compression) |
| [`framework-selection.md`](framework-selection.md) | Selection matrices by audience, purpose, tone — and the focal-fidelity scoring + skeleton stamp test (Gate 1) |
| [`narrative-arcs.md`](narrative-arcs.md) | 10 narrative arc structures with beats |
| [`communication-frameworks.md`](communication-frameworks.md) | Efficiency frameworks (Pyramid, AIDA, PAS, etc.) |
| [`agent-reference-persuasion.md`](agent-reference-persuasion.md) | Comms agent deep reference |
| [`agent-reference-visual.md`](agent-reference-visual.md) | Visual agent deep reference |
| [`agent-reference-verification.md`](agent-reference-verification.md) | Content expert deep reference |
| [`audience-profiles.md`](audience-profiles.md) | Deep audience profiles carrying through build |
| [`voice-profiles.md`](voice-profiles.md) | 7 voice profiles with auto-derive mapping |
| [`emotional-arcs.md`](emotional-arcs.md) | Framework emotional textures + audience calibration |
| [`opening-closing-strategies.md`](opening-closing-strategies.md) | Opening/closing strategy libraries |
| [`prompts/builder.md`](prompts/builder.md) | Build subagent — initial mode + revision mode (Phase 4 / 4.6) |
| [`prompts/focal-fidelity-judge.md`](prompts/focal-fidelity-judge.md) | Cold-read judge — Gate 2, single obsession: does the piece land The One Thing? |
| [`prompts/reviewer.md`](prompts/reviewer.md) | Targeted review subagents (Phase 5) — Audience Advocate + content-type-selected specialist |
| [`prompts/stress-tester.md`](prompts/stress-tester.md) | Stress test panel (Phase 5.5, high-stakes only) |
| [`examples/`](examples/) | Full workflow examples |

---

## Quick Start

1. User provides content
2. Ask output format (Presentation / Prose / Both). **If Presentation → build on the keynote-create model** (titles-as-beats + render); Narrative Engine's discovery and gates wrap around it.
3. Propose focal points → user confirms (this becomes the Focal Statement — binding through Phase 4.6; for decks it is the keynote-create punchline)
4. Ask discovery questions (audience, purpose, content type, tone)
5. Ask density mode (varies by format)
6. **Full sweep** all frameworks with focal-fidelity scoring + skeleton stamp test (**Gate 1**) → recommend 2 passing candidates + 1 dark horse → user selects
7. **Generate Build Brief** (voice, audience profile, emotional arc, strategies, killer line candidates) → user confirms
8. **Write handoff files** — Build Brief and source content to `/tmp/`
9. **Dispatch build subagent** — runs content length assessment, builds, runs **prose-craft** (Tier 1) on prose/titles, runs originality check, writes to `/tmp/ne-output.md`. Presentation path follows keynote-create Stage 3.
10. **Run Focal Fidelity Loop** (**Gate 2**) — dispatch focal-fidelity-judge subagent (decks: titles-only test). Loop revisions up to 3 passes total. Routes:
    - PASS → continue to step 10.5
    - NEEDS_REVISION → re-dispatch builder in revision mode, re-judge
    - FRAMEWORK_MISMATCH or cap reached → escalate to user; consider Phase 3 reset
10.5. **Run Humanizing Pass** (**Gate 3**) — Tier-2 discourse structural-delta check (`humanizing-pass.md`); fix drift by hand. For decks, render → `/impeccable` → PDF after this passes.
11. **Dispatch 2 targeted review subagents in parallel** — content-type selected from `prompts/reviewer.md`
12. **Director synthesis** in main conversation — present focused recommendations
13. For high-stakes content only: offer Stress Test Panel → **dispatch 3 stress test subagents** if accepted
14. User requests "tighter" if needed
15. Offer Change Log export
