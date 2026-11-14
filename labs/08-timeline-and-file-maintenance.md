# Lab 8: Plan a small change and maintain its files

Goal: connect a Project timeline to repository work, then rename a tracked file without breaking its documentation link. Use your fork and the personal Project from lab 3.

## Plan the work

1. Create two issues in your fork: `Write a command note` and `Review the command note`.
2. Create a repository milestone named `Command notes practice` and add both issues.
3. Add both issues to your Project. Create an iteration field for study sessions and put the issues in different iterations.
4. Create a roadmap view. Configure it to display the iteration field, then compare it with the board view.
5. Explain what each view shows. The milestone groups repository work; the iteration schedules Project items; the board groups their status.

Expected: you can see the same work through different planning views. Moving an item to another iteration does not close its issue or change the file content.

## Rename a file and keep the link working

Start from a clean working tree in your local fork. If the branch name below already exists, choose another unused name.

```sh
git status
git switch -c study/file-maintenance
```

Create `command-note.md` in the repository root with a short explanation of `git status`. Add a relative link to it in README with the label `My command note` and the target `command-note.md`. Then run:

```sh
git add command-note.md README.md
git diff --staged
git commit -m "Add a linked command note"
git mv command-note.md git-status-note.md
```

Update the README link target to `git-status-note.md`. Review and check the change:

```sh
git add README.md
git diff --staged
python scripts/check_content.py
git commit -m "Rename the note and update its link"
git push -u origin study/file-maintenance
```

Open a PR into your fork's main branch. Verify the renamed file and its link before merging. Link the relevant issues and close them only when their work is complete.

Expected: the local link check passes and the README opens the new path on your branch. For a deliberate failure, leave the old filename in the link and run the checker before fixing it. It should report the missing target.

Keep the PR and a short explanation of why a file rename can require edits in other files. This is optional hands-on practice, not a requirement to memorize a command flag for GH-900.

Sources: [Iterations](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-iteration-fields), [milestones](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones), [renaming files](https://docs.github.com/en/repositories/working-with-files/managing-files/renaming-a-file).
