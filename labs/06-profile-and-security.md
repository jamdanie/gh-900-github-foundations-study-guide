# Lab 6: Profile settings and account security

Goal: understand which information is public, how you sign in, and what an application is allowed to access. Use your own account; do not change another person's settings.

## Inspect your profile

Open your profile and review the name, bio, links, and pinned repositories. Decide what helps a reader understand your work. Review email privacy and commit attribution settings before publishing new commits. Public profile information and the author email recorded in Git history are different things.

For this study project, a clear description should tell readers the exam, the learning approach, and where to start. Repository topics help describe its subject; they do not guarantee a search ranking.

## Distinguish the security controls

| Control | Plain meaning | When it matters |
| --- | --- | --- |
| Two-factor authentication (2FA) | Another verification factor for a password-based sign-in | A stolen password alone should not be enough |
| Passkey | Cryptographic sign-in credential controlled through an authenticator | Sign in without typing a password; GitHub passkeys can satisfy password and 2FA requirements |
| OAuth | A framework for authorizing application access | Review what an integration may do on your behalf |
| GitHub App installation | App access governed by its permissions and selected repositories | Include the needed repo without automatically exposing every repo |
| Personal access token | A credential used for authorized API or Git access | Limit permissions, protect it, and revoke it when no longer needed |
| SSH key | A key pair used to authenticate an SSH connection | Authenticate Git operations without treating the public key as a secret |
| Branch rule | A condition on changes to a protected branch | Require appropriate reviews or checks |

OAuth is the term used here for app authorization. OATH is a different name associated with open authentication standards; do not treat the spellings as interchangeable.

## Review without weakening protection

1. Open your account's password and authentication settings. Identify the configured sign-in and recovery methods. Do not publish recovery codes or private keys.
2. Review installed GitHub Apps and authorized OAuth apps. Identify an integration you recognize and inspect its scope or repository selection.
3. Explain whether the integration needs one repository or all repositories. Do not grant broader access just to complete a lab.
4. Inspect a sandbox repository's visibility and collaborator access. State who can read it and who can change it.
5. Inspect the Security tab. Identify available dependency alerts, secret protection, or code scanning features without assuming every feature is enabled or included in your plan.

If you choose to change an authentication setting, follow GitHub's current instructions and preserve a working recovery route. This exercise can be completed as a review; disabling protection is not part of it.

Evidence: a short explanation of authentication versus authorization and the reason for an app's repository scope. Keep credentials and account recovery details out of the record.

Sources: [Passkeys](https://docs.github.com/en/authentication/authenticating-with-a-passkey/about-passkeys), [2FA](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/about-two-factor-authentication), [OAuth authorization](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps), [installed app access](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps).

## Check the result before moving on

Can you explain authentication and app authorization without exposing account details?

Write a fictional example of signing in and a separate example of an application's repository scope.

If you get stuck: If your evidence includes recovery codes, tokens, or private keys, remove those details. The exercise does not require weakening sign-in protection.

Use the [troubleshooting guide](../docs/troubleshooting-first-steps.md) to choose an inspection and the [challenge workbook](../practice/troubleshooting-challenges.md) to practice the reasoning without changing a live repository.
