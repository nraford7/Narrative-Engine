# Prose Craft (embedded module)

> **This is a verbatim embed of the standalone `prose-craft` skill, copied into Narrative Engine so
> the build subagent is self-contained — it never has to invoke another skill at dispatch time.**
> Source: `~/.claude/skills/prose-craft/SKILL.md` · embedded 2026-06-22 · re-synced 2026-08-24 (canonical b6cdbe0). If the canonical skill
> changes, re-sync this file. The companion catalog lives at
> [`prose-craft-constructions.md`](prose-craft-constructions.md).

This is Tier 1 of the [Humanizing Pass](humanizing-pass.md). The builder applies it to every prose
paragraph and every deck title — it is the sentence-level discipline; the discourse-level Tier 2
lives in `humanizing-pass.md`.

The synthesis of three sentence-level disciplines into one model. The unit of work is the sentence.

- **The Floor — Strunk.** Correctness and economy. Cut what is dead.
- **The Filter — Tropes.** Kill machine-tells. Remove what is automatic.
- **The Ceiling — Tufte.** Construct varied, intentional sentences. Add what does real work.

**The one principle that unifies all three: nothing on the page by default.** Strunk removes the unintentional. Tropes removes the reflexive. Tufte adds the deliberate. Every word and every structure is *chosen*, not defaulted. When the three seem to conflict, intention is the tiebreaker (see Conflict Resolution).

## When to Use

Any prose for human eyes. Strongest signal: the draft reads flat, padded, hedged, or like a model wrote it.

**Scope inside Narrative Engine:** this governs the *sentence*. Document-level argument structure is the host skill's job (focal, arc, gates). For **CTA lines, pricing lines, and the explicit Ask**, the Persuasion Overlay (`agent-reference-persuasion.md`) and `copy-editing` discipline take precedence — its persuasion sweeps fight the Filter, so do not let the Filter strip a working CTA. prose-craft governs the body; the overlay governs the ask. Skip entirely on code and structured data.

## The Workflow

**Editing a draft** — run three passes in this order:
1. **Ceiling first.** Read for shape. Where is the prose flat, monotone, all-one-length? Mark places to build (branching, an appositive, a cumulative trailer, parallelism). Add on purpose. Load `prose-craft-constructions.md` for the catalog and examples.
2. **Filter second.** Sweep for machine-tells. The additions you just made may have introduced some. Cut them. Hold the hard limits below.
3. **Floor last.** Tighten word by word. Cut dead words, fix passive-by-accident, put the emphatic word at the end. This pass shrinks; do it after building so you don't tighten away the music.

**Generating from scratch** — construct with the Ceiling, then run Filter and Floor as a single tightening pass.

**Threshold — edit vs. regenerate:** if the Filter pass would gut more than half the draft's *sentences*, stop editing. The draft is machine-prose, not a near-good draft with tells. Treat the original as a *brief*, extract its actual claims, and generate from scratch (Ceiling-first), still honouring the target register's Floor/Ceiling balance. **If the brief yields no defensible claim — only platitudes — say so and write the smallest honest version; do not invent substance to fill the space.** Polishing a 90%-tell paragraph word by word wastes effort and leaves the original's dead bones in place.

## The Floor — Strunk (correctness + economy)

Condensed. The rules that earn their keep:

