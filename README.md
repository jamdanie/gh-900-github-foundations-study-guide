# GH-900 GitHub Foundations study guide

Free study notes, hands-on labs, Git command references, Anki flashcards, and original practice questions.

## Table of contents

[Open the full table of contents](CONTENTS.md) for chapter sections, labs, references, and practice. Use the [alphabetical topic finder](docs/topic-finder.md) when you know the term you need.

1. [Git and GitHub basics](chapters/01-git-basics.md)
2. [Working with repositories](chapters/02-repositories.md)
3. [Collaboration and review](chapters/03-collaboration.md)
4. [Automation, editors, and AI](chapters/04-modern-development.md)
5. [Projects and planning](chapters/05-project-management.md)
6. [Security and administration](chapters/06-security-administration.md)
7. [Community and contributions](chapters/07-community.md)

Each chapter has key terms, a worked example, common points of confusion, and direct links to hands-on practice.

## Prefer visual or hands-on learning?

Use the [visual learning guide](docs/visual-learning-resources.md) for Learn Git Branching, Oh My Git!, and GitHub's interactive courses. It also explains where optional paid data-center games fit. Try the [eight hands-on challenges](practice/hands-on-challenges/README.md), [seven chapter missions](practice/visual-missions.md), or [Git diagrams](docs/visual-git-and-github.md). The challenge pack includes browser editing, file history, a simulated experiment, and worked review examples.

## How I passed without dumps

I passed GH-900 using Microsoft Learn, AI-assisted practice, occasional follow-along videos, and Anki flashcards. I did not use exam dumps.

I had AI explain the questions I was studying and ask about the same concepts in different ways. I wanted to understand what the Microsoft Learn practice questions were asking, including why the other answers did not fit. My exam was significantly different from the Learn questions. I attribute much of my success to going deeper into the content instead of only remembering an answer. It also made the material less dry.

Every once in a while, I used a follow-along video and had AI guide me through the setup so I could avoid building bad habits. My Anki cards covered commands, when to use them, how they worked, and the order I would use them. I also studied Projects, boards, timelines, Marketplace, profile settings, and account security.

This repo shares that approach and gives other people exercises to try. The labs are reader practice material, not a claim that I completed every exercise here before my exam. Read [my full study approach](docs/my-study-approach.md), then use the [exam outline](docs/exam-outline.md) to choose a section.

## New to GitHub?

Start with the [beginner guide](docs/beginner-start-here.md). It follows one small change, explains where your work is saved, and introduces Actions using this repository’s own workflow. Then try the [eight beginner checks](practice/beginner-checks.md).

For short practice sessions, use the [30 topic cards](practice/cards/README.md). Each has an expandable explanation and a follow-up exercise covering Git, collaboration, Projects, Actions, or security.

## Start where you need help

| What you need | Go here |
| --- | --- |
| My preparation and how to use this repo | [My study approach](docs/my-study-approach.md) |
| What the exam covers | [Full topic outline](docs/exam-outline.md) and [domain weights](docs/exam-map.md) |
| Choosing between similar features | [Common decisions](docs/common-decisions.md) |
| Markdown, notifications, and search | [Triage lab](labs/07-markdown-and-triage.md) |
| Timelines and file maintenance | [Planning lab](labs/08-timeline-and-file-maintenance.md) |
| Git commands in plain language | [Command dictionary](docs/command-dictionary.md) |
| Git in Visual Studio or VS Code | [Editor walkthrough](labs/01-git-and-editors.md) |
| AI prompts and `/` commands | [Copilot dictionary](docs/copilot-prompts.md) |
| Environments, automation, and tests | [Automation lab](labs/02-environments-and-actions.md) |
| Projects and boards | [Project board lab](labs/03-project-board.md) |
| Teams and permissions | [Team management lab](labs/04-team-management.md) |
| The GitHub “store” | [Marketplace lab](labs/05-marketplace-and-ai.md) |
| Short explanations of the other exam topics | [Foundations reference](docs/foundations-reference.md) |
| Explain concepts in new situations | [10 scenario exercises](practice/scenario-workbook.md) |
| Merge conflicts and PR review | [Conflict lab](labs/09-merge-conflicts.md) and [review lab](labs/10-review-a-pull-request.md) |
| Repository insights and security tools | [Evidence guide](docs/insights-and-security-tools.md) |
| Questions with explanations | [Practice guide](practice/README.md) |
| Free resources beyond Microsoft Learn | [Resource guide](docs/free-resources.md) |
| Profile, 2FA, OAuth, and security | [Account security lab](labs/06-profile-and-security.md) |
| Official material | [Sources](docs/sources.md) |

## Use it alongside Microsoft Learn

Start with [Microsoft Learn's GitHub Foundations training](https://learn.microsoft.com/en-us/training/paths/github-foundations/) and the [official GH-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900). Follow the training links on the [certification page](https://learn.microsoft.com/en-us/credentials/certifications/github-foundations/) for both learning paths and available assessment resources.

Pick a topic, read the explanation, and try the matching lab. Before checking an answer, say why you chose it. If you miss it, return to the relevant feature and try a different situation using it.

## Run the practice questions

Install Python 3.11 or newer. Clone or download this repository, open a terminal in its folder, and run:

```sh
python scripts/quiz.py
```

On Windows, `py` may be the available launcher; on macOS or Linux, use `python3` if `python` is unavailable. No extra Python packages are needed.

```sh
python scripts/quiz.py --domain basics
python scripts/quiz.py --domain modern
python scripts/quiz.py --shuffle --limit 10
python -m unittest discover -s tests -v
python scripts/check_content.py
```

There are 35 original practice questions, a Markdown answer guide, and an Anki-ready TSV. These are learning checks, not actual exam questions or a full mock exam. Scores here do not predict an exam result.

## What is included

The repository includes a development-container configuration, a CI workflow that checks the material, and a manual sandbox workflow for learning about deployment environments. The deployment exercise only produces a job summary; it does not deploy a website or cloud resource. The project and team labs explain the account setup you perform in your own sandbox.

Source review: November 13, 2026. The official exam guide and product documentation can change. This is an independent study project, not an official Microsoft or GitHub course.

Study topics: GH-900, GitHub Foundations certification, Git, GitHub Actions, Projects, Codespaces, Copilot, VS Code, Visual Studio, Anki, and free exam preparation.

## Choose your next practice session

| Your next step | Go here |
| --- | --- |
| Complete a small task with a clear finish check | [Eight hands-on challenges](practice/hands-on-challenges/README.md) |
| Choose a tool and session plan | [Hands-on learning routes](practice/choose-your-learning-route.md) |
| Investigate a failed lab | [Troubleshooting guide](docs/troubleshooting-first-steps.md) and [eight challenges](practice/troubleshooting-challenges.md) |
| Work through a complete documentation change | [Fictional simulation case](practice/simulation-case-study.md) and [worked review](practice/worked-simulation-review.md) |
| Practice short-answer recall | [Ten visual recall cards and Anki deck](practice/visual-recall.md) |
| Choose between features as requirements change | [Seven chapter decision rounds and 14-question Anki deck](practice/decision-rounds/README.md) |

These sets are separate from the 35-question CLI bank. Start with one format and use your explanation of the result to decide what to study next.
