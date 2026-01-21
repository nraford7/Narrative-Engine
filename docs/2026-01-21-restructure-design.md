# Narrative Engine Restructure Design

**Date:** 2026-01-21
**Status:** Approved for implementation

---

## Problem Statement

The Narrative Engine skill has grown organically with:
- ~200 lines of duplicated content across files
- Fixed slide counts conflicting with content-driven philosophy
- 7+ scattered checklists that could be consolidated
- Unclear boundaries between SKILL.md and reference files
- Missing compression and clarity mechanisms

## Design Goals

1. **Content-driven length** — No fixed slide counts. Decks are as long as they need to be.
2. **Integrated compression** — Every slide must justify its existence at birth.
3. **Three-level clarity** — Focal → Section → Slide validation cascade.
4. **Optional stress testing** — Simulate different audience mindsets.
5. **No duplication** — Single source of truth for all content.
6. **Clear file boundaries** — SKILL.md = workflow. References = deep content.

---

## New Workflow

```
PHASE 1:    Content Import
                ↓
PHASE 1.5:  Focal Discovery (NEW)
            Focal Agent reads content, proposes 2-3 focal point options.
            User selects or refines. This becomes the north star.
            Skip if user already stated their point explicitly.
                ↓
PHASE 2:    Discovery Questions (streamlined)
            - Audience
            - Purpose
            - Content type
            - Tone
            (Remove "Reveal Potential" — Focal Agent infers this)
                ↓
PHASE 2.5:  Density Mode Selection (NEW)
            "How concentrated should this deck be?"
            1. High-Impact — maximum compression, one idea per slide
            2. Narrative — room for story beats and emotional builds
            3. Evidence — denser proof for skeptics
                ↓
PHASE 3:    Framework Recommendation
            2-3 frameworks mapped to content + focal point
                ↓
PHASE 4:    Build (with integrated compression)
            - Section Clarity Agent validates each section against focal point
            - Slide Compression Agent validates each slide as it's born
            - Density mode governs how tight
                ↓
PHASE 5:    Review Panel (existing 5 agents)
                ↓
PHASE 5.5:  Stress Test Panel (NEW, optional)
            "Want me to run the Stress Test Panel?"
            Auto-selects 3 personas based on content type.
            Director triages output: Must Fix / Should Fix / Could Fix
                ↓
ON-DEMAND:  "Tighter"
            User can request compression passes anytime.
            Three-level system runs again: Focal → Sections → Slides
```

---

## Three-Level Clarity System

### Level 1: Focal Agent (Deck Level)

Establishes the single point before anything else is built.

**Outputs:**
- **The One Thing:** Single idea the deck must land
- **The Ask:** Action or shift being driven toward
- **The Through-Line:** Logical/emotional thread connecting everything

**Focal Statement:** 1-2 sentences that become the north star.

### Level 2: Section Clarity Agent

Reviews each major section against the Focal Statement.

**Questions:**
- Does this section advance the point, or is it a detour?
- Does the section earn its place in the narrative arc?
- Is the section's role clear? (Setup? Evidence? Turn? Resolution?)
- Could two sections merge without losing anything?

### Level 3: Slide Compression Agent

Four lenses applied to every slide:

| Lens | Question |
|------|----------|
| **Structure** | If I removed this slide, would the deck still work? |
| **Language** | Can this be said in fewer words without losing meaning? |
| **Clarity** | Can someone grasp this in 3 seconds? |
| **So What** | Why should the audience care about this specific slide? |

**Protected Species (do not cut):**
- Vivid metaphors that create memorability
- Emotional beats that build connection
- The surprising turn / reveal moment
- Specific details that make abstract concrete
- Creative language that creates atmosphere
- Callbacks and plants that pay off later

---

## Density Modes (Replaces Short/Medium/Long)

| Mode | Philosophy | Slide Characteristics |
|------|------------|----------------------|
| **High-Impact** | Maximum compression. Every slide is a punch. | One idea per slide. Headlines do heavy lifting. Spotlights surgical. For: pitches, time-constrained execs. |
| **Narrative** | Room to breathe. Story beats get space. | Emotional builds allowed. Metaphors unfold. For: thought leadership, teaching. |
| **Evidence** | Denser supporting material. | Multiple proof points per section. Data gets real estate. For: skeptics, technical audiences, due diligence. |

