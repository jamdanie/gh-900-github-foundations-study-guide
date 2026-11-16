# Job or machine

Topic: Actions

A workflow has a validate job and runs-on: ubuntu-latest. Which part selects where the job executes?

<details>
<summary>Explanation</summary>

runs-on selects the runner. validate identifies the job, which contains steps. Distinguishing the work from its execution machine helps you read workflow files without treating every name as a command.

</details>

## Try a different angle

Find the first step inside validate and explain its purpose.

Further reading and sources: [actions in plain language](../../docs/actions-in-plain-language.md).

[All practice cards](README.md)
