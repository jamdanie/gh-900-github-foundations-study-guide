# Lab 9: Resolve a merge conflict you understand

Goal: create competing edits in a new local practice repository, inspect the conflict, and choose the final wording. This is extra hands-on practice for Git and collaboration concepts, not a claim that every command flag is an exam objective.

Use a new folder outside your study-guide clone. No remote, GitHub account, or paid service is needed. You need Git and a text editor. If the folder name already exists, choose another unused name.

## Create the starting point

```sh
mkdir gh900-conflict-practice
cd gh900-conflict-practice
git init -b main
```

Configure your author identity if Git needs it before committing. Create `study.txt` with exactly this one line:

```text
Next topic: Git basics
```

```sh
git add study.txt
git commit -m "Record the starting study topic"
git switch -c study/actions
```

Replace the line in `study.txt` with `Next topic: Actions`, save it, then run:

```sh
git add study.txt
git commit -m "Choose Actions for the next session"
git switch main
```

On main, replace the original line with `Next topic: Projects`, save it, then run:

```sh
git add study.txt
git commit -m "Choose Projects for the next session"
git status
git merge study/actions
```

Expected: Git reports a content conflict in `study.txt`. Both branches changed the same line differently. The nonzero result from this merge is intentional.

## Decide what belongs in the file

Open `study.txt`. The conflict markers separate the current branch's version from the incoming version. Read both and decide what the final note should mean. For this exercise, replace all the content, including markers, with:

```text
Next topics: Projects, then Actions
```

```sh
git add study.txt
git diff --staged
git commit -m "Combine the two study plans"
git status
git log --oneline --graph --all
```

Expected: a clean working tree, the combined note, and a merge commit connecting the two branches. `git add` records your chosen resolution; it does not decide which wording is correct.

If you want to stop while the merge is unresolved, `git merge --abort` attempts to return to the pre-merge state. Starting with a clean working tree makes this safer. Do not use a force push to solve a content conflict.

## Explain the result

Why did editing different branches not prevent this conflict? Why is accepting either side automatically a poor default? What would you review if the file contained application behavior instead of a study note?

In Visual Studio or VS Code, a merge editor may offer current, incoming, or combined choices. Review the resulting file regardless of which control you use. A conflict-free file can still contain incorrect logic or wording.

Sources: [Git merge](https://git-scm.com/docs/git-merge), [GitHub merge conflicts](https://docs.github.com/en/pull-requests/reference/merge-conflicts).
