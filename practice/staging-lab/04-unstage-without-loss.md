# Unstage without deleting the edits

[Lab index and prerequisites](README.md)

## Do the task

Continue after step 3. Run:

```sh
git restore --staged observation.txt
git status --short
git diff --staged -- observation.txt
git diff -- observation.txt
```

Open the file in the editor and inspect both lines.

## Expected result

The staged comparison should now be empty. The working file still contains the changed state and cause line. Both changes appear in the unstaged comparison.

## Explain before moving on

Explain why the --staged option matters. Do not substitute plain git restore here: that command changes the working file and can discard unstaged edits.

References: [Git diff](https://git-scm.com/docs/git-diff), [Git status](https://git-scm.com/docs/git-status), [Git restore](https://git-scm.com/docs/git-restore). Command behavior reviewed November 28, 2026.
