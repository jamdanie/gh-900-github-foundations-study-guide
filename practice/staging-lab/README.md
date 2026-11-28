# Follow one file through Git staging

[Table of contents](../../CONTENTS.md) · [Command dictionary](../../docs/command-dictionary.md)

Use Git installed locally and an editor such as VS Code. Run the five steps in order in a new disposable folder outside any existing repository. The commands work in Git Bash, PowerShell, and ordinary macOS/Linux terminals. Create and edit the text file using your editor.

This lab uses fictional connection states. No game, GitHub account, network access, paid service, or remote repository is required. You can later use the same workflow to record an observation from a [visual learning resource](../../docs/visual-learning-resources.md).

| Step | Last commit | Staging area | Working file |
| --- | --- | --- | --- |
| After 1 | Connected | Connected | Connected |
| After 2 | Connected | Disconnected | Disconnected plus uncertainty |
| After 4 | Connected | Connected | Disconnected plus uncertainty |
| After 5 | Disconnected plus uncertainty | Same | Same |

The staging area is also called the index. The table is a prediction to compare with your own output, not a claim that you completed the exercise.

1. [Create the first snapshot](01-first-snapshot.md)
2. [See two versions of one file](02-two-versions.md)
3. [Decode the two status columns](03-read-short-status.md)
4. [Unstage without deleting the edits](04-unstage-without-loss.md)
5. [Commit the complete observation](05-complete-the-observation.md)

If your output differs, inspect the two diffs and the saved file before continuing. Do not use a destructive reset to match the table.

## Finish condition

Explain how the same file held staged and unstaged changes at once. Show which inspection revealed each change. Completing this lab adds no questions to the quiz or cards to existing Anki decks.
