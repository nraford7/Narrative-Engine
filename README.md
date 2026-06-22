# Narrative Engine

**A Claude Code skill that transforms any content into compelling narratives — as presentations or prose — using proven storytelling frameworks.**

Most presentations fail before they begin. Not because the content is wrong, but because the structure is. Narrative Engine matches your material to the right storytelling framework, auto-derives a distinct voice and emotional arc for your specific audience, then drives the output through three structural gates and a targeted review that catch what you'd miss.

It runs as one self-contained skill. The sentence-level discipline (`prose-craft`) and the deck title-craft (`keynote-create`) are **embedded**, not invoked — so a single run never depends on a separate skill at build time.

---

## What It Does

Paste an article, outline, research notes, or existing deck. Choose presentation or prose. Answer discovery questions. Get back:

1. **Full-sweep framework scoring** across all 10 arcs + 7 communication frameworks, with a Dark Horse option
2. **A Build Brief** translating your audience, voice, emotional arc, and strategies into concrete writing instructions
3. **A complete output** (slides or prose) with auto-derived voice, emotional pacing, and opening/closing strategies — every sentence and every slide title run through the embedded `prose-craft` discipline
4. **Three structural gates** — framework fit, focal fidelity, and an evidence-grounded **humanizing pass** that de-slops at the discourse level, not just the surface
5. **A targeted review** (content-type-selected specialists) plus an optional stress-test panel for high-stakes work
6. **Sourcing transparency** showing what came from your content vs. what was generated

---

## How It Works

### Phase 1: Discovery

```
Output format?               → Presentation / Prose / Both
Focal point?                 → Choose from 2-3 proposed angles
Who is your audience?        → Executive / Technical / Investors / Skeptics / Mixed...
What are you trying to do?   → Persuade / Inform / Inspire / Align / Report...
What type of content?        → Research / Strategy / Case study / Pitch / Vision...
What tone?                   → Authoritative / Provocative / Warm / Urgent / Balanced...
Density mode?                → High-Impact / Narrative / Evidence / ELI5
```

### Phase 2: Framework Matching

The skill draws from **17 proven frameworks** across two categories:

**10 Narrative Arcs** (engagement-optimized)
| Arc | Structure | Best For |
|-----|-----------|----------|
| The Prestige | Pledge → Turn → Prestige | Counterintuitive findings |
| Mystery Box | Clues → Red herrings → Click | Research with unexpected conclusions |
| The Heist | Goal → Obstacles → Crew → Execution | Strategy & transformation |
| Time Machine | Future-back → Present fork → Path | Vision & scenario planning |
| Trojan Horse | Relatable → Escalate → Reframe | Paradigm shifts, skeptical audiences |
| Hero's Journey | Call → Trials → Ordeal → Return | Origin stories, change management |
| Columbo | Outcome first → Reconstruction | Post-mortems, root cause analysis |
| Game of the Scene | Pattern → Name it → Heighten 3x | Hidden dynamics, cross-domain insight |
| Rashomon | Multi-view → Missing axis → Synthesis | Controversial topics, stakeholder alignment |
| Freytag's Five-Act | Exposition → Climax → Resolution | Complex emotional narratives |

**7 Communication Frameworks** (efficiency-optimized)
| Framework | Structure | Best For |
|-----------|-----------|----------|
| Minto Pyramid | Answer → MECE supports → Evidence | Executive updates, board decks |
| SCQA | Situation → Complication → Question → Answer | Opening hooks |
| AIDA | Attention → Interest → Desire → Action | Sales, fundraising |
| PAS | Problem → Agitation → Solution | Change management |
| Raskin Sales Deck | Change → Stakes → Vision → Features → Proof | B2B sales |
| Duarte Resonate | What is ↔ What could be | Keynotes, vision |
| SUCCESs | Simple, Unexpected, Concrete, Credible, Emotional, Stories | Quality checklist |

### Phase 3: Build Brief + Subagent Build

A **Build Brief** translates all discovery answers into concrete writing instructions:
- **Voice** auto-derived from audience + tone (7 distinct profiles)
- **Audience profile** with headline style, evidence preferences, CTA approach
- **Emotional arc** calibrated to audience tolerance
- **Opening/closing strategies** from the rhetorical strategy library
- **Killer line** targets for memorability

The build runs as a **subagent** via the Task tool, taking one of two paths:

