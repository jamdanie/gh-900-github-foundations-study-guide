# See two versions of one file

[Lab index and prerequisites](README.md)

## Do the task

Continue after step 1. Change the file to `State: disconnected` and save it. Run:

```sh
git add observation.txt
```

Now add a second line in the editor: `Cause: not yet tested`. Save again, then run:

```sh
git diff -- observation.txt
git diff --staged -- observation.txt
```

## Expected result

The first comparison shows the extra cause line against the staged version. The second shows the staged state change against the last commit. If you commit now without adding again, the cause line is not included.

## Explain before moving on

Predict which lines would appear in the next commit. Do not commit yet; keep this state for step 3.

References: [Git diff](https://git-scm.com/docs/git-diff), [Git status](https://git-scm.com/docs/git-status), [Git restore](https://git-scm.com/docs/git-restore). Command behavior reviewed November 28, 2026.
