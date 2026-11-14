import copy
import json
from pathlib import Path
import unittest
from scripts.check_content import validate_questions
from scripts.quiz import select_questions

QUESTIONS = json.loads((Path(__file__).resolve().parents[1] / "practice/questions.json").read_text())


class QuizTests(unittest.TestCase):
    def test_domain_filter_excludes_other_domains(self):
        result = select_questions(QUESTIONS, domain="security")
        self.assertEqual({q["id"] for q in result}, {q["id"] for q in QUESTIONS if q["domain"] == "security"})
        self.assertTrue(result)
        self.assertTrue(all(q["domain"] == "security" for q in result))

    def test_limit_keeps_source_data_intact(self):
        original = copy.deepcopy(QUESTIONS)
        self.assertEqual(len(select_questions(QUESTIONS, limit=2, shuffle=True)), 2)
        self.assertEqual(QUESTIONS, original)

    def test_duplicate_id_is_rejected(self):
        self.assertTrue(validate_questions([QUESTIONS[0], QUESTIONS[0]]))

    def test_missing_wrong_answer_explanation_is_rejected(self):
        bad = copy.deepcopy(QUESTIONS[0])
        del bad["explanations"]["A"]
        self.assertTrue(validate_questions([bad]))

    def test_invalid_answer_is_rejected(self):
        bad = copy.deepcopy(QUESTIONS[0])
        bad["answer"] = "E"
        self.assertTrue(validate_questions([bad]))
