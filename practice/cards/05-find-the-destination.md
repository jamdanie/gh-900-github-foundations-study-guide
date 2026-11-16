# Find the destination

Topic: Git

A push goes to an unexpected repository. What can you inspect without changing history?

<details>
<summary>Explanation</summary>

Use git remote -v to inspect remote URLs and git branch to inspect your local branch. A remote name such as origin is a local label, not proof that the destination belongs to you.

</details>

## Try a different angle

In your own clone, compare the remote URL with the repository you meant to use.

Further reading and sources: [git step by step](../../docs/git-step-by-step.md).

[All practice cards](README.md)
