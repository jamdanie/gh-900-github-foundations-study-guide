# Decode the two status columns

[Lab index and prerequisites](README.md)

## Do the task

Continue with the staged and unstaged edits from step 2:

```sh
git status --short
```

Find `observation.txt`. For this ordinary tracked-file example, the first column describes the index relative to the last commit; the second describes the working file relative to the index.

| Code | Meaning in this exercise |
| --- | --- |
| MM | Staged modification plus a later unstaged modification |
| M followed by a space | Staged modification only |
| Space followed by M | Unstaged modification only |
| ?? | Untracked file |

Conflicted files have additional meanings; this table is not a complete status reference.

## Expected result

You should see MM for the file if both edits were made as instructed. A different result is a reason to inspect both diffs, not to force the expected output.

## Explain before moving on

Without changing the file, explain each M using the actual line changes. Keep the current state for step 4.

References: [Git diff](https://git-scm.com/docs/git-diff), [Git status](https://git-scm.com/docs/git-status), [Git restore](https://git-scm.com/docs/git-restore). Command behavior reviewed November 28, 2026.
