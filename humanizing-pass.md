# The Humanizing Pass

The de-slopping layer for Narrative Engine output. It exists because of one finding from the
narrative-structure research corpus: **a classifier detects AI-written narrative from structure
alone at 93.2% macro-F1, and still at 93.9% *after* span-level lexical rewriting** (StoryScope,
arXiv 2604.03136; LAMP, Chakrabarty/Laban/Wu 2025). Scrubbing the surface prose does not de-AI the
structure. Therefore the humanizing pass has two tiers, and the second is not optional.

| Tier | Operates at | Tool | Catches |
|------|------------|------|---------|
| **Tier 1 — Sentence** | Word and clause | embedded `prose-craft.md` | Lexical AI-tells, monotone cadence, dead words, hedging |
| **Tier 2 — Discourse** | Paragraph, section, whole piece | The structural-delta checklist below | AI signatures that *survive* lexical cleanup — over-resolution, theme-over-statement, chronological flattening, same-move repetition |

Run Tier 1 inside the build (every pass). Run Tier 2 as a gate after focal fidelity (Phase 4.7),
before the review panel.

---

## The cardinal rule (read before using any number below)

**These are gates and drift detectors, never optimization objectives.** No reliable automatic
measure of narrative quality exists; optimizing toward a metric manufactures exactly the homogenized
slop this pass exists to remove. Use the targets to *flag* a draft that has drifted toward the AI
pole — then fix it by hand. Do not loop a generator against these numbers.

Two further don'ts from the evidence:
- **Don't trust token-level AI-detectors** (DetectGPT / GPTZero-class) as a gate — brittle, stale within months.
- **Don't trust LLM-as-judge creativity scores as oracles** — they carry position, verbosity, and self-preference bias (see *Judge hygiene* below).

**Provenance caveat.** Every percentage below is *fiction-derived* — measured on ~5,000-word
stories, not decks or articles. The human/AI structural contrast is assumed to transfer; treat the
figures as **directional**, not as thresholds to hit precisely.

---

## Tier 1 — Sentence (prose-craft)

The builder applies the **embedded prose-craft discipline** — [`prose-craft.md`](prose-craft.md) plus
its catalog [`prose-craft-constructions.md`](prose-craft-constructions.md) — to all prose output and
all deck titles. It is embedded, not invoked: the builder is a subagent and reads these files
directly rather than calling a separate skill. prose-craft is the sentence-level discipline — Floor
(Strunk economy) + Filter (kill machine-tells) + Ceiling (varied, intentional construction). It
already delivers two of the corpus's humanizing levers for free:

- **Lexical de-slop** = prose-craft's Filter (strip "it's worth noting," delve/leverage/robust, signposted conclusions).
- **Stylistic variance** (Reinhart et al., PNAS 2025: LLMs occupy a narrower band, lower sentence-length variance) = prose-craft's Ceiling, whose explicit job is to *kill monotony — vary length, vary where the weight falls.*

**Register routing** — map the Density Mode to prose-craft's register so it rations the Ceiling correctly:

| Density Mode | prose-craft register |
|---|---|
| High-Impact / Punchy | Floor-dominant — short base clauses, payload up front, ration the Ceiling |
| Narrative / Flowing | Balanced — one or two built sentences per section for rhythm |
| Evidence / Dense | Floor on claim sentences; Ceiling allowed for evidence development (longer paragraphs are fine) |
| ELI5 | Floor-dominant + prose-craft's plain-language rules reinforce ELI5 |

**Conflict with persuasion copy.** prose-craft's own boundary: it warns off pure conversion copy
because its Filter fights persuasion sweeps. For CTA lines, pricing lines, and the explicit Ask, the
Persuasion Overlay (`agent-reference-persuasion.md`) and `copy-editing` discipline take precedence —
do not let the Filter strip a CTA that is working. prose-craft governs the body; the overlay governs
the ask.

---

## Tier 2 — Discourse (the structural-delta checklist)

These are the AI signatures that lexical cleanup leaves intact. Run after Tier 1. For each, the human
pole is the target; the AI default is what to suppress. Figures are the measured human-vs-AI gap.