- **Prose path** — generate sections, then apply the embedded `prose-craft` discipline (Floor / Filter / Ceiling) to every paragraph as the sentence-level pass.
- **Presentation path** — build on the **keynote-create model** (embedded): every slide title is a short complete sentence delivering one story beat, so the titles read top-to-bottom tell the whole story. The title sequence passes the **titles-only test** before bodies are filled; `prose-craft` runs on the titles. The render → `/impeccable` → PDF export runs in the orchestrator after the gates pass.

Every unit carries source tags (`[DIRECT]` / `[PARAPHRASE]` / `[ELABORATED]` / `[GENERATED]`).

### The three gates

The output is driven through three structural gates before review:

| Gate | Phase | Catches |
|------|-------|---------|
| **1 · Framework fit** | 3 | A wrong framework whose climax can't structurally land your point (skeleton stamp test) |
| **2 · Focal fidelity** | 4.6 | Drift between intent and execution — a cold-read judge names the One Thing before reading the brief (for decks, the titles-only test) |
| **3 · Humanizing pass** | 4.7 | AI-slop the first two miss — a discourse-level de-slop grounded in the narrative-structure research corpus |

The humanizing pass is two-tier because the evidence demands it: a classifier still detects AI from *structure* at 93.9% after surface lexical cleanup, so sentence-polishing alone cannot de-slop a draft. Tier 1 is `prose-craft` (sentence); Tier 2 is a structural-delta checklist — theme-statement restraint, open threads, temporal complexity, discourse-redundancy, idiosyncrasy. **The deltas are gates and drift detectors, never optimization targets.**

### Phase 5: Targeted Review + Stress Test

Two specialist subagents review in parallel — the **Audience Advocate** always, plus one selected by content type (Comms Specialist, Content Expert, or Originality Agent). A **Director** synthesizes findings in the main conversation. For high-stakes content (pitches, policy, strategy), an optional **3-persona stress test** (e.g. CFO, COO, Skeptic) runs before delivery. Judges are run with bias hygiene (verbosity / position / self-preference), and their confidence scores are advisory, not gates.

---

## Output Example

```markdown
# Regional Governance: The Invisible Infrastructure

**Framework:** Time Machine
**Slides:** 14
**Metaphor family:** Nervous system / pulse / sensing

---

## Slide 1 — Opening Hook
**Headline:** It is March 2028, and the Mayor knows the water crisis will hit before anyone else does.

**Spotlight:** Three weeks before demand spikes, the morning brief flags the pattern.
Desalination capacity, population movement, industrial permits—the signals converged overnight.

**Design note:** Split screen—calm office on left, converging trend lines on right,
date stamp "March 2028" prominent.

**Source:** [GENERATED]

---

## Sourcing Summary

**Originality Score:** 43% user-sourced / 57% generated

- Direct from source: 3 slides
- Paraphrased: 2 slides
- Elaborated: 3 slides
- Generated: 6 slides
```

---

## Benefits

| Without Narrative Engine | With Narrative Engine |
|--------------------------|----------------------|
| Generic bullet points | Single-point headlines with power verbs |
| Unclear structure | Framework matched to audience + purpose via full sweep |
| Same voice every time | 7 auto-derived voice profiles matched to audience + tone |
| No emotional design | Emotional arcs calibrated to audience tolerance |
| Self-review blind spots | Three gates + a content-selected review panel |
| Generic AI prose | Embedded `prose-craft` (sentence) + a discourse-level humanizing pass |
| Unknown AI additions | Source tags show exactly what was generated |
| One-size-fits-all | Build Brief ensures every choice propagates through output |

---

## Installation

Copy the `Narrative-Engine` folder to your Claude Code skills directory:

```
~/.claude/skills/Narrative-Engine/
```

Or clone this repository:

```bash
git clone https://github.com/nraford7/Narrative-Engine.git ~/.claude/skills/Narrative-Engine
```

---

## Usage

Invoke with `/Narrative-Engine` in Claude Code, then:

1. Paste your content (article, notes, outline, or existing deck)
2. Choose output format (Presentation / Prose / Both)
3. Confirm focal point from 2-3 proposed angles
4. Answer discovery questions (audience, purpose, content type, tone)
5. Select density mode (High-Impact / Narrative / Evidence / ELI5)
6. Choose from 2-3 recommended frameworks (scored via full sweep)
7. Review the Build Brief, then receive complete output + 6-agent review

