# Create the first snapshot

[Lab index and prerequisites](README.md)

## Do the task

Create a new empty folder outside any existing repository. Open it in VS Code and open its integrated terminal. Run:

```sh
git init
```

In the editor, create and save `observation.txt` containing `State: connected`. Then run:

```sh
git status --short
git add observation.txt
git diff --staged
git commit -m "Record initial simulated state"
```

If Git asks for your identity, configure your own name and email before retrying. Do not copy another person's identity.

## Expected result

Before staging, the new file appears as untracked. After staging, inspect its contents in the proposed snapshot. The commit records that snapshot locally; no remote is configured in this exercise.

## Explain before moving on

Change nothing else. Explain why saving a file and committing a file are separate steps.

References: [Git diff](https://git-scm.com/docs/git-diff), [Git status](https://git-scm.com/docs/git-status), [Git restore](https://git-scm.com/docs/git-restore). Command behavior reviewed November 28, 2026.
