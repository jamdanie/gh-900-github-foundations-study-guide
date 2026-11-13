# Copilot prompts and slash commands

Use AI when you need an explanation, a first draft, or another way to practice. Read the result and test its claims. A convincing explanation is not proof that a command or permission is correct.

## Slash-command dictionary

These are documented examples for **Copilot Chat in VS Code**. Type `/` in your current chat to see what your installed version supports. Visual Studio, GitHub.com, and other clients have different commands and behavior.

| Command | Meaning | When and why |
| --- | --- | --- |
| `/explain` | Explain active code | Understand unfamiliar logic |
| `/fix` | Suggest a correction | Investigate a selected problem |
| `/tests` | Draft tests for selected code | Explore normal and edge cases |
| `/fixTestFailure` | Help diagnose a failing test | Connect the failure to code |
| `/help` | Show usage guidance | Find supported features |
| `/clear` | Start a fresh chat session | Separate unrelated topics |
| `/new` | Help create a project | Scaffold a practice project |

`/new` is especially context dependent: the GitHub website documentation uses it for a new conversation. Check the command menu, not just a remembered name.

Source: [GitHub Copilot Chat cheat sheet](https://docs.github.com/en/copilot/reference/chat-cheat-sheet).

## Plain-language prompts you can reuse

These are suggested practice prompts, not a record of prompts used on the exam. They work as normal chat text when a slash shortcut is unavailable.

| Goal | Prompt | Why use it |
| --- | --- | --- |
| Understand Git direction | “Explain fetch, pull, and push using my local repository and origin. Tell me what changes in each location.” | Forces an explanation of state |
| Practice one question | “Ask one original GH-900 practice question about pull requests. Wait for my answer, then explain every option.” | Keeps the answer hidden until you decide |
| Read automation | “Explain each event, job, and step in this workflow. Identify its permissions and any external services it calls.” | Connects configuration to behavior |
| Investigate failure | “This test expected Done but received Todo. Explain the likely cause. Show a minimal fix and a test that would catch a regression.” | Gives a concrete failure to investigate |
| Compare access | “Compare read, triage, write, maintain, and admin for this sandbox scenario. Cite the current GitHub role documentation.” | Makes the access decision reviewable |
| Review a PR | “Review this diff for incorrect claims and broken examples. Identify exact lines and explain the concern.” | Produces findings you can verify |

## A useful AI practice loop

Select the small function in `scripts/study_status.py`. Ask for an explanation before running its tests. Then ask for a test covering an unknown status. Compare the suggestion with the intended behavior and run the test yourself.

If the assistant proposes changing a permission, installing an app, or running a shell command, inspect the action first. Do not paste credentials into prompts. Give the assistant the smallest relevant code or error, and verify documentation links it supplies.

Copilot can suggest code in an editor, answer questions, and assist with multi-step work. Agent mode may edit files and use tools; review those changes before accepting or committing them. Model and agent availability depend on your client and plan. Compare individual and organization-managed offerings through current official documentation rather than memorizing prices or treating a plan name as a permission grant.

[Official Copilot documentation](https://docs.github.com/en/copilot) is the reference for current client features, models, plans, and policies.
