# Keep edits while unstaging

Topic: Git

You staged README.md too early. You want to keep your writing but remove it from the next commit.

<details>
<summary>Explanation</summary>

Use git restore --staged README.md. This changes the staging selection while retaining working edits. Do not confuse it with restoring the working file, which can discard unstaged changes.

</details>

## Try a different angle

Describe which of the working file and staging area should change.

Further reading and sources: [command dictionary](../../docs/command-dictionary.md).

[All practice cards](README.md)
