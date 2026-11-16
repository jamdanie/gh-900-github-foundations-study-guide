# Actions in plain language

Actions runs automation. For this repository, automation checks the study material after changes. CI means continuous integration: running checks as changes are brought into a project. CD refers to continuous delivery or deployment. A test workflow does not automatically deploy anything.

## Read the workflow already in this repo

Open [checks.yml](../.github/workflows/checks.yml) beside this page.

| Name | Meaning | Example in this file |
| --- | --- | --- |
| Event | What starts a run | A push, a pull request event, or a manual dispatch |
| Workflow | The configured automation process | `Study material checks` |
| Job | A group of steps executed on one runner | `validate` |
| Runner | The machine executing the job | Selected with `runs-on: ubuntu-latest` |
| Step | One task within the job | Run the lab tests |
| Action | Reusable automation called by a step | `actions/checkout@v4` retrieves the repository for the job |

The checkout step makes files available to the runner. The following `run:` steps execute Python commands. A `uses:` step calls an action; a `run:` step executes a command. The workflow file is written in YAML, a text format where indentation matters.

Source: [Understanding GitHub Actions](https://docs.github.com/en/actions/get-started/understand-github-actions).

## What does a green check tell you?

Open Actions on GitHub, select a run for the change you are studying, and open the job and its step logs. In this repo, look for the unit test result and the content check result. Verify that the run belongs to the commit you meant to inspect.

A successful run shows that the configured checks passed. It does not establish that every explanation is accurate or that every exam topic is covered. Read the material as well. If a run fails, start with the failed step's output; rerunning an unchanged mistake does not fix it.

## Environment has more than one meaning

A development environment is where you edit and run your work, such as a local setup or a Codespace. A GitHub Actions deployment environment is a named target associated with deployment settings, including applicable protection rules, variables, and secrets.

This repo's [sandbox workflow](../.github/workflows/sandbox-environment.yml) uses `study-sandbox` and writes a summary. It does not deploy an application. Follow the [environment lab](../labs/02-environments-and-actions.md) to inspect what it actually does.

Source: [Deployment environments](https://docs.github.com/en/actions/deployment/targeting-different-environments/managing-environments-for-deployment).
