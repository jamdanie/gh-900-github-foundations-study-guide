# Common decisions: what should I use and why?

The first version named these topics but gave them limited practice. This guide adds distinctions you can apply to a new situation. Reviewed November 14, 2026.

## Fork, clone, branch, or template?

| Your task | Choose | Reason |
| --- | --- | --- |
| Contribute to a project without upstream write access | Fork | Prepare changes in your own connected repository |
| Work with an existing repository on your computer | Clone | Bring its files and history to your machine |
| Develop a focused change inside a repository | Branch | Keep that line of work separate until review |
| Start an independent project from reusable starter files | Template | Reuse the structure without inheriting the source's full history |

A template-generated repository starts with a single commit. A fork retains the upstream history. Copying files is not the same as joining the upstream contribution workflow. Before choosing, ask whether you intend to contribute back or start a separate project.

Source: [Repository templates](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).

## Notifications and finding work

Watching a repository or subscribing to a thread controls updates. A star is useful for saving a repository, but does not mean you subscribed to every conversation. Participation, mentions, and assignments can also explain why you receive a notification. Review the reason instead of assuming every message came from Watch.

Use these in GitHub's issue/PR search, not in your shell or Copilot chat:

| Query | Meaning | When to use it |
| --- | --- | --- |
| `is:issue is:open assignee:@me` | Open issues assigned to you | Find your current tasks |
| `is:pr is:open review-requested:@me` | Open PRs requesting your review | Find reviews waiting on you |
| `is:issue is:open label:documentation` | Open documentation issues | Choose a writing task where that label exists |
| `is:pr is:merged` | Merged pull requests | Inspect completed changes |

In global search, add `repo:jamdanie/gh-900-github-foundations-study-guide` to limit results to this repo. A valid filter can return zero results. It cannot show private content you lack permission to read.

Sources: [Notifications](https://docs.github.com/en/subscriptions-and-notifications/concepts/about-notifications), [issue and PR search](https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests).

## Milestone, iteration, date, or roadmap?

| Need | Feature | Why |
| --- | --- | --- |
| Group repository work toward a target | Milestone | Tracks related issues and PRs and their completion |
| Organize Project items into recurring work periods | Iteration field | Associates items with repeating time blocks |
| Record a specific planned start or finish | Date field | Stores the date you choose |
| See timing across items | Roadmap view | Presents scheduling information on a timeline |

An iteration is a time grouping, not a new repository. A roadmap is a view, not an automation that completes work. A milestone's closed-item percentage is not a percentage of exam mastery.

Sources: [Milestones](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones), [iteration fields](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-iteration-fields).

## AI suggestion, agent, or workflow?

An assistive interaction answers a question or proposes code for you to review. An agent can work through multiple steps, edit files, and use tools within its available permissions. Actions executes the workflow you configured when its trigger fires. These can work together, but producing a suggestion and executing a test are different events.

Choosing a different model does not by itself grant more repository access. Before accepting agent work, inspect the diff and the evidence that checks actually ran. Use the current client and plan documentation for availability; do not assume every editor exposes the same modes.

Source: [About Copilot](https://docs.github.com/en/copilot/get-started/about-github-copilot).

## Personal account or managed user?

Enterprise Managed Users are provisioned and managed through an external identity provider. Their authentication and account lifecycle are controlled by the enterprise's identity setup. They are not simply ordinary personal accounts with a different repository role. Managed accounts have restrictions on public and outside-enterprise collaboration.

A repository Admin role, an organization owner role, and enterprise identity administration address different scopes. If a question asks who controls account provisioning, assigning Write access to a repository does not answer it.

Source: [Enterprise Managed Users](https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/identity-and-access-management/enterprise-managed-users).

## A passing check or an enforced requirement?

An Actions result reports what happened. A configured branch rule can make checks or reviews a condition of merging. A green check does not prove every other requirement is satisfied; a red check is not automatically a merge block unless the relevant rule requires it. Evaluate the rule, its target branch, and any applicable bypass behavior.

Source: [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

## Community support

GitHub Sponsors provides financial support for eligible open-source maintainers. It is different from starring a project or sending a pull request. You can contribute documentation, tests, or useful issue reports without paying for anything. This study guide does not require a sponsorship.

Source: [Sponsors](https://docs.github.com/en/sponsors/getting-started-with-github-sponsors/about-github-sponsors).

## Test yourself in a different way

Ask AI: “Create an original scenario that requires choosing between a fork and a template. Do not reveal the answer. After I answer, change one requirement so the other choice becomes appropriate.”

Try the same approach with a milestone versus an iteration, a subscription versus a star, and a suggestion versus an executed test. Check the explanation against the linked source. These are practice variations, not claims about the wording of actual exam questions.
