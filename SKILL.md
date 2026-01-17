---
name: Narrative-Engine
description: "Transform any content (articles, reports, outlines, research, or existing presentations) into narrative-driven slide decks using proven storytelling and communication frameworks. Use when: (1) Converting prose/articles into presentations, (2) Restructuring existing presentations for better narrative flow, (3) Choosing between narrative frameworks for different audiences, (4) Creating decks optimized for specific goals (persuade, inform, inspire, align). Walks users through structured questioning to recommend frameworks, shows content mapped to 2-3 options, then builds the full deck in their chosen structure."
---

# Narrative Engine

Transform content into compelling narrative presentations by matching the right storytelling framework to audience, purpose, and material.

## Overview

This skill guides users through a structured discovery process to select the optimal narrative framework, then transforms their content into a slide outline. The process:

1. **Import** — Accept user's content (article, outline, notes, existing deck)
2. **Discover** — Ask 5 structured questions (numbered options) about audience, purpose, tone, content type, and reveal potential
3. **Recommend** — Propose 2-3 numbered frameworks (with Audience + Comms agent input for high-stakes content)
4. **Length** — Ask about presentation duration (10-12 min / 30 min / 60 min)
5. **Build** — Generate full slide outline with source tags showing what came from user vs. generated
6. **Review** — Full Review Panel (5 specialist agents) evaluates deck; Director synthesizes recommendations

---

## Review Panel Architecture

Five specialist agents review the deck in parallel, each bringing a distinct lens. A Director agent synthesizes their input into unified recommendations.

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

### Agent Definitions

#### 1. Audience Advocate
**Role:** Assumes the persona of the described audience

**Lens:**
- Mental models, priorities, and concerns of this specific audience
- What they already believe, what they resist
- Time constraints, attention patterns
- What makes them say yes vs. tune out
- Political/organizational context they operate in

**Key question:** "As [audience], does this land? What would make me skeptical, bored, or confused?"

**Output:** Flags slides/sections that won't resonate; suggests reframes that match audience worldview

---

#### 2. Comms/PR Specialist
**Role:** Reviews for messaging, emotion, clarity, and persuasion

**Reference:** See [`agent-reference-persuasion.md`](agent-reference-persuasion.md) for frameworks

**Lens:**
- Message discipline — is there one clear takeaway?
- Emotional arc — does it move the audience?
- Clarity — can this be misunderstood or quoted out of context?
- Persuasion techniques — Cialdini's 7 principles (reciprocity, commitment, social proof, authority, liking, scarcity, unity)
- PR risk — anything that could backfire if leaked or shared?
- Stickiness — does it pass the SUCCESs test? (Simple, Unexpected, Concrete, Credible, Emotional, Stories)

**Draws from:**
- Made to Stick (Heath brothers) — SUCCESs framework
- Hey Whipple, Squeeze This (Luke Sullivan) — advertising copywriting
- David Ogilvy — headline and body copy principles
- Cialdini — persuasion science
- PR, advertising, propaganda, political communication

**Key question:** "Is this message tight, emotionally resonant, and bulletproof?"

**Output:** Sharpens headlines, identifies emotional dead spots, flags PR risks, suggests persuasion amplifiers, applies SUCCESs checklist

---

#### 3. Visual Designer
**Role:** Specializes in visual metaphors and supporting graphics

**Reference:** See [`agent-reference-visual.md`](agent-reference-visual.md) for frameworks

