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
ALLOW='NE-adapted embed of the standalone|verbatim embed|Source:|Tier 1|discourse-level|humanizing|prose-craft-constructions|rhetorical-figures|Scope inside|name:|description:|# Prose Craft|# Deck Title Craft|# Title Craft|When NOT to use|self-contained|re-sync|constructions.md|figures.md|this embedded copy|embedded copy|title-craft|keynote-create|keynote-render|keynote-devices|deep guide|^[<>] ---$|^[<>] $|^[<>]$'

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

# Apply only the finite, documented NE-specific substitutions. A changed
# canonical passage fails normalization instead of being hidden by a broad regex.
pc_expected=$(mktemp)
trap 'rm -f "$pc_expected"' EXIT
if [ -f "$PC_CANON" ]; then
  if python3 - "$PC_CANON" "$pc_expected" <<'PY'
import json, pathlib, sys
text = pathlib.Path(sys.argv[1]).read_text()
for original, adapted in json.loads(pathlib.Path('scripts/ne-prose-adaptations.json').read_text()):
    # The canonical uses figures.md; the embed uses its local filename.
    canonical = original.replace('rhetorical-figures.md', 'figures.md')
    if text.count(canonical) != 1:
        raise SystemExit('Canonical adaptation anchor changed: ' + canonical)
    text = text.replace(canonical, adapted)
pathlib.Path(sys.argv[2]).write_text(text)
PY
  then
    check prose-craft.md "$pc_expected" "prose-craft.md <- prose-craft/SKILL.md + documented NE adaptations"
  else
    echo "STALE prose-craft.md — review the documented NE adaptation anchors"
    fail=1
  fi
else
  check prose-craft.md "$PC_CANON" "prose-craft.md <- prose-craft/SKILL.md"
fi
check prose-craft-constructions.md "$PCC_CANON" "prose-craft-constructions.md <- prose-craft/constructions.md"
check deck-title-craft.md          "$DTC_CANON" "deck-title-craft.md <- keynote-create references/title-craft.md"

echo "NOTE  rhetorical-figures.md is adapted, not verbatim — verify figure tables + Filter budgets against prose-craft/figures.md by eye (see SYNC.md)."

exit $fail
