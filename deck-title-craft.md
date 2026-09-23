# Deck Title Craft (embedded module)

> Maintained inside Narrative Engine. Originally embedded from a title-craft reference on 2026-09-16; merged with keynote-create's 2026-09-17 revision on 2026-09-23 (single canonical copy); see SYNC.md. No external skill or renderer is required. The approved purpose, source qualifications and selected outline outrank stylistic examples below.

Slide titles in this skill carry the story. The body of each slide supports the title; the title delivers the takeaway. This document goes deeper than the core rules in `SKILL.md`.

## The core principle

A great deck title delivers one beat of the argument: normally a short complete sentence in Boardroom, or a connected fragment in Keynote. Read in sequence, the titles tell the whole narrative without needing the slide bodies at all.

This is sometimes called the **action title** or **narrative title** approach. It is the opposite of *label titles* ("Background," "Methodology," "Results"), which sort content into bins but leave the audience to construct meaning themselves.

## Rules in depth

### 1. Sentence, not label
- Weak: "Q3 Results"
- Strong: "Q3 revenue grew but margins collapsed."

A label asks the audience to figure out what matters. A sentence tells them.

### 2. Short
4–10 words. Past 12 and the eye starts skipping. The audience reads the title in the time you take to advance the slide; budget your words accordingly.

### 3. One beat per slide
A slide is a unit of story. One title = one move in the argument. If a headline carries two distinct argument beats, split them into two slides. Two short sentences may express one beat, as in “Measure first. Then expand.”

### 4. Active voice
- Weak: "Adoption was hindered by onboarding friction."
- Strong: "Onboarding friction killed adoption."

### 5. Specificity beats abstraction
- Weak: "Customer feedback was mixed."
- Strong: "Power users loved it; new users bounced."

Numbers, names, and concrete nouns hold attention. Abstractions slide off.

### 6. Forward motion
Each title should make the next feel inevitable. If adjacent titles can be swapped without loss of sense, the sequence isn't doing narrative work — it's listing.

### 7. The turn is unmistakable
When the approved structure includes a turn, make it understandable in the headlines. Direct explanations and structures without a midpoint reversal need no invented pivot.

### 8. The last title lands
The final title is the last thing the audience reads. It should resolve, reframe, commit, or open forward. Never "Thank you," "Questions?", or "In conclusion."

## Common failure modes

### The dashboard problem
Titles that name what's on the slide rather than what it means.
- Weak: "Revenue by Region, Q1–Q3"
- Strong: "The West region carried us; the East fell off a cliff."

### The hedge problem — rhetorical filler only

Remove redundant rhetorical hesitation, but preserve the source's uncertainty, scope, estimates and causal status. “The pilot may help” must not become “The pilot works” unless the source supports that stronger claim. Correlation does not establish causation. Prefer “Early results suggest onboarding contributed to lower adoption” when that is what the evidence says. The evidence gate outranks punchiness.

### The list problem
Sequential titles with parallel structure, suggesting items rather than narrative motion.
- Weak: "Finding 1: ..." / "Finding 2: ..." / "Finding 3: ..."
- Strong: Three distinct sentences each advancing the story.

### The throat-clearing problem
Front-loading slides that delay the question.
- Weak: Slide 1 "Welcome" / Slide 2 "Agenda" / Slide 3 "About us"
- Strong: Slide 1 lands the world; slide 2 sharpens the stakes; the question is live by slide 3.

### The flat ending
A last title that doesn't land.
- Weak: "Conclusion" / "Thank you" / "Questions?"
- Strong: A title that completes the arc — a commitment, a reframe, a forward-opening question.

### The disconnected sequence (spoken-prose rule)

The single most important test for a narrative deck — and the one most easily faked by the model — is the **spoken-prose test**. Titles in isolation can be individually clear and still fail this test. The deck collapses when its titles don't chain.

> **The spoken-prose test.** Concatenate every title — *literally, every one, in order* — into a single paragraph. Read it aloud as continuous prose. It must sound like something you would actually *say* to walk a stranger through the argument. Not a summary, not a glossary — spoken delivery.

