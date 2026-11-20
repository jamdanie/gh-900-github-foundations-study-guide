# Lab 13: Turn an observation into a reviewed note

[Table of contents](../CONTENTS.md)

Goal: use an observation from a learning activity to practice issues, branches, Markdown, PRs, and review. Use your own sandbox repository or fork. Do not submit practice reports to a game's maintainers.

## Choose one observation

Free route: use a branch exercise from [lab 11](11-visual-git-challenge.md). Describe a graph change you initially misunderstood.

Optional game route: if you already use a data-center game, describe one simulated capacity, cabling, or maintenance observation. Clearly identify the game and label the result as simulated. A game purchase is not required.

## Track and explain the work

1. Open an issue in your sandbox with the observed result, what you expected, and the explanation you want to improve.
2. Create a branch named `study/observation-note`.
3. Write a Markdown note describing the setup, one action, the observed result, and the limit of your conclusion.
4. Include a diagram or screenshot only if it helps explain the observation. Use your own work and remove private information.
5. Commit the note and push the branch to your sandbox.
6. Open a PR into your sandbox's main branch. Refer to the issue and explain how the note addresses it.
7. Review the diff. Inspect any configured check results; if no workflow exists, say so rather than claiming tests passed.
8. Revise if needed, then merge when applicable requirements are satisfied. Check the issue state separately.

## What counts as evidence?

A branch graph can support a claim about that Git exercise. A game screenshot can support a claim about behavior you observed in that simulation. Neither proves you administered production infrastructure.

The useful GitHub evidence is the issue, note, commit, PR discussion, and review reasoning. If you worked alone, describe it as a self-review.

Use the [evidence guide](../practice/learning-evidence.md) to write a short result statement. Related walkthrough: [lab 10](10-review-a-pull-request.md). GitHub reference: [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow).

## Check the result before moving on

Does the note accurately separate observation from conclusion?

Identify the activity, observed result, and limitation. Point to the PR diff and describe your review as a self-review if you worked alone.

If you get stuck: If there was no workflow, state that fact. If the observation came from a game, retain the simulation label when describing the result.

Use the [troubleshooting guide](../docs/troubleshooting-first-steps.md) to choose an inspection and the [challenge workbook](../practice/troubleshooting-challenges.md) to practice the reasoning without changing a live repository.
