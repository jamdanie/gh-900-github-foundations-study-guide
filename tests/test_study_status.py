import unittest
from scripts.study_status import study_status


class StudyStatusTests(unittest.TestCase):
    def test_open_item_is_todo(self):
        self.assertEqual(study_status("open"), "Todo")

    def test_started_item_is_in_progress(self):
        self.assertEqual(study_status("working"), "In Progress")

    def test_closed_item_is_done(self):
        self.assertEqual(study_status("closed"), "Done")

    def test_case_and_whitespace_are_normalized(self):
        self.assertEqual(study_status(" CLOSED "), "Done")

    def test_unknown_state_is_rejected(self):
        with self.assertRaises(ValueError):
            study_status("almost")
