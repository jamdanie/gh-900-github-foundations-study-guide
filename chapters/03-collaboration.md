# Chapter 3: Collaboration and review

[Table of contents](../CONTENTS.md) · [Previous chapter](02-repositories.md) · [Next chapter](04-modern-development.md)

Choose a collaboration tool based on what you are trying to do. Describing a problem, discussing an idea, and proposing a file change are related activities with different outputs.

## Key terms

| Term | Meaning |
| --- | --- |
| Issue | Tracks a task, request, or problem. |
| Pull request | Proposes changes between branches for discussion and review. |
| Discussion | Supports questions and broader conversation. |
| Diff | Shows the changes being compared. |

## Worked example

You notice an unclear definition. Record the problem in an issue, make a correction on a branch, and open a PR. Review Files changed to see the proposed wording and Checks to inspect automation. The issue explains the need; the PR contains the proposed solution.

## Where people get confused

Opening a PR does not merge it. A draft cannot merge until it is ready, and applicable requirements still matter. A green check does not establish that the wording is accurate. Also inspect whether the run tested the latest commit.

## Read and try

- [Issues, PRs, Gists, Wikis, and Pages](../docs/foundations-reference.md)
- [Notifications and search](../docs/common-decisions.md)
- [Triage lab](../labs/07-markdown-and-triage.md)
- [PR review lab](../labs/10-review-a-pull-request.md)
- [Merge-conflict lab](../labs/09-merge-conflicts.md)

The linked guides include product documentation and sources. Use the [official topic outline](../docs/exam-outline.md) for scope; this chapter is a reading route, not a complete replacement for the official objectives.

## Turn an observation into a PR

Use [lab 13](../labs/13-observation-to-pull-request.md) to turn a Git exercise or game observation into an issue and a reviewed note. Check the destination repository before opening the PR. The [review diagram](../docs/visual-git-and-github.md) helps separate correct content from satisfied merge requirements.

## Practice and review

Explain what you would do if a reviewer requested one more example in an open PR. Describe which branch you would edit and which check result you would inspect.

From the repository root, use `python scripts/quiz.py --domain collaboration` for the existing five-question domain sample. The sample is not a readiness prediction. Record what you could explain and what still needs practice in the [review log](../practice/review-log.md).

[Table of contents](../CONTENTS.md) · [Previous chapter](02-repositories.md) · [Next chapter](04-modern-development.md)

## Follow-up: review a diagram and its claim

Complete [lab 14](../labs/14-explain-with-a-diagram.md), then try the [simulation case study](../practice/simulation-case-study.md). Review both the diagram's syntax and the meaning of its labels. A rendered picture can still communicate an unsupported conclusion. Compare your review with the [worked example](../practice/worked-simulation-review.md).

## Test the decision in a new situation

Open the [collaboration decision round](../practice/decision-rounds/collaboration.md) for two original questions and a hands-on challenge. Explain why each alternative does not fit, then change one requirement to make a different choice appropriate. The [companion Anki deck](../practice/decision-rounds/README.md) includes these questions with explanations for every option.
