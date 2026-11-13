"""Validate quiz data and local file links, not factual accuracy or external URLs."""
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOMAINS = {"basics", "repositories", "collaboration", "modern", "projects", "security", "community"}


def validate_questions(questions):
    errors = []
    seen = set()
    for q in questions:
        ident = q.get("id", "missing-id")
        if ident in seen:
            errors.append(f"Duplicate id: {ident}")
        seen.add(ident)
        if q.get("domain") not in DOMAINS:
            errors.append(f"{ident}: invalid domain")
        for field in ("question", "key_idea", "source"):
            if not isinstance(q.get(field), str) or not q[field].strip():
                errors.append(f"{ident}: missing {field}")
        for field in ("options", "explanations"):
            values = q.get(field, {})
            if not isinstance(values, dict) or set(values) != set("ABCD"):
                errors.append(f"{ident}: {field} must contain A-D")
            elif any(not isinstance(v, str) or not v.strip() for v in values.values()):
                errors.append(f"{ident}: empty {field}")
        if q.get("answer") not in ("A", "B", "C", "D"):
            errors.append(f"{ident}: invalid answer")
        if not q.get("source", "").startswith("https://"):
            errors.append(f"{ident}: expected HTTPS source")
    if not questions:
        errors.append("No questions found")
    return errors


def main():
    questions = json.loads((ROOT / "practice/questions.json").read_text())
    errors = validate_questions(questions)
    for path in ROOT.rglob("*.md"):
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
            parsed = urlsplit(target)
            if parsed.scheme or not parsed.path:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing local target {target}")
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print(f"Validated {len(questions)} questions and local Markdown file targets.")


if __name__ == "__main__":
    main()
