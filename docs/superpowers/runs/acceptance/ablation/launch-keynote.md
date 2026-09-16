**Punchline:** Approve AED 1.9M and two dedicated engineers for six months to address recurring flag failures and monitoring that misses customer-visible outages.

## Title sequence
1. AED 1.9M. Two engineers. Six months.
2. 9:14 blank. 9:30 board presentation. 9:41 restored.
3. The product is good.
4. 41 flags. One Redis instance.
5. Three degradations. Four quarters. No alerts.
6. Availability, customer journeys, infrastructure classification
7. Approve the investment. The renewal at risk is worth 14x the ask.

## Slide 1 — AED 1.9M. Two engineers. Six months.
**Headline:** AED 1.9M. Two engineers. Six months.

**Spotlight:** The reliability investment deferred in the last two planning cycles: a highly available flag store, synthetic monitoring of customer outcomes, and an infrastructure re-classification review. Source: Post-launch review, paragraph 5.

**Design note:** Show the budget, staffing and duration as three large figures, with the requested approval beneath them.

**Spoken narration:** We are asking you to approve AED 1.9M and two dedicated engineers for six months. The investment addresses recurring flag failures and a monitoring gap that leaves us learning about customer-visible outages from customers. Here is why the deferred work needs approval.

## Slide 2 — 9:14 blank. 9:30 board presentation. 9:41 restored.
**Headline:** 9:14 blank. 9:30 board presentation. 9:41 restored.

**Spotlight:** Our largest customer's dashboard went blank on launch morning. Their CFO was due to present our numbers to their board at 9:30. We restored service at 9:41. They have not signed the renewal. Source: Post-launch review, paragraph 1.

**Design note:** Use a timeline with three labeled timestamps. Place the unsigned renewal beneath the restoration marker.

**Spoken narration:** At 9:14, our largest customer's dashboard went blank. Their CFO was presenting our numbers to their board at 9:30; we restored service at 9:41. The account team watched a spinner while a nine-figure relationship was exposed. Service returned. The renewal remains unsigned.

## Slide 3 — The product is good.
**Headline:** The product is good.

**Spotlight:** Week-one analytics activation: 61% of eligible accounts against a 45% target. Latency: down 34% against Meridian 1.9. Support ticket volume: flat. Source: Post-launch review, paragraph 3.

**Design note:** Compare activation with its target; show latency and ticket volume as separate supporting figures.

**Spoken narration:** The rest of the launch worked. Analytics activation reached 61% of eligible accounts in week one, ahead of the 45% target. Latency is down 34% against 1.9, and support ticket volume is flat. Those results make the outage's cause worth understanding: the feature-flag service failed under launch traffic.

## Slide 4 — 41 flags. One Redis instance.
**Headline:** 41 flags. One Redis instance.

**Spotlight:** Meridian 2.0 shipped behind 41 flags. The single Redis flag store hit connection limits under launch traffic and returned defaults that hid the dashboard module. Every service stayed green. Source: Post-launch review, paragraph 2.

**Design note:** Diagram the sequence: launch traffic, connection limits, returned defaults, hidden dashboard. Show green service status alongside the blank customer dashboard.

**Spoken narration:** The flag store was a single Redis instance, classified as "non-critical infrastructure" in 2023. Launch traffic pushed it into connection limits. The flag service began returning defaults, and those defaults hid the dashboard module. Our monitoring watched services. The customer's experience disappeared while every service stayed green.

## Slide 5 — Three degradations. Four quarters. No alerts.
**Headline:** Three degradations. Four quarters. No alerts.

**Spotlight:** This was the third flag-related degradation in four quarters. Each remained invisible to alerting until a customer reported it. Infrastructure labeled non-critical in 2023 now sits in the serving path of everything we sell; its monitoring never followed that change. Source: Post-launch review, paragraph 4.

**Design note:** Pair the recurrence count with the original 2023 classification and today's serving role. Avoid inventing dates or details for the earlier incidents.

**Spoken narration:** This is the third flag-related degradation in four quarters, and customers reported each one before our alerting saw it. The recurring problem is a change in infrastructure's role without a corresponding change in its monitoring. Dependencies labeled non-critical in 2023 now sit in the serving path of everything we sell.

## Slide 6 — Availability, customer journeys, infrastructure classification
**Headline:** Availability, customer journeys, infrastructure classification

**Spotlight:** Six-month scope: a highly available flag store; outcome-level synthetic monitoring on the top five customer journeys; a re-classification review of all 2023-era "non-critical" infrastructure. Source: Post-launch review, paragraph 5.

**Design note:** Use three rows pairing the observed gap with its proposed work: single instance with availability, missed outcomes with journey monitoring, outdated labels with re-classification.

**Spoken narration:** The proposed work follows the failures we observed. Build a highly available flag store. Add outcome-level synthetic monitoring to the top five customer journeys. Review all infrastructure labeled non-critical in 2023. AED 1.9M and two dedicated engineers for six months are the requested resources for that scope.

## Slide 7 — Approve the investment. The renewal at risk is worth 14x the ask.
**Headline:** Approve the investment. The renewal at risk is worth 14x the ask.

**Spotlight:** Approve AED 1.9M and two dedicated engineers for six months. The renewal at risk is worth 14x the investment request. Source: Post-launch review, paragraph 5.

**Design note:** Place the approval request beside the source's 14x comparison, explicitly labeled "renewal at risk / investment ask."

**Spoken narration:** The renewal at risk is worth fourteen times this ask. That is exposure, rather than a promised return or a guarantee of renewal. Approve AED 1.9M and two dedicated engineers for six months to address the flag dependency, the customer-outcome monitoring gap and the outdated infrastructure classifications.