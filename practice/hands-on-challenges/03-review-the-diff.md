# Challenge 3: Review the meaning of a change

[Challenge menu](README.md)

This is an original fictional review exercise. No repository edits are required.

A contributor proposes this change:

```diff
- The simulator displayed a connection failure after I removed one link.
- Restoring that link cleared the displayed failure.
+ The network has no redundancy.
+ Restoring the link proves the network is secure.
```

## Make a decision

Before opening the answer, write a review comment. Identify the supported observation, the unsupported conclusion, and a specific revision. Would a passing Markdown link checker change your decision?

<details>
<summary>Worked review</summary>

“I can follow the two observations in the original note. I don't see a test of alternate paths or security controls, though. Please keep the observed failure and recovery, and list redundancy and security as untested.”

A link checker can find a missing local file target. It cannot establish whether the simulation supports the new claims. Passing that check doesn't resolve the content problem.

</details>

## Try a better revision

Write two sections: **Observed** and **Still unknown**. Keep the actions and displayed results in the first. Put questions about alternate paths, workload, and other failure conditions in the second.

If practicing in your own sandbox, put that revision on a branch and inspect the PR's changed files before merging. A solo self-check is useful practice; do not describe it as an independent review.

Finish when your comment gives the contributor a clear next action and your revised note stays within the evidence.
