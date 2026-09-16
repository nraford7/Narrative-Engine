# Narrative Engine

**Turn a pile of information into a story or argument people can follow.**

Narrative Engine is a skill for Claude Code. Give it a report, rough notes, an article or an existing presentation, and tell it who you want to reach. It helps find the point worth making, choose an opening, arrange the evidence and write the piece.

The aim is to make each part lead somewhere. In a presentation, the slide titles should carry an argument when read in order. In an article or briefing, the sections should develop an idea rather than repeat it in different words.

It can produce:

- **Presentation content:** slide titles, supporting text and visual suggestions.
- **Prose:** a briefing, article, essay or other written piece.
- **Both:** develop one version, then adapt it to the other format.

## How it works

1. **Understand the audience and the purpose.** Who is this for? What should they understand, decide or do after reading it?
2. **Read for what matters.** Look for the real stakes, an unresolved question, a useful finding or a strong passage already in the source. A surprise is useful when one exists; it should never be invented.
3. **Offer a few possible main points.** Claude proposes two or three directions and explains the choice. You can choose one, change it or keep the point you started with.
4. **Work out the argument.** Decide what the reader needs to understand and what each section adds. The usual approach is to state the answer early and explain it. Storytelling structures are available when the material suits them.
5. **Write and review.** One reviewer reads the piece before seeing the brief, checking what it actually communicates. Another compares its claims with the source. Claude repairs problems it finds and brings unresolved issues back to you.

You choose how much guidance to give:

- **Fast:** Claude makes the initial choices and shows you one brief to correct or approve.
- **Guided:** Claude asks the questions one at a time.

For presentations, you can also choose **Boardroom**, with full-sentence titles that carry the argument, or **Keynote**, with shorter titles supported by spoken narration. The amount of useful material determines the length.

## A worked example

This is a fictional, simplified example showing the intended approach, not a recorded test output.

### The starting material

> Over a six-week period, our support team's average first reply fell from six hours to two hours. Average time to resolve a ticket stayed at five days. Tickets needing engineering help waited an average of three days before an engineer took ownership. The team proposes a four-week pilot that assigns an engineer when those tickets are escalated. We need the head of customer operations to approve the pilot.

You could ask:

```text
/Narrative-Engine

Turn these notes into a short presentation for our head of customer
operations. The decision is whether to approve the four-week pilot.
Use Fast mode and Boardroom titles. Keep the limits of the evidence clear.
```

### Finding the point

A topic list would be easy: response times, resolution times, engineering, next steps. It would leave the reader to work out why those subjects belong together.

The useful tension is that the team's headline improvement has not shortened the customer's wait for a fix. The engineering handoff gives the team a specific next step to test.

A possible main point is:

> Test earlier engineering ownership to see whether it shortens the time customers wait for a fix.

### Building the sequence

| Slide title | What the slide establishes |
|---|---|
| **Faster replies still leave customers waiting five days for a fix.** | First replies improved from six hours to two; average resolution time stayed unchanged. |
| **Tickets needing engineering wait three days for someone to take ownership.** | There is a specific delay worth investigating within that group of tickets. |
| **Assign an engineer at escalation and test whether that wait falls.** | The proposed pilot addresses the observed handoff delay. Its effect is still unknown. |
| **Approve a four-week pilot and measure whether customers get their fixes sooner.** | The decision and the measure of success follow from the opening problem. |

The opening gives the audience a reason to care. The middle identifies a possible explanation and a practical test. The ending asks for a decision the evidence can support.

The evidence reviewer should catch a title such as “Earlier engineering ownership will cut resolution time.” The notes support testing that idea; they do not establish that it works. The three-day figure also applies specifically to tickets needing engineering, not to every ticket.

## What it's good at

- **Turning reports into arguments.** Useful for decision papers, executive briefings, research summaries and presentations that have plenty of information but no clear direction.
- **Connecting slide titles.** Helping a sequence move from a question or finding to its implications and a decision.
- **Finding a useful opening in existing material.** Especially when a concrete detail or tension is buried under background information.
- **Keeping claims close to the evidence.** Checking that a possibility has not become a promise, or an association has not become a claim of cause and effect.
- **Adapting a piece for a particular audience.** The same material may need a different starting point for a board, a technical team or a general audience.

## What it's not so good at

- **Getting the hook right every time.** It can choose a sensible but predictable opening, or introduce a recommendation before the reader has a reason to care. Your judgment still matters.
- **Matching a distinctive voice without examples.** Give it passages you like, especially if warmth, humor or an unusual style is important.
- **Making weak material persuasive.** Missing evidence and unclear decisions often need more work from the author. Better wording cannot supply the missing substance.
- **Checking whether the source itself is true.** Its evidence review compares the writing with the material you provide. It is not independent research or external fact-checking.
- **Quick, tiny edits.** The questions and review stages can be excessive for a short email or a single sentence. They also use more time and model allowance than a simple writing prompt.
- **Producing finished slide design on its own.** It develops presentation content. The later rendering step uses the separate [keynote-create](https://github.com/nraford7/keynote-create) tools and their setup.

The latest small comparison found stronger results for source fidelity and argument flow than for opening hooks. It used Codex-generated drafts against saved earlier outputs while Claude was unavailable, so it cannot cleanly separate improvements in the skill from differences between models. Treat it as useful evidence, not a guarantee.

## How to install it

You'll need **Claude Code** and **Git**. This repository is set up for Claude Code's local skills, rather than a plain chat window. See [Claude Code's guide to skills](https://code.claude.com/docs/en/skills) for how local skills are loaded.

### 1. Download the skill

Open a terminal and run:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/nraford7/Narrative-Engine.git ~/.claude/skills/Narrative-Engine
```

This puts the skill in your personal skills folder, where Claude Code can use it across projects.

### 2. Check the file paths

Some instructions currently contain paths from the maintainer's computer. If you are installing on another computer, ask Claude Code:

```text
I installed Narrative Engine in ~/.claude/skills/Narrative-Engine.
Check the instructions in its prompts folder and update any paths beginning
/Users/noahraford/.claude/skills/Narrative-Engine/ to point to my installation.
Keep all other instructions unchanged.
```

The writing guides are included in the repository. You do not need to install prose-craft separately to use them. Finished slide rendering requires the separate keynote-create setup mentioned above.

### 3. Try it

Start Claude Code and type:

```text
/Narrative-Engine
```

Then paste your material or point Claude to a file, and say who it is for and what you want the piece to achieve. For example:

```text
Use Narrative Engine on quarterly-review.md. Write a short briefing for
our leadership team. They need to decide which of the three proposals
to fund. Use Fast mode, and preserve the uncertainty in the estimates.
```

### Updating an existing installation

If you have not changed the local files:

```bash
git -C ~/.claude/skills/Narrative-Engine pull --ff-only
```

If you adjusted file paths or other instructions, ask Claude to preserve those changes while updating. Do not overwrite your customizations just to make the update succeed.

## Looking under the hood

[SKILL.md](SKILL.md) contains the full workflow. The [prompts folder](prompts/) contains the writer and reviewer instructions, and [SYNC.md](SYNC.md) explains where the included writing guides come from. Historical development plans and test records remain in Git history.