**Lens:**
- Visual storytelling — does the imagery reinforce the narrative?
- Metaphor coherence — is the visual language consistent? (one metaphor family per deck)
- Data visualization — Tufte principles (data-ink ratio, no chartjunk, graphical integrity)
- Slide composition — Duarte's 3-second rule, balance, hierarchy, whitespace
- Memorability — S.T.A.R. moments (Something They'll Always Remember)
- Iconography & symbolism — appropriate cultural and art historical references

**Draws from:**
- Edward Tufte — data visualization principles
- Nancy Duarte — Slide:ology and Resonate
- Visual metaphor frameworks (replacement, fusion, juxtaposition)
- Art history iconography (vanitas, surrealism, etc.)
- Universal symbolism and cultural considerations

**Key question:** "What image or visual would make this slide unforgettable?"

**Output:** Upgrades design notes with specific visual metaphors, references art/culture where appropriate, ensures metaphor family consistency, identifies S.T.A.R. moment opportunities

---

#### 4. Critic
**Role:** Offers critical assessment of overall quality and efficacy

**Lens:**
- Pacing — too fast, too slow, uneven?
- Redundancy — are we repeating ourselves?
- Weak links — which slides don't earn their place?
- Logical flow — does the argument hold together?
- Efficacy — will this actually achieve the stated purpose?
- Opposition research — what counterarguments exist?

**Key question:** "If I had to cut 20% of this deck, what goes? What's the weakest link?"

**Perplexity Search Requirement:**
After reviewing the deck, conduct a Perplexity search to identify:
- Opposing viewpoints or counterarguments to the deck's thesis
- Known weaknesses or criticisms of the approach
- Potential objections the audience might raise
- Edge cases or failure modes

**Search prompts to use:**
- "Arguments against [thesis]"
- "Criticism of [approach/framework]"
- "[Topic] counterarguments objections"
- "Why [claim] might be wrong"

**Output format:**
```
### Opposition Research

**Potential counterarguments the audience may raise:**
1. [Counterargument] — Source: [URL]
   - Suggested preemption: [How to address in deck]

**Weaknesses to acknowledge or address:**
- [Weakness identified]
```

**Output:** Identifies cuts, flags pacing issues, ranks slides by strength, assesses likelihood of achieving goal, surfaces opposing viewpoints user should address or preempt

---

#### 5. Content Expert
**Role:** Fact-checks and ensures accuracy

**Reference:** See [`agent-reference-verification.md`](agent-reference-verification.md) for frameworks

**Lens:**
- Factual accuracy — are claims verifiable?
- Source integrity — is the sourcing clear and honest?
- Fabrication check — is anything invented or embellished?
- Logical validity — do conclusions follow from evidence? (see logical fallacies list)
- Completeness — are important caveats missing?
- Supporting research — what additional evidence exists?

**Draws from:**
- IFCN fact-checking methodology
- Logical fallacy detection
- SIFT method for source evaluation
- Confidence rating frameworks

**Key question:** "Can every claim in this deck be defended if challenged?"

**Perplexity Search Requirement:**
After reviewing the deck, conduct a Perplexity search to:
- Find supporting evidence that strengthens the user's claims
- Identify context the audience may need
- Discover related research or data that enriches the narrative
- Verify statistics, quotes, and attributions

**Search prompts to use:**
- "[Topic] statistics 2024 2025 data"
- "[Claim] evidence research study"
- "Is it true that [specific claim]"
- "[Industry/field] trends analysis"

**Output format:**
```
### Supporting Research Found

**Additional evidence for user's claims:**
1. [Claim from deck]: [Supporting evidence found]
   - Source: [URL]
   - Confidence: High/Medium/Low

**Useful context to add:**
- [Finding that could enrich the deck]

**Verification results:**
- [Statistic]: Verified / Needs correction / Unable to verify
```

**Output:** Flags unsupported claims, identifies where citations are needed, catches logical leaps, notes missing caveats, provides supporting research from Perplexity search

---

### When Agents Activate

| Phase | Agents Active | Purpose |
|-------|---------------|---------|
| Phase 3 (Framework Recommendation) | Audience Advocate, Comms Specialist | Validate framework choice for high-stakes content* |
| Phase 5 (Review) | All 5 agents in parallel | Full review of completed deck |

*High-stakes content types that trigger Phase 3 agent review:
- Investor pitch / fundraising
- Sales pitch
- Multi-stakeholder / controversial topic
- Policy recommendation
- Strategic plan / transformation roadmap
- Paradigm shift / new mental model

---

### Director Synthesis Rules

The Director integrates all agent feedback into a unified recommendation.

**Conflict Resolution:**

| Conflict Type | Resolution |
|---------------|------------|
| **Minor disagreement** | Director uses best judgment based on audience, content, and intent. Implements stronger recommendation silently. |
| **Strong disagreement** | Flag to user as "Points requiring your decision" with both perspectives presented. Let user resolve. |

**What constitutes "strong disagreement":**
- Two agents directly contradict (e.g., Critic says "cut slide 12" / Audience Advocate says "slide 12 is essential")
- An agent flags something as high-risk or critical
- Content Expert identifies factual concern that conflicts with narrative flow

**Director Output Format:**

```markdown
## Review Panel Synthesis

### Strengths (what's working)
- [Observation] — *[Agent attribution]*
- [Observation] — *[Agent attribution]*

### Recommended Changes
1. **[Change]** — *[Agent attribution]*
   [Specific recommendation]

2. **[Change]** — *[Agent attribution]*
   [Specific recommendation]

### Points Requiring Your Decision
> **Conflict:** [Agent A] recommends [X], but [Agent B] recommends [Y]
>
> **Agent A's view:** [Rationale]
> **Agent B's view:** [Rationale]
>
> **Your call:** [Options for user to choose]

### Overall Assessment
[2-3 sentence summary: Is it ready? What's most important? Confidence level?]
```

## PHASE 1: Content Import

Accept content in any form:
- Pasted prose, articles, or reports
- Outlines or bullet points
- Research notes or data
- Existing presentation text
- URLs (fetch and extract)

If user pastes content without instructions, acknowledge receipt and proceed directly to discovery questions.

## PHASE 2: Structured Discovery

Ask these 5 questions sequentially. Provide context for each but don't overwhelm — ask 1-2 at a time.

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

User can respond with a number or in their own words.

### Question 2: Purpose

> **What are you trying to accomplish?**
> 1. Persuade to act (get approval, close a deal, drive decision)
> 2. Inform / Educate (transfer knowledge, explain)
> 3. Inspire / Motivate (energize, create vision)
> 4. Align / Build consensus (get buy-in across stakeholders)
> 5. Report / Update (share status, results)
> 6. Defend / Justify (support a position, handle objections)
> 7. Entertain / Engage (keynote, thought leadership)

User can respond with a number or in their own words.

### Question 3: Content Type

> **What type of content is this?**
> 1. Counterintuitive research findings
> 2. Strategic plan / transformation roadmap
> 3. Scenario planning / decision fork
> 4. Paradigm shift / new mental model
> 5. Company/product origin story
> 6. Post-mortem / retrospective
> 7. Pattern recognition / hidden dynamics
> 8. Multi-stakeholder / controversial topic
> 9. Sales pitch
> 10. Investor pitch / fundraising
> 11. Product launch
> 12. Case study
> 13. Data/analytics report
> 14. Policy recommendation
> 15. Vision/inspiration piece

User can respond with a number or in their own words.

### Question 4: Tone

> **What tone or attitude do you want?**
> 1. Authoritative / Expert
> 2. Provocative / Challenging
> 3. Warm / Relatable
> 4. Urgent / Action-oriented
> 5. Balanced / Objective
> 6. Visionary / Aspirational
> 7. Playful / Creative

User can respond with a number or in their own words.

### Question 5: Reveal Potential

> **Does your material contain a genuine surprise, counterintuitive finding, or reframe?**
> 1. Yes — there's a twist, unexpected conclusion, or "aha moment"
> 2. No — it's more straightforward information delivery
> 3. Uncertain — help me identify if there's a hidden reveal

User can respond with a number or in their own words.

This question determines whether to recommend **engagement-optimized arcs** (mystery, delayed revelation) or **efficiency-optimized frameworks** (answer-first, linear).

## PHASE 3: Framework Recommendation

Based on discovery answers, recommend 2-3 frameworks. For each recommendation:

1. **Name the framework** and category (Narrative Arc vs. Communication Framework)
2. **Explain fit** in 2-3 sentences specific to their situation
3. **Show the skeleton** — their content mapped to the framework's beats (bullet form)
4. **Flag tradeoffs** — what this framework does well vs. potential drawbacks

### Early Agent Review (High-Stakes Content)

For high-stakes content types, run **Audience Advocate** and **Comms Specialist** during framework recommendation:

**Trigger content types:**
- Investor pitch / fundraising
- Sales pitch
- Multi-stakeholder / controversial topic
- Policy recommendation
- Strategic plan / transformation roadmap
- Paradigm shift / new mental model

**Process:**
1. Generate framework recommendations as normal
2. Run Audience Advocate: "Given [audience profile], which framework will land best? Any frameworks to avoid?"
3. Run Comms Specialist: "Which framework gives the tightest message discipline? Any PR risks with these approaches?"
4. Integrate their input into recommendation rationale

**Output addition for high-stakes content:**

```markdown
### Agent Input on Framework Choice

**Audience Advocate:** [1-2 sentences on which framework fits audience psychology]

**Comms Specialist:** [1-2 sentences on message clarity and persuasion potential]
```

### Framework Selection Logic

See [`references/framework-selection.md`](references/framework-selection.md) for complete selection matrix.

**Quick selection heuristics:**

| If... | Consider... |
|-------|-------------|
| Executive audience + any purpose | Columbo or Pyramid — answer-first |
| Skeptical audience | Trojan Horse — meet them where they are |
| Material has genuine surprise | The Prestige or Mystery Box — build to reveal |
| Strategy/transformation | The Heist — goal-obstacles-crew-execution |
| Vision/future focus | Time Machine — future-back framing |
| Origin story | Hero's Journey — transformation arc |
| Multi-stakeholder | Rashomon — multiple views to synthesis |
| Post-mortem/root cause | Columbo — outcome-first reconstruction |
| Pattern/insight | Game of the Scene — name and heighten the game |
| Sales to executives | The Heist + Pyramid hybrid |
| Investor pitch | Hero's Journey + Cinderella shape |
| Keynote/thought leadership | The Prestige or Trojan Horse + S.T.A.R. moment |

### Output Format for Recommendations

Present recommendations as numbered options so users can respond with a number or text:

```markdown
## Recommendation 1: [Framework Name]

**Category:** Narrative Arc / Communication Framework
**Fit score:** ★★★★☆

**Why this works for you:**
[2-3 sentences specific to their answers]

**Your content in this structure:**
1. [Beat name]: [Their content mapped to this beat]
2. [Beat name]: [Their content mapped to this beat]
...

**Tradeoffs:**
- ✓ [Strength]
- ✓ [Strength]
- ⚠ [Limitation or risk]
```

Provide 2-3 numbered recommendations, then ask: **"Which framework would you like me to develop into a full slide outline? Type the number or name, or describe a hybrid combining elements from multiple options."**

## PHASE 3.5: Deck Length Selection

After user selects a framework, ask about presentation length:

> **How long is your presentation?**
> 1. Short (10-12 minutes) — ~12-15 slides, key points only
> 2. Medium (30 minutes) — ~25-35 slides, full narrative with supporting detail
> 3. Full (60 minutes) — ~45-55 slides, comprehensive coverage with depth

User can respond with a number or in their own words.

Adjust slide count and depth accordingly. Shorter versions compress or omit supporting slides while preserving the core narrative arc and reveal timing.

## PHASE 4: Full Deck Build

Once user selects a framework and length, generate the complete slide outline.

### Slide Format (Single-Point)

Each slide contains:
- **Headline:** Single sentence, ≤14 words, active voice, follows evocative headline rules
- **Spotlight:** ≤60 words — ONE example, statistic, case, or quote supporting the headline (with citation if from source)
- **Design note:** ONE specific visual suggestion
- **Source tag:** Indicates content origin (see Content Sourcing below)

### Content Sourcing

Every slide must indicate where the content came from. Use these tags:

| Tag | Meaning |
|-----|---------|
| `[DIRECT]` | Quoted or nearly verbatim from user's source material |
| `[PARAPHRASE]` | User's ideas restated in different words |
| `[ELABORATED]` | User's concept expanded with additional context or examples |
| `[GENERATED]` | New content created to support narrative flow or fill gaps |

At the end of the deck, include a **Sourcing Summary**:

```markdown
## Sourcing Summary

**Originality Score:** X% user-sourced / Y% generated

- Direct from source: N slides
- Paraphrased: N slides
- Elaborated: N slides
- Generated: N slides

[Optional notes on what was generated and why]
```

This transparency helps users know what came from their material versus what was added for narrative coherence.

### Headline Style Rules

Apply to every headline:
- **Image & Action:** Concrete actors/things + strong transitive verbs; avoid "is/are"
- **Tension & Turn:** Because/Therefore, Not/But, Before/After, Seen/Unseen
- **Cadence:** 8-14 words; favor two-beat rhythm
- **Specific Anchors:** Name a time/place/actor/number in at least every third headline
- **Banlist:** innovative, disruptive, best-in-class, leading, robust, scalable, world-class, cutting-edge
- **Power verbs (rotate):** tilts, unseats, ignites, drains, compounds, widens, narrows, unlocks, hardens, softens, mutes, amplifies, spills, sharpens, bends, crowds out, anchors, accelerates, stalls
- **Variety:** Don't reuse same pattern/verb in adjacent headlines
- **Metaphor:** One family only across the deck (journey OR ecology OR weather OR stagecraft, etc.)

### Deck Sizing

Slide counts are determined by user's selected presentation length (see Phase 3.5), not source length:

| Presentation Length | Slide Count | Depth |
|---------------------|-------------|-------|
| Short (10-12 min) | 12-15 slides | Core narrative only, one spotlight per beat |
| Medium (30 min) | 25-35 slides | Full narrative with supporting examples |
| Full (60 min) | 45-55 slides | Comprehensive with depth, multiple examples per section |

For shorter versions, compress by:
- Combining related beats into single slides
- Choosing strongest spotlight per section
- Preserving reveal timing (percentage position stays constant)

### Quality Gates (Apply Before Output)

Run these checks on every deck:

1. **Headline Gate:** Vivid verb, concrete nouns, one idea, causal/contrastive turn where possible
2. **Spotlight Gate:** ≤60 words, specific, directly tied to headline, includes citation
3. **Variety Gate:** No three consecutive headlines share same pattern or verb
4. **Balance Gate:** Limitations/counterevidence each get their OWN slides
5. **Arc Integrity Gate:** Reveal/click at correct position (~55-65% for twist arcs); plants and callbacks present

### Output Format

```markdown
# [Deck Title]

**Framework:** [Name]
**Slide count:** [N]
**Presentation length:** [Short/Medium/Full]
**Metaphor family:** [chosen metaphor]

---

## Slide 1 — [Section/Beat Name]
**Headline:** [Full sentence, ≤14 words]

**Spotlight (≤60 words):** [One supporting element with citation]

**Design note:** [Specific visual suggestion]

**Source:** [DIRECT/PARAPHRASE/ELABORATED/GENERATED]

---

## Slide 2 — [Section/Beat Name]
...

---

## Narrative Readout (4-6 sentences)

[A concise script that can be read aloud to present the deck's story arc]

---

## Sourcing Summary

**Originality Score:** X% user-sourced / Y% generated

- Direct from source: N slides
- Paraphrased: N slides
- Elaborated: N slides
- Generated: N slides
```

## Framework Reference

### 10 Narrative Arcs (Engagement-Optimized)

These arcs use mystery, delayed revelation, and reframing. Best for keynotes, thought leadership, and content with genuine surprises.

| Arc | Structure | Reveal Position |
|-----|-----------|-----------------|
| The Prestige | Pledge → Turn → Prestige | ~60% |
| Mystery Box | Open loops → False trails → Click | ~60% |
| The Heist | Target → Obstacles → Crew → Execution → Getaway | ~75% |
| Time Machine | Future-back → Past-forward → Fork | ~55% |
| Trojan Horse | Relatable scene → Escalation → Reframe → Demo → Button | ~50% |
| Hero's Journey | Call → Threshold → Trials → Ordeal → Return | ~65% |
| Freytag's Five-Act | Exposition → Rising → Climax → Falling → Dénouement | ~60% |
| Columbo/Whydunit | Outcome first → Methodical rebuild → Telltale → Howdunit | ~70% |
| Game of the Scene | Base reality → Unusual thing → Name the game → Heighten x3 | ~65% |
| Rashomon | Multi-view → Missing axis → Synthesis | ~70% |

See [`references/narrative-arcs.md`](references/narrative-arcs.md) for detailed beat-by-beat structures.

### Communication Frameworks (Efficiency-Optimized)

These frameworks prioritize clarity, speed, and persuasion. Best for executive communication, sales, and straightforward information delivery.

| Framework | Structure | Best For |
|-----------|-----------|----------|
| Minto Pyramid | Answer → MECE supports → Evidence | Executive updates, board decks |
| SCQA | Situation → Complication → Question → Answer | Opening hooks, problem framing |
| AIDA | Attention → Interest → Desire → Action | Sales, marketing, fundraising |
| PAS | Problem → Agitation → Solution | Change management, skeptics |
| Raskin Sales Deck | Change → Stakes → Vision → Features → Proof | B2B sales, category creation |
| Duarte Resonate | What is ↔ What could be (oscillation) | Keynotes, vision presentations |
| SUCCESs | Simple, Unexpected, Concrete, Credible, Emotional, Stories | Quality checklist for any deck |

See [`references/communication-frameworks.md`](references/communication-frameworks.md) for detailed structures.

### Persuasion Overlays

Layer these principles onto any framework:

| Principle | Application |
|-----------|-------------|
| Reciprocity | Lead with valuable insights before any ask |
| Commitment | Build micro-agreements toward major ask |
| Social Proof | Testimonials from relatable peers, logos |
| Scarcity | Cost of inaction, limited opportunity |
| Unity | "We" language, shared identity |

### Cognitive Optimization

Apply to all decks:

- **3-5 items max** per concept (working memory limit)
- **Peak-end rule:** Design one memorable peak; craft powerful ending
- **Primacy/recency:** Core thesis at start; CTA and summary at end
- **Dual coding:** Complementary (not redundant) visual + verbal

## Hybrid Frameworks

When two frameworks fit equally well, combine them:

| Hybrid | When to Use | How to Combine |
|--------|-------------|----------------|
| Pyramid + Prestige | Exec audience but material has twist | Answer-first, but structure evidence as "Turn" |
| Heist + Columbo | Strategy explaining past success | Goal → how crew achieved it |
| Trojan Horse + Rashomon | Controversial reframe | Multiple views → reveal missing axis |
| Time Machine + Heist | Strategic planning with execution | Future-back vision → "crew assembly" |
| Mystery Box + Pyramid | Research for execs | SCQA hook with mystery → Pyramid body |
| Hero's Journey + Game of Scene | Case study with pattern insight | Transformation → "name the game" lesson |

## PHASE 5: Review Panel

After delivering the deck, run the full Review Panel.

### Execution

Run all 5 agents in parallel, each reviewing the complete deck through their specialized lens:

1. **Audience Advocate** — Reviews as the target audience; flags what won't land
2. **Comms Specialist** — Reviews for messaging, emotion, persuasion; sharpens language
3. **Visual Designer** — Reviews design notes; upgrades visual metaphors
4. **Critic** — Reviews for pacing, redundancy, weak links; identifies cuts
5. **Content Expert** — Reviews for accuracy, sourcing, logical validity; flags fabrication

### Agent Prompts (Internal)

When invoking agents, use these prompts:

**Audience Advocate:**
> You are the [audience description]. Review this deck through your eyes.
> - What resonates with your priorities and mental models?
> - What makes you skeptical, bored, or confused?
> - What's missing that you'd need to see?
> - Which slides would you tune out on?
> Provide specific slide-level feedback.

**Comms Specialist:**
> You are a PR/communications strategist drawing from advertising, political communication, and persuasion science.
> - Is there one clear takeaway? State it.
> - Map the emotional arc — where are the dead spots?
> - Flag any PR risks (could this be misquoted? Leaked badly?)
> - Identify 3 headlines that could be sharper and rewrite them.
> - What persuasion techniques are underutilized?

**Visual Designer:**
> You are a visual storytelling expert.
> - Is the metaphor family consistent throughout?
> - Which slides have weak or generic design notes? Upgrade them.
> - What visual would make the key reveal unforgettable?
> - Are any data visualizations missing that would strengthen the argument?
> - Identify the 3 most memorable potential visuals and describe them specifically.

**Critic:**
> You are a ruthless editor focused on efficacy.
> - If you had to cut 5 slides, which would they be and why?
> - Rank the slides from strongest to weakest (top 5 and bottom 5).
> - Where does pacing drag? Where does it rush?
> - Does the argument actually hold together? Find the weakest logical link.
> - Probability this deck achieves its stated purpose: X%. Explain.

**Content Expert:**
> You are a fact-checker and accuracy specialist.
> - Flag any claims that aren't directly supported by the source material.
> - Identify slides marked [GENERATED] that make factual claims — are they defensible?
> - Are there logical leaps where conclusions don't follow from evidence?
> - What caveats or limitations are missing that a challenger would raise?
> - Rate confidence in each major claim: High / Medium / Low / Unsupported.

### Director Synthesis

After receiving all agent feedback, the Director:

1. **Identifies consensus** — Where do multiple agents agree? These are high-confidence recommendations.

2. **Resolves minor conflicts** — When agents mildly disagree, Director decides based on:
   - Audience profile (Audience Advocate gets tiebreaker on resonance)
   - Content type (Content Expert gets tiebreaker on factual claims)
   - Purpose (Comms Specialist gets tiebreaker on persuasion)

3. **Escalates strong conflicts** — When agents directly contradict or flag critical issues, present to user for resolution.

4. **Synthesizes output** — Produce unified recommendations with attribution.

### Output Format

```markdown
## Review Panel Synthesis

### Strengths
- [What's working] — *Audience Advocate*
- [What's working] — *Comms Specialist*
- [What's working] — *Visual Designer*

### Recommended Changes

**Messaging & Language**
1. Slide [N]: [Change] — *Comms Specialist*
2. Slide [N]: [Change] — *Comms Specialist*

**Audience Fit**
1. Slide [N]: [Change] — *Audience Advocate*

**Visual Upgrades**
1. Slide [N]: [Specific visual recommendation] — *Visual Designer*
2. Slide [N]: [Specific visual recommendation] — *Visual Designer*

**Cuts & Pacing**
1. [Recommendation] — *Critic*

**Accuracy & Sourcing**
1. Slide [N]: [Flag or fix] — *Content Expert*

### Research Findings

**Supporting Evidence (for your use)** — *Content Expert*
- [Claim]: [Supporting data/study found] — [Source URL]
- [Additional context that could enrich the deck]

**Opposition & Counterarguments (to address or preempt)** — *Critic*
- [Counterargument audience may raise] — [Source URL]
  - Suggested preemption: [How to handle]
- [Known weakness to acknowledge]

### Points Requiring Your Decision

> **Conflict:** [Description]
>
> **[Agent A]:** [Their view and rationale]
>
> **[Agent B]:** [Their view and rationale]
>
> Which approach do you prefer?
> 1. [Option A]
> 2. [Option B]
> 3. Keep as-is

### Overall Assessment

**Ready to present?** [Yes / Yes with minor edits / Needs revision]

**Most important improvement:** [Single sentence]

**Confidence this achieves [stated purpose]:** [X%] — *Critic*

**Factual defensibility:** [High / Medium / Low] — *Content Expert*
```

## Example Workflow

**User:** [Pastes 2,000-word article about remote work productivity research]

**Claude:**
> Got it — I've reviewed your article on remote work productivity research. Let me ask a few questions to recommend the right framework.
>
> **Who is your audience?**
> 1. Executive / Board
> 2. Technical / Engineering
> 3. Sales / Marketing
> 4. Investors / VCs
> 5. General Public / Keynote
> 6. Skeptics / Resisters
> 7. Mixed / Cross-functional
> 8. Academic / Research

**User:** 1

**Claude:**
> **What are you trying to accomplish?**
> 1. Persuade to act
> 2. Inform / Educate
> 3. Inspire / Motivate
> 4. Align / Build consensus
> 5. Report / Update
> 6. Defend / Justify
> 7. Entertain / Engage

**User:** Persuade them to update our hybrid work policy

**Claude:**
> **What tone do you want?**
> 1. Authoritative / Expert
> 2. Provocative / Challenging
> 3. Warm / Relatable
> 4. Urgent / Action-oriented
> 5. Balanced / Objective
> 6. Visionary / Aspirational
> 7. Playful / Creative

**User:** 1 but not aggressive

**Claude:**
> **Does your research contain a counterintuitive finding or surprise?**
> 1. Yes — there's a twist or "aha moment"
> 2. No — straightforward information delivery
> 3. Uncertain — help me identify

**User:** 1 — the data shows fully remote workers are MORE productive than hybrid

**Claude:**
> That counterintuitive finding is gold. Here are my recommendations:
>
> ## Recommendation 1: The Prestige + Pyramid Hybrid
> **Fit score:** ★★★★★
>
> **Why this works:** Your exec audience wants efficiency (Pyramid), but you have a genuine "Turn" — the counterintuitive finding that fully remote beats hybrid. This hybrid lets you lead with the recommendation while structuring evidence as a revelation.
>
> **Your content in this structure:**
> 1. **Pledge (Answer):** "Our data suggests fully remote outperforms hybrid for productivity"
> 2. **Setup:** Conventional wisdom says hybrid is best of both worlds
> 3. **Evidence stack:** Show expected patterns first
> 4. **Turn [REVEAL]:** "But when we isolated for X, the pattern inverted"
> 5. **Prestige:** Reframe what this means for policy
> 6. **Recommendation:** Specific policy changes
>
> [Continue with 2 more numbered recommendations...]
>
> **Which framework would you like? Type 1, 2, 3, or describe a hybrid.**

**User:** 1

**Claude:**
> **How long is your presentation?**
> 1. Short (10-12 minutes)
> 2. Medium (30 minutes)
> 3. Full (60 minutes)

**User:** 2

**Claude:**
> [Generates full deck with source tags and sourcing summary]
>
> Running Review Panel...

**Claude:**
> ## Review Panel Synthesis
>
> ### Strengths
> - The "Turn" reveal at slide 12 will genuinely surprise this audience — *Audience Advocate*
> - Message discipline is tight: one clear takeaway (remote > hybrid) — *Comms Specialist*
> - The before/after productivity chart will be memorable — *Visual Designer*
>
> ### Recommended Changes
>
> **Messaging & Language**
> 1. Slide 3: "challenges conventional wisdom" → "contradicts what most leaders assume" — *Comms Specialist*
>
> **Audience Fit**
> 1. Slide 8: Add one sentence acknowledging hybrid's perceived benefits before dismissing — *Audience Advocate*
>
> **Visual Upgrades**
> 1. Slide 12 (reveal): Add animation showing productivity lines crossing — *Visual Designer*
>
> **Cuts & Pacing**
> 1. Slides 5-6 cover similar ground; combine into one — *Critic*
>
> **Accuracy & Sourcing**
> 1. Slide 14: "30% productivity increase" needs citation from source — *Content Expert*
>
> ### Points Requiring Your Decision
>
> > **Conflict:** Critic recommends cutting slide 9 (methodology), but Content Expert says it's essential for credibility.
> >
> > **Critic:** "Execs don't care about methodology. This will lose them."
> >
> > **Content Expert:** "Without methodology, skeptics will dismiss the findings as cherry-picked."
> >
> > Which approach?
> > 1. Cut slide 9
> > 2. Keep slide 9
> > 3. Compress methodology to 2 bullets within another slide
>
> ### Overall Assessment
>
> **Ready to present?** Yes with minor edits
>
> **Most important improvement:** Add the acknowledgment of hybrid benefits (slide 8) to preempt objections.
>
> **Confidence this achieves persuasion:** 78% — *Critic*
>
> **Factual defensibility:** High (one citation needed) — *Content Expert*


