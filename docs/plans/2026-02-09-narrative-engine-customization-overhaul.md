# Narrative Engine Customization Overhaul

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make the Narrative Engine produce powerful, unique storytelling that genuinely varies across audiences, arcs, and intents — eliminating the sameness problem where discovery answers don't propagate into the build phase.

**Architecture:** Three systemic changes: (1) Create new reference files that carry audience/voice/emotion data through the entire workflow, (2) Insert a Build Brief phase that translates all discovery answers into concrete writing instructions, (3) Modify the main skill and existing reference files to wire everything together — including anti-sameness mechanisms and an Originality Agent.

**Skill directory:** `/Users/noahraford/.claude/skills/Narrative-Engine/`

---

## Task 1: Create Audience Profiles Reference

**Why:** Currently, audience selection is a label used once for framework selection, then dropped. Deep profiles carry audience intelligence into every build decision.

**Files:**
- Create: `audience-profiles.md`

**Step 1: Write the audience profiles file**

Create `audience-profiles.md` with deep profiles for all 8 audience types. Each profile must include:

| Section | Purpose |
|---------|---------|
| **Mental model** | How this audience processes information (deductive vs. inductive, data-first vs. story-first) |
| **Trust signals** | What makes them believe you (data, credentials, peer examples, methodology) |
| **Resistance triggers** | What makes them tune out or push back |
| **Evidence style** | What types of proof they find compelling |
| **Language register** | Vocabulary level, sentence rhythm, formality, jargon tolerance |
| **Emotional range** | What emotional register works vs. backfires |
| **What they quote** | What they'll repeat after the presentation (the metric? the metaphor? the story?) |
| **Persuasion priorities** | Which 2-3 Cialdini principles work best for this audience |
| **Headline style** | How headlines should read for this audience specifically |
| **CTA style** | Hard ask vs. soft ask vs. implied, specificity level |

The 8 audiences:
1. Executive / Board
2. Technical / Engineering
3. Sales / Marketing
4. Investors / VCs
5. General Public / Keynote
6. Skeptics / Resisters
7. Mixed / Cross-functional
8. Academic / Research

**Key design principle:** These profiles should be written as *instructions to the writer*, not descriptions of the audience. "Write short declarative sentences. Lead every section with the conclusion." not "Executives prefer concise communication."

**Step 2: Verify completeness**

Check that all 8 profiles contain all 10 sections. Check that the profiles produce meaningfully different writing instructions — if two profiles give the same headline style guidance, differentiate them.

**Step 3: Commit**

```bash
cd /Users/noahraford/.claude/skills/Narrative-Engine
git add audience-profiles.md
git commit -m "feat: add deep audience profiles that carry through build phase"
```

---

## Task 2: Create Voice Profiles Reference

**Why:** The skill currently produces one voice: "competent professional AI." Voice profiles create distinct writing personalities that the user can select or that auto-derive from audience + tone answers.

**Files:**
- Create: `voice-profiles.md`

**Step 1: Write the voice profiles file**

Create `voice-profiles.md` with 7 distinct voice profiles. Each profile must include:

