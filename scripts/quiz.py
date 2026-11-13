"""One-question-at-a-time practice. Python standard library only."""
import argparse
from collections import defaultdict
import json
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parents[1]
DOMAINS = ("basics", "repositories", "collaboration", "modern", "projects", "security", "community")


def select_questions(questions, domain=None, limit=None, shuffle=False):
    selected = [q for q in questions if domain is None or q["domain"] == domain]
    if shuffle:
        random.shuffle(selected)
    return selected if limit is None else selected[:limit]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--domain", choices=DOMAINS)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--shuffle", action="store_true")
    args = parser.parse_args()
    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be at least 1")
    questions = json.loads((ROOT / "practice/questions.json").read_text())
    selected = select_questions(questions, args.domain, args.limit, args.shuffle)
    results = defaultdict(lambda: [0, 0])
    print("Original learning checks, not actual exam questions. Q quits.")
    for question in selected:
        print(f"\n{question['id']} [{question['domain']}] {question['question']}")
        for key, value in question["options"].items():
            print(f"{key}. {value}")
        while True:
            try:
                answer = input("Your answer: ").strip().upper()
            except (EOFError, KeyboardInterrupt):
                answer = "Q"
            if answer in ("A", "B", "C", "D", "Q"):
                break
            print("Enter A, B, C, D, or Q.")
        if answer == "Q":
            break
        correct = answer == question["answer"]
        results[question["domain"]][0] += int(correct)
        results[question["domain"]][1] += 1
        print(f"{'Correct' if correct else 'Review this one'}. Answer: {question['answer']}")
        for key, reason in question["explanations"].items():
            print(f"{key}: {reason}")
        print("Key idea:", question["key_idea"])
        print("Source:", question["source"])
    total = sum(value[1] for value in results.values())
    score = sum(value[0] for value in results.values())
    print(f"\nResult: {score}/{total} answered. This is not an exam score prediction.")
    for domain, (right, answered) in sorted(results.items()):
        print(f"{domain}: {right}/{answered}")


if __name__ == "__main__":
    main()
