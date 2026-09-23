# Embed Sync Manifest

Narrative Engine embeds copies of external material so the build subagent runs standalone. Copies drift when their canonicals change. This manifest is the ledger; `scripts/check-sync.sh` is the mechanical check. Run it after editing this repo OR any canonical listed below.

| Embed (this repo) | Canonical | Type | Last synced |
|---|---|---|---|
| `prose-craft.md` | `~/Dropbox/Noah_Remote_Shared/claude-brain/skills/prose-craft/SKILL.md` | Adapted body (finite NE substitutions in `scripts/ne-prose-adaptations.json`; header, scope and local refs differ) | 2026-09-23; banned-word rewording from prose-craft 558a26f; NE adaptations unchanged |
| `prose-craft-constructions.md` | `~/Dropbox/Noah_Remote_Shared/claude-brain/skills/prose-craft/constructions.md` | Verbatim (title + internal refs differ) | 2026-09-23 (prose-craft 558a26f) |
| `deck-title-craft.md` | Canonical here. Merged 2026-09-23 with keynote-create's 2026-09-17 revision (headline chain governs both registers; evidence qualifications survive in titles). keynote-create now reads this file from its vendored NE copy and keeps no title guide of its own. | Canonical, not synchronized | 2026-09-23 |
| `rhetorical-figures.md` | `~/Dropbox/Noah_Remote_Shared/claude-brain/skills/prose-craft/figures.md` | **Adapted, not verbatim** — this file adds NE-specific sections (humanizing-pass tie-in, deck-title tests); the figure tables and Filter budgets must stay aligned | 2026-09-23 (banned-word rewording, prose-craft 558a26f) |

## Sync procedure

1. Run `scripts/check-sync.sh`. It checks canonical pairs, applying only the exact prose substitutions recorded in `scripts/ne-prose-adaptations.json` before comparison. Missing or changed canonical anchors fail the check. These NE adaptations remove catalog loading, ornament quotas, and the conflict with answer-first openings. Header/ref differences remain allowed.
2. If a pair is stale: apply the canonical's changes to the embed (keep the embed's header banner and local file references), update the Last synced column, and note the canonical's commit sha where it has one.
3. `rhetorical-figures.md` is checked by eye: confirm the figure tables and the Filter reconciliation budgets (anaphora ≤2, one tricolon/section, zero negative-parallelism) match `figures.md`.
4. Update the embed banner's re-synced date inside the file itself.

The title guide is now a maintained standalone reference. Its historical provenance is preserved here; changes in another skill do not silently alter or invalidate Narrative Engine. Review title changes against the presentation behavioral scenarios and the source-fidelity rules. `check-sync.sh` continues checking the prose-craft embeds against available canonicals.
