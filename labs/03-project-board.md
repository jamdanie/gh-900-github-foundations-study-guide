# Lab 3: Build a study Project

Goal: track a weak topic from an issue through a reviewed change, and observe a built-in Project automation.

Use a Project owned by your personal account for this solo lab. Creating an organization is not required.

1. Create a GitHub Project named `GH-900 study practice` and choose a board layout.
2. Add a Status field with Todo, In Progress, and Done options if these do not already exist.
3. Add a single-select Domain field using the seven domain names from the exam map.
4. In your fork, create an issue titled `Explain fetch versus pull` and another titled `Identify the parts of an Actions workflow`.
5. Add both issues to the Project and set their Domain values. Assign yourself if useful.
6. Create a table view to compare fields and keep a board view grouped by Status. These views show the same underlying items.
7. Open the Project's Workflows settings and enable the built-in workflow that sets an item to Done when its issue is closed. Confirm the target Status value.
8. Move the Git issue to In Progress. Create a branch, write a note explaining the commands, and open a PR into your fork's default branch.
9. In the PR description, use `Closes #` followed immediately by the actual number of the issue you created. Review the diff and merge.
10. Check that the linked issue closed and that its Project item moved to Done.

Expected: the closed issue's status changes through the configured Project workflow. Dragging an item to Done is not, by itself, proof that the linked issue closed.

If the issue remains open, inspect the closing keyword, issue number, and merge target. If it closed but the card stayed put, check that it is an issue-backed item in this Project and the workflow is enabled. A draft item is not automatically a repository issue.

## Other controls to try

Use a label such as `study` to categorize repository issues. Use a milestone for related issues and PRs with a shared target. Filter a Project view to one domain to make a focused review list. If you add dates, try a roadmap view. Inspect Project insights for a chart of your current items; do not confuse the chart with evidence that you understand the material.

Save a short reply explaining how contributors should report unclear questions and reuse it when appropriate. Adjust issue subscriptions so practice notifications remain useful.

Evidence to keep: the issue, PR, and the before/after board state. Explain why you used a Project field, a label, and a milestone for different purposes.

Sources: [About Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects), [Project automation](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project).

## Check the result before moving on

Did the issue close before the Project item moved?

Record the issue state and Project status separately, then explain which configured workflow connects them.

If you get stuck: If only one changed, check that stage of the process. A manually moved card does not demonstrate the issue-closed automation.

Use the [troubleshooting guide](../docs/troubleshooting-first-steps.md) to choose an inspection and the [challenge workbook](../practice/troubleshooting-challenges.md) to practice the reasoning without changing a live repository.
