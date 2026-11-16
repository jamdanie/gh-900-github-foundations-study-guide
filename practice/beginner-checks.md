# Beginner checks: explain the next step

These are original learning exercises, separate from the 35-question quiz and Anki deck. Answer in one or two sentences before opening each explanation. There is no score that predicts an exam result.

## 1. Saved, but not recorded

You saved an edited file in VS Code. Have you made a Git commit?

<details>
<summary>Explanation</summary>

No. Saving updates the working file. Review it, stage the content you want, then commit. Saving, staging, and committing are separate steps. See [where your Git changes go](../docs/git-step-by-step.md).
</details>

## 2. Staged, then edited again

You staged a file, then added another sentence and saved. Will a normal commit of the staged content include that new sentence?

<details>
<summary>Explanation</summary>

No. The staging area still holds the earlier version. Inspect both diffs and stage again if you want the newer sentence in the commit. See [Git stages](../docs/git-step-by-step.md).
</details>

## 3. Recorded, but not published

Your terminal shows a new local commit. GitHub does not. What should you inspect before making another commit?

<details>
<summary>Explanation</summary>

Check whether you pushed, which remote received the push, and which branch you are viewing on GitHub. Repeating the commit does not solve a publishing or branch-selection problem. See [Git stages](../docs/git-step-by-step.md).
</details>

## 4. Task or proposed change?

You want to report that the setup directions are unclear, but have not edited them. Should you start with an issue or a PR?

<details>
<summary>Explanation</summary>

An issue records the problem and desired result. A PR is appropriate when proposing file changes. Once you have an edit, the PR can refer to the issue. See [one small change](../docs/beginner-start-here.md).
</details>

## 5. Same work, different view

You want to see your Project tasks as columns today and a table tomorrow. Do you need to recreate each issue?

<details>
<summary>Explanation</summary>

No. Project views can present the same items differently. Use a board for grouping and a table for comparing fields. See [Projects explained](../docs/beginner-start-here.md).
</details>

## 6. Name the part

In a workflow, `validate` contains several steps and `runs-on` selects Ubuntu. Which is the job, and which setting chooses its runner?

<details>
<summary>Explanation</summary>

`validate` is the job identifier. `runs-on` chooses the runner that executes it. The runner is the machine; the job describes the grouped work. See [Actions vocabulary](../docs/actions-in-plain-language.md).
</details>

## 7. Green checks, unclear explanation

Tests pass, but the proposed study note says a commit automatically uploads to GitHub. Is the note ready?

<details>
<summary>Explanation</summary>

No. Fix the inaccurate explanation. A local commit records history locally; push publishes it. Checks only cover what they were configured to check. See [reading check results](../docs/actions-in-plain-language.md).
</details>

## 8. Merged online, old file locally

You merged a PR into your fork's main branch on GitHub. Your local main still has the older wording. Why?

<details>
<summary>Explanation</summary>

The remote and local branches do not update each other automatically. In the first lab's clean setup, switch to local main and run `git pull --ff-only`. If it stops, inspect why before proceeding. See [the editor lab](../labs/01-git-and-editors.md).
</details>

After each answer, change one detail and explain how your next step would change. Then try the longer [scenario workbook](scenario-workbook.md).
