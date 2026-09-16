**Punchline:** Approve AED 1.9M and two dedicated engineers for six months to address recurring customer-visible failures in infrastructure now critical to Meridian.

## Title sequence
1. Approve AED 1.9M to address recurring failures customers see.
2. The launch exposed those failures at our largest customer.
3. A failing flag store hid the customer's dashboard.
4. Our alerts have missed three flag degradations in four quarters.
5. Strong product results coexist with this reliability gap.
6. Fund two engineers for six months to address the gap.

---

## Slide 1 — Approve AED 1.9M to address recurring failures customers see.
**Headline:** Approve AED 1.9M to address recurring failures customers see.
**Spotlight:** The reliability investment was deferred in the last two planning cycles. The renewal now at risk is worth 14x the ask. Requested commitment: AED 1.9M and two dedicated engineers for six months. Source: Post-launch review, paragraph 5.
**Design note:** Place the requested commitment beside the renewal-to-ask ratio; label the renewal as at risk.

---

## Slide 2 — The launch exposed those failures at our largest customer.
**Headline:** The launch exposed those failures at our largest customer.
**Spotlight:** At 9:14, our largest customer's dashboard went blank. Their CFO was presenting our numbers to their board at 9:30. Service returned at 9:41. The customer has not signed the renewal. Source: Post-launch review, paragraph 1.
**Design note:** Use a three-point timeline: dashboard blank, scheduled board presentation, service restored. Place renewal status beneath it.

---

## Slide 3 — A failing flag store hid the customer's dashboard.
**Headline:** A failing flag store hid the customer's dashboard.
**Spotlight:** Meridian 2.0 shipped behind 41 flags. The flag store, a single Redis instance classified as "non-critical infrastructure" in 2023, hit connection limits under launch traffic. It returned defaults that hid the dashboard module. The feature-flag service caused the outage. Source: Post-launch review, paragraph 2.
**Design note:** Show the causal sequence as four connected boxes: launch traffic, connection limits, returned defaults, hidden dashboard.

---

## Slide 4 — Our alerts have missed three flag degradations in four quarters.
**Headline:** Our alerts have missed three flag degradations in four quarters.
**Spotlight:** Every service stayed green during this incident. All three flag-related degradations were invisible to alerting until a customer reported them. Infrastructure labeled non-critical in 2023 now sits in the serving path of everything we sell; its monitoring never followed that change. Source: Post-launch review, paragraphs 2 and 4.
**Design note:** Pair green service indicators with the blank dashboard, then display the recurrence count beneath them.

---

## Slide 5 — Strong product results coexist with this reliability gap.
**Headline:** Strong product results coexist with this reliability gap.
**Spotlight:** Week-one activation of the new analytics module reached 61% of eligible accounts, ahead of the 45% target. Latency is down 34% against version 1.9. Support ticket volume is flat. Source: Post-launch review, paragraph 3.
**Design note:** Show activation against its target, latency against version 1.9, and ticket volume as flat. Keep each comparison explicitly labeled.

---

## Slide 6 — Fund two engineers for six months to address the gap.
**Headline:** Fund two engineers for six months to address the gap.
**Spotlight:** Approve AED 1.9M and two dedicated engineers for six months to deliver:
- A highly available flag store.
- Outcome-level synthetic monitoring on the top five customer journeys.
- A reclassification review of all 2023-era "non-critical" infrastructure.

Source: Post-launch review, paragraph 5.
**Design note:** Present the three workstreams beneath a single approval line stating budget, staffing, and duration.