# Start here if GitHub is new to you

You can learn these ideas with a text file. You do not need to build an application first. The examples below describe practice situations, not the author's exam questions or personal lab history.

## Git and GitHub do different work

Git records versions of files and lets you work with branches on your computer. GitHub hosts repositories and adds tools for collaboration, planning, and automation. You can make a local Git commit without an internet connection. Publishing that commit to GitHub needs a connection and permission.

A repository, often shortened to repo, holds a project's files and Git history. A README is a file that explains the project to readers. It is useful to start by editing a README because you can see the result without running code.

Source: [Getting started with Git](https://docs.github.com/en/get-started/learning-to-code/getting-started-with-git).

## Follow one small change

Imagine a study guide has a confusing definition of “commit.” You want to clarify it.

| Step | What it means in this example |
| --- | --- |
| Create an issue | Record the problem: the definition needs a clearer example |
| Create a branch | Give this change its own line of work inside the repository |
| Edit and commit | Save the improved wording in Git history |
| Push, if working locally | Send your branch's commits to GitHub |
| Open a pull request, or PR | Propose bringing that branch's changes into a target branch |
| Review | Read the changes and discuss whether they solve the problem |
| Merge | Integrate the accepted change into the target branch |

An issue describes work. A PR proposes file changes. Opening either one does not automatically make the wording better. You still need to edit and review the file. When editing on GitHub's website, the commit is already on GitHub; there is no separate local push for that browser edit.

Source: [Hello World](https://docs.github.com/en/get-started/using-github/hello-world).

## Branch, fork, and clone: where does the work live?

A branch is a line of development within a repository. A fork is a separate repository on GitHub connected to its source. A clone is a local copy of a repository and its history.

If you cannot push to someone else's repository, you can fork it, clone your fork, create a branch, and propose a change back through a PR. These are different steps that can all belong to one contribution. For practice in this guide, open the PR into your own fork so you can manage the exercise yourself.

Try the [editor lab](../labs/01-git-and-editors.md) after reading [where your Git changes go](git-step-by-step.md). The [common decisions guide](common-decisions.md) also explains when a template is useful.

## Issue, Project, board, and roadmap

Think about tracking three study tasks: learn branches, review permissions, and try Actions. Each task can be an issue. Add those issues to a Project to plan them together.

A board view can group the items by status. A table view makes fields easier to compare. A roadmap view shows timing. They are different views of Project data, not three separate sets of tasks you must recreate.

Moving a card to Done changes its Project status. Whether that also closes an issue depends on the automation you configured. Check both instead of assuming they are the same setting.

Source: [About Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects). Practice: [Project board lab](../labs/03-project-board.md).

## Learn in an order you can explain

1. Read [where your Git changes go](git-step-by-step.md), then complete the editor lab.
2. Read [Actions in plain language](actions-in-plain-language.md), then inspect one real workflow run.
3. Try the [beginner checks](../practice/beginner-checks.md) without opening the answers first.
4. Use the [exam outline](exam-outline.md) to move into the remaining topics, including security, community, and account management.

This is a starting route, not the entire exam outline. When a term is unclear, ask: what does it change, where does that change happen, and how would I check the result?
