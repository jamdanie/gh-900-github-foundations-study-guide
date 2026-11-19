# Chapter 6: Security and administration

[Table of contents](../CONTENTS.md) · [Previous chapter](05-project-management.md) · [Next chapter](07-community.md)

Ask three separate questions: who is signing in, what they are allowed to do, and which conditions apply to a change. Account authentication, repository permissions, and merge requirements answer different questions.

## Key terms

| Term | Meaning |
| --- | --- |
| Authentication | Verifying identity during access. |
| Authorization | Deciding what an identity may do. |
| Team | An organization group used for collaboration and access management. |
| Branch rule | A configured condition governing changes to matching branches. |

## Worked example

A teammate can sign in successfully but cannot push to a repository. Successful authentication does not grant repository write permission. Inspect the account and applicable repository access before changing unrelated security settings.

## Where people get confused

A repository role is not the same as an organization owner role. Likewise, a workflow result is not automatically an enforced merge condition. Identify the scope of the setting and the rule that actually applies.

## Read and try

- [Teams and access lab](../labs/04-team-management.md)
- [2FA, OAuth, and account settings](../labs/06-profile-and-security.md)
- [Accounts, visibility, and roles](../docs/foundations-reference.md)
- [Security tool comparisons](../docs/insights-and-security-tools.md)
- [Managed users and branch requirements](../docs/common-decisions.md)

The linked guides include product documentation and sources. Use the [official topic outline](../docs/exam-outline.md) for scope; this chapter is a reading route, not a complete replacement for the official objectives.

## Practice access decisions on paper first

Use fictional requests: one person needs to read documentation and another needs to propose an edit on a repository branch. Explain the appropriate access for each using [the team lab](../labs/04-team-management.md). This mission does not require changing anyone's permissions. Keep credentials out of screenshots and follow the [evidence guide](../practice/learning-evidence.md).

## Practice and review

Explain why an exposed token needs to be revoked or rotated even after its visible text is deleted. Then explain why giving someone Admin access is not a routine fix for every access problem.

From the repository root, use `python scripts/quiz.py --domain security` for the existing five-question domain sample. The sample is not a readiness prediction. Record what you could explain and what still needs practice in the [review log](../practice/review-log.md).

[Table of contents](../CONTENTS.md) · [Previous chapter](05-project-management.md) · [Next chapter](07-community.md)
