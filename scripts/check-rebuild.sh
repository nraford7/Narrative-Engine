#!/usr/bin/env bash
# check-rebuild.sh — mechanical grep gates for the 2026-09-16 NE spine rebuild.
# Run from anywhere; resolves the repo root from its own location.
# One OK/FAIL line per gate. Exit 1 if any gate fails, 0 otherwise.

set -u

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT" || exit 1

FAILED=0

pass() { printf 'OK   Gate %s: %s\n' "$1" "$2"; }
fail() { printf 'FAIL Gate %s: %s\n' "$1" "$2"; FAILED=1; }

# ---------------------------------------------------------------------------
# Gate 1 — builder.md references no catalogs (voice-profiles, audience-profiles,
# emotional-arcs, opening-closing-strategies, narrative-arcs).
# ---------------------------------------------------------------------------
if grep -q -E 'voice-profiles|audience-profiles|emotional-arcs|opening-closing-strategies|narrative-arcs' prompts/builder.md; then
  fail 1 "prompts/builder.md references a catalog file"
else
  pass 1 "prompts/builder.md has zero catalog references"
fi

# ---------------------------------------------------------------------------
# Gate 2 — body-only output template: no focal metadata in the ne-output.md
# template region of builder.md, and no "Focal Statement:" before the sidecar
# section (all focal metadata lives in ne-output-meta.md).
# ---------------------------------------------------------------------------
g2_ok=1
if awk '/^### `ne-output\.md`/{on=1} /^### `ne-output-meta\.md`/{on=0} on' prompts/builder.md \
   | grep -q -i 'focal'; then
  g2_ok=0
fi
sidecar_line="$(grep -n '^### `ne-output-meta\.md`' prompts/builder.md | head -1 | cut -d: -f1)"
if [ -z "$sidecar_line" ]; then
  g2_ok=0
elif head -n "$((sidecar_line - 1))" prompts/builder.md | grep -q 'Focal Statement:'; then
  g2_ok=0
fi
if [ "$g2_ok" -eq 1 ]; then
  pass 2 "builder.md output template is body-only (focal metadata only in the sidecar section)"
else
  fail 2 "focal metadata found in builder.md ne-output.md template region or before the sidecar section"
fi

# ---------------------------------------------------------------------------
# Gate 3 — no unconditional ornament mandates in builder-facing files.
# "metaphor family" may appear only in ban/license phrasing (never impose /
# MAY carry / reference-banner lines); no "must ... killer line" mandate class.
# ---------------------------------------------------------------------------
BUILDER_FACING="prompts/builder.md humanizing-pass.md checklists.md"
g3_ok=1
# shellcheck disable=SC2086
if grep -h -i 'metaphor famil' $BUILDER_FACING 2>/dev/null \
   | grep -v -i -e 'never impose' -e 'MAY carry' -e 'Reference layer' \
   | grep -q .; then
  g3_ok=0
fi
# shellcheck disable=SC2086
if grep -q -i -E 'must[^.]*killer line|killer line[^.]*(must|required|mandatory)|every (piece|deck)[^.]*killer line' $BUILDER_FACING 2>/dev/null; then
  g3_ok=0
fi
if [ "$g3_ok" -eq 1 ]; then
  pass 3 "no unconditional ornament mandates in builder-facing files (metaphor family only in ban/license phrasing; no killer-line mandate)"
else
  fail 3 "unconditional ornament mandate found in builder-facing files (metaphor family outside ban/license phrasing, or a killer-line mandate)"
fi

# ---------------------------------------------------------------------------
# Gate 4 — attention-loop.md: the "one per piece" quota is gone.
# ---------------------------------------------------------------------------
if grep -q -i 'one per piece' attention-loop.md; then
  fail 4 "attention-loop.md still contains 'one per piece'"
else
  pass 4 "attention-loop.md has zero hits for 'one per piece'"
fi

# ---------------------------------------------------------------------------
# Gate 5 — reference-layer banner present on all 7 catalogs, absent from the
# builder's four craft files.
# ---------------------------------------------------------------------------
CATALOGS="narrative-arcs.md voice-profiles.md audience-profiles.md emotional-arcs.md opening-closing-strategies.md communication-frameworks.md rhetorical-figures.md"
CRAFT_FILES="prose-craft.md prose-craft-constructions.md deck-title-craft.md humanizing-pass.md"
g5_ok=1
for f in $CATALOGS; do
  if ! grep -q '\*\*Reference layer\.\*\*' "$f" 2>/dev/null; then
    g5_ok=0
  fi
done
for f in $CRAFT_FILES; do
  if grep -q -i 'Reference layer' "$f" 2>/dev/null; then
    g5_ok=0
  fi
done
if [ "$g5_ok" -eq 1 ]; then
  pass 5 "reference banner on all 7 catalogs and absent from the 4 builder craft files"
else
  fail 5 "reference banner missing from a catalog or present in a builder craft file"
fi

