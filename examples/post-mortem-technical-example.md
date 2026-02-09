# Example Workflow: Authentication System Post-Mortem

This example shows the Narrative Engine workflow applied to a post-mortem analysis of a major authentication outage, demonstrating the **Columbo** framework, **Investigator** voice, **Startling Statistic** opening, and **The Simple Truth** closing. Compare with the [climate keynote example](climate-keynote-example.md) (Time Machine + TED Stage) to see how the same system produces a piece that reads, feels, and moves completely differently.

---

## Input

**User:** [Pastes 4,100-word incident report about a 14-hour authentication outage that affected 2.3 million users. The report includes timeline data, root cause analysis (a race condition in the token refresh service triggered by a routine database migration), affected services, remediation steps taken, and a list of follow-up action items. The original report is thorough but written in standard incident response format — chronological, dry, blame-avoidant.]

---

## Phase 1.5: Output Format

**Claude:**
> **What format do you need?**
> 1. **Presentation** — Slide deck with headlines, spotlights, and design notes
> 2. **Prose** — Long-form document with sections, transitions, and flow
> 3. **Both** — Build one, derive the other (specify which first)

**User:** 1 — Presentation. This is going to the engineering all-hands.

---

## Phase 1.75: Focal Discovery

**Claude:**
> I've reviewed your incident report on the authentication outage. Based on the content, I see these potential focal points:
>
> 1. **The hidden coupling:** The outage wasn't caused by the migration or the token service independently — it was caused by a coupling between them that nobody mapped. The real lesson is about invisible dependencies.
> 2. **The 9-minute gap:** There was a 9-minute window between the first anomalous log entry and the migration completing where an alert could have caught this. Understanding why it didn't is the actionable finding.
> 3. **The cascading trust failure:** When the auth service went down, 14 downstream services failed in sequence because none had independent fallback authentication — revealing a single point of failure that was documented as "resilient."
>
> Which direction should we optimize for? Or is there a different point you want to land?

**User:** 1 — the hidden coupling angle. That's the systemic lesson.

**Claude:**
> Got it. Our focal statement: **"The 14-hour outage wasn't caused by a database migration or a race condition — it was caused by an invisible coupling between two systems that passed every review we had. Until we map the dependencies we can't see, we're one routine change away from the next one."**
>
> The One Thing: Our review processes don't catch invisible couplings.
> The Ask: Invest in dependency mapping and coupling detection before the next migration.
> The Through-Line: What you can't see can break you — tracing the invisible thread from cause to collapse.

---

## Phase 2: Discovery Questions

**Claude:**
> **Who is your audience?**
> 1. Executive / Board
> 2. Technical / Engineering
> 3. Sales / Marketing
> 4. Investors / VCs
> 5. General Public / Keynote
> 6. Skeptics / Resisters
> 7. Mixed / Cross-functional
> 8. Academic / Research

**User:** 2 — Technical / Engineering

**Claude:**
> **What are you trying to accomplish?**
> 1. Persuade to act
> 2. Inform / Educate
> 3. Inspire / Motivate
> 4. Align / Build consensus
> 5. Report / Update
> 6. Defend / Justify
> 7. Entertain / Engage

**User:** 2 and 6 — both. Educate on what happened, and justify the remediation investment we're requesting.

**Claude:**
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

**User:** 6

**Claude:**
> **What tone or attitude do you want?**
> 1. Authoritative / Expert
> 2. Provocative / Challenging
> 3. Warm / Relatable
> 4. Urgent / Action-oriented
> 5. Balanced / Objective
> 6. Visionary / Aspirational
> 7. Playful / Creative

**User:** 1 — Authoritative. No sugarcoating but no blame either.

---

## Phase 2.5: Density Mode

**Claude:**
> **How concentrated should this deck be?**
>
> 1. **High-Impact** — Maximum compression. One punch per slide. For pitches and time-constrained execs.
> 2. **Narrative** — Room to breathe. Story beats get space to land. Emotional builds allowed.
> 3. **Evidence** — Denser supporting material. Multiple proof points per section. For skeptics and due diligence.
> 4. **ELI5** — Maximum accessibility. Simple words, concrete analogies, zero jargon.

**User:** 3 — Evidence. Engineers will want the details.

---

## Phase 3: Framework Recommendation — Full Sweep

