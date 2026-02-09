# Narrative Engine

**A Claude Code skill that transforms any content into compelling narratives — as presentations or prose — using proven storytelling frameworks.**

Most presentations fail before they begin. Not because the content is wrong, but because the structure is. Narrative Engine matches your material to the right storytelling framework, auto-derives a distinct voice and emotional arc for your specific audience, then builds the output with a 6-agent review panel that catches what you'd miss.

---

## What It Does

Paste an article, outline, research notes, or existing deck. Choose presentation or prose. Answer discovery questions. Get back:

1. **Full-sweep framework scoring** across all 10 arcs + 7 communication frameworks, with a Dark Horse option
2. **A Build Brief** translating your audience, voice, emotional arc, and strategies into concrete writing instructions
3. **A complete output** (slides or prose) with auto-derived voice, emotional pacing, and opening/closing strategies
4. **A 6-agent review** including an Originality Agent that catches generic AI patterns
5. **Sourcing transparency** showing what came from your content vs. what was generated

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

The build then generates presentation slides or prose sections, each with source tags (`[DIRECT]` / `[PARAPHRASE]` / `[ELABORATED]` / `[GENERATED]`).

The build runs as a **subagent** via the Task tool — offloading the heaviest generation work from the main conversation and reducing context pressure.

### Phase 4: Review Panel (6 Parallel Subagents)

Six specialist agents review your output in parallel:

```
                    ┌─────────────────────────────────────┐
                    │            DIRECTOR                 │
                    │  Synthesizes, resolves conflicts,   │
                    │  presents unified recommendations   │
                    └─────────────────────────────────────┘
                                     ▲
        ┌────────┬─────────┬─────────┼─────────┬─────────┬────────┐
        ▼        ▼         ▼         ▼         ▼         ▼
   AUDIENCE  COMMS/PR   VISUAL    CRITIC   CONTENT  ORIGINALITY
   ADVOCATE  SPECIALIST DESIGNER           EXPERT   AGENT
```

| Agent | Key Question |
|-------|--------------|
| **Audience Advocate** | "As [audience], does this land?" |
| **Comms Specialist** | "Is this tight and bulletproof?" |
| **Visual Designer** | "What visual makes this unforgettable?" |
| **Critic** | "What's the weakest link?" |
| **Content Expert** | "Can every claim be defended?" |
| **Originality Agent** | "Would this feel different from a generic AI output?" |

The **Director** synthesizes feedback, resolves conflicts, and surfaces decisions you need to make.

All six agents run as **parallel subagents** via the Task tool, returning findings simultaneously for the Director to synthesize in the main conversation.

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
| Self-review blind spots | 6-agent review including Originality Agent |
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
| `agent-reference-persuasion.md` | Comms agent frameworks (Cialdini, SUCCESs, Ogilvy) |
| `agent-reference-visual.md` | Visual agent frameworks (Tufte, Duarte, metaphors) |
| `agent-reference-verification.md` | Content agent frameworks (IFCN, SIFT, fallacies) |
| `prompts/` | Subagent prompt templates (builder, reviewer, stress-tester) |
| `examples/` | Full workflow examples (climate keynote, post-mortem, remote work) |

### Architecture

Phases 1–3.5 (discovery) run interactively in the main conversation. Phases 4+ dispatch subagents:
- **Build** (Phase 4): Single subagent reads the Build Brief from `/tmp/`, generates output, self-reviews for originality
- **Review** (Phase 5): 6 parallel subagents, each with a specialist lens and reference file
- **Stress Test** (Phase 5.5): 3 parallel subagents with auto-selected personas

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
