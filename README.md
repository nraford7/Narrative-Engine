# Narrative Engine

**A Claude Code skill that transforms any content into narrative-driven slide decks using proven storytelling frameworks.**

Most presentations fail before they begin. Not because the content is wrong, but because the structure is. Narrative Engine matches your material to the right storytelling framework—then builds a complete slide outline with headlines, visuals, and a multi-agent review panel that catches what you'd miss.

---

## What It Does

Paste an article, outline, research notes, or existing deck. Answer 5 quick questions. Get back:

1. **2-3 framework recommendations** tailored to your audience, purpose, and material
2. **A complete slide outline** with single-point headlines, supporting spotlights, and visual design notes
3. **A 5-agent review** that stress-tests your deck from multiple perspectives
4. **Sourcing transparency** showing what came from your content vs. what was generated

---

## How It Works

### Phase 1: Discovery (5 Questions)

```
Who is your audience?        → Executive / Technical / Investors / Skeptics / Mixed...
What are you trying to do?   → Persuade / Inform / Inspire / Align / Report...
What type of content?        → Research / Strategy / Case study / Pitch / Vision...
What tone?                   → Authoritative / Provocative / Warm / Urgent / Balanced...
Is there a surprise/reveal?  → Yes / No / Help me find one
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

### Phase 3: Deck Generation

Each slide includes:
- **Headline:** Single sentence, ≤14 words, active voice, power verbs
- **Spotlight:** ≤60 words supporting the headline (with source citation)
- **Design note:** Specific visual recommendation
- **Source tag:** `[DIRECT]` / `[PARAPHRASE]` / `[ELABORATED]` / `[GENERATED]`

### Phase 4: Multi-Agent Review Panel

Five specialist agents review your deck in parallel:

```
                    ┌─────────────────────────────────────┐
                    │            DIRECTOR                 │
                    │  Synthesizes, resolves conflicts,   │
                    │  presents unified recommendations   │
                    └─────────────────────────────────────┘
                                     ▲
        ┌────────────┬───────────────┼───────────────┬────────────┐
        ▼            ▼               ▼               ▼            ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  AUDIENCE    │ │  COMMS/PR    │ │   VISUAL     │ │   CRITIC     │ │   CONTENT    │
│  ADVOCATE    │ │  SPECIALIST  │ │   DESIGNER   │ │              │ │   EXPERT     │
└──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘
```

| Agent | Lens | Key Question |
|-------|------|--------------|
| **Audience Advocate** | Mental models, priorities, what makes them tune out | "As [audience], does this land?" |
| **Comms Specialist** | Message discipline, emotional arc, PR risk, persuasion | "Is this tight and bulletproof?" |
| **Visual Designer** | Metaphor coherence, Tufte principles, S.T.A.R. moments | "What visual makes this unforgettable?" |
| **Critic** | Pacing, redundancy, weak links, counterarguments | "What's the weakest link?" |
| **Content Expert** | Factual accuracy, logical fallacies, source integrity | "Can every claim be defended?" |

The **Director** synthesizes feedback, resolves conflicts, and surfaces decisions you need to make.

---

## Output Example

```markdown
# Regional Governance: The Invisible Infrastructure

**Framework:** Time Machine
**Slides:** 14
**Metaphor family:** Nervous system / pulse / sensing

---

## Slide 1 — Opening Hook
**Headline:** It is March 2028, and the Prince knows the water crisis will hit before anyone else does.

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
| Unclear structure | Framework matched to audience + purpose |
| No visual guidance | Specific design notes per slide |
| Self-review blind spots | 5-agent review catches what you miss |
| Unknown AI additions | Source tags show exactly what was generated |
| One-size-fits-all | 17 frameworks × 3 lengths = tailored output |

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
2. Answer the 5 discovery questions
3. Choose from 2-3 recommended frameworks
4. Select presentation length (10-12 min / 30 min / 60 min)
5. Receive complete slide outline + review panel synthesis

---

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Main skill definition and workflow |
| `narrative-arcs.md` | Beat-by-beat structures for all 10 arcs |
| `communication-frameworks.md` | Detailed framework descriptions |
| `framework-selection.md` | Selection matrix by audience/purpose/content |
| `framework_selection_guide.md` | Complete integration guide |
| `agent-reference-persuasion.md` | Comms agent frameworks (Cialdini, SUCCESs, Ogilvy) |
| `agent-reference-visual.md` | Visual agent frameworks (Tufte, Duarte, metaphors) |
| `agent-reference-verification.md` | Content agent frameworks (IFCN, SIFT, fallacies) |

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
