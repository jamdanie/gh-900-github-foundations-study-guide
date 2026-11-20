# Lab 12: Read a local commit graph

[Table of contents](../CONTENTS.md)

Goal: make separate edits on two branches and inspect their shared history. Use Git and a text editor. No remote or paid service is needed.

## Start in a new folder

Use an unused folder outside any existing repository. If this name exists, choose another.

```sh
mkdir gh900-history-practice
cd gh900-history-practice
git init -b main
```

Configure your Git author identity if needed. Create `overview.md` with the sentence “This repository is for reading Git history.” Save it.

```sh
git add overview.md
git commit -m "Start the history exercise"
git switch -c study
```

Create `branch-note.md` with your own definition of a branch, then save it.

```sh
git add branch-note.md
git commit -m "Explain a branch"
git switch main
```

Create a different file, `main-note.md`, with your own definition of a commit. Save it.

```sh
git add main-note.md
git commit -m "Explain a commit"
git log --oneline --graph --all --decorate
```

Expected: two lines of work share the starting commit. The branch note is on study, while the commit note is on main.

## Combine and inspect

Confirm the working tree is clean with `git status`, then:

```sh
git merge study -m "Combine the study notes"
git log --oneline --graph --all --decorate
git status
```

Expected: both note files are present on main, the history includes a merge joining the branches, and the working tree is clean. Commit hashes and display order can differ. Because this exercise adds different files, a content conflict is not expected.

Explain why both branches share the first commit and why switching to main did not itself merge study. None of these commands uploaded anything to GitHub.

Keep a brief explanation and the graph output if useful. You can leave this disposable repository in place for later practice; the lab does not require deleting files or changing your main study-guide clone.

Sources: [Git merge](https://git-scm.com/docs/git-merge), [Git log](https://git-scm.com/docs/git-log). Compare with the [visual guide](../docs/visual-git-and-github.md).

## Check the result before moving on

Can you identify the shared starting commit and the two lines of work?

Use the graph output and inspect both note files after the merge. Explain why switching branches and merging are different actions.

If you get stuck: If your history looks different, compare the actual sequence with the lab. Do not rewrite it merely to imitate the picture; explain the difference first.

Use the [troubleshooting guide](../docs/troubleshooting-first-steps.md) to choose an inspection and the [challenge workbook](../practice/troubleshooting-challenges.md) to practice the reasoning without changing a live repository.