**Key change:** No minimum slide counts. Content determines length.

---

## Stress Test Panel

### 7 Personas (Auto-select 3 based on content type)

| Persona | Lens | What They Catch |
|---------|------|-----------------|
| **The Engineer** | "How does this actually work?" | Hand-wavy claims, missing mechanisms, logical gaps |
| **The Skeptic** | "Why should I believe this?" | Unsubstantiated claims, weak proof, confirmation bias |
| **The Risk Officer** | "What could go wrong?" | Downside blindness, missing caveats, overconfidence |
| **The CFO** | "What are the numbers?" | Fuzzy math, missing ROI, unclear investment ask |
| **The Lawyer** | "What's the exposure?" | Overpromises, liability language, compliance issues |
| **The Conservative** | "Why change what's working?" | Unaddressed status-quo concerns, too aggressive |
| **The COO** | "Would this actually work?" | Operational blindspots, unrealistic execution, market fit |

### Auto-Selection Matrix

| Content Type | Auto-Selected Panel |
|--------------|---------------------|
| Investor pitch / fundraising | CFO, COO, Skeptic |
| Sales pitch | Skeptic, COO, Engineer |
| Strategic plan / transformation | COO, Conservative, Risk Officer |
| Technical proposal | Engineer, Skeptic, COO |
| Policy recommendation | Lawyer, Risk Officer, Conservative |
| Product launch | COO, Skeptic, Engineer |
| Post-mortem / retrospective | Engineer, Risk Officer, COO |
| Keynote / thought leadership | Skeptic, Conservative |

### Director Triage

After all personas review, Director categorizes:

- 🔴 **Must Fix** — Will undermine the deck if ignored
- 🟡 **Should Fix** — Strengthens meaningfully
- 🟢 **Could Fix** — Nice-to-have, low priority

---

## File Structure (Post-Restructure)

```
Narrative-Engine/
├── SKILL.md                      # Workflow only (~400 lines target)
├── agent-reference-persuasion.md # Comms agent deep reference
├── agent-reference-visual.md     # Visual agent deep reference
├── agent-reference-verification.md # Content expert deep reference
├── communication-frameworks.md   # All framework details (single source)
├── framework-selection.md        # Selection matrices
├── narrative-arcs.md             # Arc details
├── checklists.md (NEW)           # All checklists consolidated
├── examples/ (NEW)
│   └── remote-work-example.md    # Example workflow moved here
└── docs/
    └── 2026-01-21-restructure-design.md (this file)
```

### File Boundaries

| File | Contains | Does NOT Contain |
|------|----------|------------------|
| **SKILL.md** | Phases, workflow, agent definitions, output format | Framework details, examples, deep checklists |
| **checklists.md** | All quality checklists in one place | Workflow instructions |
| **communication-frameworks.md** | Framework deep dives | Workflow references |
| **agent-reference-*.md** | Agent-specific deep content | Workflow phases |

---

## Duplication Removal Plan

| Duplicated Content | Keep In | Remove From |
|--------------------|---------|-------------|
| Verbalization/Headline Multipliers | agent-reference-persuasion.md | SKILL.md |
| Intensification Checklist | checklists.md (new) | SKILL.md, agent-reference-persuasion.md |
| Cialdini's 7 Principles | communication-frameworks.md | SKILL.md, agent-reference-persuasion.md |
| AIDA Framework | communication-frameworks.md | SKILL.md, agent-reference-persuasion.md |
| SUCCESs Framework | communication-frameworks.md | SKILL.md, agent-reference-persuasion.md |
| Headline Banlist (expanded) | checklists.md | SKILL.md (keep brief reference only) |
| All scattered checklists | checklists.md | Everywhere else |

---

## Implementation Order

1. **Create checklists.md** — Consolidate all checklists
2. **Create examples/remote-work-example.md** — Move example workflow
3. **Rewrite SKILL.md** — New phases, remove duplications, link to references
4. **Update agent-reference-persuasion.md** — Remove duplications, keep unique content
5. **Verify cross-references** — All links work, no orphaned content

---

## Success Criteria

- [ ] SKILL.md under 500 lines
- [ ] Zero content duplication across files
- [ ] New workflow phases implemented
- [ ] Stress Test Panel documented
- [ ] All checklists in one file
- [ ] Example workflow in separate file
