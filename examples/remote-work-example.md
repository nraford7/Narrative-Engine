# Example Workflow: Remote Work Research

This example shows the Narrative Engine workflow applied to a research article about remote work productivity. It follows the spine flow: focal discovery → discovery questions → density → argument outline + shape → build brief → subagent build (body-only output + metadata sidecar) → gates → targeted review.

---

## Input

**User:** [Pastes 2,000-word article about remote work productivity research]

---

## Phase 1.75: Focal Discovery

**Claude:**
> First, two one-liners so every candidate gets judged against them:
>
> **Audience:** The executive team that owns the 2022 hybrid policy.
> **Ask:** Approve a shift from hybrid to a remote-first team model.
>
> **Material Read:**
> - **Stake:** The current hybrid policy is costing measurable output; the leases and the policy renew this year.
> - **Tension:** The policy was designed for "best of both worlds" — the data says the worlds don't combine.
> - **Genuine surprise:** The mechanism. Belonging predicted retention better than compensation did.
> - **Strongest existing passages:** the 23%/847-employee output comparison; the belonging-vs-compensation regression; the context-switching cost analysis.
> - **What changes:** Execs stop treating remote work as a perk to balance and start treating team cohesion as the thing to engineer.
>
> Candidate focal points:
>
> 1. **The performance claim:** Fully remote outperformed hybrid by 23% — rebuild the team model around it.
> 2. **The cost claim:** Hybrid's context-switching is a measurable productivity tax the current policy pays every week.
> 3. **The talent claim:** Remote-first is now an outright hiring and retention advantage.
>
> Which should we optimize for? Or is there a different point you want to land?

**User:** 1

**Claude:**
> Focal Statement: **"Fully remote outperformed hybrid by 23% — rebuild the team model around it."**
> - **The One Thing:** Remote won outright; the policy should follow the winner.
> - **The Ask:** Approve the remote-first transition.
> - **The Through-Line:** We measured what we assumed — and the assumption lost.
>
> `focal_origin: user-selected`

---

## Phase 2: Discovery Questions

*Audience was pinned in Phase 1.75, so that question is skipped.*

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

---

## Phase 2.5: Density Mode

**Claude:**
> **How concentrated should this deck be?**
>
> 1. **High-Impact** — Maximum compression. One punch per slide. For time-constrained execs who want the answer fast.
> 2. **Narrative** — Room for the story to breathe. Emotional builds and context. For audiences who came to learn.
> 3. **Evidence** — Denser supporting material. Multiple proof points. For skeptics or due diligence.
> 4. **ELI5** — Maximum accessibility. Simple words, concrete analogies, zero jargon.

**User:** 1 — they have limited time

---

## Phase 3: Argument Outline + Conditional Shape

**Claude:**
> **Argument Outline** — what this exec team needs, in order:
> 1. The answer and the recommendation, immediately (they have limited time).
> 2. Why we believed hybrid was right — the 2022 bet, stated fairly.
> 3. What we measured and what we expected to find.
> 4. Why remote won — the mechanism (belonging predicted retention better than compensation).
> 5. What the transition costs and what staying costs.
> 6. The decision and the timeline.
>
> **Shape: answer-first.** The claim lands on slide 1; the middle defends it. The Material Read names one genuine surprise — the belonging mechanism — so the deck holds that back for the mid-deck turn while the headline finding leads. No named arc needed; the argument outline already carries the piece.

**User:** Agreed

---

## Phase 3.5: Build Brief (Abbreviated)

**Claude:**
> Here's the Build Brief I'll hand the builder — focal statement (`user-selected`), audience + ask, the full Material Read, the outline above, shape `answer-first` · register `boardroom`, density High-Impact, plus voice and audience essentials (trust signals: sample size, methodology transparency; resistance trigger to avoid: implying the 2022 decision was foolish). Anything you'd change before I build?

**User:** Build it.

---

## Phase 4: Build (Subagent, Abbreviated)

The builder runs THE SPINE in a subagent and writes **two files**: the body-only deliverable and a metadata sidecar. No framework names, focal restatements, or sourcing tags appear in the deliverable.

### `ne-output.md` (body only)

