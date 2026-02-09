# Audience Profiles — Writing Instructions by Audience Type

Reference file for the Narrative Engine Build phase (Phase 4). When writing for a selected audience, load the matching profile and follow its directives throughout content generation — headlines, spotlights, prose paragraphs, CTAs, and review panel calibration.

These are **instructions to the writer**, not descriptions of the audience. Follow them as rules.

---

## 1. Executive / Board

### Mental model

Lead every section with the conclusion. State the answer, then provide supporting evidence — never the reverse. Use deductive structure: claim first, proof second, implication third. Executives scan for the "so what" in the first sentence of every section; if it isn't there, they stop reading. Organize supporting points as MECE buckets (mutually exclusive, collectively exhaustive). Never make the reader work to find your point.

### Trust signals

Anchor every claim with a number — revenue, margin, timeline, headcount, cost. Cite named companies or named competitors, not "industry sources." Reference board-level concerns (fiduciary duty, shareholder value, risk exposure) explicitly. Use frameworks the audience already trusts: ROI calculations, payback periods, TAM/SAM/SOM. If you must cite research, name the firm (McKinsey, Gartner, BCG) — not the study title.

### Resistance triggers

Never bury the lead. Do not build suspense or use slow narrative ramps — the reader will disengage before the payoff. Avoid jargon from disciplines outside business (no neuroscience metaphors, no software engineering terms unless the company is a software company). Never present information without a recommendation. Do not hedge excessively — state your position, then acknowledge risks as a separate item.

### Evidence style

Use financial metrics, competitive benchmarks, and named case studies. Prefer "Company X achieved Y in Z months" over abstract statistics. Show before/after comparisons with dollar values. Include a risk/mitigation table for any significant recommendation. One strong case study beats five weak data points.

### Language register

Write short declarative sentences. Average sentence length: 10-15 words. Use business-standard vocabulary — no slang, no academic prose, no flowery language. Formality level: boardroom memo. Use "we" for the company, "the board" or "you" for the audience. Eliminate qualifiers: replace "somewhat significant" with "significant" or cut it.

### Emotional range

Use controlled urgency — competitive threat, market window closing, cost of delay. Invoke ambition sparingly: "market leadership," "category definition." Never use fear-mongering or hype. Avoid inspirational language — replace "imagine a world where" with "by Q3, we will." Confidence is the dominant register; vulnerability has no place here.

### What they quote

They will repeat the single metric that justifies the decision: "47% margin improvement in 9 months." They will also repeat the one-line recommendation. Write both to be quotable in a hallway conversation — short enough to say in one breath, specific enough to act on.

### Persuasion priorities

**Authority** — Cite credible sources and show command of the data. **Scarcity** — Emphasize the closing window, the competitive threat, the cost of delay. **Commitment/Consistency** — Connect the recommendation to decisions the board has already made ("This extends the strategy we approved in Q2").

### Headline style

Write headlines as declarative verdicts. Subject-verb-object, active voice. Include one number or named entity per headline. Never use questions as headlines. Never use metaphors as headlines. Examples: "Cloud migration cuts infrastructure costs 34% by Q4." "Three acquisitions close our distribution gap in APAC."

### CTA style

Hard ask. One specific action, one owner, one deadline. "Approve $2.4M for Phase 1 by March 15." Never use "consider" or "explore" — use "approve," "fund," "authorize," "direct." Include the cost of inaction as a single line beneath the ask.

---

## 2. Technical / Engineering

### Mental model

Present the mechanism before the outcome. Engineers process bottom-up: they want to understand HOW before they accept WHAT. Structure arguments inductively — evidence accumulates toward a conclusion rather than descending from one. Show your work. Include the reasoning chain, not just the final answer. When presenting a system or architecture, start with components and build to the whole.

### Trust signals

Show methodology. Explain sample sizes, error margins, and edge cases. Reference RFCs, published benchmarks, peer-reviewed papers, or open-source implementations. Name the tools, frameworks, and versions used. Accuracy and reproducibility signal credibility — polish and branding do not. Acknowledge limitations before the audience finds them; this builds trust faster than any credential.

### Resistance triggers

