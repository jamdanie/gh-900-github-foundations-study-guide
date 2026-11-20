# Troubleshooting: inspect before changing

[Table of contents](../CONTENTS.md)

Start with the exact result you observed. “Git is broken” does not distinguish a local file problem from an authentication failure or a remote branch mismatch.

## Local files and commits

| Symptom | Inspect first | What the result can tell you |
| --- | --- | --- |
| A saved change is missing from the commit | `git status`, `git diff`, and `git diff --staged` | Whether the change is untracked, unstaged, or staged |
| A file has both staged and unstaged changes | Both diffs | You may have edited again after staging |
| GitHub does not show a local commit | Local log, branch, and remote URL | Whether the commit exists locally and which destination you intended |
| A file disappeared after switching branches | Current branch and its history | The file may exist only on another branch |
| A renamed note no longer opens from README | The link target and actual filename | A link may still name the previous path |

These inspections do not decide what content you should keep. Read the result before staging or restoring anything. In particular, an empty unstaged diff does not prove the staging area is empty.

Sources: [Git status](https://git-scm.com/docs/git-status), [Git diff](https://git-scm.com/docs/git-diff). See the [command dictionary](command-dictionary.md) for command meanings.

## A manual workflow is not available

Check that you selected the intended repository and workflow. A manual run requires `workflow_dispatch`; the workflow must be present on the default branch, and the user needs the required repository access. A workflow file on only a practice branch may explain why the expected button is missing.

Do not change unrelated permissions just to make a button appear. Read the workflow configuration and the current access first.

Source: [Manually running a workflow](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow).

## A workflow ran but failed

Open the failing job and step. Record the command, the reported failure, and the commit being tested. In this repo, an assertion failure in the study-status test differs from a missing Markdown target reported by the content checker.

Fix the identified problem, run the relevant check, and inspect the new result. A successful older run is not evidence for a new revision. A queued run is not a failed test.

## A Project item did not move

Check the underlying issue state, whether the item is backed by that issue, and the configured Project workflow. If an issue did not close, investigate that step first. If it closed but its card did not move, investigate the Project's automation.

Follow the [Project lab](../labs/03-project-board.md) for the intended setup. A status label alone does not prove the linked issue changed state.

## Ask for help with useful evidence

Describe the goal, the command or control used, the expected result, and the actual result. Include only relevant output. Remove credentials and private details. Say what you have already checked so the next person does not have to guess.

Try the [challenge workbook](../practice/troubleshooting-challenges.md) before troubleshooting a live repository.
