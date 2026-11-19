import unittest
from engine.followup_engine import select_next_question

class AdaptiveSelectionTests(unittest.TestCase):
    def test_question_that_splits_diagnoses_balanced_is_preferred(self):
        assertions = [{"fact": "symptom_a", "description": "Symptom A"}, {"fact": "symptom_b", "description": "Symptom B"}, {"fact": "symptom_c", "description": "Symptom C"}]
        rules = [
            {"id": 1, "conditions": ["root", "symptom_a"], "conclusion": "cause_a"},
            {"id": 2, "conditions": ["root", "symptom_a"], "conclusion": "cause_b"},
            {"id": 3, "conditions": ["root", "symptom_b"], "conclusion": "cause_c"},
            {"id": 4, "conditions": ["root", "symptom_c"], "conclusion": "cause_d"},
        ]
        question = select_next_question(["root"], {}, rules, assertions)
        self.assertEqual(question["fact"], "symptom_a")
        self.assertEqual(question["diagnosis_count"], 4)
        self.assertEqual(question["discrimination_score"], 2)

    def test_no_and_not_sure_exclude_rule_conditions(self):
        assertions = [{"fact": "a", "description": "A"}, {"fact": "b", "description": "B"}]
        rules = [{"id": 1, "conditions": ["root", "a"], "conclusion": "x"}, {"id": 2, "conditions": ["root", "b"], "conclusion": "y"}]
        question = select_next_question(["root"], {"a": "no"}, rules, assertions)
        self.assertEqual(question["fact"], "b")
        question2 = select_next_question(["root"], {"b": "not_sure"}, rules, assertions)
        self.assertEqual(question2["fact"], "a")

    def test_no_repeat_and_no_questions_without_active_rules(self):
        assertions = [{"fact": "a", "description": "A"}]
        rules = [{"id": 1, "conditions": ["root", "a"], "conclusion": "x"}]
        self.assertIsNone(select_next_question(["root"], {"a": "yes"}, rules, assertions))
        self.assertIsNone(select_next_question([], {}, rules, assertions))

    def test_explicitly_excluded_fact_is_never_questioned(self):
        assertions = [{"fact": "a", "description": "A"}, {"fact": "b", "description": "B"}]
        rules = [{"id": 1, "conditions": ["root", "a"], "conclusion": "x"}, {"id": 2, "conditions": ["root", "b"], "conclusion": "y"}]
        q = select_next_question(["root"], {}, rules, assertions, excluded_facts=["a"])
        self.assertEqual(q["fact"], "b")

    def test_duplicate_rules_for_same_diagnosis_do_not_inflate_competition(self):
        assertions = [{"fact": "a", "description": "A"}, {"fact": "b", "description": "B"}]
        rules = [
            {"id": 1, "conditions": ["root", "a"], "conclusion": "cause_a"},
            {"id": 2, "conditions": ["root", "a"], "conclusion": "cause_a"},
            {"id": 3, "conditions": ["root", "b"], "conclusion": "cause_b"},
        ]
        q = select_next_question(["root"], {}, rules, assertions)
        self.assertEqual(q["fact"], "a")
        self.assertEqual(q["diagnosis_count"], 2)

if __name__ == "__main__":
    unittest.main()