Never hand-wave. If you skip a step in reasoning, they will distrust the entire chain. Do not use business buzzwords ("synergy," "leverage," "disruptive") — each one costs you credibility. Never present benchmarks without stating the conditions under which they were measured. Do not oversimplify to the point of inaccuracy. Do not appeal to authority without showing the underlying data — "Gartner says" is insufficient; show what Gartner measured.

### Evidence style

Use benchmarks with stated methodology. Show code snippets, architecture diagrams, or data tables when relevant. Prefer reproducible evidence: "Run this query and you'll see X" over "We observed X." Include failure cases and edge cases — what doesn't work is as informative as what does. Comparative tables (Option A vs. Option B vs. Option C) with quantified trade-offs are the most trusted format.

### Language register

Use precise technical vocabulary appropriate to the domain — do not simplify terms the audience already knows. Sentence length can vary; compound sentences are acceptable when describing causal chains. Formality: technical blog post, not academic paper and not marketing copy. Use "you" or imperative voice for instructions; use passive voice only when the actor is genuinely irrelevant. Define acronyms on first use even if common — it signals rigor.

### Emotional range

Use intellectual curiosity and the satisfaction of elegant solutions. Phrases like "Here's what's interesting" or "This is where it gets non-obvious" work. Humor is welcome if dry and domain-relevant. Never use hype ("revolutionary," "game-changing"). Never appeal to fear of missing out. Do not attempt to inspire — instead, intrigue. The emotional register is "colleague sharing a finding," not "leader rallying troops."

### What they quote

They will repeat the surprising technical finding, the elegant mechanism, or the specific benchmark that challenges a common assumption. They will also quote the limitation you were honest about. Write the key technical insight as a standalone sentence that could be pasted into a Slack channel.

### Persuasion priorities

**Authority** — Demonstrate deep technical understanding; show you've done the work. **Commitment/Consistency** — Build from principles the audience already accepts (DRY, YAGNI, CAP theorem) to your conclusion. **Social proof** — Reference adoption by respected engineering organizations or open-source communities ("Stripe moved to this pattern in 2024").

### Headline style

Write headlines that name the mechanism or finding. Include technical specifics — a protocol, a metric, an architecture pattern. Avoid marketing-style superlatives. Use "how" and "why" constructions when they add clarity. Examples: "Event sourcing eliminates 80% of state reconciliation bugs." "Why connection pooling outperforms per-request auth at 10K+ RPS."

### CTA style

Soft ask framed as a logical next step. "Try it in staging and compare the results." "Review the RFC and comment by Friday." Never demand enthusiasm — request evaluation. Include a link, a command to run, or a document to read. Make the first step zero-friction and reversible.

---

## 3. Sales / Marketing

### Mental model

Lead with the competitive angle — what this means for winning deals, capturing market share, or outpositioning rivals. Sales and marketing audiences process information through a "How does this help me win?" filter. Use inductive structure: start with a vivid customer example or win/loss story, then extract the principle. Move fast — this audience rewards pace and energy over depth.

### Trust signals

Use customer quotes, win/loss data, and competitive intelligence. Name specific deals, accounts, or campaigns — not abstractions. Show before/after pipeline numbers. Reference what top performers are already doing. Social proof from peers and customers is more persuasive than analyst reports. Testimonials from named customers outrank everything else.

### Resistance triggers

Never lead with internal process changes or operational detail — lead with the customer-facing impact. Do not present data without a "so what" for the field. Avoid academic framing or theoretical models unless they directly connect to a pitch script or objection handler. Never suggest that current performance is satisfactory — this audience needs urgency to act. Do not use passive voice; it signals hesitation.

### Evidence style

Use win/loss stories: "We lost Acme Corp because X — here's how we prevent that." Show competitive teardowns: feature-by-feature comparisons with named competitors. Pipeline metrics, conversion rates, and deal velocity are the most compelling numbers. Include customer verbatims — the exact words a buyer used. One vivid customer story outweighs five statistical summaries.

### Language register

Write punchy, energetic prose. Short sentences. Active verbs. Use "you" and "your" frequently — this is direct, second-person communication. Colloquial vocabulary is fine; forced casualness is not. Match the register of a top-performing sales kickoff speaker: confident, direct, slightly competitive. Use the audience's own terminology — ARR, ACV, pipeline, quota, close rate, churn.

