# Lab 10: Review a small pull request

Goal: separate the quality of the proposed change from the status of its automated checks. Use your fork. This lab does not ask you to invite a reviewer or change branch rules.

1. Create a branch named `study/review-practice` from an up-to-date main branch.
2. Add a short command explanation to your own note and commit it. Push the branch.
3. Open a draft PR into your fork's main branch. Explain the problem and the expected result. Confirm that the destination is your fork.
4. Open Files changed and read the exact diff. Look for unrelated edits, inaccurate claims, and broken links.
5. Open Checks. Identify the commit being checked and read the relevant test output. Explain what the checks cover and what still requires a person to review.
6. Make one useful revision on the same branch, commit, and push. Confirm that the PR updates and inspect the new run.
7. When the change is ready, mark the draft ready for review. Inspect the merge status. If you are practicing alone, do not claim you received an independent review or enable a review requirement you cannot satisfy.
8. Merge only if the content and applicable checks are correct. Return to main locally and pull the merged result.

Expected evidence: a diff you can explain, a workflow result for the current commit, and a short review note. For example: “The link check passed, but I also read the command explanation because that check cannot verify its meaning.” Write only what you actually observed.

If the wrong commit was checked, look at the newer run. If a draft cannot merge, that is expected. If another requirement remains, identify it rather than bypassing it for the exercise.

Source: [Pull requests](https://docs.github.com/en/pull-requests/reference/pull-requests). See [repository insights and security tools](../docs/insights-and-security-tools.md) for more ways to interpret the evidence.

## Check the result before moving on

Did you review the current revision?

Match the PR's latest change with the run you inspected. Describe one content check you performed manually.

If you get stuck: If the PR changed after your review, inspect that new diff and run. Do not reuse an older green result as evidence for the new commit.

Use the [troubleshooting guide](../docs/troubleshooting-first-steps.md) to choose an inspection and the [challenge workbook](../practice/troubleshooting-challenges.md) to practice the reasoning without changing a live repository.
