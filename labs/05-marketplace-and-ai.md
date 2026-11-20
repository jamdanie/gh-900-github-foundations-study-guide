# Lab 5: Marketplace and AI

GitHub Marketplace is the catalog for Actions and apps. It is the “store” relevant to this study topic. An action can be a reusable step in a workflow. An app integrates with GitHub through its own permissions and installation model.

## Inspect before adding

Open [GitHub Marketplace](https://github.com/marketplace). Find the listing for the official checkout action used by this repository and compare the publisher with the `actions/checkout` repository.

Record what problem it solves, its required inputs, what permissions it needs, and where its source is maintained. Compare the version reference in the listing with this repo's workflow. A verified creator badge is not a guarantee that every version is safe or suitable.

Next, inspect an app listing without installing it. Identify which repositories and permissions it requests and whether its pricing fits a sandbox. Explain why you would use an app rather than a single workflow step for the chosen task.

The included workflow uses read-only repository contents permission and disables persisted checkout credentials. For a production workflow, review GitHub's guidance on pinning actions to a full commit SHA and keeping dependencies updated. Do not copy an unfamiliar action into a privileged workflow just because its name sounds useful.

## Ask AI to help with a real, small task

Open `scripts/study_status.py` in your editor. Use `/explain` if your Copilot client offers it, or ask for an explanation in normal text. Then ask for tests of an unknown status and mixed-case input.

Compare its proposed tests with the function's intended behavior: matching is case-insensitive, supported states map to board labels, and unknown states raise `ValueError`. Run the tests. If AI changes the intended behavior to make a test pass, decide whether that change is justified before accepting it.

Explain the difference between asking AI for test code and Actions actually running that code. AI output is a proposal; the test execution is an observed result.

Evidence to keep: a short action-versus-app comparison and one AI suggestion you checked against a real test. You do not need to install a paid app or publish private chat history.

Sources: [Actions versus apps](https://docs.github.com/en/actions/get-started/actions-vs-apps), [choosing actions](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/find-and-customize-actions), [secure use](https://docs.github.com/en/actions/reference/security/secure-use).

## Check the result before moving on

Did a proposed test actually execute?

Separate the AI suggestion, the test you accepted, and the command output. Explain what behavior the test checks.

If you get stuck: If an AI edit changes expected behavior merely to pass, review the requirement before accepting it. If you only inspected an app, do not claim it was installed.

Use the [troubleshooting guide](../docs/troubleshooting-first-steps.md) to choose an inspection and the [challenge workbook](../practice/troubleshooting-challenges.md) to practice the reasoning without changing a live repository.