### Emotional range

Use competitive energy and urgency freely. "Our competitors are already doing X" is a legitimate motivator. Celebrate wins loudly — name the rep, name the deal, name the number. Use aspirational language: "category-defining," "market-making." Fear of losing to a competitor is acceptable; fear of personal failure is not. The emotional register is "coach at halftime" — energizing, direct, demanding.

### What they quote

They will repeat the competitive sound bite — the one sentence that explains why we win. They will also repeat the customer's exact words. Write the competitive differentiator as a sentence that fits on a battle card. Write the customer quote so it can be dropped into a prospect email.

### Persuasion priorities

**Social proof** — "The top 10% of our reps already use this approach." **Scarcity** — "The market window closes in Q2" or "Competitors launched this last month." **Liking** — Mirror the audience's energy, use "we" language, celebrate shared wins.

### Headline style

Write headlines that create urgency and name the competitive stakes. Use action verbs and specific numbers. Include named competitors or market positions when possible. Questions work here if they're provocative: "Why did we lose 12 enterprise deals to [Competitor] last quarter?" Also effective: "How the top 5% of reps close 3x their quota." Headlines should feel like a subject line you'd actually open.

### CTA style

Hard ask with specific next steps and a deadline. "Update your pitch deck with slide 7 by Monday." "Run this play on your next three discovery calls and report back." Include a template, script, or asset they can use immediately. Make the action feel like a competitive advantage, not a chore.

---

## 4. Investors / VCs

### Mental model

Present the narrative arc: problem, insight, traction, scale. Investors process through pattern matching — they are looking for a shape they recognize (exponential growth, market timing, founder-market fit). Lead with the market opportunity, then prove you can capture it. Structure the argument as a story of momentum: where you started, what you've proven, where you're going, and why now.

### Trust signals

Show traction metrics with clear time axes: MRR growth, cohort retention, unit economics. Name recognizable customers, partners, or investors already involved. Reference market size with a credible bottoms-up calculation, not a top-down TAM fantasy. Show you know the risks — investors trust founders who name the three things that could kill the company and explain their mitigation plan.

### Resistance triggers

Never claim "no competition" — it signals naivety. Do not present projections without stating the assumptions behind them. Avoid vanity metrics (downloads, page views, registered users) unless paired with engagement or revenue metrics. Never use "conservative estimate" — every founder says this and investors discount it. Do not show a hockey stick without explaining the mechanism that creates it.

### Evidence style

Use cohort data, month-over-month growth rates, and unit economics. Show customer logos in a recognizable grid. Reference specific deals in the pipeline with dollar values and stages. Include a "Why now?" slide that ties to a market shift or technology inflection, not just your readiness. One paying customer's story — how they found you, what they pay, why they stay — is more convincing than a TAM slide.

### Language register

Write with confident precision. Avoid superlatives ("best-in-class," "world-class") — let the numbers speak. Vocabulary should be fluent in venture/startup lexicon: burn rate, runway, LTV/CAC, NDR, ARR, blended CAC. Keep sentences tight — 12-18 words average. Formality: pitch meeting, not academic paper and not blog post. Use "we" for the company, never "I" (it signals team, not hero).

### Emotional range

Use controlled ambition — the conviction that this market is big, this team is right, and this timing is perfect. Confidence without arrogance. Show passion for the problem, not just the solution. Vulnerability is acceptable in exactly one place: the honest acknowledgment of risk. Otherwise, the register is "founder who has done the work and sees the path." Never plead; never oversell.

### What they quote

They will repeat the growth metric and the market insight: "They're growing 25% MoM with 140% NDR" and "They saw that [market shift] before anyone else." Write the growth number and the market insight as standalone, quotable sentences that an investor could relay to their partners in a Monday meeting.

### Persuasion priorities

**Authority** — Demonstrate deep domain expertise and market knowledge. **Social proof** — Reference recognizable customers, brand-name co-investors, or advisory board members. **Scarcity** — "This round closes March 1" or "We're allocating the remaining $1.2M to two partners."

### Headline style

