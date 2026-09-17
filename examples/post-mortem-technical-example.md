# Educational retrospective: comparing direct explanation and Columbo

Fictional source and framing, not a recorded evaluation.

## Source

“The service returned errors for 18 minutes.” “Connections exhausted at 09:14 even after traffic returned to normal.” “Idle connections remained open after timed-out requests; the chart counted active requests only.” “The retry path opened a new connection without closing the old one.” “Replaying the path reproduced accumulation; disabling it stopped accumulation.” “That accumulation explains the full pool despite normal traffic and the resulting outage.” “Other paths were not tested.” Cleanup and a regression test were proposed, not completed.

## Assignment

Fast explicitly selected. Purpose: educate informed operations staff who know the outcome but not the mechanism. Success: explain how normal traffic coexisted with exhausted connections and where the finding stops. Standalone prose, about 900 words. Standard detail, informed knowledge, conversational rhythm, balanced tone. No funding or approval request.

## Material Read and provisional points

The distinction between requests and retained connections addresses the stated knowledge gap. The reproduction supports the retry mechanism, limited to the tested path. Candidate A explains the outage mechanism; candidate B emphasizes monitoring limits; candidate C emphasizes bounded causal tests. A best fits the assignment; B and C can support it. This is a proposal, not yet the approved focal.

## Compare structures

**Direct explanation:** mechanism first; explain request/connection distinction; walk the evidence; end with limits. Advantage: immediate comprehension. Cost: less reconstruction of how the evidence fits.

**Columbo:** known outage → apparent traffic explanation → idle-connection detail → retry mechanism → reinterpret the chart → return to the outage with its cause clear. Advantage: readers reconstruct the explanation. Cost: the mechanism arrives later.

Essential source support:

| Anchor | Quoted support |
|---|---|
| Known outcome | “The service returned errors for 18 minutes.” |
| Telltale detail | “Idle connections remained open after timed-out requests; the chart counted active requests only.” |
| Mechanism | “The retry path opened a new connection without closing the old one.” |
| Re-read evidence | “That accumulation explains the full pool despite normal traffic and the resulting outage.” |
| Callback | Return to “The service returned errors for 18 minutes” now explained by the quoted accumulation mechanism. |

The callback reuses supported evidence; it does not invent another event. No red herring or untested mechanism is added. Other-path safety remains unknown in either structure.

## Final approval

The user selects point A and Columbo together. The brief carries the retained skeleton, source anchors, limits, educational success and length. The writer must deliver the causal explanation; simply recreating suspense would fail the purpose check. A named arc is not proof of better engagement than the direct alternative.
