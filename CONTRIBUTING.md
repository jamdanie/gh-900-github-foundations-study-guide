# Contributing

Use an issue to report an unclear explanation or an incorrect answer. Include the file, the claim, and a current official source supporting the correction. Do not submit recalled exam questions or assessment copies.

For a change, fork the repo, create a branch, edit the material, and run:

```sh
python -m unittest discover -s tests -v
python scripts/check_content.py
```

Open a PR explaining the problem, the corrected behavior or explanation, and what you checked. Keep examples small and explain why the other answer choices do not fit.
