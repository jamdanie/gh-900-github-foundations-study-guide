# Lab 7: Write a useful issue and find your work

Goal: practice Markdown, issue templates, assignments, and search in your own fork. No paid service is required.

1. Create a practice issue called `Clarify a Git command` using the study-question template. Describe a command that you want explained.
2. Include a heading, an inline command, and a task list. The sample below is original practice text you can adapt.

```markdown
## What I want to understand

What changes locally when I use `git fetch`?

- [ ] Read the command documentation
- [ ] Try it in my sandbox
- [ ] Explain the result without notes
```

3. Preview before submitting. Confirm that the heading and checklist render, and the command is shown as code.
4. Assign yourself and add a `documentation` label, creating that label in your fork if needed.
5. In the repository's Issues search, enter `is:issue is:open assignee:@me`. Your open assigned issue should appear.
6. Add `label:documentation`. The issue should still appear. Remove the label from the issue and repeat the filter; it should disappear from those filtered results without being deleted.
7. Inspect the issue's subscription control and your repository Watch setting. Decide whether you need this one conversation or broader repository updates.
8. If you implement the clarification, use a branch and PR into your fork. Review the wording before merging.

Expected evidence: a rendered issue, two filter results showing the effect of a label, and an explanation of why subscribing differs from assigning yourself. A checkbox is a record of a task, not proof that the underlying command was run.

If the search is empty, check the repository scope, issue state, assignee, and exact label name. If the Markdown is displayed literally, inspect whether you accidentally wrapped the whole issue body in a code fence.

Sources: [Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax), [search](https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests), [notifications](https://docs.github.com/en/subscriptions-and-notifications/concepts/about-notifications).

## Check the result before moving on

Does changing the filter change the result rather than delete the issue?

Open the issue directly after removing its label, then compare the labeled search. The issue can exist while being excluded by the filter.

If you get stuck: If results are empty unexpectedly, inspect scope, state, assignee, and exact label. Verify the rendered Markdown separately from the search.

Use the [troubleshooting guide](../docs/troubleshooting-first-steps.md) to choose an inspection and the [challenge workbook](../practice/troubleshooting-challenges.md) to practice the reasoning without changing a live repository.
