# Narrative Engine

A Claude Code skill for developing source-supported arguments as presentations or prose. It establishes the audience and purpose, reads the material, builds an argument outline, and checks the resulting piece through separate comprehension and evidence reviews.

## Workflow

1. **Choose the communication situation.** Import the source, choose Fast or Guided mode, and identify the audience, ask, format and density. Presentations support Boardroom sentence titles or Keynote fragments with narration.
2. **Find the focal claim.** A Material Read identifies stakes, tensions, strongest passages and any genuine surprise. Two or three candidates are surfaced even in Fast mode. User-selected claims remain under the user's control.
3. **Develop the argument.** Explain what each section contributes before choosing a shape. Answer-first is the default. Named arcs are optional and must have source-supported essential beats.
4. **Approve the compiled brief.** The builder receives the brief, source and embedded craft files. Catalogs are references for the orchestrator and reviewers; their relevant guidance is compiled into the brief.
5. **Build the piece.** The builder follows the argument, checks the title or section-opening sequence, preserves qualifications, and applies sentence craft. Ornament is optional; a plain, supported sentence passes.
6. **Review and repair.** A blind reader checks what the piece communicates. A separate reviewer checks claims against the source. Repairs use one bounded route, with unresolved findings retained and surfaced.

Fast mode infers the discovery choices and presents one consolidated brief for correction or approval. Guided mode asks step by step. Content determines length; there are no minimum slide or word counts.

## Gates

| Gate | Purpose |
|---|---|
| Shape fit, Phase 3 | Named arcs must pass a source-support audit and the skeleton stamp test. Direct explanation is a valid choice. |
| Focal fidelity, Phase 4.6 | Read the audience-facing body before the source or brief. Check recovered point, engagement and the register-appropriate argument sequence. |
| Humanizing check, Phase 4.7 | Flag repetitive or manufactured writing; repairs return to the builder. This check never directly edits the approved draft. |
| Evidence review, Phase 4.8 | Check unsupported claims, changed qualifications, missing reasoning, ask overreach and provenance tags against the original material. |

A focal mismatch may reopen discovery once when the focal was inferred. User-stated or selected focals receive an advisory instead. Any revision receives evidence review; the first evidence audit covers the full draft. Later audits check changes and prior findings. Review caps escalate unresolved issues rather than silently approving them.

Specialist reviews add audience and persuasion checks for high-stakes material. The narrative-structure research informing the humanizing checklist is fiction-derived; its percentages are directional context, not validated deck-quality thresholds.

## Outputs

Each run uses its own `/tmp/ne-<date>-<slug>/` directory.

| File | Contents |
|---|---|
| `ne-build-brief.md` | Audience, ask, focal origin, Material Read, argument outline and compiled instructions |
| `ne-source-content.md` | Original source material |
| `ne-output.md` | Audience-facing presentation or prose |
| `ne-output-meta.md` | Focal metadata, executed outline, source anchors and revision notes; withheld from the blind judge |
| `ne-cold-read.md` | Reader's recovered argument and subsequent source check |
| Review reports | Focal, evidence and humanizing findings, archived before resolved trigger files are removed |

Unresolved reports survive escalation. The sidecar remains available through delivery. For a presentation, the later rendering stage invokes the existing keynote-create renderer; this rebuild changes Narrative Engine only.

## Installation and use

Clone into the Claude Code skills directory:

```bash
git clone https://github.com/nraford7/Narrative-Engine.git ~/.claude/skills/Narrative-Engine
```

Invoke `/Narrative-Engine` and supply your material. The build's sentence and title-craft resources are embedded, so they do not require separate skill invocations.

## Reference library

- [SKILL.md](SKILL.md): operative workflow and file contracts.
- [framework-selection.md](framework-selection.md): conditional selection, payload fit and source-support tests.
- [narrative-arcs.md](narrative-arcs.md) and [communication-frameworks.md](communication-frameworks.md): optional structures.
- Audience, voice, emotional-arc, opening/closing and rhetorical-figure catalogs: orchestrator/reviewer references.
- [prose-craft.md](prose-craft.md), [prose-craft-constructions.md](prose-craft-constructions.md), [deck-title-craft.md](deck-title-craft.md), and [humanizing-pass.md](humanizing-pass.md): embedded craft resources.
- [prompts/](prompts/): builder, blind judge, evidence reviewer and specialist contracts.
- [SYNC.md](SYNC.md): canonical sources and exact Narrative Engine adaptations.

## Verification

```bash
bash scripts/check-rebuild.sh
bash scripts/check-sync.sh
```

The first command checks key workflow invariants; the second checks embedded material against locally available canonicals, including a finite list of documented adaptations. Neither substitutes for behavioral acceptance tests. Historical development plans and acceptance records remain available in Git history.
