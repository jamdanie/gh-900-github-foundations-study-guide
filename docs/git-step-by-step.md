# Where your Git changes go

Run these commands inside your local repository folder. Your editor's terminal works. This page explains the sequence used in the [first lab](../labs/01-git-and-editors.md); it does not require a second setup.

## Four places to keep separate

| Place | Plain meaning | How to inspect it |
| --- | --- | --- |
| Working files | The files you are currently editing | Open the file and run `git status` |
| Staging area, also called the index | The content selected for the next commit | `git diff --staged` |
| Local history | Commits saved in your clone | `git log --oneline -3` |
| Remote repository | The repository your clone connects to, such as your GitHub fork | `git remote -v`, then inspect that repository on GitHub |

Saving in the editor writes the file. Staging selects content. Committing records it in local history. Pushing publishes commits to a remote. Each step has a different result.

## A small example, in order

Start on your practice branch from the first lab. Create `notes.md` with a sentence explaining commit versus push, and save it.

| Do this | What changed? | What to check |
| --- | --- | --- |
| `git status` | Nothing; this inspects your state | A new file is initially untracked |
| `git add notes.md` | The current saved content is staged | `git diff --staged` shows what you selected |
| `git commit -m "Explain commit and push"` | Staged content becomes a local commit | `git log --oneline -3` shows the commit |
| `git push -u origin study/first-lab` | The branch is published, if access allows | Select `study/first-lab` on GitHub and find the commit |

The push command assumes the branch name and fork setup from the first lab. `origin` is the remote name created by a typical clone. It is not a username. `-u` sets the branch's upstream so later pushes can use that relationship. Inspect `git remote -v` before publishing.

## Why did my latest edit miss the commit?

Suppose you stage a sentence, then rewrite it and save again. Git still has the earlier staged version. The newer edit is in the working file. The same file can therefore have both staged and unstaged changes.

Run `git diff` to inspect the unstaged change and `git diff --staged` to inspect the proposed commit. If you want the newer saved version included, stage the file again. Review it before committing.

Source: [git add](https://git-scm.com/docs/git-add).

## Fetch, pull, and push

Fetch downloads information and history from a remote without integrating it into your current branch. Pull fetches and then integrates according to the options used. Push sends local commits to the remote.

After you merge a PR on GitHub, your local main branch has not automatically moved. In the first lab, switch to main and use `git pull --ff-only` to update it. This option stops if Git cannot advance the branch without reconciling diverged histories. A stop is a reason to inspect the history, not to force the update.

Sources: [git fetch](https://git-scm.com/docs/git-fetch), [git pull](https://git-scm.com/docs/git-pull), [Git reference](https://git-scm.com/docs/git). For more commands, use the [dictionary](command-dictionary.md).

## If the result surprises you

If GitHub does not show a local commit, check whether you pushed, which remote you used, and which branch you are viewing. If Git says there is nothing to commit, check that you saved the file and opened the correct repository folder. Use `git status` before trying commands that discard or rewrite work.
