# Challenge 2: Find the exact version

[Challenge menu](README.md)

Goal: connect a claim to the version of the file you inspected. This is read-only; you can use this guide's README.

1. Open a Markdown file and compare Preview with Raw. Identify one heading marker that appears in Raw but is formatted in Preview.
2. Open Blame and choose a line that interests you. Open its associated commit and read the change.
3. Explain what changed using the diff. If the commit message doesn't explain why, record that the reason is unknown.
4. Return to the file on the default branch. Press `y` to obtain a commit-specific permalink, then copy it.
5. Compare that URL with the branch URL. Identify the branch name in one and commit identifier in the other.

## Worked interpretation

A fictional note changes from “the test passed” to “the link check passed.” The narrower wording tells readers which check ran. Blame helps locate the revision, but the author's name alone cannot explain the decision.

A branch link follows the branch's current version. A commit permalink identifies the version you reviewed, so another reader can inspect the same text while the branch continues changing.

## Finish check

Write a short evidence note with the file path, commit permalink, observed change, and any unanswered question. Do not infer intent from an author's identity.

Sources, checked November 25, 2026: [file views and Blame](https://docs.github.com/en/repositories/working-with-files/using-files/viewing-and-understanding-files) and [permanent links](https://docs.github.com/en/repositories/working-with-files/using-files/getting-permanent-links-to-files).
