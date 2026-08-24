# Embed Sync Manifest

Narrative Engine embeds copies of external material so the build subagent runs standalone. Copies drift when their canonicals change. This manifest is the ledger; `scripts/check-sync.sh` is the mechanical check. Run it after editing this repo OR any canonical listed below.

| Embed (this repo) | Canonical | Type | Last synced |
|---|---|---|---|
| `prose-craft.md` | `~/Dropbox/Noah_Remote_Shared/claude-brain/skills/prose-craft/SKILL.md` | Verbatim body (header + scope section + file refs differ by design) | 2026-08-24 @ canonical `b6cdbe0` |
| `prose-craft-constructions.md` | `~/Dropbox/Noah_Remote_Shared/claude-brain/skills/prose-craft/constructions.md` | Verbatim (title + internal refs differ) | 2026-08-24 |
| `deck-title-craft.md` | `~/Projects/keynote-create-skill/references/title-craft.md` | Verbatim body (header differs) | 2026-08-24 |
| `rhetorical-figures.md` | `~/Dropbox/Noah_Remote_Shared/claude-brain/skills/prose-craft/figures.md` | **Adapted, not verbatim** — this file adds NE-specific sections (humanizing-pass tie-in, deck-title tests); the figure tables and Filter budgets must stay aligned | 2026-08-24 |

## Sync procedure

1. Run `scripts/check-sync.sh`. It diffs each verbatim pair, filters known-benign header/ref differences, and prints anything else.
2. If a pair is stale: apply the canonical's changes to the embed (keep the embed's header banner and local file references), update the Last synced column, and note the canonical's commit sha where it has one.
3. `rhetorical-figures.md` is checked by eye: confirm the figure tables and the Filter reconciliation budgets (anaphora ≤2, one tricolon/section, zero negative-parallelism) match `figures.md`.
4. Update the embed banner's re-synced date inside the file itself.
