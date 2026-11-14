# Foundations reference

Use these distinctions to decide which feature fits a task. Follow the sources for details and plan-specific availability.

## Repositories and collaboration

| Term | Plain meaning | When it fits |
| --- | --- | --- |
| Git | Version control on your machine | Record and inspect file history |
| GitHub | Hosting and collaboration around repositories | Share work, review changes, and track tasks |
| Branch | A separate line of work within a repository | Propose a focused change |
| Fork | Your own repository copy connected to an upstream project | Contribute without upstream write access |
| Clone | A local copy of a repository | Work on your computer |
| Template repository | Starting files for a new project | Reuse a structure without copying its full commit history |
| Issue | A task, bug, or request | Track work to do |
| Pull request | A proposed branch change with discussion and review | Decide whether to merge work |
| Discussion | A place for broader conversation and questions | Explore ideas without treating every thread as a task |
| Markdown | Text formatting syntax | Write readable READMEs, issues, and PR descriptions |

A closing keyword such as `Closes #12` in a PR description can close the referenced issue when the PR merges into the default branch. A mention alone does not mean the issue will close.

Sources: [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow), [linking PRs and issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue), [contributing to open source](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-open-source).

## Files and publishing

| Item | What it tells a reader |
| --- | --- |
| README | What the project does and how to use it |
| LICENSE | The permissions and conditions for reuse |
| CONTRIBUTING | How to propose a useful contribution |
| CODEOWNERS | Which people or teams own matching paths |
| SECURITY | How to report a security concern |
| Wiki | Longer project documentation |
| Gist | A small shareable snippet with Git history |
| Pages | A static website published from repository content |

A public repository is not automatically licensed for unrestricted reuse. A secret gist is unlisted, not private: someone with its URL can view it. CODEOWNERS identifies owners; requiring their approval needs the appropriate repository rule.

Sources: [README](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes), [licensing](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository), [code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners), [gists](https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists), [Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).

## Accounts, privacy, and administration

A personal account identifies a person. An organization provides shared ownership and administration of repositories. An enterprise can manage policies across organizations. GitHub Enterprise Cloud is hosted; Enterprise Server is a separately administered deployment option.

Public content is visible broadly; private repository access is restricted to permitted users. Internal visibility is an enterprise feature, not a synonym for private. Check its exact audience before sharing work.

Two-factor authentication adds another verification factor to a password-based sign-in. Passkeys use cryptographic credentials with your device's authentication mechanism. Keep recovery methods available. Enterprise Managed Users allow an enterprise to manage account lifecycle and authentication through its identity provider; this differs from a person's ordinary account joining an organization.

Branch protections and rulesets can require checks or reviews. Running a workflow alone does not make it a merge requirement. Organization policies can control Copilot availability and usage separately from an individual's editor settings.

Sources: [GitHub plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans), [2FA](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/about-two-factor-authentication), [Enterprise Managed Users](https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/identity-and-access-management/enterprise-managed-users), [repository roles](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization).

## Modern tools and useful signals

GitHub Desktop offers a graphical Git workflow. GitHub Mobile supports collaboration while away from a computer. Neither changes the meaning of a commit. github.dev is useful for quick browser edits; Codespaces supplies compute for running tools.

Copilot individual plans provide personal access. Business and Enterprise offerings support organization-managed access and policies, with differences in features and eligibility. Use the [current plan comparison](https://docs.github.com/en/copilot/get-started/plans) for exact limits and supported models. Selecting a model, using an editor's agent mode, and assigning work to an agent are related but distinct choices.

Stars help you save and discover repositories. Watching controls notifications. Following a user or organization helps you keep up with their activity. Repository Insights can show traffic and contribution history; dependency information helps you inspect what a project relies on. Activity counts alone do not measure code quality or learning. Feature previews provide access to selected evolving features and can change.

Sources: [repository graphs](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/about-repository-graphs), [github.dev](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor), [Copilot plans](https://docs.github.com/en/copilot/get-started/plans).

## Community

Open-source contributions can include documentation, bug reports, tests, and code. Read a project's contribution guidance before proposing work. GitHub Sponsors supports eligible open-source contributors financially; starring a repo does not send money. InnerSource applies open-source collaboration practices inside an organization without requiring public access to its repositories.

Try finding one documentation issue you can understand, reading the contribution guidance, and describing a proposed fix before editing. A useful contribution solves an identified problem and gives the maintainer enough information to review it.

Source: [Contributing to open source](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-open-source). Review community coverage in the [official exam outline](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900).

## More practice for common gaps

Use [common decisions](common-decisions.md) to compare similar features, [lab 7](../labs/07-markdown-and-triage.md) for Markdown and triage, and [lab 8](../labs/08-timeline-and-file-maintenance.md) for planning and file maintenance. Questions GHF-022 through GHF-035 cover the added material.
