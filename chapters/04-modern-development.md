# Chapter 4: Automation, editors, and AI

[Table of contents](../CONTENTS.md) · [Previous chapter](03-collaboration.md) · [Next chapter](05-project-management.md)

Separate the place you edit, the system that executes work, and the assistant that proposes changes. This makes it easier to choose a tool and verify what actually happened.

## Key terms

| Term | Meaning |
| --- | --- |
| Workflow | A configured automated process. |
| Job | A group of workflow steps executed on a runner. |
| Runner | The machine executing a job. |
| Dev container | Configuration for a container-based development environment. |

## Worked example

You want to correct a typo and then run the project tests. A browser edit may handle the typo, but running tests requires an execution environment such as your local setup or a Codespace. An AI suggestion can explain a command; the output of an actual run is the evidence that the command executed.

## Where people get confused

A slash command in chat is not a Git command in a terminal. Available AI commands depend on the client. A named deployment environment also does not mean an application was deployed: read the workflow steps and results.

## Read and try

- [Read an Actions workflow](../docs/actions-in-plain-language.md)
- [Environments and automation lab](../labs/02-environments-and-actions.md)
- [Copilot prompts and commands](../docs/copilot-prompts.md)
- [Editors, Codespaces, and plans](../docs/foundations-reference.md)

The linked guides include product documentation and sources. Use the [official topic outline](../docs/exam-outline.md) for scope; this chapter is a reading route, not a complete replacement for the official objectives.

## Inspect a real run

Open a workflow run and locate its commit, job, and step output. Predict what the checkout step makes available before reading later logs. Use the [modern development mission](../practice/visual-missions.md) and record only results you observed. [GitHub's interactive courses](../docs/visual-learning-resources.md) provide another route into repository-based practice.

## Practice and review

Identify the event, job, runner, and steps in this repository's checks workflow. Explain which result would support saying the tests passed.

From the repository root, use `python scripts/quiz.py --domain modern` for the existing five-question domain sample. The sample is not a readiness prediction. Record what you could explain and what still needs practice in the [review log](../practice/review-log.md).

[Table of contents](../CONTENTS.md) · [Previous chapter](03-collaboration.md) · [Next chapter](05-project-management.md)
