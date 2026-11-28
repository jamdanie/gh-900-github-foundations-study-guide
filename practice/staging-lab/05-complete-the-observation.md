# Commit the complete observation

[Lab index and prerequisites](README.md)

## Do the task

Continue after step 4. Stage and inspect the complete note:

```sh
git add observation.txt
git diff --staged -- observation.txt
git commit -m "Record simulated disconnection and uncertainty"
git status --short
```

Check that the state change and uncertainty line were both selected before committing.

## Expected result

With no other files or edits, short status prints no entries after the commit. That means this working tree and index are clean; it does not mean anything was uploaded to GitHub.

## Explain before moving on

Write a short explanation of the difference between the first and second snapshots. These states are invented practice data. If you later record a game session, use only what you actually observed.

References: [Git diff](https://git-scm.com/docs/git-diff), [Git status](https://git-scm.com/docs/git-status), [Git restore](https://git-scm.com/docs/git-restore). Command behavior reviewed November 28, 2026.