```markdown
# Rethinking Remote: What Our Data Actually Shows

**Punchline:** Fully remote outperformed hybrid by 23% — rebuild the team model around it.

## Title sequence
1. Fully remote outperformed hybrid by 23% — rebuild the team model around it
2. We bet on hybrid to capture the best of both worlds
3. We tracked three cohorts for 18 months expecting hybrid to win
4. Belonging predicted retention better than compensation did
   [...titles 5-8 continue: costs, transition plan, decision]

---

## Slide 1 — The Answer
**Headline:** Fully remote outperformed hybrid by 23% — rebuild the team model around it
**Spotlight (≤60 words):** 847 employees tracked for 18 months: fully remote workers produced 23% more output than hybrid workers, with equivalent collaboration scores (Productivity study, §3). The recommendation: rebuild the team model around fully remote work.
**Design note:** Single large stat (23%) against white space; recommendation as a one-line subhead.

---

## Slide 2 — The Bet We Made
**Headline:** We bet on hybrid to capture the best of both worlds
**Spotlight (≤60 words):** The 2022 policy assumed hybrid combines face-to-face creativity with at-home deep work. Most Fortune 500 companies made the same bet, on the same reasoning (Productivity study, §1–2).
**Design note:** Timeline strip, 2022 policy milestone highlighted.

---

## Slide 3 — What We Expected
**Headline:** We tracked three cohorts for 18 months expecting hybrid to win
**Spotlight (≤60 words):** The study tracked full-office, hybrid, and full-remote cohorts on output, satisfaction, and collaboration quality (Productivity study, §4). Our hypothesis: hybrid tops both.
**Design note:** Three-column cohort layout; hybrid column visually favored.

---

## Slide 4 — The Turn
**Headline:** Belonging predicted retention better than compensation did
**Spotlight (≤60 words):** Across all three cohorts, team-belonging scores predicted 12-month retention more strongly than total compensation (Productivity study, §9). Remote teams built belonging deliberately — rituals, working agreements, protected focus time (6.2 vs 4.1 hrs/day). Hybrid assumed the office would supply it, and paid for that assumption in context-switching costs.
**Design note:** Two-bar comparison: belonging vs compensation as retention predictors.

---

[Slides 5-8 continue with costs, transition plan, and the decision ask...]
```

Slide 1 already delivered the finding and the recommendation; slide 4's job is the *mechanism* — the one thing in the source this audience doesn't already believe. The Turn adds new information; it never re-reveals the answer.

### `ne-output-meta.md` (sidecar, excerpt)

```markdown
## Sourcing Summary
| Slide | Tag | Source anchor |
|---|---|---|
| 1 | [DIRECT] | 23% output comparison, ¶3 |
| 2 | [PARAPHRASE] | 2022 policy rationale, ¶1-2 |
| 3 | [ELABORATED] | study design, ¶4 |
| 4 | [DIRECT] | belonging regression, ¶9 |

**Originality:** 72% source-derived / 28% generated.
```

---

## Phases 4.6–4.8: Gates (Abbreviated)

- **Gate 2 (blind focal judge):** cold-reads the body only, names the One Thing ("remote won; rebuild around it"), checks the source for a more consequential claim, finds none — **PASS**. Title-chain tests pass: the sequence reads as spoken prose, no dangling antecedents.
- **Gate 3 (humanizing check):** no structural flags.
- **Gate 4 (evidence review):** spot-checks the sidecar's tags against the source; confirms the belonging claim carries the source's correlational hedge — **CLEAN**.

---

## Phase 5: Targeted Review (Abbreviated)

**Claude:**
> ## Review Summary
>
> **Reviewers:** Audience Advocate + Content Expert (selected for counterintuitive research — the evidence must be bulletproof)
>
> ### Strengths
> - Answer-first opening respects exec time; slide 4 then gives them something new — *Audience Advocate*
> - The belonging claim keeps the source's correlational framing, and the 23% figure travels with its sample size — *Content Expert*
>
> ### Recommended Changes
>
> 1. **Slide 4 evidence** — Content Expert
>    Put the regression's effect sizes in an appendix; a counterintuitive claim this central needs the numbers within reach.
>
> 2. **Preempt objections** — Audience Advocate
>    Add one sentence acknowledging hybrid's perceived benefits before the cost slides.
>
> ### Overall Assessment
> **Ready to present?** Yes with minor edits
> **Most important change:** Add acknowledgment of hybrid benefits to preempt objections.

---

## Phase 5.5: Stress Test Panel (Optional)

**Claude:**
> Want me to run the Stress Test Panel? This is a strategic plan presented to decision-makers, so I'd test against: **COO**, **Conservative**, and **Risk Officer**.
>
> You can also add: Engineer, Skeptic, CFO, Lawyer
>
> Run it?

**User:** Yes

**Claude:**
> ## Stress Test Panel Results
>
> ### The COO — FLAGGED
> **Concerns:**
> 1. Implementation timeline not specified — how fast can we actually transition?
> 2. What happens to the office space we're leasing?
>
> ### The Conservative — FLAGGED
> **Concerns:**
> 1. 18 months is a short study period — could this be a pandemic anomaly?
> 2. What about new employee onboarding? The data may not capture that.
>
> ### The Risk Officer — PASSED WITH NOTES
> **Concerns:**
> 1. Sample size is good but selection bias possible — who self-selected into each cohort?
>
> ---
>
> ## Director Triage
>
> ### 🔴 Must Fix
> 1. **Implementation timeline** (COO) — Execs will ask "okay, what's the plan?" Add a slide with phased timeline.
>
> ### 🟡 Should Fix
> 1. **Study duration caveat** (Conservative) — Acknowledge 18 months is a snapshot; recommend continued tracking.
> 2. **Selection bias** (Risk Officer) — Add one sentence about how cohorts were formed.
>
> ### 🟢 Could Fix
> 1. **Office space** (COO) — Important but probably out of scope for this deck.

---

## Final Deck

User implements Must Fix and Should Fix items, resulting in a tight 10-slide deck that leads with the recommendation, lands the belonging mechanism mid-deck, and preempts the key objections.
