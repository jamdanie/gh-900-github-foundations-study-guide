# A fast-forward stop

Topic: Git

git pull --ff-only stops because local and remote histories diverged. Should you force a push?

<details>
<summary>Explanation</summary>

No. The stop means this update cannot simply advance the branch. Inspect the histories and understand both sets of changes before choosing a reconciliation method. Force pushing is not a default repair.

</details>

## Try a different angle

Explain what work you could overwrite by treating every stopped pull as an upload problem.

Further reading and sources: [git step by step](../../docs/git-step-by-step.md).

[All practice cards](README.md)