**Claude:**
> Based on your inputs:
> - Technical / Engineering audience
> - Inform / Educate + Defend / Justify purpose
> - Post-mortem / retrospective
> - Authoritative / Expert tone
> - Evidence density
>
> ### Step 1: Full Arc Scoring
>
> | Arc | Fit (1-5) | Key reason |
> |-----|-----------|------------|
> | A) Prestige | 3 | The "hidden coupling" reveal has Turn potential, but post-mortem audiences expect outcome-first, not suspense |
> | B) Mystery Box | 3 | Could frame the root cause as a puzzle, but engineers want the answer before the investigation — not after |
> | C) Heist | 1 | Goal-obstacles-crew is the wrong shape entirely for a retrospective |
> | D) Time Machine | 2 | No meaningful future fork — this is about understanding the past, not choosing a future |
> | E) Trojan Horse | 3 | Could reframe "we had a migration failure" → "we have a dependency visibility failure" — but the revelation is better served by evidence accumulation than escalation-to-reframe |
> | F) Hero's Journey | 2 | Transformation narratives feel self-congratulatory in post-mortems |
> | G) Freytag | 3 | The dramatic arc could work for the incident timeline, but Freytag's climax-and-catharsis shape risks making a systems failure feel like entertainment |
> | H) Columbo | 5 | Perfect — outcome-first ("here's what happened"), then methodical reconstruction of the mechanism, telltale detail (the 9-minute gap), and how/why reveal. This is exactly how engineers want to process a post-mortem |
> | I) Game of Scene | 3 | Could name the "invisible coupling" as a game/pattern that appears across systems — interesting but too abstract for a post-mortem where people want specifics |
> | J) Rashomon | 3 | Multiple views (infra team, app team, SRE team) could work, but the goal is synthesis, not perspective exploration |
>
> ### Step 2: Top Communication Frameworks
>
> | Framework | Fit (1-5) | Key reason |
> |-----------|-----------|------------|
> | Pyramid (answer-first) | 4 | Engineers expect the conclusion first — Columbo already provides this via the Cold Open Outcome |
> | Story Spine | 3 | Causal chain structure overlays well on Columbo's mechanism steps |
> | Hopkins Specificity | 4 | Post-mortems live or die on specifics — exact timestamps, exact error codes, exact sequence |
> | SCQA | 3 | Situation-Complication-Question-Answer maps to the post-mortem shape |
> | Cognitive Load | 3 | Useful for chunking the mechanism steps so engineers can follow |
>
> ---
>
> ## Recommendation 1: Columbo + Hopkins Specificity ★★★★★
>
> **Why this works:** Columbo is the natural shape for post-mortems — state the outcome, then reconstruct how it happened, with the real insight arriving through the Telltale Detail (the 9-minute gap) and the How/Why Reveal (invisible coupling). Hopkins Specificity ensures every claim is anchored in exact data — timestamps, error codes, request counts — which is how this audience builds trust.
>
> **Your content in this structure:**
> 1. **Cold Open Outcome:** "On March 14 at 02:17 UTC, authentication failed for 2.3 million users across 14 services. The outage lasted 14 hours. Here's what actually caused it — and it wasn't the migration."
> 2. **Baseline Theory:** "The initial assumption: the database migration corrupted token state."
> 3. **Mechanism Step 1:** The migration itself — what it changed, what it didn't
> 4. **Mechanism Step 2:** The token refresh service — how it handles concurrent requests
> 5. **Mechanism Step 3:** The race condition — how migration timing intersected with refresh cycles
> 6. **Red Herrings:** Database corruption hypothesis, load spike hypothesis
> 7. **Telltale Detail:** The 9-minute gap — one anomalous log entry that nobody flagged
> 8. **How/Why Reveal:** The invisible coupling — the migration and refresh service shared an undocumented dependency on row-lock ordering
> 9. **Re-read Evidence:** Earlier mechanism steps now make sense through the coupling lens
> 10. **Transfer:** Where else this pattern of invisible coupling exists in our systems
> 11. **Playbook:** Dependency mapping investment and coupling detection tooling
> 12. **Callback:** "The outage lasted 14 hours. The coupling had existed for three years."
>
> **Emotional preview:** Satisfaction (outcome known) → methodical engagement → false confidence in baseline theory → surprise at telltale detail → deeper understanding → competence
>
> **Tradeoffs:**
> - Strength: Engineers will trust this because it shows its work — every step of the reconstruction is visible
> - Strength: The Telltale Detail beat gives the 9-minute gap its proper dramatic weight without being theatrical
> - Risk: At Evidence density, the mechanism steps could become verbose — keep each step to 2-3 slides maximum
>
> ## Recommendation 2: Trojan Horse + SCQA ★★★
>
> **Why this works:** Reframes the audience's mental model from "migration failure" to "coupling failure." Could be powerful for changing how the team thinks about reviews.
>
> **Tradeoffs:**
> - Strength: Creates a lasting mental model shift
> - Risk: Trojan Horse's escalation structure can feel manipulative to engineers — they'd rather see the evidence and draw their own conclusions
>
> ## Dark Horse: Game of the Scene ★★★
>
> **Why this is interesting:** What if you named the pattern? "Invisible coupling" isn't just what caused this outage — it's a recurring pattern across your infrastructure. The Game of the Scene structure would let you show this outage as one instance of a broader game: heighten across the auth system, then the deployment pipeline, then the monitoring stack. The Name-the-Game beat — "Every system we call 'decoupled' shares at least one undocumented dependency" — could become the most memorable takeaway of the whole post-mortem.
>
> **What it would unlock:** A shift from "here's what broke" to "here's the pattern that keeps breaking things, and this is its name." Engineers love named patterns.
>
> ## Rejection Log
>
> Heist (1) structures around goals and execution — wrong shape for looking backward. Hero's Journey (2) risks making a system failure feel like a triumph narrative. Time Machine (2) is forward-looking by design, and this content is about understanding the past. Mystery Box (3) withholds the answer too long for an audience that expects outcome-first.

