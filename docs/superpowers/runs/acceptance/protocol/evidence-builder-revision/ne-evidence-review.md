# Evidence Review

## Verdict
FINDINGS

## Findings

1. **BLOCKING** — Section 3, closing paragraph; unsupported causation and altered qualification (checks 1 and 2).
   - Source says: "accounts that received a retention discount churned at 2.3x the rate of undiscounted accounts within 18 months of the concession — the discount predicts churn better than the price objection it was meant to answer."
   - Output says: "Discounts caused the churn."
   - Required fix: Delete this sentence; the source establishes a predictive association, not causation, and section 2 already states that limitation accurately.

2. **BLOCKING** — Sidecar, Sourcing Summary section 3 and Originality statement; failed provenance tag (check 5).
   - Source says: "Preliminary modeling suggests option (c) affects 18-month retention 3-4x more per dirham than discounting, but it requires sales to absorb tougher price conversations in Q4."
   - Output says: "Discounts caused the churn." The sidecar labels section 3 "[PARAPHRASE]" and states "100% source-derived / 0% generated."
   - Required fix: Remove the unsupported causal sentence identified in finding 1 so that section 3's paraphrase tag and the source-derived attribution accurately describe its content.

## Spot-Check Record

Sampled all three sections tagged [PARAPHRASE], including section 2's additional [ELABORATED] tag. Section 3 failed; the required expanded sample therefore already covers every tagged section. No sampling shortage exists.

- **Section 1 — PASS.** Located verbatim: "gross revenue retention 91.2% (down 1.1pp QoQ)"; "three of the seven largest churned accounts cited cost in exit interviews"; "sales has requested an expanded retention-discount pool for Q4 (current pool: AED 2.6M/yr, average concession 18%)"; and "reallocate AED 1.8M of the pool to a guided-onboarding service". The opening's recommendation is supported by the source's option (c) and preliminary modeling, with that qualification retained.
- **Section 2 — PASS.** Located verbatim: "a cohort analysis across 1,240 accounts renewing in the last 24 months"; "accounts that received a retention discount churned at 2.3x the rate of undiscounted accounts within 18 months of the concession"; "the strongest single predictor of renewal in the entire dataset was days-to-first-saved-report during onboarding"; "accounts that built and saved a report within 14 days renewed at 96%, versus 71% for accounts that took longer than 45 days, regardless of price paid, segment, or discount status"; and "Exit-interview price citations concentrate almost entirely in the slow-onboarding cohort." The paraphrases preserve population, thresholds, time windows, and predictive status. The causal limitations accurately elaborate the limits of the reported evidence. The cold read's highest-impact claims were checked and pass.
- **Section 3 — FAIL.** Located verbatim: "reallocate AED 1.8M of the pool to a guided-onboarding service targeting first-saved-report inside 14 days for all new mid-market and SMB accounts" and "Preliminary modeling suggests option (c) affects 18-month retention 3-4x more per dirham than discounting, but it requires sales to absorb tougher price conversations in Q4." These support the scope, target, estimate, and tradeoff. No passage supports "Discounts caused the churn." The section therefore fails its [PARAPHRASE] tag as delivered.

All five checks ran in order across the entire draft. Checks 1 and 2 found the causal overclaim above; the remaining factual sentences and titles have traceable support and retain the source's qualifications. Check 3 found no additional missing reasoning: the discount association, onboarding predictor, preliminary comparative model, and sales tradeoff supply the recommendation's supporting steps for the executive audience. Check 4: the strongest supported action is to choose the source's option (c), reallocating AED 1.8M to guided onboarding for all new mid-market and SMB accounts, with preliminary modeled benefits and tougher Q4 sales conversations acknowledged. The delivered ask matches that action and does not overreach. Check 5 found the provenance failure above.

## Summary
FINDINGS: 2 BLOCKING findings and 0 MINOR findings. The worst gap is the unsupported claim that discounts caused churn; that same sentence also makes section 3's paraphrase attribution inaccurate.
