# Practice guide

[Table of contents](../CONTENTS.md) · [Topic finder](../docs/topic-finder.md) · [Review log](review-log.md)

## Choose a practice format

| What you need | Start here |
| --- | --- |
| Explain a basic next step | [Eight beginner checks](beginner-checks.md) |
| Review one small concept | [Thirty topic cards](cards/README.md) |
| Apply a concept when a requirement changes | [Ten scenarios](scenario-workbook.md) |
| Answer multiple-choice questions | [Question bank](questions.md) or the CLI below |
| Repeat concepts in flashcards | Anki import instructions below |
| Decide what to study next | [Review log](review-log.md) |

## Multiple-choice practice

This starter set contains 35 original questions: five in each domain. It is not a full or exam-weighted mock test. Questions do not come from recalled exam content.

Run `python scripts/quiz.py` from the repo root for one question at a time. The program waits for A, B, C, or D, explains every choice, and shows results by domain. Enter Q to quit. Results are printed locally and are not uploaded or saved.

Use `--domain` with `basics`, `repositories`, `collaboration`, `modern`, `projects`, `security`, or `community`. Use `--shuffle` to change question order and `--limit 10` for a short session. The choices retain their original letters.

For browser reading, open [questions and explanations](questions.md). Answers are inside expandable sections.

## Anki import

Import `anki.tsv` as a tab-separated text file using a Basic note type. Map column 1 to Front, column 2 to Back, and column 3 to Tags. Enable HTML in fields. Exclude the first header row from import if Anki does not recognize it automatically. Preview one note before completing the import.

Every front contains the full question and every choice. The back repeats the choices, marks the correct answer, explains each option, and gives a key idea and source. Domain tags let you study a weak section separately.

## Review what you missed

After a wrong answer, explain which word in the scenario changes the decision. Return to the matching guide or lab and demonstrate the concept. Later, try a different example. Repeatedly recognizing the same answer does not show that you can apply the concept in a new situation.

## Short-answer practice

The [scenario workbook](scenario-workbook.md) adds 10 original exercises with explanations and changed conditions. It is separate from the 35-question CLI quiz and TSV deck. Use it to practice explaining your choice instead of recognizing an answer letter.

## Before the quiz

Try the [eight beginner checks](beginner-checks.md) if the terms still feel unfamiliar. Each asks for a next step and explains the reason. These are separate from the CLI quiz and Anki deck.
