# Brief workflow validation — 2026-09-17

These are observed instruction-following checks in Codex, not a guarantee of future compliance, an evaluation of reader engagement, or a Claude runtime certification. Fictional fixtures are in behavioral-scenarios.md. No whole production workflow was claimed: discovery responses and isolated writer/reviewer stages were tested separately.

| Check | Observation |
|---|---|
| Fresh CLI, quick briefing with no explicit mode | Asked Fast/Deep and stopped. |
| Fresh CLI, Deep with missing framing | Asked purpose first and stopped for the answer. |
| Fresh CLI, explicit standing preference requiring mode even with “no questions” | Asked Fast/Deep and stopped. |
| Fresh CLI, Fast educational retrospective | Compared direct explanation and a source-supported Columbo outline, quoted essential-beat support, preserved limits, requested approval before drafting. |
| Independent Fast presentation framing, supplied point + unsupported Hero's Journey | Rejected unsupported essential beats; preserved user-stated focal; proposed direct explanation and waited for approval. |
| Independent Fast framing, same ticket source with persuasive purpose | Proposed a bounded investigation, preserved sample/effectiveness limits, and requested approval; unlike the educational brief, included a supportable action and possible objection. |
| Isolated writer, approved educational prose brief | Produced a 450–600-word briefing preserving audience, purpose and source limits. |
| Isolated writer, approved presentation brief | Produced exactly five slides with bounded supporting text. |
| Fresh blind prose judge, body → source → prior check → brief | PASS; explained the required count/cause/effort distinctions. |
| Separate evidence reviewer, prose and presentation | Both CLEAN; no blocking or minor findings. |
| Fresh blind judge, focal-matching but explanation-free draft | NEEDS_REVISION: repeating the point did not satisfy the educational success condition. |
| Independent release review | Three actionable findings fixed: prebuild reviewer inputs, external guidance references and a complete example brief. Recheck found no remaining release-blocking inconsistency. |

## Known mode-gate limitation

Two fresh CLI runs with an explicit “just write it, no questions” request and no standing preference bypassed the skill's mode rule and produced a briefing. Moving the rule to the entrypoint did not resolve this direct instruction conflict. A normal “quick” request and the same conflict with the user's standing mode preference explicitly supplied both stopped correctly. The README documents this host instruction-precedence limitation. The skill never intentionally defaults to Fast, but the interaction gate is not software-enforced.

The initial three-case simulated next-response inspection also passed, but missed this conflict. It is not counted as evidence of an end-to-end pass.

## Mechanical checks

- All 13 existing rebuild guards passed.
- Embedded prose-craft synchronization passed; the title guide is now explicitly maintained locally rather than compared to another installed skill.
- All three sync-check regression tests passed.
- Skill metadata validation passed after normalizing the identifier to `narrative-engine`.
- Local links in entrypoint, README, prompts and examples resolved; whitespace check passed.

The ten narrative arcs remain available. Reference simplification removes categorical prescriptions and conflicting rhetorical quotas; it does not establish improved output quality without comparative reader testing.
