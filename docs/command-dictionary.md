# Git and GitHub command dictionary

Run Git commands in a terminal opened inside your repository. They work with the same local files that your editor displays. A Git command changes or inspects version control; a Copilot slash command asks an AI assistant to do something in chat.

## Start, inspect, and save

| Command | Plain meaning | When and why |
| --- | --- | --- |
| `git --version` | Show installed Git version | Check that Git is available |
| `git init` | Start local repository history | Begin tracking an existing folder |
| `git clone URL` | Copy a repository and history | Start working with a remote repo |
| `git status` | Show branch and file state | Check your position before changing anything |
| `git diff` | Show unstaged edits | Review work before staging |
| `git diff --staged` | Show staged edits | Review the next commit |
| `git add README.md` | Stage one file | Select what goes into the commit |
| `git commit -m "Clarify setup"` | Record staged work locally | Save a meaningful change |
| `git log --oneline -5` | Show five recent commits | Check the recent history |
| `git remote -v` | Show remote addresses | Confirm where fetch and push connect |

`URL` means the clone address shown by your own repository's Code menu. Do not type the word URL literally. The lab uses a fork so you can push your own changes.

Source: [Git command reference](https://git-scm.com/docs/git).

## Branch and synchronize

| Command | Plain meaning | When and why |
| --- | --- | --- |
| `git switch -c study/git-flow` | Create and enter a branch | Isolate a new change |
| `git switch main` | Enter the existing main branch | Return to the base branch |
| `git branch` | List local branches | Check which branch is active |
| `git fetch origin` | Download remote history and update remote-tracking refs | Inspect incoming work before integrating it |
| `git pull --ff-only` | Fetch and advance the current branch only if it can fast-forward | Update without creating an unexpected merge; stops if histories diverge |
| `git push -u origin study/git-flow` | Upload this branch and set its upstream | Publish the first branch push |
| `git push` | Upload commits using configured defaults | Share later work on a configured branch |
| `git merge study/git-flow` | Integrate that branch into the current branch | Practice local merging; inspect your current branch first |

A commit does not upload your work. Fetch does not merge changes into the checked-out branch. Pull fetches and integrates according to its options. Push sends local commits to the remote. If `--ff-only` stops, inspect the history rather than forcing an update.

Sources: [switch](https://git-scm.com/docs/git-switch), [pull](https://git-scm.com/docs/git-pull), [Git reference](https://git-scm.com/docs/git).

## Undo deliberately

| Command | Plain meaning | When and why |
| --- | --- | --- |
| `git restore --staged README.md` | Unstage this file while keeping its working edits | Remove a file from the next commit |
| `git restore README.md` | Replace working file content from the index by default | Discard unwanted unstaged edits; those edits can be lost |
| `git stash push -m "unfinished notes"` | Store tracked working changes temporarily | Pause unfinished tracked edits |
| `git stash list` | List saved stashes | Find the work you paused |
| `git stash apply` | Reapply the latest stash without deleting it | Resume work and check for conflicts |
| `git revert HEAD` | Create a new commit reversing the latest commit | Undo a normal published commit while preserving history |

Use `git status` and inspect the diff first. Stash does not include untracked files by default; `-u` includes them. Revert may require conflict resolution, and reverting a merge needs additional choices. Practice on an ordinary single-parent commit. Avoid using a destructive reset or a force push as the default response to confusion.

Sources: [restore](https://git-scm.com/docs/git-restore), [stash](https://git-scm.com/docs/git-stash), [revert](https://git-scm.com/docs/git-revert).

## GitHub CLI is a separate tool

GitHub CLI uses `gh`. Git uses `git`. Install and sign in to GitHub CLI only if you want the optional terminal route; the labs also work through GitHub's website.

| Command | Meaning | When and why |
| --- | --- | --- |
| `gh auth status` | Inspect CLI authentication | Check which account is active |
| `gh repo view --web` | Open the current repository | Move from terminal to GitHub |
| `gh issue list` | List issues | Find work to take on |
| `gh pr create` | Start creating a pull request | Propose your pushed branch for review |
| `gh pr checks` | Show checks for the current PR | See whether automation passed |
| `gh run list` | List workflow runs | Find automation results |

These commands require GitHub CLI and appropriate access. Check `gh help` and the [official CLI manual](https://cli.github.com/manual/) for current options.
