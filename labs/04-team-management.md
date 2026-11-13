# Lab 4: Team management and access

Goal: choose permissions based on the task and understand the account boundary.

An organization team groups organization members and can receive repository access. A personal repository can have collaborators, but it does not contain organization teams. A Project board also does not grant repository write access.

## Choose a role before changing anything

These are practice scenarios, not invitations to real people.

| Sandbox responsibility | Role to investigate | Reason |
| --- | --- | --- |
| Read documentation | Read | No code changes needed |
| Organize issues and PRs | Triage | Manage work without repository write access |
| Push implementation branches | Write | Contribute code |
| Handle routine repository management | Maintain | Manage without full sensitive administration |
| Configure access and major settings | Admin | Requires broad control |

Consult the current role matrix for exact operations and any additional roles offered by your organization. A repository role is different from an organization owner role. Giving someone Admin because it is convenient removes the distinction this lab is meant to teach.

## Solo route

Write a short access plan for the five scenarios above. Identify which settings belong to the repository and which belong to the organization. Inspect your own repository's collaborator settings without adding anyone. Explain how you would remove access when a task ends.

## Optional organization sandbox route

If you already administer a suitable sandbox organization, create a team for practice and connect it to a sandbox repository. Choose the lowest role that supports the task. Add another person only when they have agreed to participate. Team members must be organization members; outside collaborators cannot be team members.

Review who can maintain the team and who owns the organization. Inspect branch rules that require pull requests or checks. Check plan support before assuming a protection feature is available. The included CODEOWNERS file identifies the study repo owner; it does not independently enforce a required review.

Use a disposable branch to propose a documentation change. Inspect whether a check or review requirement actually blocks merging. A check running in Actions is not automatically a required check.

Evidence to keep: the selected role and your reason, the rule you tested, and its observed effect. Do not publish member lists or access screenshots from a real workplace.

Sources: [Organization teams](https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams), [repository roles](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization).