The failure mode: titles that each presume context they never set up. "Twenty-eight leaders gave the same answer" — *to what?* "They support the strategy" — *what strategy?* "They say the policies are hurting them" — *what policies?* Each title answers a question that hasn't been asked. The reader is two beats behind on every line.

The fix: each title must *carry its setup with it* or *resolve the previous title's open thread*. Pronouns require antecedents. New nouns either get introduced explicitly or specify a noun from the prior title. "Strategy" must either be named or follow a title that establishes which strategy. "The policies" must either be named or be followed by a title that names them.

**Antecedent test (run before the spoken-prose test):**

For each title after the cover:
- What is its subject? Is the subject either introduced in this title or carried forward from the previous one?
- What new nouns or pronouns does it use? Is each one either self-contained (a proper name, a concrete object) or referring to something the prior title established?
- If a title says "they" / "those" / "the firms" / "the policies" — find the antecedent in the previous title or two. If you can't, rewrite.

**Worked example — fail vs pass:**

| Failed sequence (each individually clear, paragraph fails) | Passes spoken-prose test |
|---|---|
| Twenty-eight UAE business leaders gave the same answer. | We asked twenty-eight UAE business leaders what's working and what isn't. |
| They support the strategy. They say the policies are now hurting them. | They told us the country's strategy is sound — but its policies are now hurting them. |
| The Golden Visa is raising rents faster than wages. | The Golden Visa is pushing rents above what salaries can pay. |
| Junior salaries cannot pay one-bedroom rent. | A junior employee can no longer afford a one-bedroom apartment. |
| High rents and Golden Visa policy are one problem, not two. | So the cost crisis and the Golden Visa are one problem, not two. |

Read both columns aloud as paragraphs. The left is a list. The right is a story.

### The narrative-flow exception to 4–10 words

The 4–10 word rule keeps titles tight, but tight titles often can't carry the connective tissue a narrative needs ("So…", "They told us that…", "What stalls their investment is…"). For a narrative deck where titles must read as spoken prose, **stretch up to 15 words when context demands it**. Past 15, the title has become two beats — split it.

The hierarchy when the rules conflict:
1. **Clarity to a stranger** (the opaque-title rule below)
2. **Chains in spoken prose** (the spoken-prose test, this section)
3. **Short** (the 4–10 word default)

When 1 and 2 require length, length wins.

### The opaque title (clarity rule)

A title can be short, active, and specific — and still be opaque. This is the most common failure on technical or expert source material: the model leans into the source's compressed shorthand and produces titles that the source's author would recognise but a stranger would not.

> **The stranger test.** A smart reader who has not read the source must be able to tell what the slide is about from the title alone. If they would ask "what does that mean?" — the title fails.

The rule: **plain over clever**. Technical compression, metaphorical shorthand, and verbless noun-stacks all read as smart writing inside the source but as opaque jargon outside it. Cut them.

**Rewrite examples:**

| Opaque (compressed source-voice) | Plain (passes stranger test) |
|---|---|
| "Golden Visa thresholds lift the rent floor." | "The Golden Visa is pushing rents higher." |
| "Regulatory ambiguity, not burden, defers the capex." | "Unclear rules — not strict ones — are blocking investment." |
| "The cost crisis is the Golden Visa, viewed from the other side." | "Rents and the Golden Visa are one problem, not two." |
| "Operation 300bn cannot survive procurement bias toward offshore." | "Current procurement rules favour offshore work over local delivery." |
| "Variable cost base bends; fixed cost base breaks." | "Firms that can cut costs quickly survive the shock." |

**Common opacity patterns to scan for:**

- **Compound nouns acting as adjectives.** "Receivables cycles squeeze SME liquidity" reads as policy-paper shorthand. Rewrite with verbs: "Late payments are draining small-business cash."
- **Metaphors without anchors.** "The window is open" only works if a prior title established what window. Standalone, it's empty.
- **Initialisms and inside-baseball terms.** "ICV," "capex," "BPO," "OOH" — if the audience is the source's specialist community, OK. If broader, expand or replace.
- **Meta-language that comments instead of advancing.** "Viewed from the other side," "the same problem," "the unintended cost" — these comment on the argument instead of making it. Replace with the actual argument.

