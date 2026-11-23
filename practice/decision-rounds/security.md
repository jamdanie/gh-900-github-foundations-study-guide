# Decision round: Security and administration

[All decision rounds](README.md) · [Chapter](../../chapters/06-security-administration.md)

Choose an answer and explain why the other choices do not fit before opening the explanation. These are original practice questions, not recalled exam content.

## 1. An enterprise wants its identity provider to provision managed GitHub user accounts and control their lifecycle. Which concept fits?

A. A README badge

B. Enterprise Managed Users

C. A repository milestone

D. A secret gist

<details>
<summary>Answer and explanations</summary>

Correct answer: **B**.

- A. A badge displays information and does not provision accounts.
- B. Enterprise Managed Users connects managed account lifecycle and authentication to an identity provider.
- C. A milestone organizes work, not identities.
- D. An unlisted snippet does not manage account provisioning.

</details>

## 2. An integration only needs one sandbox repository. Which access decision should you investigate first?

A. Grant every repository because it is easier

B. Turn off 2FA

C. Limit its installation to the needed repository and permissions

D. Make every repository public

<details>
<summary>Answer and explanations</summary>

Correct answer: **C**.

- A. Broad access is not justified by a one-repository task.
- B. Weakening sign-in protection does not establish the integration's required scope.
- C. Inspect the needed repository selection and permissions rather than assuming broad access is necessary.
- D. Changing visibility exposes content and is not a substitute for scoped integration access.

</details>

## Hands-on challenge

Write a fictional one-repository integration request and list what it actually needs to do. Inspect available scopes without installing an app or changing real permissions.

## Change the requirement

Rewrite one question so a different feature becomes appropriate. Explain the changed requirement; do not merely swap the answer letters. Use the [review log](../review-log.md) if the difference remains unclear.

Reading and sources: [related guide](../../docs/foundations-reference.md) and its linked official documentation. These rounds supplement the main quiz; two questions cannot establish mastery of a domain.