**User:** 1 — Columbo. The engineers will respect the evidence-first approach.

---

## Phase 3.5: Build Brief

**Claude:**
> ### Build Brief
>
> **Focal Statement:** The 14-hour outage wasn't caused by a database migration or a race condition — it was caused by an invisible coupling between two systems that passed every review we had. Until we map the dependencies we can't see, we're one routine change away from the next one.
>
> **Framework:** Columbo (H) + Hopkins Specificity overlay
> **Density:** Evidence
>
> **Voice Profile:** Investigator (auto-derived: Technical + Authoritative)
> - Measured, mid-length sentences (10-20 words). Evidence chains where each sentence adds one new fact.
> - Precise, specific language. Name the date, the document, the error code, the timestamp.
> - Investigative verbs: "reveals," "suggests," "traces back to," "contradicts."
> - Avoid emotional language — let the facts generate the feeling.
> - Signature moves to deploy: The Breadcrumb Trail (evidence accumulating toward pattern), The Quiet Reveal (most important finding in most understated language), The "Notice Something" Beat (pause for audience to examine evidence)
>
> **Audience Profile:** Technical / Engineering
> - Trust signals: Show methodology. Explain error margins. Name tools, frameworks, and versions. Acknowledge limitations before the audience finds them.
> - Resistance triggers to avoid: Hand-waving, business buzzwords, benchmarks without conditions, oversimplification, appeals to authority without underlying data
> - Evidence style: Reproducible evidence. Architecture diagrams. Failure cases. Comparative tables with quantified trade-offs.
> - Headline style: Name the mechanism or finding. Include technical specifics. No marketing-style superlatives.
>
> **Emotional Arc:** Columbo emotional texture
> - Shape: Satisfaction (answer known) → curiosity (how?) → methodical engagement → false confidence → surprise → deeper understanding → competence
> - Intensity dial: 1-2 (Technical — restrained. Intellectual curiosity and the satisfaction of elegant analysis. No hype.)
> - Key emotional moment: Beat 7 — the Telltale Detail. Small and specific. The 9-minute gap between the first anomalous log entry and migration completion. Deliver it quietly. Set it apart. Let the audience feel the "oh..." before explaining its significance.
>
> **Persuasion Strategy:**
> - Primary: Authority — demonstrate deep technical understanding. Show the work.
> - Secondary: Commitment/Consistency — build from principles engineers already accept (loose coupling, defense in depth, observability) to the conclusion that current tooling doesn't enforce them.
>
> **Opening Strategy:** Startling Statistic — Lead with the number that violates expectations. "2.3 million users. Fourteen hours. Root cause: one undocumented dependency." Combined with Columbo's Cold Open Outcome beat.
>
> **Closing Strategy:** The Simple Truth — After all the evidence, strip it to one sentence. Combined with Columbo's Callback beat. "We didn't have a migration failure. We had a visibility failure."
>
> **Killer Line Candidates:**
> 1. "We didn't have a migration failure. We had a visibility failure."
> 2. "The coupling had existed for three years. It took 14 hours to find."
> 3. "Every system we call 'decoupled' shares at least one dependency we haven't mapped."
>
> **Anti-Sameness Notes:** Post-mortem decks tend to follow a predictable incident-timeline-remediation format. This Columbo structure will feel different — it opens with the outcome, then reconstructs the mechanism like a detective case. Lean into the investigative feel. The Telltale Detail (9-minute gap) should be the slide that engineers talk about in the hallway afterward. Avoid corporate blamelessness language ("learnings," "opportunities for improvement") — use plain, direct language about what broke and why.
>
> ---
>
> Here's the Build Brief I'll use to guide the output. Anything you'd change before I build?