| Rule | Do |
|------|----|
| Active voice | Subject acts. The passive is a tool, not a fault — reach for it on purpose (see *Passive: when it's the right choice* below), never by accident. |
| Positive form | Say what *is*, not what isn't. ("forgot" not "did not remember") |
| Definite, specific, concrete | The named thing beats the abstraction every time. |
| Omit needless words | Every word must report. Cut filler, not qualification that earns its place. |
| Keep related words together | Subject near verb, modifier near what it modifies. |
| Emphatic word at the end | The end of the sentence is the loudest position. Put the payload there. |
| Parallel form for parallel ideas | Co-ordinate ideas take co-ordinate grammar. |

**Cut by default** (these survive only if they pass the naming test — a nameable rhetorical job, e.g. "actually" flagging a real contrast): very, really, quite, just, actually, basically, in order to (→ to), the fact that, there is/are openings. Default is delete; the burden is on the word to earn its place. Replace: utilize→use, leverage→use, facilitate→help.

**Passive: when it's the right choice.** The passive earns its place for four specific jobs — and never as mere change of pace, never back-to-back:
- **Dropped agent.** The actor is unknown, obvious, or irrelevant. "Aristotle's psychology is marred with obscurity" — naming the agent yields the absurd "marred *by Aristotle*."
- **End-weight.** The payload deserves the loud final slot. "...the fundamentals of life, such as death." Active buries "death" mid-sentence and kills the punch.
- **Cohesion.** Keeps one recurring topic in subject position across sentences so the reader tracks a single thread.
- **Right-branching room.** Lets a heavy, long-modified subject branch forward from its logical start instead of clogging the front.

If none of those four is the payoff, use active. Variety alone is not a reason.

**The first sentence is its own job.** The opening line of a piece does work no other sentence does: it decides whether the reader continues. Make it create curiosity, not summarize. It earns rewrites the rest of the draft doesn't — give it disproportionate effort and judge it by one test: does the reader want the second sentence?

## The Filter — Tropes (kill machine-tells)

A single instance is usually fine. The tell is repetition or stacking. Sweep for:

**Canonical source:** the full tell list lives in the `writing-tropes` skill; this section is its condensation. On any mismatch the stricter reading wins. Mirror every edit to both files, and to this embedded copy.

**Scope of the limits below:** *piece* = the whole document; *section* = one heading-delimited block; a standalone paragraph counts as both. A 3-paragraph essay with no headings = 3 sections, so a per-section cap (e.g. one tricolon) resets each paragraph; in a lone paragraph the per-piece and per-section caps are identical.

**Word choice** — Ban: delve, utilize, leverage (verb), robust, streamline, harness, certainly, tapestry, landscape (for domains), paradigm, synergy, ecosystem, framework (for anything not literally a framework), multifaceted, nuanced, pivotal, transformative, compelling (as generic praise). Ban magic adverbs faking significance: quietly, deeply, fundamentally, remarkably, arguably, strikingly. Ban verbs faking depth: underscore, resonate, illuminate, pave the way. Ban: plethora, myriad, "when it comes to" (→ for). Don't dodge the copula: "is" beats "serves as / stands as / marks / represents."

**Sentence structure** — Negative parallelism ("not X — it's Y"): **zero per piece, hard ban.** Always use positive form instead — state what the thing *is*, never define it by what it isn't. The ban covers the variants: causal ("not because X, but because Y") and the cross-sentence reframe ("The question isn't X. The question is Y."). Ban the countdown ("Not X. Not Y. Just Z."), the self-answered question ("The X? A Y."), anaphora past two in a row, stacked tricolons (**one rule-of-three per section max** — the cap rations the *device*; build the ones that survive as a real series form, see `prose-craft-constructions.md` → The Series). Ban "it's worth noting / it bears mentioning / importantly / interestingly / notably." No "-ing" significance tails ("highlighting its role," "reflecting broader trends"). Ban "earns its weight / earns its place" (generic significance). Ban "one of the most [superlative] in history/ever" (generic superlative — be specific or cut). False ranges: "from X to Y" only when X and Y sit on a real spectrum with a meaningful middle.

**Paragraph shape** — No sentence fragments standing alone as paragraphs for manufactured punch. No listicle-in-prose ("The first... The second... The third..."): use a real list, or write genuinely connected paragraphs.

**Tone** — Ban: "here's the kicker / here's the thing," "let's break this down / unpack / dive in," "imagine a world where," "the truth is simple." No grandiose stakes inflation — match stakes to actual stakes. No vague attributions ("experts say") without names. No invented concept-labels treated as established. No teacher-mode analogies ("think of it as..."): an analogy survives only when it is clearer than the concept. No performative vulnerability or staged self-awareness: real specificity beats polished confession.

**Formatting** — **Em-dashes: three per piece, hard ceiling.** Provenance doesn't raise the cap — naming decides *which* dashes survive, never how many are allowed, and cuts habitual ones even when you're under budget. (Same for any rationed device — see the naming test under Conflict Resolution.) No bold-first on every bullet. No arrows, no smart quotes — standard keyboard characters.

**House-style override.** The caps here are ceilings, not entitlements. A house or personal style guide layered above this skill may lower any cap (em-dashes to zero, for instance); the lower cap always wins.

**Composition** — No fractal summaries (say it once). No signposted conclusion ("in conclusion, to sum up"). No "despite its challenges" acknowledge-then-dismiss. If the argument is one point, write it in the space one point needs. Retire a metaphor after two uses. One example developed well beats five name-dropped companies or revolutions.

## The Ceiling — Tufte (construct on purpose)

The positive moves none of the other layers teach. Full catalog with real examples in `prose-craft-constructions.md`. The core set:

| Move | What it does | Mini-example |
|------|--------------|--------------|
| **Cumulative sentence** | Base clause, then trailing modifiers that unspool like thought | "I watched him warily, wondering who he was." |
| **Left-branching** | Front-loaded modifiers delay the subject for a climax | "Now that the cycle of boom and bust has been tamed, the challenges have taken a new turn." |
| **Mid-branching** | Interrupt the base clause to suspend and tighten | "Taking out my pen, I did, in blue, dare set my name." |
| **Appositive** | Rename smoothly without changing the syntactic plan | "The Zoo Story, my first real play, ..." |
| **Nominative absolute** | Attach a sub-scene with its own subject | "...she gazed out, her head to one side, her lips moving." |
| **Parallelism** | Co-ordinate ideas in matching grammar for rhythm and weight | — |
| **Syntactic symbolism** | Make the *shape* enact the meaning (suspense via a held sentence, balance via a balanced one) | — |

**The Ceiling's job: kill monotony.** If every sentence is the same length and shape (subject-verb-object, subject-verb-object), the prose is dead even when each sentence is "correct." Vary length. Vary where the weight falls. Build at least one sentence that earns a reader's breath.

**The Figure — the optional fourth axis.** Named rhetorical schemes of surprise and repetition (antithesis, chiasmus, controlled anaphora) that intensify a piece's two or three anchor moments: the opening, the turn, the close. Catalog in `rhetorical-figures.md`. Load it only for savored registers; every figure lives inside the Filter's caps and passes the naming test.

## Cohesion — the paragraph-level move

The three layers above work one sentence at a time. This is how sentences *join*. The rule: **explicit connector words are the weakest tier.** "Furthermore / Moreover / Additionally" bolted on every sentence is a machine-tell — it signals a link the word order should have supplied for free. Before reaching for a transition word, fix the cohesion structurally:

- **Carry the key term forward.** Repeat the exact word, don't pronoun it away or swap a synonym.
- **Point a demonstrative back.** Open with *this / that* scooping the whole prior idea ("...we must come back to love. **That** alone raises us..."). Replaces "This is important because..." padding.
- **End-load the pivot.** Drive the connecting word to the end of one sentence so it sits beside its echo at the start of the next ("...brought into man's suffering. **This joy** becomes..."). The order makes the link; no "Furthermore" needed.
- **Hang parallel members off a topic sentence.** Shared structure *is* the cohesion ("We live in an era of great inventions. Television sets bring... Atomic submarines travel... Manned ships orbit...").
- **Given-before-new ordering**, including a deliberate passive, keeps the thread visible across the seam.

Use a connector word only when none of these fits and the logical turn (*but, so, yet*) genuinely needs naming — then use it once, accurately.

## Conflict Resolution

The three layers disagree in exactly two places. Resolve both with **intention + register**, never compromise-to-mush.

**Economy (Floor) vs. elaboration (Ceiling).**
Strunk says omit needless words and avoid loose sentences. Tufte celebrates the long cumulative sentence. Both are right in different scopes:
- Economy governs the **base clause and word choice** — always. Cut dead words, every pass.
- Elaboration governs **modifiers you add on purpose** — when each does real work.
- **The deletion test:** can you cut the modifier without losing meaning *or* music? If yes → filler, Floor wins, cut it. If no → craft, Ceiling wins, keep it.

**Device budget (Filter) vs. devices (Ceiling).**
Tropes rations em-dashes and long/varied sentences; Tufte's mid-branching leans on dashes and his cumulatives run long. Resolve by **provenance:**
- The caps are absolute (em-dashes: three, period). A device you deploy *on purpose, for an effect you can name in one phrase,* is craft, not a tell — but craft still lives within the cap.
- **The naming test (governs every rationed element — words, em-dashes, tricolons, parallel runs):** name the effect in a phrase ("dash suspends the clause for surprise"). Can't name the job? It's a tell — cut it, *even when you're under budget.* Naming never raises a cap; it decides which instances survive when you're at or over the cap, and strips the unearned ones below it. The cap sets the maximum; the naming test removes everything that doesn't earn its place underneath.
- Master-on-purpose beats model-by-default, even when the surface structure is identical.

**Note — where Floor and Filter agree:** both push you off negative constructions. Strunk's "positive form" and the Filter's ban on negative parallelism reinforce each other. No conflict; double weight.

## Register Calibration

The same sentence is right in one place and wrong in another. The Filter is always on. The Floor/Ceiling balance shifts:

| Register | Lean | Sentences |
|----------|------|-----------|
| CTA, UI text, error message, exec summary, anything scanned | **Floor-dominant.** Ration the Ceiling. | Short base clauses, minimal branching, payload up front. |
| Memo, briefing, report body | **Balanced.** | Mostly tight; one or two built sentences per section for rhythm. |
| Essay, argument passage, narrative, anything read linearly and savored | **Ceiling earns its place.** | Cumulative sentences, varied branching, syntactic symbolism welcome. |

A cumulative sentence is gorgeous in an essay and a liability on a button.

## Quick Reference — one combined sweep

When context is tight, run this single checklist instead of three passes:

- [ ] Active, positive, concrete; emphatic word at the end (Floor)
- [ ] First sentence creates curiosity, not summary; rewritten until it earns the second (Floor)
- [ ] Dead words cut: very/just/actually/in order to/the fact that (Floor)
- [ ] Zero negative parallelism (any variant, incl. "not because X, but because Y"), ≤1 tricolon/section, ≤3 em-dashes total (Filter)
- [ ] No delve/leverage/robust/tapestry/nuanced/pivotal/compelling, no "earns its weight," no "it's worth noting," no signposted conclusion, no generic superlatives (Filter)
- [ ] No fragment-paragraphs, no listicle-in-prose, no false ranges; metaphors retired after two uses (Filter)
- [ ] Sentence lengths vary; openers vary (not every sentence subject-first); at least one built sentence per section (Ceiling)
- [ ] Anchor moments figured on purpose (savored registers only, `rhetorical-figures.md`); everything else left plain (Figure)
- [ ] Lists built as a real series form, not the reflex `A, B, and C`; passive used only for one of its four jobs (Ceiling/Floor)
- [ ] Sentences cohere structurally — key-term, demonstrative, end-loaded pivot — not by bolted-on "Furthermore/Moreover" (Cohesion)
- [ ] Every device passes the naming test; every modifier passes the deletion test (Conflict Resolution)
- [ ] Register-appropriate Floor/Ceiling balance (Calibration)

## Worked Example — one paragraph through the three passes

**Before:**

> The migration was completed by the team over the weekend. It's worth noting that there were several unexpected issues that came up during the process. The database is very large and the process was quite slow. The new system serves as the foundation for everything we're planning to build next quarter, highlighting the importance of getting this right.

**Pass 1 — Ceiling (build).** Every sentence is subject-verb-object at roughly the same length. Mark two builds: turn the vague "several unexpected issues" into a real series, and name the new system with an appositive.

**Pass 2 — Filter (cut tells).** "It's worth noting" (say the thing). "Serves as" (copula dodge). "Highlighting the importance" (-ing significance tail).

**Pass 3 — Floor (tighten).** "Was completed by the team" is passive with no job: make it active. Cut "very" and "quite." Put the payload at the end.

**After:**

> The team finished the migration over the weekend, working through a corrupted index, a failed replica, and a four-hour lock nobody had predicted. The database is large and the work was slow. The new system, the base for next quarter's roadmap, had to come up clean — and it did.

Every device in the after is named: the series is the section's one tricolon, built as a real triple; the appositive renames without a new clause; the single dash suspends the close for the payoff. Three sentences, three different shapes.

## The Mechanical Sweep — before delivering

Rules a model forgets are rules a literal search catches. Run this on the finished draft; no judgment required:

1. **Ban list.** Substring-scan for every banned word in the Filter (delve, leverage, robust, nuanced, pivotal, plethora...). Any hit goes.
2. **Em-dashes.** Count them. Four or more: cut to the cap, keeping only the named ones. Then check the survivors against any stricter house cap.
3. **Templates.** Search for: "not X — it's", "isn't just", "not because", "The question isn't", "worth noting", "In conclusion", "Think of it as".
4. **Openers.** Three consecutive sentences opening with the same word: vary one.

Anything the scan flags goes back through the Filter by hand. The scan finds; it does not fix.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Running Floor first, then trying to build | Build first (Ceiling), tighten last (Floor). Tightening kills music you haven't written yet. |
| Treating Filter caps as absolute bans | They're defaults for unconscious use. Named, intentional devices are exempt. |
| Adding Ceiling devices everywhere | Monotone elaboration is as dead as monotone simplicity. One or two built sentences per section. |
| Using this on a landing page | Wrong tool. Conversion copy → `copy-editing`. |
| Elaborating to sound smart | If the modifier fails the deletion test, it's filler dressed as craft. Cut it. |