# ---------------------------------------------------------------------------
# Gate 6 — dispatch tables single-sourced: the example-dispatch table row
# "Investor pitch" appears in neither reviewer.md nor stress-tester.md.
# ---------------------------------------------------------------------------
if grep -q 'Investor pitch' prompts/reviewer.md prompts/stress-tester.md; then
  fail 6 "duplicated dispatch table ('Investor pitch') found in reviewer.md or stress-tester.md"
else
  pass 6 "dispatch tables single-sourced (zero 'Investor pitch' hits in reviewer.md and stress-tester.md)"
fi

# ---------------------------------------------------------------------------
# Gate 7 — FOCAL_MISMATCH wired: >=3 hits in the focal judge, >=2 in SKILL.md,
# and focal_origin present in both.
# ---------------------------------------------------------------------------
judge_fm="$(grep -c 'FOCAL_MISMATCH' prompts/focal-fidelity-judge.md 2>/dev/null || echo 0)"
skill_fm="$(grep -c 'FOCAL_MISMATCH' SKILL.md 2>/dev/null || echo 0)"
if [ "$judge_fm" -ge 3 ] && [ "$skill_fm" -ge 2 ] \
   && grep -q 'focal_origin' prompts/focal-fidelity-judge.md \
   && grep -q 'focal_origin' SKILL.md; then
  pass 7 "FOCAL_MISMATCH wired (judge=$judge_fm hits, SKILL.md=$skill_fm hits; focal_origin in both)"
else
  fail 7 "FOCAL_MISMATCH under-wired (judge=$judge_fm need >=3, SKILL.md=$skill_fm need >=2, focal_origin required in both)"
fi

# ---------------------------------------------------------------------------
# Gate 8 — framework sweep gone: no "Score all 10" / "Full Sweep" in SKILL.md
# or framework-selection.md.
# ---------------------------------------------------------------------------
if grep -q -e 'Score all 10' -e 'Full Sweep' SKILL.md framework-selection.md; then
  fail 8 "framework sweep language ('Score all 10' / 'Full Sweep') still present in SKILL.md or framework-selection.md"
else
  pass 8 "framework sweep gone (zero hits for 'Score all 10' and 'Full Sweep')"
fi

# ---------------------------------------------------------------------------
# Gate 9 — sidecar contract: ne-output-meta present in builder.md,
# evidence-reviewer.md, and SKILL.md; absent from the focal judge (cold read
# stays de-contaminated).
# ---------------------------------------------------------------------------
g9_ok=1
for f in prompts/builder.md prompts/evidence-reviewer.md SKILL.md; do
  if ! grep -q 'ne-output-meta' "$f" 2>/dev/null; then
    g9_ok=0
  fi
done
if grep -q 'ne-output-meta' prompts/focal-fidelity-judge.md 2>/dev/null; then
  g9_ok=0
fi
if [ "$g9_ok" -eq 1 ]; then
  pass 9 "sidecar contract wired (ne-output-meta in builder/evidence-reviewer/SKILL.md, absent from the focal judge)"
else
  fail 9 "sidecar contract broken (ne-output-meta missing from a writer/reader or present in the focal judge)"
fi

# Gate 10 — a focal PASS must not bypass the two remaining default gates.
if grep -q -i -E 'proceed to Phase 5' prompts/focal-fidelity-judge.md; then
  fail 10 "focal judge PASS skips Phase 4.7/4.8"
elif grep -q 'Phase 4.7' prompts/focal-fidelity-judge.md && grep -q '4.8' prompts/focal-fidelity-judge.md; then
  pass 10 "focal judge PASS routes through the remaining default gates"
else
  fail 10 "focal judge PASS has no explicit remaining-gate route"
fi

# Gate 11 — the embedded craft inputs must not restore retired mandates.
if grep -q -E 'Load it only for savored|Build at least one sentence|at least one built sentence|two or three anchor moments get|one or two built sentences per section' prose-craft.md humanizing-pass.md; then
  fail 11 "embedded craft restores catalog loading or ornament quotas"
else
  pass 11 "embedded craft has no retired catalog-loading or ornament quota instructions"
fi

# Gate 12 — retain unresolved reports on escalation and clear triggers on restart.
if grep -q 'after all gates pass (or the run escalates), delete' SKILL.md; then
  fail 12 "escalation deletes unresolved reports"
elif grep -q 'Preserve unresolved' SKILL.md && grep -q 'Fresh-draft restart' SKILL.md; then
  pass 12 "escalation retains evidence and fresh drafts clear prior triggers"
else
  fail 12 "missing escalation preservation or fresh-draft restart contract"
fi

# Gate 13 — a partial recheck can only follow a full evidence audit.
if grep -q 'first evidence review of a draft always audits the entire draft' SKILL.md; then
  pass 13 "first evidence audit covers the full draft even after an earlier-gate repair"
else
  fail 13 "first evidence audit can be mistaken for a changed-sections recheck"
fi

exit "$FAILED"
