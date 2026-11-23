# Decision round: Git and GitHub basics

[All decision rounds](README.md) · [Chapter](../../chapters/01-git-basics.md)

Choose an answer and explain why the other choices do not fit before opening the explanation. These are original practice questions, not recalled exam content.

## 1. You are offline and want to record an already staged change in your local repository. Which operation fits?

A. Create a local commit

B. Open a PR on GitHub

C. Push the branch to GitHub

D. Change the repository's Watch setting

<details>
<summary>Answer and explanations</summary>

Correct answer: **A**.

- A. A commit records the staged content in local history and does not require a remote connection.
- B. A PR is hosted collaboration and does not substitute for a local commit.
- C. Push communicates with a remote and is a separate publishing step.
- D. Watch manages notifications, not local history.

</details>

## 2. You want to inspect exactly what is selected for the next commit. Which command fits?

A. git remote -v

B. git diff --staged

C. git fetch origin

D. git branch

<details>
<summary>Answer and explanations</summary>

Correct answer: **B**.

- A. This displays remote addresses.
- B. This displays the staged changes relative to the current commit.
- C. This retrieves remote information rather than showing the staged selection.
- D. This lists local branches rather than the selected file content.

</details>

## Hands-on challenge

On your sandbox branch, stage one small edit and inspect the staged diff. Explain why reading status alone would not show every changed line.

## Change the requirement

Rewrite one question so a different feature becomes appropriate. Explain the changed requirement; do not merely swap the answer letters. Use the [review log](../review-log.md) if the difference remains unclear.

Reading and sources: [related guide](../../docs/command-dictionary.md) and its linked official documentation. These rounds supplement the main quiz; two questions cannot establish mastery of a domain.
