# Narrative Engine

Narrative Engine is a skill for turning notes, reports and research into a clear, engaging argument. It can write articles, essays, briefings and presentation narratives.

It starts by working out who the piece is for, what it needs to accomplish and what the source actually supports. Then it helps you choose the main point and how the piece should unfold. It writes and reviews the result against that brief.

## How it works

Every new piece begins with a required choice. There is no default:

- **Deep:** work through the unanswered framing questions together.
- **Fast:** let the agent infer missing answers and show you its assumptions and proposed brief for approval.

Asking for a “quick pass” does not select Fast. Both modes do the same analysis and reviews.

The process is:

1. **Define the assignment.** Choose the purpose—educate, persuade, inspire, align, report, defend or engage—and describe what success means.
2. **Understand the audience.** Establish what they know, believe and care about. Choose prose, a presentation or both, and set the intended use and length.
3. **Read the material.** Identify useful evidence, strong passages, uncertainty, conflicting findings and missing information. Explain why particular material matters to this audience.
4. **Explore possible points.** Compare a few claims or insights, with their support and limitations.
5. **Compare ways to tell it.** See a direct explanation alongside any narrative arc the material supports. Each option shows an opening, progression, payoff and trade-off.
6. **Approve the brief.** Choose the point and structure together, with the writing treatment and evidence boundaries visible.
7. **Write and review.** A separate writer follows the brief. Reviewers check what the result actually communicates, whether it fulfills the purpose and whether its claims hold up against the source.

You can choose the amount of detail, assumed reader knowledge, rhythm and tone separately. A detailed piece can still be accessible; a short piece can still be written for specialists.

## A worked example

This is a fictional example of the process, not a recorded result.

**The source:** A team reviewed 100 support tickets from one week. Forty-two concerned initial setup. Managers selected the sample; it was not random. No onboarding improvement was tested, and the review did not measure staffing needs.

**The assignment:** Write a short briefing to educate managers who assume that more tickets always require more staff.

The skill connects the assignment to the evidence:

> The setup finding helps explain that requests have different causes. But counting requests does not tell us how much work they require, and this sample cannot establish staffing needs.

It offers possible points:

- “Ticket counts alone do not establish staffing needs.”
- “The review identifies a setup problem worth investigating, but not a proven solution.”

It then compares structures. A direct explanation can work: explain what the sample shows, what it cannot show, and what information would answer the staffing question. A mystery or transformation arc would need events or discoveries this source does not contain, so it should be rejected.

You choose the first point. The resulting brief calls for a plain explanation of counts, causes and effort, preserves the sample limitations, and avoids a sales pitch for an untested intervention.

A different source could support a different structure. A retrospective with a documented outcome, overlooked clue and tested mechanism might suit **Columbo**: state what happened, then reconstruct why. You see that outline alongside the direct explanation before choosing.

## What the narrative arcs do

The ten arcs offer different ways to organize understanding:

| Arc | Useful movement |
|---|---|
| Prestige | Expectation → contradiction → reinterpretation |
| Mystery Box | Question → clues → explanation |
| Heist | Goal → obstacles → capabilities → execution |
| Time Machine | Possible futures → causes → present choice |
| Trojan Horse | Familiar case → deeper implication → new frame |
| Hero’s Journey | Starting position → challenges → transformation |
| Freytag | Developing conflict → turning point → consequences |
| Columbo | Known outcome → reconstruction → explanation |
| Game of the Scene | Examples → recurring pattern → recognition |
| Rashomon | Different accounts → comparison → synthesis |

An arc earns its place through the source. Essential stages need evidence. Missing ones reject the arc; optional stages can be omitted. There is always a direct-explanation option. No invented surprise, obligatory emotional reversal or minimum number of sections.

## What it is good at

- Finding a useful main point in substantial source material.
- Adapting the same material for different audiences and purposes.
- Turning disconnected sections into a connected argument.
- Comparing narrative approaches before committing to one.
- Making uncertainty and limits harder to lose during rewriting.
- Producing written presentation sequences as well as prose.

## What it is less good at

- **Supplying missing evidence.** It works from the material you provide. It does not automatically research a weak claim into a strong one.
- **Knowing your audience without context.** It can suggest assumptions, but you are better placed to correct them.
- **Guaranteeing a compelling hook.** A source may support a useful explanation without a dramatic discovery.
- **Guaranteeing truth or reader response.** Writers and reviewers are language models. Their judgments can be wrong, and choosing a named arc does not prove it will engage readers better.
- **Producing finished visual decks.** Its presentation output is written content and, where needed, narration—not a rendered PDF, PowerPoint or Keynote file.

**Instruction limits:** the mode choice is required by the skill, but it is an instruction rather than a software-enforced dialog. Some hosts give an explicit “no questions” request priority over skill instructions. Avoid that conflict, or state that the Fast/Deep choice must still be asked.

Deep mode takes more conversation. Fast reduces the back-and-forth, but you still need to inspect and approve the brief. Independent writing and review also use more time and tokens than a single prompt.

## How to install it

The writing guides and narrative references are included. No other writing or presentation skill is required.

### Claude Code

For a new installation:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/nraford7/Narrative-Engine.git ~/.claude/skills/Narrative-Engine
```

Start a new session and ask:

```text
Use Narrative Engine in Deep mode on my report.
I want a short briefing for our leadership team.
Help me establish the purpose and main point before writing.
```

### Codex

For a new standalone installation:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/nraford7/Narrative-Engine.git ~/.agents/skills/narrative-engine
```

Start a new session and ask for `narrative-engine` (Narrative Engine) by name. If several installed skills expose that name, specify the standalone installation path.

The agent resolves references from the installed folder. Independent reviews require a host that supports isolated agents. If those are unavailable, the skill should disclose that limitation and label the result as a draft rather than claim independent review.

### Updating

From the installation you want to update:

```bash
git pull --ff-only
```

If you have edited the skill locally, preserve your changes when updating. The clone commands above are for new installations, not replacements for existing folders.

## Files and examples

[SKILL.md](SKILL.md) contains the workflow. [Framework selection](framework-selection.md) explains how structures qualify. The [prompts](prompts/) contain the writer and reviewer instructions. The [examples](examples/) show complete framing decisions using fictional material. [SYNC.md](SYNC.md) records the included craft references.

For repeatable checks, run `bash scripts/check-rebuild.sh` and follow the [behavioral scenarios](tests/behavioral-scenarios.md). These check instructions and observed behavior; they do not certify the quality of every future piece.
