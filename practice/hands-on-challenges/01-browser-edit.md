# Challenge 1: Where is the saved change?

[Challenge menu](README.md)

Goal: distinguish an editor buffer from a committed file. You need a GitHub account and a disposable repository you own, initialized with a README.

1. Create a branch named `practice/browser-note` from your sandbox's default branch.
2. Open the repository in `github.dev` by changing that part of its URL. Confirm the selected branch.
3. Add `session-note.md` with two sentences: what you plan to learn and what you will inspect afterward.
4. Inspect Source Control. Before committing, open the same branch on github.com in another tab. Look for the new file.
5. Stage the file, review its changes, and commit with a message explaining the note.
6. Return to github.com, refresh, and confirm the file and commit exist on that branch.

## Explain the result

Before the commit, the web editor keeps your work in browser storage. Seeing text in the editor doesn't prove that it is in the repository. After committing, verify it independently on github.com.

The web editor has no integrated compute terminal for running this repository's Python quiz. Use a local Python installation or an appropriate Codespace for that task. Check Codespaces usage settings before creating one.

## If it differs

Check account, repository, branch, and the Source Control error message. Keep a separate copy of unsaved text before troubleshooting browser storage. Don't clear storage as your first repair.

Finish when you can point to the committed note and explain where it was before committing.

Source: [GitHub's web editor documentation](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor), checked November 25, 2026.