Write headlines that combine a metric with a narrative claim. Subject-verb-object with a number and a market position. Examples: "140% net dollar retention proves product-market fit in enterprise." "Three Fortune 100 customers validated our platform in 6 months." Avoid aspirational headlines without proof — every headline must be verifiable from the data in the deck.

### CTA style

Direct but staged. Primary ask: specific investment amount and terms. Secondary ask: follow-up meeting with a specific date. "We're raising $8M Series A at $40M pre. Let's schedule a partner meeting next week." Include a clear deadline for the round. Provide a data room link as the lowest-friction next step.

---

## 5. General Public / Keynote

### Mental model

Start with a concrete, human story — a single person, a vivid moment, a sensory detail. Then zoom out to the principle. This audience processes story-first, concept-second. Use inductive structure throughout: specific example leads to general insight, never the reverse. Return to the specific frequently — every abstraction needs a concrete anchor within two sentences. Think in scenes, not in arguments.

### Trust signals

Use relatable human examples and everyday analogies. Credibility comes from showing you understand the audience's world, not from credentials or data. If you cite research, translate it into a human impact: "That's 1 in 5 families" rather than "20% of households." Named, real stories (with permission or from public record) beat hypotheticals. The trust signal is "this person has thought about what this means for people like me."

### Resistance triggers

Never assume specialized knowledge. Any undefined jargon, acronym, or technical term causes the audience to disconnect. Do not present data tables — translate every number into a human story or physical comparison. Avoid inside-baseball references to any industry. Never lecture or condescend — the register is "discovery together," not "expert explains." Do not go longer than 3 minutes (or 3 paragraphs) without a story, example, or concrete image.

### Evidence style

Use "one person" stories: a named individual whose experience illustrates the point. Use physical scale comparisons: "enough to fill a football stadium," "the weight of 14 blue whales." Use before/after transformations that the audience can visualize. Social proof works when it's "people like you" — neighbors, parents, workers — not executives or experts. Photographs and real images outperform charts.

### Language register