**User:** The first killer line candidate is the one. Build it.

---

## Phase 4: Build (Abbreviated — 4 Slides Shown)

**Claude generates deck guided by Build Brief:**

```markdown
# The Invisible Thread: Auth Outage Post-Mortem

**Framework:** Columbo (H) + Hopkins Specificity
**Density:** Evidence
**Focal Statement:** The 14-hour outage was caused by an invisible coupling between the token refresh service and the user-sessions database — a dependency that passed every review for three years.
**Metaphor family:** Visibility/blindness (threads, maps, dark spots, blind spots)
**Voice:** Investigator
**Emotional arc:** Satisfaction → methodical engagement → false confidence → surprise → understanding → competence
**Opening strategy:** Startling Statistic
**Closing strategy:** The Simple Truth
**Killer Line:** "We didn't have a migration failure. We had a visibility failure."

---

## Slide 1 — Cold Open Outcome (Beat 1)
**Headline:** 2.3 million users locked out for 14 hours — root cause: one undocumented dependency

**Spotlight (≤60 words):** On March 14 at 02:17 UTC, the authentication service began returning 401 errors across all endpoints. Within 11 minutes, 14 downstream services entered degraded state. Full resolution came at 16:42 UTC. The initial incident review attributed the failure to the scheduled database migration. That attribution was incorrect. The actual mechanism is more instructive — and more concerning.

**Design note:** Black background. White text. The three numbers stacked vertically: 2.3M / 14h / 1. Stark. No decoration. Let the contrast between the massive impact and the singular cause do the visual work.

**Source:** [DIRECT]

---

## Slide 2 — Baseline Theory (Beat 2)
**Headline:** The first assumption was reasonable: the migration corrupted token state

**Spotlight (≤60 words):** Within two hours of the outage, the incident team identified that the user-sessions database migration had been running during the failure window. The migration altered the sessions table schema — adding a `last_verified_at` column with a NOT NULL constraint. The correlation was obvious. Five of six on-call engineers surveyed afterward said their first hypothesis was schema-related corruption. The hypothesis was wrong.

**Design note:** Architecture diagram showing the database migration touching the sessions table. A red "X" that the audience will later learn was misplaced. Build the visual so it can be re-shown in the Re-read Evidence phase with the X moved to the actual failure point.

**Source:** [PARAPHRASE]

---

## Slide 3 — Mechanism Step 1 (Beat 3)
**Headline:** The migration itself completed without error in 4 minutes and 12 seconds

**Spotlight (≤60 words):** Migration logs show clean execution. Schema change applied at 02:14:33 UTC. Column added, backfill completed across 847,000 rows, constraints applied. Zero write failures. Zero lock escalations. The migration was tested in staging three times; production execution matched staging to within 8 seconds. By every measure the infrastructure team tracks, this migration was unremarkable.

**Design note:** Migration log excerpt — actual timestamps, actual status codes. Monospace font. Green checkmarks next to each step. The visual should communicate "everything looks fine" — because that is the point.

**Source:** [DIRECT]

---

## Slide 4 — Telltale Detail (Beat 7)
**Headline:** At 02:18:41 UTC, one log entry appeared that nobody was watching

**Spotlight (≤60 words):** Nine minutes after the migration started, the token refresh service logged a single warning: `WARN: row lock acquisition exceeded 200ms threshold on sessions.user_id index (actual: 2,847ms)`. The warning fired once. It was not configured to trigger an alert. It was not part of the migration runbook's monitoring checklist. It was the first visible symptom of a dependency that had never been documented — and the only signal that could have prevented the next 14 hours.

**Design note:** A single log line on a dark terminal background. The timestamp highlighted. The rest of the slide empty. One line. One clue. This is the "Notice Something" beat — give it visual weight by giving it visual space.

**Source:** [ELABORATED]

---

[Slides 5-13 continue with Mechanism Steps 2-3, Red Herrings, How/Why Reveal (the row-lock ordering dependency), Re-read Evidence, Transfer to other systems, Limits, Playbook with investment request, and Callback...]

---

## Sourcing Summary

**Originality Score:** 78% user-sourced / 22% generated

- Direct from source: 5 slides
- Paraphrased: 4 slides
- Elaborated: 3 slides
- Generated: 1 slide (transfer/framing)
```