**The flat test (use this in addition to the read-aloud test):** Restate the title in the dullest possible language. If the flat version is generic, the original was empty. If the flat version is clearer than the polished one, you over-compressed — rewrite to plain.

| Title | Flat version | Verdict |
|---|---|---|
| "Golden Visa thresholds lift the rent floor." | "Visa rules push rents up." | Flat is clearer → rewrite to plain. |
| "Junior salaries cannot pay one-bedroom rent." | "Junior staff cannot afford rent." | Polished is clearer and concrete → keep. |
| "Back-office automation is the next decade's prize." | "Automating boring office work is the next opportunity." | Polished holds → keep. |

## Rewrite examples across genres

### Research summary

Label-titled original:
1. Background
2. Research Question
3. Methodology
4. Results: Quantitative
5. Results: Qualitative
6. Discussion
7. Conclusion

Action-titled rewrite:
1. Remote teams looked productive on paper.
2. But retention was quietly collapsing.
3. We asked 240 engineers what was wrong.
4. The numbers said hours; the interviews said belonging.
5. People weren't burned out — they were lonely.
6. Belonging predicted retention better than compensation did.
7. Rebuild the team, or lose the talent.

### Business pitch

Original:
1. Company Overview
2. The Market
3. The Problem
4. Our Solution
5. Traction
6. Team
7. Ask

Rewrite:
1. Small clinics handle 60% of US care.
2. Their billing software is twenty years behind.
3. Every missed claim costs a clinic $400.
4. We catch the misses before they're filed.
5. Forty clinics signed; none have churned.
6. We've built billing software for a decade.
7. Two million dollars takes us to a hundred clinics.

### Personal essay or talk

Original:
1. Introduction
2. My background
3. The turning point
4. What I learned
5. Closing

Rewrite:
1. I built my identity around being the smartest person at every meeting.
2. Then the rooms got bigger and I wasn't.
3. I quit the job I'd planned my life around.
4. The wreckage taught me what the achievement never could.
5. The smartest move is to stop measuring.

### Technical postmortem

Original:
1. Incident summary
2. Timeline
3. Root cause
4. Impact
5. Action items

Rewrite:
1. The checkout API died for forty-three minutes on Tuesday.
2. A routine deploy pushed a config change to the wrong cluster.
3. Our health checks were green the whole time.
4. We lost an estimated $180k and three enterprise customers' trust.
5. Health checks now verify behavior, not just response codes.

## The read-aloud test

The single most useful diagnostic: read your title sequence aloud as if it were a paragraph. Don't pause between titles; don't add filler. If it sounds like a story being told, you're done. If it sounds like a table of contents, rewrite.

When unsure between two candidate titles, pick the one a friend would more likely repeat back to you the next day.

## Keynote mode — connected fragments, complete argument

**The headline-chain test governs the entire deck in both modes.** Keynote changes the visual and grammatical register, not the requirement that the headline sequence alone communicate the complete argument.

Fragments, clauses and questions are valid when their meaning connects to the preceding and following headlines. Each headline introduces a necessary premise, adds evidence, preserves a qualification, draws an implication or lands the ask. One-word beats are allowed only if the sequence remains understandable without narration. There is no quota rationing complete sentences; use one whenever the argument needs it.

Read every headline in order before looking at bodies, images or narration. Do not supply imagined bridge sentences. A listener should be able to recover the point, the reasoning and the conclusion from that sequence alone. Pronouns and ellipses need recoverable antecedents. Evidence qualifications must survive in the headlines when necessary to avoid overstating the argument.

**Pass — connected fragments:**
1. Twenty satisfied volunteers.
2. But no proof of productivity.
3. Measure first. Then expand.

**Fail — labels whose reasoning exists only in narration:**
1. The pilot.
2. The gap.
3. What's next?

Even a perfect spoken script cannot make the second headline chain pass. Rewrite the headlines first. Written narration remains required for Keynote delivery review, but it elaborates the already-readable argument. A chained-caption climax is an optional rhetorical device, not the only part of a Keynote that must connect.

Keep source qualifications, plain language and forward movement. The distinction is grammatical completeness of each headline versus argumentative completeness of the sequence: the former can vary; the latter cannot.