Write at an 8th-grade reading level. Use common words — prefer "use" over "utilize," "start" over "initiate," "show" over "demonstrate." Average sentence length: 10-12 words. Vary rhythm: short punchy sentences alternating with one slightly longer sentence for flow. Use contractions (it's, they're, we've). Use "you" and "we" throughout. Formality: TED Talk — approachable, clear, warm, not dumbed down.

### Emotional range

Full emotional range is available. Use wonder, humor, empathy, righteous urgency, and hope. Build emotional arcs — start with curiosity, move through tension or empathy, resolve with hope or a call to shared action. Humor should be observational, never sarcastic or insider. Vulnerability from the speaker (a personal admission, a moment of doubt) builds connection. The emotional register is "trusted storyteller" — someone who makes you feel something and gives you something to think about.

### What they quote

They will repeat the metaphor, the human story, or the single surprising fact. They will NOT repeat a number unless it's shockingly large or personally relevant. Write one "cocktail party sentence" — the thing someone says to a friend over dinner: "Did you know that [surprising, concrete, human-scale fact]?" Also write one sticky metaphor that reframes the topic.

### Persuasion priorities

**Liking** — Be relatable, warm, self-deprecating where appropriate. Mirror the audience's values and concerns. **Unity** — Create a shared identity: "We all..." or "Every parent knows..." **Reciprocity** — Give the audience something valuable (an insight, a reframe, a tool) before asking for anything.

### Headline style

Write headlines as intriguing promises or vivid images. Use sensory or narrative language. Questions work well if they're questions the audience is already wondering. Avoid data-heavy headlines — use one evocative detail instead. Examples: "The six-word email that changed a thousand families." "What a bus driver in Detroit taught me about resilience." Headlines should make someone lean forward and think "tell me more."

### CTA style

Soft ask or implied. Frame it as an invitation, not a demand. "Next time you see X, try Y." "Share this with one person who needs to hear it." "The next time someone tells you Z, you'll know better." The CTA should feel like a natural outgrowth of the story, not a sudden pivot to salesmanship. If there's a harder ask (donate, sign up, vote), wrap it in the story: "If Maria's story moved you, here's one thing you can do."

---

## 6. Skeptics / Resisters

### Mental model

Acknowledge the opposing position first — accurately and without strawmanning. This audience will not listen to your argument until they hear you articulate theirs. Use a concessive structure: "The case for [their position] is strong: [reasons]. And yet [specific evidence] suggests a different conclusion." Build inductively from the evidence they already accept. Never lead with your thesis — arrive at it as a logical consequence of shared evidence. Every step in the argument must be small enough that they nod before you move to the next.

### Trust signals

Cite sources the skeptic already trusts — not your own research, but independent or even adversarial sources. Acknowledge what you got wrong in the past or what your position gets wrong now. Show intellectual honesty: "The data on X is genuinely mixed — here's what both sides show." Use primary sources (the actual study, the actual dataset) rather than secondhand summaries. The strongest trust signal is conceding a real point to the other side.

### Resistance triggers

Never dismiss their position. Even one sentence that implies "you're wrong and here's why" will lose them permanently. Do not use social proof — "everyone is doing X" makes skeptics dig in harder. Do not appeal to authority unless it's an authority they specifically respect. Avoid enthusiasm and certainty — the more sure you sound, the less they trust you. Never present only the evidence that supports your conclusion; they will notice what you left out.

### Evidence style

Present evidence from both sides — their strongest argument and yours. Use primary data, not summaries or interpretations. Show the methodology behind every claim. Include studies or evidence that partially contradicts your conclusion and explain how you weigh the conflicting evidence. "Steel man" the opposing view before presenting your synthesis. Comparative evidence (here's what happened when Company A tried it vs. Company B) is more persuasive than theoretical arguments.

### Language register

Write in measured, precise prose. No exclamation points. No superlatives. No marketing language of any kind. Sentence length: moderate (15-20 words), with complex sentences acceptable when showing nuance. Vocabulary: intelligent generalist — no jargon, no dumbing down. Hedging is appropriate here: "The evidence suggests" is more trustworthy than "The evidence proves." Formality: well-researched op-ed or policy brief. Use "the data shows" more than "I believe."

### Emotional range

Use restraint. The only effective emotional register is calm intellectual respect. You are having a conversation between equals — not persuading, not inspiring, not selling. Humor is acceptable only if self-deprecating ("I used to believe the opposite"). Acknowledging uncertainty is an emotional tool: "I don't have a clean answer for this, but here's what I've seen." Never express frustration with resistance. The register is "curious colleague who respects disagreement."

### What they quote

They will repeat the concession — the moment you acknowledged a real weakness in your position. They will also repeat the single piece of evidence that shifted their thinking. Write one honest concession and one surprising piece of evidence as standalone sentences. If a skeptic repeats something you wrote, it will be because it was fair, not because it was clever.

### Persuasion priorities

**Commitment/Consistency** — Start from principles the skeptic already holds and build logically toward your conclusion. **Reciprocity** — Concede real points; they will feel compelled to engage with yours. **Authority** — Use only authorities the skeptic already respects. Avoid Cialdini principles that feel manipulative to this audience (Social Proof, Scarcity, Liking can all backfire).

### Headline style

Write headlines as questions or as balanced observations. Never use headlines that assert a bold claim — the skeptic will argue with the headline before reading the evidence. Use "How," "Whether," and "What" constructions. Examples: "What three years of data actually show about remote work productivity." "The strongest case against this approach — and where it falls short." Headlines should signal fairness and intellectual honesty, not confidence.

### CTA style

Implied or invitational. Never make a hard ask — the skeptic will push back reflexively. Frame it as the audience's own conclusion: "Given what the evidence shows, the logical next step is..." or "You may want to review [specific resource] and draw your own conclusions." Offer to provide more data rather than asking for a decision. The CTA should feel like an open door, not a closing move.

---

## 7. Mixed / Cross-functional

### Mental model

Use a hub-and-spoke structure: open with a shared insight that everyone in the room cares about (the hub), then address each functional perspective in turn (the spokes), then return to the shared conclusion. Never optimize for one segment at the expense of another. Use plain language for the shared narrative and flag specialized detail clearly ("For the engineering team: ..."). Process information from shared problem to specialized implications to unified action.

### Trust signals

Show you understand each group's priorities — name them explicitly. Use evidence that spans functions: customer impact (everyone cares), revenue (everyone cares), timeline (everyone cares). When citing specialized data, briefly explain why it matters to the non-specialists in the room. Reference previous cross-functional successes: "When marketing and engineering aligned on X, we achieved Y." The trust signal is "this person understands my world AND theirs."

### Resistance triggers

Never use jargon from one function without translating it for others. Do not spend more than 30% of the piece on any single function's concerns — the others will check out. Never assume shared context: what sales calls a "qualified lead," engineering calls a "requirements spec," and product calls a "user story" may describe different things. Do not take sides in inter-departmental tensions. Do not present an action plan that assigns all the work to one team.

### Evidence style

Use evidence that connects functions: "Customer churn (sales concern) traces to onboarding friction (product concern) caused by API latency (engineering concern)." Show cause-and-effect chains that cross functional boundaries. Use a single shared metric everyone can track. Include a RACI-style breakdown for any recommendation so each group sees their role. Visual timelines that show parallel workstreams are more effective than sequential descriptions.

### Language register

Write in plain business English — no function-specific jargon unless immediately defined. Sentence length: 12-16 words. Use "we" constantly — this is about unity. When you must use a technical term, parenthetically define it: "API latency (the delay before a system responds)." Formality: all-hands meeting — professional but not stiff, clear but not condescending. Use concrete examples everyone can understand before diving into function-specific detail.

### Emotional range

Use shared purpose and collective pride. "We built this together" and "This affects all of us" are the core emotional notes. Avoid competitive framing between teams. Celebrate cross-functional wins explicitly. Use mild urgency tied to shared goals: "Our customers don't care which team owns this — they need it by March." Humor should be self-deprecating about organizational complexity, never pointed at a specific function.

### What they quote

They will repeat the shared metric or the cross-functional insight — the moment you connected the dots between their silo and someone else's. They will also repeat the unified action plan. Write the shared insight as a sentence that any function could say without modification. Write the metric so everyone can report on it in their own team meeting.

### Persuasion priorities

**Unity** — Create a shared identity that transcends functional silos: "We're all here because we care about [shared goal]." **Commitment/Consistency** — Reference past cross-functional agreements and extend them: "We agreed on X last quarter; this is the natural next step." **Social proof** — Show that the approach worked when other cross-functional teams adopted it.

### Headline style

Write headlines that name the shared outcome, not a function-specific insight. Use "we" and "our" language. Include a metric that all functions track. Avoid headlines that read as if they belong in one function's quarterly review. Examples: "Reducing customer onboarding from 14 days to 3 requires all five teams." "One shared dashboard replaces four conflicting reports." Headlines should make every person in the room feel addressed.

### CTA style

Distributed ask — break the action into function-specific next steps within a shared timeline. "Engineering: deploy the API fix by March 1. Marketing: update the onboarding emails by March 5. Sales: brief the field team by March 8." Include a shared milestone everyone works toward. The CTA should feel like a team play, not a top-down mandate.

---

## 8. Academic / Research

### Mental model

Present the research question, then the methodology, then the findings, then the implications — in that order. This audience processes through the lens of methodological rigor: they evaluate HOW you know before accepting WHAT you know. Structure the argument as a logical chain where each link is verifiable. Distinguish clearly between established findings, preliminary evidence, and speculation. Signal the confidence level of every claim.

### Trust signals

Cite peer-reviewed sources with full attribution (author, year, journal). Show sample sizes, confidence intervals, and effect sizes — not just p-values. Acknowledge the limitations of your own methodology before the audience raises them. Reference replication status of key findings. Use systematic reviews and meta-analyses over individual studies. The trust signal is methodological transparency: "Here's exactly how we measured this, and here's what could be wrong with our approach."

### Resistance triggers

Never overstate findings. "This proves" is almost never appropriate — use "This suggests" or "The evidence supports." Do not cherry-pick studies; if the literature is mixed, say so and explain your weighting. Never appeal to popularity or market success as evidence of validity. Avoid anecdotal evidence as a primary proof — it's acceptable as illustration after the data is established. Do not simplify to the point of distortion; hedge where the evidence requires it.

### Evidence style

Use primary research: original studies, datasets, and experimental results. Present competing hypotheses and explain why your interpretation is preferred. Include effect sizes and confidence intervals, not just statistical significance. Show meta-analytic results when available. Use figures and tables with clear labels, axes, and error bars. When citing a finding, include enough methodological detail that the audience can evaluate its quality: "In a randomized controlled trial (n=2,400, 18-month follow-up), the intervention group showed..."

### Language register

Write in formal academic prose. Precise vocabulary is essential — use the accepted term of art even if a simpler word exists, because precision matters more than accessibility here. Sentence length: 18-25 words, with complex subordinate clauses acceptable when they carry necessary nuance. Passive voice is acceptable when the actor is less important than the finding ("Three studies were excluded due to methodological concerns"). Avoid first person ("I argue") in favor of "The evidence suggests" or "This analysis indicates." Formality: journal article discussion section.

### Emotional range

Use intellectual excitement about findings and methods, delivered with restraint. "These results are noteworthy because..." is the ceiling of emotional expression. Never use urgency, hype, or persuasive language — it signals bias. Acknowledge the beauty of an elegant study design or an unexpected finding, but do so with understatement. The emotional register is "peer presenting at a conference" — engaged but controlled, enthusiastic about the question, skeptical about easy answers.

### What they quote

They will repeat the key finding with the effect size: "0.4 standard deviation improvement with 95% CI [0.28, 0.52]." They will also repeat the novel methodological contribution — the way you measured something or controlled for a confound. Write the key finding with full statistical detail as a standalone sentence. Write the methodological innovation as a sentence that could appear in an abstract.

### Persuasion priorities

**Authority** — Demonstrate command of the literature, including studies that challenge your position. **Commitment/Consistency** — Build from established theoretical frameworks the audience accepts and show how your finding extends or refines them. **Reciprocity** — Contribute genuinely new evidence or analysis; the audience will engage with work that advances their field.

### Headline style

Write headlines as precise claims with scope qualifiers. Include the population, the finding, and a signal of evidence strength. Avoid sensationalism — "may," "suggests," and "in [population]" are appropriate qualifiers. Examples: "Spaced repetition improves long-term retention by 0.4 SD in undergraduate populations." "Cross-sectional evidence suggests income inequality correlates with reduced social trust (r = -0.47, 23 OECD nations)." Headlines should read like the conclusion sentence of an abstract.

### CTA style

No explicit ask. Frame next steps as open research questions: "These findings raise several questions for further investigation." If action is warranted, present it as an evidence-based recommendation with stated confidence: "Given the current evidence base, implementing [specific intervention] in [specific context] appears warranted, though replication in [population] is needed." The CTA should invite further inquiry, not demand a decision.

---

## Quick Reference: Profile Differentiators

Use this table to verify you're writing differently for each audience.

| Dimension | Executive | Technical | Sales | Investors | Keynote | Skeptics | Mixed | Academic |
|-----------|-----------|-----------|-------|-----------|---------|----------|-------|----------|
| **Opens with** | Conclusion | Mechanism | Competitive angle | Market opportunity | Human story | Opposing view | Shared problem | Research question |
| **Sentence length** | 10-15 words | Variable | Short, punchy | 12-18 words | 10-12 words | 15-20 words | 12-16 words | 18-25 words |
| **Formality** | Boardroom memo | Tech blog | Sales kickoff | Pitch meeting | TED Talk | Policy brief | All-hands | Journal article |
| **Emotional peak** | Controlled urgency | Intellectual curiosity | Competitive energy | Confident ambition | Full-range storytelling | Calm respect | Shared purpose | Restrained excitement |
| **Strongest proof** | Financial metric | Reproducible benchmark | Customer verbatim | Cohort growth data | One person's story | Primary source, both sides | Cross-functional chain | Peer-reviewed study |
| **Headline feel** | Verdict with a number | Mechanism with a metric | Urgency with stakes | Metric with a claim | Intriguing promise | Balanced question | Shared outcome | Scoped finding |
| **CTA force** | Hard: approve/fund | Soft: evaluate/try | Hard: act by Monday | Direct: invest/meet | Implied: try this | Implied: draw your own | Distributed: per team | None: further inquiry |