---

## Phase 4.5: Originality Check (Internal)

Before sending to Review Panel, the Originality & Anti-Sameness checklist is run:

- [x] Opening uses Startling Statistic strategy, not generic framework Cold Open
- [x] Closing uses The Simple Truth strategy, combined with Callback beat
- [x] Headline structure variety: declarative (Slide 1), declarative (Slide 2), declarative (Slide 3), temporal/scene-setting (Slide 4) — three consecutive declaratives. **FLAG.** Slide 2 headline restructured.
- [x] Voice profile check: Investigator verified — measured sentences, specific timestamps and codes, investigative verbs ("attributed," "hypothesis," "symptom"), emotional restraint, Breadcrumb Trail signature move building across mechanism steps
- [x] Killer Line placed at Callback (closing beat): "We didn't have a migration failure. We had a visibility failure."
- [x] AI Test: Opening does NOT use "In today's complex infrastructure landscape..." — it opens with specific numbers and a contradiction

**Revision made:** Slide 2 headline changed from "The first hypothesis: the migration corrupted token state" to "The first assumption was reasonable: the migration corrupted token state" — the word "reasonable" does crucial work for the Investigator voice (it acknowledges the hypothesis without dismissing it, which builds trust with engineers who made that same assumption).

---

## Phase 5: Review Panel (Abbreviated)

**Claude:**
> ## Review Panel Synthesis
>
> ### Strengths
> - The Investigator voice is consistent and well-calibrated for engineers — precise language, no hype, evidence-first. The contrast with how this would sound in TED Stage voice is night and day. — *Originality Agent*
> - The Telltale Detail slide (the single log entry) is the strongest beat in the deck. The visual design of one log line on a dark background will be the image engineers remember. — *Visual Designer*
> - Source attribution is strong — 78% user-sourced gives high credibility with a technical audience that will fact-check internally. — *Content Expert*
> - Evidence density is appropriate — mechanism steps show actual timestamps, row counts, and error codes. This audience will trust it. — *Audience Advocate*
>
> ### Recommended Changes
>
> **Messaging**
> - The Playbook section (not shown in abbreviated output) should include a cost estimate for the dependency mapping tooling. Engineers accept investments when the cost is specific: "$340K and 3 engineering-months" beats "meaningful investment." — *Audience Advocate*
>
> **Originality**
> - The deck metaphor family is "visibility/blindness" — strong fit. However, "blind spot" appears in two separate slide spotlights. Replace one instance with a different metaphor from the same family: "dark spot on the dependency map" maintains the family without repetition. — *Originality Agent*
>
> **Technical Accuracy**
> - Slide 3: Verify that "847,000 rows" matches the actual incident data. If approximate, state it as "approximately 850K rows" — engineers notice when specificity implies precision that doesn't exist. — *Content Expert*
>
> **Emotional Arc**
> - The transition from the Telltale Detail (Beat 7) to the How/Why Reveal (Beat 8) should include a "Notice Something" pause. Consider a transition slide with just: "That 2,847ms lock wait. Think about what it means." Give the audience one beat to arrive at the conclusion before you state it. The Investigator voice earns its power by letting the audience be detectives too. — *Comms Specialist*
>
> ### Originality Agent — Detailed Findings
>
> **Flagged:**
> 1. "Blind spot" used twice in separate spotlights — violates metaphor variety within the visibility/blindness family. **Fix: Replace one instance with "dark spot on the dependency map."**
> 2. The Re-read Evidence section (not shown) uses the phrase "in hindsight" — this is a generic post-mortem word. Replace with something more precise: "viewed through the coupling lens" maintains the Investigator voice and the visibility metaphor.
>
> **Passed:**
> - Voice consistency: Investigator voice is maintained throughout — every slide checked shows measured sentences, precise timestamps, evidence-accumulation rhythm, emotional restraint
> - Build Brief adherence: The Brief specified "no corporate blamelessness language" — confirmed zero instances of "learnings," "opportunities for improvement," or "going forward"
> - Headline variety: After the Slide 2 revision, headline structures now vary (declarative, evaluative, declarative, temporal)
> - The Simple Truth closing ("We didn't have a migration failure. We had a visibility failure.") earns its weight because the preceding 12 slides built the evidence that makes this sentence true. Without the build, it would be a platitude. After the build, it's a verdict.
>
> ### Overall Assessment
> **Ready to present?** Yes with minor edits
> **Most important improvement:** Add the "Notice Something" transition before the How/Why Reveal — it's the difference between an Investigator delivering a verdict and an Investigator letting the room solve the case together.

