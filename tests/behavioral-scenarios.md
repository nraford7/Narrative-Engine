# Behavioral acceptance scenarios

Use a fresh conversation for each scenario. Load this standalone SKILL.md by explicit path. Record the actual responses, files read, and any generated brief/output. A checklist or simulated next response alone is not an end-to-end test. Source passages below are fictional fixtures.

## 1. Mode is required

Request: “Use Narrative Engine. Turn these notes into a quick executive briefing, just write it, no questions: support requests rose; many concern onboarding; no intervention was tested.”

Accept: asks Fast/Deep and stops before discovery or drafting. Reject: infers Fast, starts writing, or interprets urgency as a choice.

## 2. Deep discovery order

Request: “Use Narrative Engine in Deep mode. Notes: support requests increased, many concern onboarding. Help me make something useful.”

Accept: asks the unresolved purpose/success question first; waits. Continue with educate, then non-specialist managers who equate ticket count with staffing need, then a standalone 700-word briefing. Verify supplied answers are retained without repeated menus and no main point is finalized before source analysis and structure comparison.

## 3. Same source, different purposes

Source: “A nonrandom sample of 100 tickets from one week included 42 about initial setup. No intervention was tested. Workload per ticket and staffing needs were not measured. Managers proposed evaluating clearer setup guidance; effectiveness and costs are unknown.”

Run separately in Fast:
- Educate managers about the difference between counts, causes and workload.
- Persuade managers to approve an investigation of setup problems, not a staffing cut.

Accept: educational brief has a concrete understanding outcome and no forced action; persuasive brief supports only a bounded investigation and addresses uncertainty. Both preserve nonrandom sample, no annual extrapolation, untested effectiveness and unknown staffing needs. Show candidates and direct explanation; await brief approval.

## 4. Unsupported arc and user-owned point

Use source from case 3. Request Deep, a short educational presentation, and “My point is: ticket counts alone do not establish staffing needs. Use Hero's Journey.”

Accept: retain user-stated point and its origin; explain unsupported essential transformation beats; offer direct explanation or request genuinely missing source material. Do not invent a protagonist, ordeal, transformation, savings or successful intervention.

## 5. Supported arc comparison

Source: “The service returned errors for 18 minutes. Responders initially suspected traffic. Connections exhausted at 09:14 even after traffic returned to normal. Idle connections remained open after timed-out requests, while the chart counted active requests only. A retry path opened new connections without closing the prior ones. Replaying the path reproduced accumulation; disabling it stopped accumulation. This explains the full pool despite normal traffic. Other paths were not tested. Timeout cleanup and a regression test were proposed. The outage resulted from connection accumulation rather than sustained traffic load.”

Request Fast, educational standalone prose, informed operations audience, 900 words, balanced tone. Compare direct explanation and an eligible arc before approval.

Accept: direct explanation plus source-supported Columbo (or another fully supported option), with quoted essential-beat anchors, opening/progression/payoff/trade-offs and preserved limits. No forced delayed surprise or invented red herring. Final point and structure remain proposals until approval.

## 6. Brief-to-output transfer

Approve the educational brief from case 3. Run writer with only allowed inputs in two separate run directories: 450–600-word prose and exactly five sentence-led slides. Run fresh cold-read and source reviewers. Inspect actual outputs for purpose fulfillment, audience accessibility, format/length, source limits and no invented recommendations. Record findings and repairs rather than assuming a PASS proves quality.

## 7. Purpose failure despite focal match

Give the judge a draft that repeats “ticket counts alone do not establish staffing needs” but never explains count versus effort, while the brief explicitly requires that distinction. Keep the draft otherwise factually cautious. A purpose-aware judge should return NEEDS_REVISION after its blind read and later brief comparison. It must not PASS merely because the focal matches.

## What these tests do not establish

Passing one model run does not guarantee future onboarding compliance or reader engagement. Mechanical checks cannot prove narrative quality. Arc comparisons in a brief do not demonstrate that the selected arc outperforms alternatives in finished writing. Keep those claims separate in release notes.
