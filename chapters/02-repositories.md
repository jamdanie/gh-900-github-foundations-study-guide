# Chapter 2: Working with repositories

[Table of contents](../CONTENTS.md) · [Previous chapter](01-git-basics.md) · [Next chapter](03-collaboration.md)

A repository should help a reader understand the project, find its files, and know how to contribute. Start with the purpose of each supporting file before memorizing its name.

## Key terms

| Term | Meaning |
| --- | --- |
| README | Explains the project and how to use it. |
| CONTRIBUTING | Explains how to propose changes. |
| CODEOWNERS | Identifies owners for matching file paths. |
| SECURITY | Describes how to report security concerns. |

## Worked example

A reader finds a confusing setup step. The README explains the setup, while CONTRIBUTING explains how to submit a correction. If ownership rules apply to that path, CODEOWNERS can identify the relevant reviewers. Requiring their approval also needs the appropriate repository rule.

## Where people get confused

A file that identifies reviewers and a rule that requires approval are different. Similarly, public visibility is not a substitute for a license. Read LICENSE for reuse terms instead of assuming every public project allows unrestricted reuse.

## Read and try

- [Repository files and licensing](../docs/foundations-reference.md)
- [Fork versus template](../docs/common-decisions.md)
- [Insights and dependencies](../docs/insights-and-security-tools.md)
- [File maintenance lab](../labs/08-timeline-and-file-maintenance.md)

The linked guides include product documentation and sources. Use the [official topic outline](../docs/exam-outline.md) for scope; this chapter is a reading route, not a complete replacement for the official objectives.

## Map the repository before editing

Draw a small file map of your own sandbox. Beside README, CONTRIBUTING, and SECURITY, write the question each file answers. If a file is absent, record that accurately instead of inventing its contents. Use the [repository mission](../practice/visual-missions.md) to check whether another reader could find the right instructions.

## Practice and review

Choose the file you would read before reporting a vulnerability. Explain why opening a public issue is not automatically the right first step.

From the repository root, use `python scripts/quiz.py --domain repositories` for the existing five-question domain sample. The sample is not a readiness prediction. Record what you could explain and what still needs practice in the [review log](../practice/review-log.md).

[Table of contents](../CONTENTS.md) · [Previous chapter](01-git-basics.md) · [Next chapter](03-collaboration.md)

## Follow-up: what should the reader receive?

Compare a current README with a tagged version and release notes using [tags and releases](../docs/tags-and-release-notes.md). Explain whether the reader needs instructions, a website, or a specific downloadable version. Use the [publishing comparison](../docs/choose-a-publishing-feature.md) to justify the choice. Release practice is supporting material, not an additional weighted exam domain.
