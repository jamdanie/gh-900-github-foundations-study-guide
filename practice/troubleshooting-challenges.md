# Troubleshooting challenges

[Table of contents](../CONTENTS.md) · [First steps guide](../docs/troubleshooting-first-steps.md)

These are original fictional practice situations. Predict your next inspection before opening the explanation. They do not require breaking a repository or buying a game.

## 1. The disappearing new sentence

You stage a note, add another sentence, save, and commit the staged content. The commit contains the earlier version.

<details>
<summary>Inspect and explain</summary>

Compare the unstaged and staged diffs before the commit, or inspect the remaining working change afterward. Staging selected the earlier saved content. Editing afterward did not update that selection automatically. Stage the additional sentence only if you want it in another commit.

Change one condition: if the file was never saved in the editor, Git cannot stage the unsaved editor buffer.
</details>

## 2. The wrong branch on the website

The push reports success, but the note is absent from GitHub's main branch.

<details>
<summary>Inspect and explain</summary>

Check the branch that was pushed and the branch selected on the website. A successful push of a study branch does not merge it into main. Find the commit on the intended branch, then use a PR if integration is the next task.

Change one condition: if the remote URL points to a different repository, inspect that destination as well.
</details>

## 3. The missing Run workflow button

Your practice branch contains a new workflow with a manual trigger, but you cannot run it through the expected interface.

<details>
<summary>Inspect and explain</summary>

Check the default branch, the workflow's trigger, repository access, and the selected workflow. The manual workflow must be present on the default branch. Do not assume copying a file to any branch is enough.

Change one condition: if the workflow uses only a push trigger, it was not configured for manual dispatch.
</details>

## 4. Green yesterday, red today

A PR passed checks, then received another commit. The newest run is red.

<details>
<summary>Inspect and explain</summary>

Read the latest run's failing step and its commit. The earlier success does not validate the revision. Compare expected and actual results before changing the implementation.

Change one condition: if the latest run is still queued, wait for its result instead of calling it a failed test.
</details>

## 5. The card says Done

A Project item shows Done, but the linked issue is still open.

<details>
<summary>Inspect and explain</summary>

Inspect both properties and the Project workflow. Project status and issue state are separate. The lab's issue-closed-to-Done automation is not proof that manually choosing Done closes the issue in reverse.

Change one condition: if the item is a draft item, it may not be a repository issue at all.
</details>

## 6. The broken renamed link

A note was renamed, and the content checker reports its old path as missing.

<details>
<summary>Inspect and explain</summary>

Compare the README link target with the new filename. Update the link, run the checker again, and open the link in the branch being reviewed. A file rename can require changes in other files.

Change one condition: if the link is external, this repository's local target check does not prove that website is available.
</details>

## 7. The simulator does not recognize a command

A command from your local Git notes is rejected in a browser teaching tool.

<details>
<summary>Inspect and explain</summary>

Read the simulator's supported commands and instructions. A simulation may implement a limited interface. Do not conclude that installed Git lacks the command solely because the simulator rejected it.

Change one condition: if installed Git rejects it too, inspect the exact error, version, syntax, and current repository state.
</details>

## 8. The game result sounds like work experience

A note says “I repaired a failed production switch,” but the evidence is from a Steam game.

<details>
<summary>Inspect and explain</summary>

Revise the claim to identify the simulation and the observed action. A screenshot can support what happened in the game. It does not establish production experience. The GitHub learning evidence can still be the issue, note, PR, and review.

Change one condition: completing a real local Git exercise supports a local Git claim, but still does not demonstrate administering a production network.
</details>

## Review your reasoning

For each challenge, identify the observed fact, a possible explanation, and the next check that would distinguish explanations. Return to the [command dictionary](../docs/command-dictionary.md), [automation lab](../labs/02-environments-and-actions.md), [Project lab](../labs/03-project-board.md), or [evidence guide](learning-evidence.md) when the distinction is unclear.

These explanations rely on those linked guides and their documentation sources. They are separate from the CLI quiz and Anki deck.