| Section | Purpose |
|---------|---------|
| **Description** | 1-2 sentences capturing the personality |
| **Sentence structure** | Typical length, complexity, rhythm pattern |
| **Vocabulary** | Register level, preferred word types, forbidden patterns |
| **Paragraph rhythm** | How paragraphs build, typical length, variation pattern |
| **Emotional register** | How emotion shows up (or doesn't) |
| **Signature moves** | 2-3 techniques this voice uses that others don't |
| **Example paragraph** | A sample paragraph in this voice about a generic business topic |
| **Auto-derive rule** | Which audience + tone combinations map to this voice |

The 7 voices:

1. **Boardroom** — Short. Declarative. Numbers anchor every claim. No hedging except genuine uncertainty. "The data shows X. This costs us Y. We recommend Z."

2. **TED Stage** — Conversational authority. Questions to audience. Personal bridges to data. Building to collective realization. Varied sentence length for rhythm.

3. **Provocateur** — Challenges assumptions directly. Comfortable with discomfort. Willing to be polarizing. Short punchy sentences mixed with longer elaborations.

4. **Investigator** — Builds evidence methodically. Lets reader draw conclusions moments before stating them. "Notice something odd?" energy. Careful, accumulating.

5. **Storyteller** — Character-driven. Scenes, not summaries. Concrete sensory detail. Dialogue. "It was 2am on a Tuesday when the dashboard turned red."

6. **Academic** — Precise. Qualified. Evidence-layered. Methodology-visible. "A longitudinal analysis of N=847, controlling for X, suggests..."

7. **Dry Wit** — Understated. Ironic. Smart. Says the serious thing in the least serious way. Lets the audience feel clever for catching the implication.

**Auto-derive mapping table:**

Include a matrix showing which audience + tone combinations auto-select which voice:

| | Authoritative | Provocative | Warm | Urgent | Balanced | Visionary | Playful |
|---|---|---|---|---|---|---|---|
| **Executive** | Boardroom | Provocateur | Storyteller | Boardroom | Boardroom | TED Stage | Dry Wit |
| **Technical** | Academic | Investigator | Investigator | Boardroom | Academic | TED Stage | Dry Wit |
| **Sales/Marketing** | TED Stage | Provocateur | Storyteller | Provocateur | TED Stage | TED Stage | Dry Wit |
| **Investors** | Boardroom | Provocateur | Storyteller | Boardroom | Boardroom | TED Stage | Dry Wit |
| **General Public** | TED Stage | Provocateur | Storyteller | TED Stage | TED Stage | TED Stage | Storyteller |
| **Skeptics** | Investigator | Provocateur | Storyteller | Investigator | Academic | Investigator | Dry Wit |
| **Mixed** | TED Stage | TED Stage | Storyteller | Boardroom | TED Stage | TED Stage | Dry Wit |
| **Academic** | Academic | Academic | Investigator | Academic | Academic | TED Stage | Dry Wit |

Also include a note that the user can override the auto-derived voice.

**Step 2: Verify distinctiveness**

Read each example paragraph. If any two voices sound similar, rewrite until they're clearly distinguishable. The test: could someone identify which voice wrote a paragraph without seeing the label?

**Step 3: Commit**

```bash
cd /Users/noahraford/.claude/skills/Narrative-Engine
git add voice-profiles.md
git commit -m "feat: add 7 distinct voice profiles with auto-derive mapping"
```

---

## Task 3: Create Emotional Arc Maps

**Why:** Frameworks define structural beats but not emotional beats. The audience should *feel* something specific at each stage, and those feelings should differ by audience type.

**Files:**
- Create: `emotional-arcs.md`

**Step 1: Write the emotional arcs file**

Create `emotional-arcs.md` with:

**Section 1: Framework Emotional Textures**

For each of the 10 narrative arcs, define:

| Element | Description |
|---------|-------------|
| **Core emotional shape** | The feeling trajectory (e.g., "comfort → unease → snap → reorientation") |
| **Pacing feel** | How the rhythm should feel (e.g., "measured, then sudden, then reflective") |
| **Language texture** | How the writing style shifts across beats (e.g., "precise and clinical in the setup, breaks register at the Turn") |
| **Tension management** | How tension builds, peaks, and resolves |
| **The key emotional moment** | Which beat carries the most emotional weight and how to handle it |

Example for The Prestige:
- **Core shape:** Confidence → comfort → slight unease → surprise → reorientation → urgency
- **Pacing:** Measured and deliberate through beats 1-4, then a sharp break at the Turn, then expansive in the Prestige
- **Language texture:** Clinical precision in the setup (builds false authority), register break at the Turn (shorter sentences, more direct), reflective expansion in the Prestige
- **Tension:** Build through false security — the audience should feel *too* comfortable, which makes the Turn land harder
- **Key moment:** The Turn. It must feel like a physical snap. One sentence that reframes everything. Don't soften it with hedging or transition language.

Do this for all 10 arcs: Prestige, Mystery Box, Heist, Time Machine, Trojan Horse, Hero's Journey, Freytag, Columbo, Game of Scene, Rashomon.

**Section 2: Audience-Specific Emotional Calibration**

A matrix showing how emotional intensity and type should shift per audience:

| Audience | Emotional ceiling | Primary emotions to use | Emotions that backfire | Intensity dial (1-5) |
|----------|------------------|------------------------|----------------------|---------------------|
| Executive | Controlled | Urgency, clarity, confidence | Sentimentality, fear | 2 |
| Technical | Restrained | Intellectual curiosity, respect for rigor | Hype, inspiration-speak | 1-2 |
| Investors | Calibrated | Excitement, FOMO, confidence | Desperation, overselling | 3 |
| General Public | Full range | Wonder, recognition, hope | Condescension, complexity | 4-5 |
| Skeptics | Earned slowly | Respect, intellectual honesty, surprise | Enthusiasm before proof | 1→3 (builds) |
| etc. | | | | |

**Section 3: Emotional Beat Maps**

For the 3 most common framework + audience combinations, write full emotional beat maps showing *what the audience should feel at each beat*. These serve as models for generating maps for other combinations.

Example combinations:
1. Prestige + Executive
2. Trojan Horse + Skeptics
3. Hero's Journey + General Public/Keynote

**Step 2: Verify coverage**

Ensure all 10 frameworks have emotional textures. Ensure the audience calibration matrix covers all 8 audiences. Ensure the 3 example beat maps are detailed enough to serve as templates.

**Step 3: Commit**

```bash
cd /Users/noahraford/.claude/skills/Narrative-Engine
git add emotional-arcs.md
git commit -m "feat: add emotional arc maps with audience-specific calibration"
```

---

## Task 4: Create Opening & Closing Strategies Reference

**Why:** Currently, opening and closing are dictated entirely by framework structure. A strategies library gives more control and variety.

**Files:**
- Create: `opening-closing-strategies.md`

**Step 1: Write the strategies file**

Create `opening-closing-strategies.md` with:

**Section 1: Opening Strategies (8 types)**

For each opening type, include:
- **Name and description** (1 sentence)
- **How it works** (2-3 sentences explaining the mechanism)
- **Best for** (which audience + purpose + framework combinations)
- **Example** (a concrete example applied to a generic business topic)
- **Avoid when** (when this opening backfires)

The 8 openings:
1. **Cold Open Scene** — Drop into a specific moment with sensory detail
2. **Provocative Question** — A question that challenges assumptions
3. **Startling Statistic** — The number that stops the room
4. **Personal Anecdote** — First-person story that bridges to the topic
5. **Historical Parallel** — "In 1997, Nokia..." draws a parallel to today
6. **Future Projection** — "Imagine it's 2028 and..."
7. **Contradiction** — "You've been told X. The data says the opposite."
8. **Shared Pain** — "We've all been in that meeting where..."

**Section 2: Closing Strategies (7 types)**

Same structure as openings. The 7 closings:
1. **Callback** — Return to opening image/moment with new meaning
2. **Challenge** — "The question isn't whether — it's when you'll act"
3. **Future Vision** — Paint the transformed state vividly
4. **Lingering Question** — Leave one unanswered question that stays with them
5. **The Simple Truth** — Strip everything away to one sentence
6. **Personal Commitment** — "Here's what I'm doing Monday morning"
7. **The Image** — One vivid picture that encapsulates the entire argument

**Section 3: Pairing Matrix**

A table showing recommended opening + closing combinations by audience and purpose.

**Section 4: Anti-Repetition Rule**

Instruction: "When building, consult this file and select an opening and closing strategy that fits the Build Brief. Do NOT default to the framework's standard opening beat. The framework defines the *structural* opening; this file defines the *rhetorical* opening. They combine: the Prestige's Pledge beat might use a Cold Open Scene or a Shared Pain opening. Note the selected strategies in the Build Brief."

**Step 2: Verify variety**

Check that the pairing matrix doesn't funnel most combinations to the same 2-3 pairings. Ensure at least 5 distinct opening-closing pairs appear as primary recommendations across the matrix.

**Step 3: Commit**

```bash
cd /Users/noahraford/.claude/skills/Narrative-Engine
git add opening-closing-strategies.md
git commit -m "feat: add opening/closing strategy libraries with pairing matrix"
```

---

## Task 5: Add Emotional Texture to Narrative Arcs

**Why:** The 10 arcs currently define beats and slide counts only. They need emotional texture, pacing instructions, and language-shifting guidance baked into each arc's definition.

**Files:**
- Modify: `narrative-arcs.md`

**Step 1: Add emotional texture section to each arc**

For each of the 10 arcs in `narrative-arcs.md`, add a new section after the beat structure table called `### Emotional Texture & Pacing`. This section should include:

1. **Emotional shape** (1 line: the feeling trajectory)
2. **Pacing instructions** (2-3 lines: how the rhythm shifts across the arc)
3. **Language shifts** (2-3 lines: how the writing style changes at key moments — e.g., register breaks, sentence length changes, vocabulary shifts)
4. **The key moment** (2-3 lines: which beat is the emotional peak, and specific instructions for how to handle it — e.g., "Don't soften the Turn with hedging. One sentence. Let it land.")
5. **Protected emotional beats** (list which beats are emotional "protected species" that must not be compressed or cut)

**Important:** Reference `emotional-arcs.md` for the full emotional framework, but include a compact version directly in each arc definition so it's immediately visible during the build phase.

**Step 2: Verify each arc has the new section**

Read through all 10 arcs and confirm each has the Emotional Texture & Pacing section with all 5 elements.

**Step 3: Commit**

```bash
cd /Users/noahraford/.claude/skills/Narrative-Engine
git add narrative-arcs.md
git commit -m "feat: add emotional texture, pacing, and language shift instructions to all 10 arcs"
```

---

## Task 6: Overhaul Framework Selection — Anti-Bias + Dark Horse

**Why:** The current selection process gravitates to the same 4-5 frameworks. Need to force consideration of the full library and surface unexpected options.

**Files:**
- Modify: `framework-selection.md`
- Delete: `framework_selection_guide.md` (redundant — merge any unique content into `framework-selection.md` first)

**Step 1: Merge unique content from `framework_selection_guide.md` into `framework-selection.md`**

Compare the two files. `framework_selection_guide.md` has a more detailed Part 7 with framework descriptions. Identify any content in `framework_selection_guide.md` that isn't already in `framework-selection.md` or `communication-frameworks.md`. Merge only truly unique content.

**Step 2: Add "Full Sweep Requirement" section**

Add a new section at the top of `framework-selection.md` after the title:

```markdown
## Framework Selection Protocol

**REQUIRED: Before recommending 2-3 frameworks, complete the full sweep below.**

### Step 1: Score all 10 narrative arcs

For the user's specific combination of audience + purpose + content type + tone, score each arc 1-5:

| Arc | Fit Score (1-5) | Key reason |
|-----|----------------|------------|
| A) Prestige | | |
| B) Mystery Box | | |
| C) Heist | | |
| D) Time Machine | | |
| E) Trojan Horse | | |
| F) Hero's Journey | | |
| G) Freytag | | |
| H) Columbo | | |
| I) Game of Scene | | |
| J) Rashomon | | |

### Step 2: Score communication frameworks

Score the top 5 most relevant communication frameworks.

### Step 3: Recommend

- Present the top 2 scoring arcs with their best communication framework pairing
- **Dark Horse requirement:** Also present 1 arc that scored 3 or higher but is NOT the obvious choice. Explain what it would unlock that the top picks wouldn't. Label it "Dark Horse."
- **Rejection log:** In 1-2 sentences, note why the lowest-scoring arcs don't fit. This demonstrates genuine consideration and helps the user understand the tradeoffs.
```

**Step 3: Balance underused frameworks in the selection matrices**

Review the By Audience, By Purpose, and By Tone tables. Ensure that Freytag, Game of Scene, Story Circle, Vonnegut shapes, and Schwartz Awareness each appear as a primary recommendation in at least 2 rows. Currently some appear zero times. Add them where genuinely appropriate with notes on when they shine.

**Step 4: Remove the Quick Selection Heuristics from SKILL.md**

(This happens in Task 8 when modifying SKILL.md — note here as a dependency.)

**Step 5: Delete the redundant file**

```bash
cd /Users/noahraford/.claude/skills/Narrative-Engine
git rm framework_selection_guide.md
```

**Step 6: Commit**

```bash
cd /Users/noahraford/.claude/skills/Narrative-Engine
git add framework-selection.md
git commit -m "feat: add full sweep protocol, dark horse requirement, and balance underused frameworks"
```

---

## Task 7: Add Anti-Sameness Checks to Checklists

**Why:** Need explicit mechanisms to detect and prevent generic, repetitive output.

**Files:**
- Modify: `checklists.md`

**Step 1: Add Originality Checklist section**

Add a new section to `checklists.md`:

```markdown
## Originality & Anti-Sameness Checklist

Run after the build, before the review panel:

### Structure
- [ ] At least one beat breaks the expected pattern (shorter/longer than expected, different format, unexpected placement)
- [ ] The opening is NOT the framework's default first beat used generically — it combines the framework beat with a specific opening strategy from `opening-closing-strategies.md`
- [ ] The closing is NOT just a callback — verify it uses the selected closing strategy

### Language
- [ ] No three consecutive headlines share the same grammatical structure (declarative, question, imperative, conditional — vary)
- [ ] Voice profile is consistently applied — read 3 random sections and verify they match the selected voice
- [ ] At least 2 headlines would NOT work in a different deck (they're specific to THIS content)

### The Killer Line
- [ ] One line in the piece is explicitly designed to be quoted/remembered
- [ ] It passes the tests: short (< 15 words), concrete, surprising, repeatable
- [ ] It appears at a high-impact moment (the Turn, the close, or the S.T.A.R. moment)
- [ ] Flag it in the output with **[KILLER LINE]** tag

### Emotional Distinctiveness
- [ ] The emotional arc matches the framework's emotional texture (from `emotional-arcs.md`)
- [ ] The writing shifts register at least once (e.g., clinical → direct at the Turn)
- [ ] The piece would feel different if you swapped in a different framework — if not, the framework isn't doing enough work

### The AI Test
- [ ] Read the opening. Does it sound like it could have come from any AI? If yes, rewrite.
- [ ] Check for these generic AI patterns and eliminate: "In today's rapidly changing...", "Let's dive in...", "In conclusion...", "The question isn't if but when...", "At its core..."
- [ ] The piece has at least one moment of genuine surprise, wit, or personality
```

**Step 2: Add Killer Line Checklist section**

```markdown
## Killer Line Design Checklist

Every piece must have ONE line designed to be remembered. Use this checklist to craft and verify it.

### Crafting
- [ ] Expresses the focal statement in the most compressed, vivid form possible
- [ ] Uses concrete imagery (not abstract concepts)
- [ ] Contains tension, contrast, or surprise
- [ ] Is self-contained (doesn't need context to make sense)
- [ ] Would work as an email subject line, tweet, or meeting title

### Testing
- [ ] Say it aloud. Is it easy to repeat verbatim?
- [ ] Cover the rest of the deck. Does this line capture the essence?
- [ ] Could a competitor claim this line? (If yes, make it more specific)
- [ ] Would someone text this to a colleague? (The viral test)

### Placement
- [ ] Appears at a high-impact structural moment
- [ ] Gets its own visual/typographic emphasis in the design notes
- [ ] Is NOT buried in a spotlight — it's a headline or standalone element

### Examples of strong killer lines
- "Email isn't communication — it's other people's to-do lists for you"
- "The office isn't where work happens — it's where work gets interrupted"
- "Build what differentiates us; buy everything that doesn't"
- "Every communication tool eventually becomes an anxiety delivery system"
```

**Step 3: Commit**

```bash
cd /Users/noahraford/.claude/skills/Narrative-Engine
git add checklists.md
git commit -m "feat: add originality, anti-sameness, and killer line checklists"
```

---

## Task 8: Overhaul SKILL.md — The Main Skill File

**Why:** This is where everything comes together. The main skill needs a new Build Brief phase, rewired Phase 3, rewired Phase 4, a new Originality Agent, and references to all the new files.

**Files:**
- Modify: `SKILL.md`

This is the largest task. Break it into sub-steps.

**Step 1: Update the Workflow Overview**

Replace the current workflow diagram with:

```
PHASE 1     Content Import
    ↓
PHASE 1.5   Output Format — Presentation / Prose / Both
    ↓
PHASE 1.75  Focal Discovery — "What's the ONE point?"
    ↓
PHASE 2     Discovery Questions — Audience, purpose, content type, tone
    ↓
PHASE 2.5   Density Mode — Varies by output format
    ↓
PHASE 3     Framework Recommendation — Full sweep + dark horse
    ↓
PHASE 3.5   Build Brief — Translates ALL discovery into concrete writing instructions
    ↓
PHASE 4     Build — Guided by Build Brief, voice profile, emotional arc
    ↓
PHASE 4.5   Originality Check — Anti-sameness sweep before review
    ↓
PHASE 5     Review Panel — 6 specialist agents (now includes Originality Agent)
    ↓
PHASE 5.5   Stress Test Panel — Optional, auto-selected personas
    ↓
ON-DEMAND   "Tighter" — Compression passes anytime
```

**Step 2: Modify Phase 3 — Remove Quick Heuristics, Add Full Sweep**

Replace the "Quick Selection Heuristics" table and the current Phase 3 instructions with:

```markdown
## PHASE 3: Framework Recommendation

Based on discovery answers, recommend frameworks using the Full Sweep Protocol.

**REQUIRED:** Before recommending, complete the framework scoring sweep in [`framework-selection.md`](framework-selection.md). This means:
1. Score all 10 narrative arcs (1-5) against this specific combination of inputs
2. Score the top 5 communication frameworks
3. Present the top 2 arc + framework pairings with skeleton and tradeoffs
4. Present 1 Dark Horse — an unexpected option that scores 3+ and could produce something more original
5. Include a Rejection Log — 1-2 sentences on why low-scoring options don't fit

For each recommendation:
1. **Name the framework** and category
2. **Explain fit** in 2-3 sentences specific to their situation
3. **Show the skeleton** — their content mapped to the framework's beats
4. **Flag tradeoffs** — what this framework does well vs. potential drawbacks
5. **Emotional preview** — what the audience will *feel* at the key moments (reference [`emotional-arcs.md`](emotional-arcs.md))

See [`framework-selection.md`](framework-selection.md) for the full sweep protocol and selection matrices.
See [`narrative-arcs.md`](narrative-arcs.md) for arc details including emotional textures.
See [`communication-frameworks.md`](communication-frameworks.md) for framework details.
```

Also keep the "High-Stakes Content: Early Agent Review" section as-is.

**Step 3: Add Phase 3.5 — The Build Brief**

Insert a new phase between Phase 3 and Phase 4:

```markdown
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

**Persuasion Strategy:** [2-3 Cialdini principles prioritized for this audience]
- Primary: [principle] — apply by [specific instruction]
- Secondary: [principle] — apply by [specific instruction]

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
```

**Step 4: Rewire Phase 4 — Build**

Replace the current Phase 4 opening paragraph with:

```markdown
## PHASE 4: Build

Generate the output guided by the Build Brief. Every decision references the brief — voice, audience, emotional arc, opening/closing, persuasion strategy. The Build Brief is the primary reference; framework beat structure is the secondary reference.
```

Add these new subsections within Phase 4:

**After the Three-Level Clarity System, before the output format sections:**

```markdown
### Voice Application

Apply the selected voice profile from [`voice-profiles.md`](voice-profiles.md) throughout:
- **Sentence structure** must match the profile's patterns
- **Vocabulary** must stay within the profile's register
- **Paragraph rhythm** must follow the profile's variation pattern
- **Signature moves** should appear at least 2-3 times in the piece

### Emotional Arc Application

Follow the framework's emotional texture from [`emotional-arcs.md`](emotional-arcs.md):
- Map the intended audience emotion to each beat
- Shift language register at the points specified in the arc's texture
- Calibrate intensity to the audience's emotional ceiling
- The key emotional moment gets extra craft — do not rush it

### Killer Line Placement

During the build, identify the Killer Line:
- Refine the candidates from the Build Brief
- Place it at the highest-impact moment
- Tag it with **[KILLER LINE]** in the output
- Verify it passes the tests in [`checklists.md`](checklists.md) Killer Line checklist
```

**Update the Headline Rules** to add audience-conditional instructions:

After the existing headline rules, add:

```markdown
**Audience-Conditional Headline Adjustments:**
- Consult the selected audience profile in [`audience-profiles.md`](audience-profiles.md) for headline style specific to this audience
- The generic rules above are the baseline; the audience profile overrides where they conflict
- Example: Executive audience headlines should be answer-first and data-anchored; Keynote audience headlines can be more provocative and metaphor-driven
```

**Update the output templates** to include Build Brief metadata:

In both the Presentation and Prose output templates, add after the existing metadata:

```markdown
**Voice:** [selected voice profile]
**Emotional arc:** [shape summary]
**Opening strategy:** [type]
**Closing strategy:** [type]
**Killer Line:** "[the line]"
```

**Step 5: Add Phase 4.5 — Originality Check**

Insert between Phase 4 and Phase 5:

```markdown
## PHASE 4.5: Originality Check

Before sending to the Review Panel, run the Originality & Anti-Sameness Checklist from [`checklists.md`](checklists.md).

If any check fails, revise before proceeding. Key checks:
- Voice profile consistently applied
- Emotional arc matches framework texture
- No three consecutive headlines share grammatical structure
- Killer Line identified and placed
- Opening/closing use selected strategies (not defaults)
- The AI Test: opening doesn't sound generic
```

**Step 6: Modify Phase 5 — Add Originality Agent**

Update the Review Panel diagram to show 6 agents:

```
                    ┌─────────────────────────────────────┐
                    │            DIRECTOR                 │
                    │  Synthesizes, resolves conflicts    │
                    └─────────────────────────────────────┘
                                     ▲
        ┌──────┬──────┬──────────────┼──────────────┬──────┬──────┐
        ▼      ▼      ▼             ▼              ▼      ▼      ▼
   AUDIENCE  COMMS  VISUAL      CRITIC        CONTENT  ORIGINALITY
   ADVOCATE        DESIGNER                   EXPERT    AGENT
```

Add the Originality Agent role:

```markdown
**Originality Agent** — Reviews for distinctiveness, freshness, and anti-sameness.
- Reference: [`checklists.md`](checklists.md) — Originality & Anti-Sameness Checklist
- Key questions:
  - "Would this be distinguishable from any other AI-generated piece on this topic?"
  - "Is the Build Brief actually reflected in the output, or did the build revert to generic?"
  - "What's the one element that makes this piece *this piece* and no other?"
- Checks: Voice consistency, emotional arc adherence, headline variety, killer line quality, opening/closing strategy execution
- Flags: Generic patterns, AI-isms, missed opportunities for distinctiveness
```

**Step 7: Update the Reference Files table**

Add the new files to the reference table at the bottom:

```markdown
| [`audience-profiles.md`](audience-profiles.md) | Deep audience profiles carrying through build |
| [`voice-profiles.md`](voice-profiles.md) | 7 voice profiles with auto-derive mapping |
| [`emotional-arcs.md`](emotional-arcs.md) | Framework emotional textures + audience calibration |
| [`opening-closing-strategies.md`](opening-closing-strategies.md) | Opening/closing strategy libraries |
```

**Step 8: Update Quick Start**

Replace the current Quick Start with:

```markdown
## Quick Start

1. User provides content
2. Ask output format (Presentation / Prose / Both)
3. Propose focal points → user confirms
4. Ask discovery questions (audience, purpose, content type, tone)
5. Ask density mode (varies by format)
6. **Full sweep** all frameworks → recommend 2 + 1 dark horse → user selects
7. **Generate Build Brief** (voice, audience profile, emotional arc, strategies, killer line candidates) → user confirms
8. Build output guided by Build Brief
9. **Originality check** before review
10. Run Review Panel (6 agents including Originality Agent)
11. Offer Stress Test Panel
12. User requests "tighter" if needed
13. Offer Change Log export
```

**Step 9: Verify the full file**

Read the entire modified SKILL.md end-to-end. Check:
- Workflow diagram matches actual phases
- All new phases are present and in order
- All references to new files use correct filenames
- No orphaned references to removed content (Quick Selection Heuristics)
- Phase 4 explicitly references Build Brief as primary guide

**Step 10: Commit**

```bash
cd /Users/noahraford/.claude/skills/Narrative-Engine
git add SKILL.md
git commit -m "feat: add Build Brief phase, Originality Agent, rewire build to use discovery answers"
```

---

## Task 9: Create Additional Examples

**Why:** The single existing example (remote work / executive / Prestige) demonstrates only one path through the skill. Need examples that show range.

**Files:**
- Create: `examples/climate-keynote-example.md`
- Create: `examples/post-mortem-technical-example.md`

**Step 1: Write a keynote example**

Create `examples/climate-keynote-example.md` showing the full workflow for:
- **Audience:** General Public / Keynote
- **Purpose:** Inspire / Motivate
- **Content type:** Vision/inspiration piece
- **Tone:** Visionary / Aspirational
- **Framework:** Time Machine (D) — to show an underused framework
- **Voice:** TED Stage
- **Opening strategy:** Future Projection
- **Closing strategy:** Future Vision

Show: Content import → focal discovery → discovery answers → density (Narrative) → framework recommendation (showing the full sweep with scores, dark horse, rejection log) → Build Brief → abbreviated build output (3-4 slides) → review panel excerpt → how the Originality Agent flagged something and it got fixed.

**Step 2: Write a technical post-mortem example**

Create `examples/post-mortem-technical-example.md` showing:
- **Audience:** Technical / Engineering
- **Purpose:** Inform / Educate + Defend / Justify
- **Content type:** Post-mortem / retrospective
- **Tone:** Authoritative / Expert
- **Framework:** Columbo (H) — standard for post-mortems but with Investigator voice
- **Voice:** Investigator
- **Opening strategy:** Startling Statistic
- **Closing strategy:** The Simple Truth

Show the same phases but demonstrate how the voice, emotional arc, and Build Brief produce a piece that *reads completely differently* from the keynote example.

**Step 3: Commit**

```bash
cd /Users/noahraford/.claude/skills/Narrative-Engine
git add examples/
git commit -m "feat: add keynote and post-mortem examples demonstrating voice/arc variety"
```

---

## Task 10: Final Integration Verification

**Why:** Everything needs to work together. Verify cross-references, consistency, and that nothing was missed.

**Step 1: Verify all cross-references**

Check every file reference in SKILL.md and confirm:
- `audience-profiles.md` exists and is referenced correctly
- `voice-profiles.md` exists and is referenced correctly
- `emotional-arcs.md` exists and is referenced correctly
- `opening-closing-strategies.md` exists and is referenced correctly
- `framework_selection_guide.md` is deleted (no dangling references)
- All existing file references still work

**Step 2: Trace a user path**

Mentally walk through the skill as a user with these inputs:
- Content: A research article about AI in education
- Audience: Skeptics / Resisters
- Purpose: Persuade to act
- Tone: Balanced / Objective

Verify that at each phase, the new files are consulted and produce different output than the same content for an Executive audience with Urgent tone. Specifically check:
- Different framework scores in the full sweep
- Different voice auto-derived
- Different Build Brief
- Different emotional arc calibration
- Different opening/closing strategies
- Different headline style instructions

**Step 3: Check for bloat**

The main skill file (SKILL.md) should not have grown beyond what the model can process effectively. If it has, consider moving detailed instructions into reference files and keeping SKILL.md as an orchestration document with pointers. Target: SKILL.md stays under 800 lines.

**Step 4: Final commit**

```bash
cd /Users/noahraford/.claude/skills/Narrative-Engine
git add -A
git commit -m "chore: final integration verification and cross-reference cleanup"
```

---

## Dependency Map

```
Task 1 (Audience Profiles)  ─┐
Task 2 (Voice Profiles)      ├─→ Task 8 (SKILL.md overhaul) ─→ Task 10 (Integration)
Task 3 (Emotional Arcs)      │
Task 4 (Opening/Closing)    ─┘
Task 5 (Arc Textures)       ─→ Task 8
Task 6 (Framework Selection) ─→ Task 8
Task 7 (Checklists)         ─→ Task 8
                               Task 9 (Examples) ─→ Task 10
```

Tasks 1-7 can be executed in parallel (they create/modify independent files).
Task 8 depends on Tasks 1-7 (it references all new files).
Task 9 can run in parallel with Task 8.
Task 10 depends on Tasks 8 and 9.

---

## Summary of All Files Touched

| Action | File | Task |
|--------|------|------|
| **Create** | `audience-profiles.md` | 1 |
| **Create** | `voice-profiles.md` | 2 |
| **Create** | `emotional-arcs.md` | 3 |
| **Create** | `opening-closing-strategies.md` | 4 |
| **Modify** | `narrative-arcs.md` | 5 |
| **Modify** | `framework-selection.md` | 6 |
| **Delete** | `framework_selection_guide.md` | 6 |
| **Modify** | `checklists.md` | 7 |
| **Modify** | `SKILL.md` | 8 |
| **Create** | `examples/climate-keynote-example.md` | 9 |
| **Create** | `examples/post-mortem-technical-example.md` | 9 |
