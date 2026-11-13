# Lab 1: Git in Visual Studio and VS Code

Goal: make a small change on a branch, publish it, and explain what was local at each step.

You need Git, a GitHub account, and either editor. Fork this study repo into your account using GitHub's Fork button. Clone your fork using the URL in its Code menu. Open the cloned folder in your editor. Configure your Git author identity if this is your first commit; use GitHub's private commit email option if you do not want your personal address in public history.

## Use the terminal

Run these commands in the cloned repository:

```sh
git status
git switch -c study/first-lab
```

Create `notes.md` in the editor. Write your own explanation of the difference between a commit and a push, save it, then run:

```sh
git status
git add notes.md
git diff --staged
git commit -m "Explain commit and push in my own words"
git log --oneline -3
git push -u origin study/first-lab
```

`git diff` alone does not show a new untracked file. The staged diff shows its content after `git add`.

On GitHub, open a pull request from this branch into **your fork's main branch**, not the upstream study repo. Describe what the note explains. Review the diff and check the Actions result. Merge when the change is correct. Locally, return to main and update:

```sh
git switch main
git pull --ff-only
```

Expected result: the note appears in your fork's main branch and your local main after the pull. Before the push, the commit existed only in your local clone.

## Find the equivalent editor controls

| Task | Visual Studio | VS Code |
| --- | --- | --- |
| Open a repository | Git menu / clone or open repository | Clone Repository / Open Folder |
| Inspect changes | Git Changes window | Source Control view |
| Stage a file | Stage the selected change | Plus beside the selected file |
| Record local work | Commit staged changes | Commit staged changes |
| Change branches | Git Repository window / branch selector | Branch indicator in the status bar |
| Share commits | Push | Push from Source Control |

Menu labels can differ by version. Avoid treating Sync as a synonym for commit: it may combine pull and push. Inspect what it will do before using it.

## Check your understanding

Explain why the PR appeared after the push, why merging on GitHub did not immediately update your local main, and why a branch is different from a fork.

If the push is denied, inspect `git remote -v` and confirm you cloned your fork. If Git reports no author identity, configure it before retrying the commit. If the pull cannot fast-forward, inspect the diverged history before choosing how to reconcile it.

Evidence to keep: your commit, PR, and a short explanation of local versus remote state. These are your own lab results, not required submissions to this repository.

Sources: [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow), [VS Code source control](https://code.visualstudio.com/docs/sourcecontrol/overview), [Git in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/version-control/git-with-visual-studio).
