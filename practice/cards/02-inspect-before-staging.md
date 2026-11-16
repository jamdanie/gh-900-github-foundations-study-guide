# Inspect before staging

Topic: Git

An existing tracked file changed unexpectedly. Which command helps you read its unstaged edits?

<details>
<summary>Explanation</summary>

Use git diff. It compares working changes with staged content. Read the changed lines before deciding whether to stage them; status tells you file state but does not explain every edit.

</details>

## Try a different angle

Compare what git status tells you with what git diff tells you.

Further reading and sources: [command dictionary](../../docs/command-dictionary.md).

[All practice cards](README.md)
