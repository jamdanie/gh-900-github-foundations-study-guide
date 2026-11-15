# Repository insights and security tools

Reviewed November 15, 2026. These topics help with repository management and security vocabulary. The scanner comparisons are supporting practice; they are not separate weighted exam domains.

## Read the evidence a feature actually supplies

| Question | Look at | What the evidence means |
| --- | --- | --- |
| What work has happened here? | Available repository activity and contribution graphs | Activity in the displayed period |
| Are people visiting or cloning the project? | Traffic, when your access permits it | Recorded usage within the available reporting window |
| What packages does this project use? | Dependency graph | Detected or submitted dependencies |
| What other projects use its package? | Dependents information | Known supported dependency relationships |
| What changed in this proposal? | Pull request diff | The proposed file edits |
| Did the configured tests run? | Checks and workflow logs | Results for the displayed run and commit |

Repository graphs have plan, visibility, and data limits. Empty data does not automatically mean a project is unused. Stars, commits, and closed issues do not prove code quality, exam readiness, or that every reader succeeded.

Source: [Repository graphs](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/about-repository-graphs).

## Dependencies versus dependents

If your app uses a package, the package is a dependency of your app. If another project uses your published package, that project is a dependent. The dependency graph uses supported manifests, lock files, and submitted dependency information. It is not a list of every relationship that could exist outside GitHub's supported data.

A direct dependency is one your project requests. A transitive dependency arrives through another dependency. Consider both when investigating a vulnerable package.

Source: [Dependency graph](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-graph).

## Choose the right security tool

| Situation | Feature to investigate | Why |
| --- | --- | --- |
| A package version has a known vulnerability | Dependabot alerts | Identifies vulnerable dependencies in supported ecosystems |
| A token or API key was committed | Secret scanning | Looks for exposed credentials |
| Your source may contain a security flaw | Code scanning | Analyzes code for vulnerabilities and errors |
| Changes must pass a review before merging | Branch rules | Enforces the configured merge conditions |

An alert is a finding to investigate, not proof of remediation. A suggested update or fix still needs review. If a real credential is exposed, revoke or rotate it promptly; deleting the visible line alone does not invalidate the credential. Do not commit a real credential to test detection.

Check the repository's current settings and plan before assuming a tool is enabled. These exercises do not require buying security products or changing protection settings on a production repository.

Sources: [Dependabot alerts](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-alerts), [secret scanning](https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning), [code scanning](https://docs.github.com/en/code-security/concepts/code-scanning/code-scanning), [branch protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

## Inspect a pull request in the right place

Use the description and conversation to understand the purpose, Files changed to inspect the diff, Commits to inspect the proposed history, and Checks to inspect automation. The merge status explains remaining blockers. Passing checks do not turn an unfinished draft PR into a merge-ready change.

A draft PR shares work in progress and cannot be merged while it remains a draft. Mark it ready when it is prepared for review; that action does not itself merge it.

Source: [Pull requests](https://docs.github.com/en/pull-requests/reference/pull-requests).
