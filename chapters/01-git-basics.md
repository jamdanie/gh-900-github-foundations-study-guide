# Chapter 1: Git and GitHub basics

[Table of contents](../CONTENTS.md) · [Next chapter](02-repositories.md)

Git records file versions. GitHub hosts repositories and provides collaboration tools. Begin by explaining where a change exists: in your working files, in the staging area, in a local commit, or on GitHub.

## Key terms

| Term | Meaning |
| --- | --- |
| Repository | Project files and their Git history. |
| Commit | A recorded snapshot in Git history. |
| Branch | A line of development within a repository. |
| Staging area | Content selected for the next commit. |

## Worked example

You correct a sentence in a local note and save it. The file changed, but no commit exists yet. Stage the note, inspect the staged diff, and commit. That commit is still local until you push. If you instead edit and commit through GitHub's website, the commit is already hosted there.

## Where people get confused

Saving and committing both preserve something, but they preserve different things. A saved working file is not automatically a historical checkpoint. A commit also does not automatically publish local work.

## Read and try

- [Beginner route](../docs/beginner-start-here.md)
- [Command order and file state](../docs/git-step-by-step.md)
- [Command dictionary](../docs/command-dictionary.md)
- [Git in your editor](../labs/01-git-and-editors.md)
- [Markdown practice](../labs/07-markdown-and-triage.md)

The linked guides include product documentation and sources. Use the [official topic outline](../docs/exam-outline.md) for scope; this chapter is a reading route, not a complete replacement for the official objectives.

## Practice and review

Explain why a new local commit may not appear on GitHub. Then describe how you would check the branch and remote before trying another command.

From the repository root, use `python scripts/quiz.py --domain basics` for the existing five-question domain sample. The sample is not a readiness prediction. Record what you could explain and what still needs practice in the [review log](../practice/review-log.md).

[Table of contents](../CONTENTS.md) · [Next chapter](02-repositories.md)