---

## What This Example Demonstrates

### The Voice Difference

Read Slide 1 of this example and Slide 1 of the [climate keynote](climate-keynote-example.md) back to back.

**Climate keynote (TED Stage voice):**
> "It's 2031 and the air above a cement plant in Gujarat smells like rain."

**Post-mortem (Investigator voice):**
> "2.3 million users locked out for 14 hours — root cause: one undocumented dependency."

Same system. Same Phase 4 build process. Completely different output. The TED Stage voice opens with a sensory scene, uses present tense, invites you into a world. The Investigator voice opens with three data points and a contradiction, uses past tense, and hands you a case file.

This is what the voice profiles, audience profiles, and Build Brief accomplish: they ensure that the discovery answers (audience, tone, purpose) propagate all the way into the actual sentences, not just the framework selection.

### The Emotional Arc Difference

The climate keynote runs at intensity 4-5. Full emotional range: wonder, vertigo, fork anxiety, agency, resolve. The audience is meant to *feel* something at every beat.

This post-mortem runs at intensity 1-2. The emotional register is intellectual curiosity and the quiet satisfaction of understanding a mechanism. The Telltale Detail creates a single moment of genuine surprise (the log entry nobody watched), and the Investigator voice handles it with restraint — no "shocking discovery," just the fact, sitting there, doing its work. The audience should feel a growing "wait, really?" as evidence accumulates, but the prose never tells them to feel it.

### The Opening/Closing Strategy Difference

| | Climate Keynote | Post-Mortem |
|---|---|---|
| **Opening** | Future Projection — "It's 2031 and..." | Startling Statistic — "2.3M users. 14 hours. 1 dependency." |
| **Closing** | Future Vision — vivid picture of chosen future | The Simple Truth — "We didn't have a migration failure. We had a visibility failure." |
| **Emotional shape** | Expansive → contracted → expansive | Compressed → expanded → compressed |

The keynote opens wide (a scene) and closes wide (a vision). The post-mortem opens tight (three numbers) and closes tight (one sentence). Both are effective. Neither would work for the other's audience.

### The Originality Agent in Action

In the keynote example, the Originality Agent flagged a TED-talk cliche ("Here's the number that should rewrite how you think"). In this post-mortem, it flagged metaphor repetition ("blind spot" used twice) and a generic post-mortem word ("in hindsight"). Different content types have different sameness risks — the Agent adapts its checks to the genre.

### Key System Features Demonstrated

1. **Full Sweep Protocol:** Columbo scored 5 for a post-mortem; Time Machine scored 5 for a vision piece. The same scoring process produced different winners because the inputs were different — not because of a heuristic shortcut.

2. **Build Brief as binding contract:** Every element of the Build Brief (Investigator voice, Technical audience profile, intensity 1-2, Startling Statistic opening, The Simple Truth closing) is visible in the output. The Build Brief didn't just describe intent — it constrained and shaped execution.

3. **Evidence density calibrated to audience:** The keynote uses "enough to fill a football stadium" comparisons. This post-mortem uses "847,000 rows" and "02:18:41 UTC." Same system, different audience profile instructions.

4. **Framework + opening/closing strategy combination:** Columbo's Cold Open Outcome beat (structural requirement: state the result) was delivered through a Startling Statistic (rhetorical approach: the number that stops the room). The framework said *what* the opening must accomplish; the strategy said *how* to accomplish it.
