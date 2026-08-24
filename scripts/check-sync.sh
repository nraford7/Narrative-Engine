#!/bin/bash
# check-sync.sh — detect drift between Narrative Engine's embedded copies and their canonicals.
# Exit 0 = all in sync. Exit 1 = at least one embed is stale (diff lines printed).
# See SYNC.md for the manifest and sync procedure.

cd "$(dirname "$0")/.." || exit 2

PC_CANON="$HOME/Dropbox/Noah_Remote_Shared/claude-brain/skills/prose-craft/SKILL.md"
PCC_CANON="$HOME/Dropbox/Noah_Remote_Shared/claude-brain/skills/prose-craft/constructions.md"
DTC_CANON="$HOME/Projects/keynote-create-skill/references/title-craft.md"

# Lines that legitimately differ between embed and canonical (headers, banners,
# frontmatter, local file references). Anything NOT matching these is drift.
ALLOW='verbatim embed|Source:|Tier 1|discourse-level|humanizing|prose-craft-constructions|rhetorical-figures|Scope inside|name:|description:|# Prose Craft|# Deck Title Craft|# Title Craft|When NOT to use|self-contained|re-sync|constructions.md|figures.md|this embedded copy|embedded copy|title-craft|keynote-create|keynote-render|keynote-devices|deep guide|^[<>] ---$|^[<>] $|^[<>]$'

fail=0

check () {
  local embed="$1" canon="$2" label="$3"
  if [ ! -f "$canon" ]; then
    echo "SKIP  $label — canonical not found at $canon"
    return
  fi
  local drift
  drift=$(diff "$embed" "$canon" | grep "^[<>]" | grep -Evc "$ALLOW")
  if [ "$drift" -eq 0 ]; then
    echo "OK    $label"
  else
    echo "STALE $label — $drift unexplained line(s):"
    diff "$embed" "$canon" | grep "^[<>]" | grep -Ev "$ALLOW" | head -10 | sed 's/^/      /'
    fail=1
  fi
}

check prose-craft.md               "$PC_CANON"  "prose-craft.md <- prose-craft/SKILL.md"
check prose-craft-constructions.md "$PCC_CANON" "prose-craft-constructions.md <- prose-craft/constructions.md"
check deck-title-craft.md          "$DTC_CANON" "deck-title-craft.md <- keynote-create references/title-craft.md"

echo "NOTE  rhetorical-figures.md is adapted, not verbatim — verify figure tables + Filter budgets against prose-craft/figures.md by eye (see SYNC.md)."

exit $fail