---

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Main skill definition and workflow |
| `narrative-arcs.md` | Beat-by-beat structures for all 10 arcs |
| `communication-frameworks.md` | Detailed framework descriptions |
| `framework-selection.md` | Full sweep protocol and selection matrices |
| `audience-profiles.md` | Deep audience profiles with writing instructions |
| `voice-profiles.md` | 7 voice profiles with auto-derive mapping |
| `emotional-arcs.md` | Framework emotional textures + audience calibration |
| `opening-closing-strategies.md` | Opening/closing strategy libraries + pairing matrix |
| `checklists.md` | All quality checklists (headlines, CTAs, originality, killer line) |
| `humanizing-pass.md` | The de-slop layer — Tier 1 (prose-craft) + Tier 2 (discourse structural-delta checklist), judge hygiene, the gate-not-objective rule. Grounded in the narrative-structure research corpus. |
| `prose-craft.md` + `prose-craft-constructions.md` | Embedded sentence-level discipline (Floor/Filter/Ceiling + construction catalog). Applied directly by the builder — not a separate skill call. |
| `deck-title-craft.md` | Embedded keynote-create title guide — action titles, titles-only test, antecedent test, rewrite examples. Used by the presentation build path. |
| `agent-reference-persuasion.md` | Comms agent frameworks (Cialdini, SUCCESs, Ogilvy) |
| `agent-reference-visual.md` | Visual agent frameworks (Tufte, Duarte, metaphors) |
| `agent-reference-verification.md` | Content agent frameworks (IFCN, SIFT, fallacies) |
| `prompts/` | Subagent prompt templates (builder, focal-fidelity-judge, reviewer, stress-tester) |
| `examples/` | Full workflow examples (climate keynote, post-mortem, remote work) |

### Architecture

Phases 1–3.5 (discovery) run interactively in the main conversation. Phases 4+ dispatch subagents:
- **Build** (Phase 4): single subagent reads the Build Brief from `/tmp/`, generates output, runs the embedded `prose-craft` pass (Tier 1), self-reviews for originality
- **Gate 2 — Focal Fidelity** (Phase 4.6): a cold-read judge loops the builder up to 3 passes until the output lands the One Thing
- **Gate 3 — Humanizing Pass** (Phase 4.7): discourse-level structural-delta check (Tier 2)
- **Review** (Phase 5): 2 parallel subagents (Audience Advocate + content-selected specialist) + Director synthesis
- **Stress Test** (Phase 5.5, high-stakes only): 3 parallel subagents with auto-selected personas

**Embedded, not invoked.** `prose-craft` and the keynote-create title guide are copied into the skill so the build subagent never calls another skill at dispatch time. Only the deck render stage (`keynote-render.mjs` → `/impeccable`) calls keynote-create, and that runs in the orchestrator. Each embed carries a source-path + date header for clean re-syncing.

---

## Framework Selection Quick Reference

| If your audience is... | And your goal is... | Consider... |
|------------------------|---------------------|-------------|
| Executive / Board | Any | Pyramid or Columbo (answer-first) |
| Skeptics | Persuade | Trojan Horse + PAS |
| Investors | Inspire | Hero's Journey + Cinderella |
| Mixed / Cross-functional | Align | Rashomon or Heist |
| General / Keynote | Entertain | Prestige or Time Machine |

| If your content has... | Consider... |
|------------------------|-------------|
| A genuine surprise | Prestige or Mystery Box |
| Multiple stakeholder views | Rashomon |
| A transformation story | Hero's Journey |
| Future vision | Time Machine |
| Root cause analysis | Columbo |

---

## License

MIT

---

## Credits

Built on frameworks from:
- Barbara Minto (Pyramid Principle)
- Nancy Duarte (Resonate, Slide:ology)
- Chip & Dan Heath (Made to Stick)
- Robert Cialdini (Influence)
- Andy Raskin (Greatest Sales Deck)
- Edward Tufte (Data Visualization)
- Joseph Campbell (Hero's Journey)
- Christopher Nolan / J.J. Abrams (Narrative structures)
- William Strunk Jr. (economy) — via the embedded `prose-craft` discipline
- The humanizing pass is grounded in a fact-checked narrative-structure research corpus (Labov, McAdams, Reagan et al., StoryScope, Reinhart et al., QUDsim) — gates and drift detectors, never optimization targets
