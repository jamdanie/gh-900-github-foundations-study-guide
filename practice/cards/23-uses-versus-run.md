# Uses versus run

Topic: Actions

One step has uses: actions/checkout@v4. Another has run: python3 scripts/check_content.py. What differs?

<details>
<summary>Explanation</summary>

The uses step calls a reusable action. The run step executes a shell command. In this workflow, checkout makes repository files available before the Python checker reads them.

</details>

## Try a different angle

Explain what the checker would need if repository files were unavailable on the runner.

Further reading and sources: [actions in plain language](../../docs/actions-in-plain-language.md).

[All practice cards](README.md)
