# Lab 2: Environments, automation, and tests

Goal: run a real check, observe a deliberate failure, fix it, and explain the difference between a development environment and a deployment environment.

## Choose where to run code

| Option | What it supplies | Use it for |
| --- | --- | --- |
| Local editor and terminal | Tools installed on your computer | Everyday editing and testing |
| github.dev | Browser editor without a compute terminal | Small source edits |
| Codespaces | Hosted development environment with compute | Editing and running tools in the browser |
| Dev container | Repeatable tool configuration | Making environment setup consistent |
| Actions environment | Deployment-related rules, variables, and secrets | Controlling a job that targets an environment |

A deployment environment does not provide a development machine. A runner executes the Actions job.

This repo includes `.devcontainer/devcontainer.json`. You can open the fork in a local Dev Containers setup or create a Codespace from GitHub's Code menu. Review usage allowances before starting hosted compute; stop the Codespace when finished. A local Python installation also works and does not require Codespaces.

## Run the checks locally

From the repo root:

```sh
python -m unittest discover -s tests -v
python scripts/check_content.py
```

Expected: all tests pass and the content check reports no errors. The content check validates question structure and local Markdown file links; it does not verify external websites or the truth of every statement.

## Make the test fail on purpose

1. In your fork, create the branch `study/failing-check`.
2. In `scripts/study_status.py`, change the mapping for `closed` from `Done` to `Todo`.
3. Run the tests. The closed-item test should fail.
4. Commit and push the change, then open a PR into your fork's main branch. If Actions is disabled in your fork, enable the workflows in its Actions tab.
5. Open the failed workflow run. Find the test name and compare expected with actual output.
6. Restore the `closed` mapping to `Done`, rerun locally, commit, and push again.
7. Confirm that the new run passes before merging.

This function is a small teaching example. It does not connect to a live Project or move real cards.

## Read the workflow

Open `.github/workflows/checks.yml`. Find its `push`, `pull_request`, and manual `workflow_dispatch` triggers. Locate the job, its Ubuntu runner, the checkout action, and the commands that run the tests. A workflow contains jobs; a job contains steps. `uses` references an action and `run` executes a shell command.

## Try a sandbox deployment environment

In your fork, go to Settings → Environments and create `study-sandbox`. Add an environment variable named `STUDY_MESSAGE` with the value `Sandbox ready`. Do not use a secret for this harmless message.

From Actions, choose **Sandbox environment demo** and run it manually on main. This workflow must be present on the default branch for the manual run interface. It references `study-sandbox`, reads the variable, and writes a job summary. It creates deployment records but does not publish an application.

Expected: a successful run whose summary contains `Sandbox ready`. If the variable is absent, the workflow uses a visible fallback. Confirm the environment spelling and variable scope if you see that fallback unexpectedly.

Where your plan and repository visibility support it, inspect required reviewers and deployment branch restrictions. A reviewer-gated run can wait for approval before its job starts. Do not enable a gate that you cannot satisfy in a solo exercise. An automatically created environment has no custom protection rules merely because its name appears in YAML.

Evidence to keep: one failed run, the fix commit, a passing run, and the sandbox summary. Explain which part tested code and which part demonstrated environment configuration.

Sources: [Actions concepts](https://docs.github.com/en/actions/get-started/understand-github-actions), [Codespaces](https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces), [deployment environments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments).
