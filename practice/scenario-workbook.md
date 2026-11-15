# Explain it, then change the scenario

Ten original short-answer exercises. These supplement the 35-question quiz and Anki deck; they are not copied exam questions. Answer aloud before opening each explanation. Then answer the changed scenario without relying on the same memorized wording.

## 1. A commit is missing online

You committed a note in your clone. It appears in the local log but not on GitHub. What should you inspect before uploading it?

<details>
<summary>Reasoning and a changed scenario</summary>

Check the current branch and remote, then push the intended branch if you have access. A local commit does not upload itself. Creating another issue would not send the commit.

Try this change: The commit is already on your remote branch, but not main. Now explain why a PR and merge may be the next steps.

[Review the topic](../docs/command-dictionary.md)

</details>

## 2. Two people change the same line

Two branches replace the same sentence with different instructions. Git refuses to merge automatically. What should you do?

<details>
<summary>Reasoning and a changed scenario</summary>

Read both edits and choose correct final content, remove conflict markers, stage the resolution, and complete the merge. A force push is not a substitute for deciding what the file should say.

Try this change: The edits are on separate lines and Git merges automatically. Explain why reviewing the combined result still matters.

[Review the topic](../labs/09-merge-conflicts.md)

</details>

## 3. A green draft

Your draft PR has passing checks. Can it be merged immediately?

<details>
<summary>Reasoning and a changed scenario</summary>

Not while it remains a draft. Mark it ready when the work is prepared for review, then inspect any other merge requirements. Passing tests do not change the draft state.

Try this change: The PR is ready, but a required review is missing. Explain which condition remains unsatisfied.

[Review the topic](../docs/insights-and-security-tools.md)

</details>

## 4. An alarming package version

A dependency version has a published vulnerability. Which feature helps identify this, and what does its alert not prove?

<details>
<summary>Reasoning and a changed scenario</summary>

Dependabot alerts identify known vulnerable dependencies. The alert does not prove an update was applied or that the application was tested after a fix.

Try this change: The finding is an exposed API key rather than a vulnerable package. Explain why secret scanning is the closer match.

[Review the topic](../docs/insights-and-security-tools.md)

</details>

## 5. An exposed credential

A real token was committed and then removed in a new commit. Is that enough?

<details>
<summary>Reasoning and a changed scenario</summary>

No. Revoke or rotate the credential promptly. Removing its visible use does not invalidate it or remove it from prior history. Do not post the token in an issue while discussing the fix.

Try this change: A secret-scanning alert is a false positive. Explain why the finding needs investigation before deciding how to resolve it.

[Review the topic](../docs/insights-and-security-tools.md)

</details>

## 6. Lots of commits

A repository has many commits this week. Does that prove the material is accurate?

<details>
<summary>Reasoning and a changed scenario</summary>

No. Activity counts record activity. Read the actual changes, examine evidence, and review the claims. Small commits and generated edits can increase counts without improving accuracy.

Try this change: Traffic rises after sharing the guide. Explain what that can suggest and why it does not establish exam pass rates.

[Review the topic](../docs/insights-and-security-tools.md)

</details>

## 7. Two meanings of dependency

Your app imports a package. Another project imports a package you publish. Which is a dependency and which is a dependent?

<details>
<summary>Reasoning and a changed scenario</summary>

The imported package is your dependency. The project using your package is a dependent. The direction of the relationship determines the term.

Try this change: Your imported package itself imports another package. Explain why the second package is a transitive dependency of your app.

[Review the topic](../docs/insights-and-security-tools.md)

</details>

## 8. A board says Done

You drag an issue-backed Project item to Done. Is the issue necessarily closed?

<details>
<summary>Reasoning and a changed scenario</summary>

No. Project Status and issue state are distinct. Check the configured automation and the issue itself before reporting it closed.

Try this change: The issue closed but the board stayed In Progress. Identify which Project workflow you would inspect.

[Review the topic](../labs/03-project-board.md)

</details>

## 9. A browser editor cannot run a test

You can edit a file in github.dev but need a terminal to execute Python. What would you choose?

<details>
<summary>Reasoning and a changed scenario</summary>

Use local tools or a Codespace with compute. Editing text in github.dev does not supply the same execution environment. Codespaces is optional for this repo.

Try this change: You only need to fix a spelling mistake. Explain why a browser editor may now be sufficient.

[Review the topic](../labs/02-environments-and-actions.md)

</details>

## 10. AI gives a confident answer

AI says a command is safe and supplies a test. How do you decide whether to accept it?

<details>
<summary>Reasoning and a changed scenario</summary>

Inspect the command, compare its behavior with official documentation, and run an appropriate test in a sandbox. Generated test text is not proof of a successful run.

Try this change: The assistant did run the test and shows a result. Explain why you still inspect the diff and whether the test covers the intended behavior.

[Review the topic](../docs/copilot-prompts.md)

</details>

## Review your reasoning

Give yourself one point for naming the right feature or next action, one for explaining why it fits, and one for explaining the changed scenario. This is a self-review aid, not an exam passing threshold. Revisit any answer that depends on a guessed permission, a hidden assumption, or an unverified AI claim.