### 1. Theme-statement budget — the sharpest one

**Humans state the theme 52% of the time; AI states it 77%.** Restraint on theme-statement is a
top humanizing lever — and Narrative Engine's own machinery (the Focal Statement, the Killer Line,
the cold-read judge obsessing over whether the piece "lands the point") *pushes toward over-statement.*
This is the engine optimizing along the single strongest AI tell.

- [ ] Count the on-the-nose theme declarations ("the point is…", "what this means is…", "the lesson here…").
- [ ] Cut to let evaluation and structure carry the point implicitly **wherever the piece can afford it.**
- **Exception — the focal still has to land.** Keep the explicit statement at the climax and the close
  (that is the Ask doing its job). Cut the *redundant* restatements in the body. The budget rations
  body restatements; it never removes the one payoff that delivers the One Thing.

### 2. Tolerate asymmetry and open threads

**57% of human stories carry subplots; 79% of AI stories have "no subplots." 59% of human protagonists
are morally ambiguous vs 38% AI.** AI resolves and moralizes every beat.

- [ ] Resist the urge to tie off every thread. Where the material has an open question, leave it open.
- [ ] Allow a beat to sit unresolved or ambiguous if the truth is unresolved. Not every section needs a tidy bow.

### 3. Preserve temporal complexity

AI flattens to clean chronology; humans use flashback, flash-forward, and iterative telling ("every
summer we…").

- [ ] Verify any intended non-linearity (an in-medias-res open, a flashback) survived the build and wasn't tidied back to chronological order.
- [ ] Where a pattern recurs, tell it iteratively once rather than as N tidy instances.

### 4. Discourse redundancy — "every paragraph makes the same move"

QUDsim (2025) measures the tell where each paragraph re-asks and re-answers the same implicit question.
Reviewers miss it because each paragraph reads fine *locally.*

- [ ] Read the section as a sequence of *moves*, not sentences. If three paragraphs all do "claim → example → restate-claim," collapse or vary them.
- [ ] No fractal summary — the piece should not say the same thing at three zoom levels.

### 5. Restore idiosyncrasy

**Feature-space rarity: 0.71 human vs 0.49 AI (Cohen's d = 0.83).** AI clusters at the mean.

- [ ] Replace one generic phrasing per section with a concrete particular — a specific number, name, image, or the source's own words.
- [ ] At least one moment of genuine specificity, wit, or personality that a template could not produce. (This is the existing "AI Test," now with a measured target behind it.)

---

## Judge hygiene (Phases 4.6, 5, 5.5)

The whole judge stack — cold-read judge, reviewers, stress-testers — is LLM-as-judge, and the
corpus flags three biases in exactly that setup:

- **Verbosity bias** — judges reward longer output. Counter: instruct judges to score against the
  Content-Driven Length principle; a tight 8-slide deck is not worse than a padded 20-slide one.
- **Position bias** — when comparing options, order changes the verdict. Counter: don't ask judges to rank A-vs-B by presentation order; ask each to evaluate against the Brief independently.
- **Self-preference bias** — a model rates its own family's prose higher. Counter where possible: the
  builder and the judge should not be locked to the same model; prefer a different reviewer model when available.

Use these as advisory corrections, not hard gates — the reliable signal is the structural-delta
checklist plus a human spot-check, not the judge's confidence score.

---

## One-pass quick reference

When context is tight, the humanizing pass collapses to:

- [ ] **Tier 1:** ran prose-craft (register-matched to density); CTAs exempted to the persuasion overlay.
- [ ] **Theme:** body restatements cut; explicit statement kept only at climax + close.
- [ ] **Resolution:** at least one thread left honestly open; no forced moral bow on every beat.
- [ ] **Time:** intended non-linearity survived; recurring patterns told iteratively.
- [ ] **Redundancy:** no run of paragraphs making the identical move; no fractal summary.
- [ ] **Idiosyncrasy:** one concrete particular restored per section; one un-templatable moment present.
- [ ] **Gate, not objective:** none of the above was optimized toward as a target.
