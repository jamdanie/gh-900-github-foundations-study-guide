# Case study: document a simulated service interruption

[Table of contents](../CONTENTS.md)

This is a fictional exercise supplied by the guide. It does not describe a feature tested in any particular Steam game. You can complete it with paper and a GitHub sandbox. If you use a game instead, substitute only observations you actually made and identify the title.

## Supplied observations

A simulated service was available before a link was disconnected. After the disconnection, the simulated service became unavailable. Restoring the link restored service in this attempt. No other links or failures were tested.

## Stage 1: Separate the claim from the evidence

Write a short note describing the before state, action, after state, and restoration. Does this prove the entire design lacks redundancy? Does it show what would happen with a different link?

<details>
<summary>Review your conclusion</summary>

The observations support a narrow claim about this attempt. They do not establish every property of the topology. Record the untested conditions as questions. Avoid presenting an interpretation about all redundancy as a measured result.
</details>

## Stage 2: Track the documentation task

Create an issue in your own sandbox asking for a clearer diagram and an explanation of the limitation. Include a finish condition: the note must distinguish the observed interruption from untested failure paths.

Add it to a Project if useful. This is a documentation exercise, not a request to change real infrastructure.

## Stage 3: Propose an improvement

Create a branch, add the note and diagram, and open a PR into your sandbox. Use [lab 14](../labs/14-explain-with-a-diagram.md) to keep the drawing and prose consistent. You can draw a simple supplied topology, but label it as an illustration rather than inventing measured devices or traffic.

## Stage 4: Review

Check whether the note claims more than the observations establish. Inspect the diff, any available checks, and the issue's finish condition. If working alone, identify the review as a self-review.

Compare your explanation with the [worked review](worked-simulation-review.md), then revise if needed.

## Stage 5: Explain the GitHub part

Identify the issue, branch, commit, PR, and Project item, if used. Explain the difference between merging the note and repairing a service. No real equipment was repaired in this exercise.

For optional software, use the existing [visual resource guide](../docs/visual-learning-resources.md). A game purchase is not required.
