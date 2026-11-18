import unittest

from validate_data import audit_knowledge_base, validate_knowledge_base


class KnowledgeBaseAuditTests(unittest.TestCase):
    def test_repository_knowledge_base_passes_audit(self):
        report = validate_knowledge_base()
        failed = [
            (name, details)
            for name, passed, details in report["checks"]
            if not passed
        ]
        self.assertEqual(failed, [])
        self.assertEqual(report["rule_count"], 100)
        self.assertEqual(report["fact_count"], 300)

    def test_missing_condition_fact_is_reported(self):
        rules = [{
            "id": 1,
            "conditions": ["unknown_phone_fact"],
            "conclusion": "sample_diagnosis",
            "solution": "Check the device."
        }]
        facts = [{
            "id": 1,
            "fact": "known_phone_fact",
            "description": "A known fact.",
            "keywords": ["known"]
        }]
        report = audit_knowledge_base(rules, facts)
        self.assertEqual(report["missing_facts"], ["unknown_phone_fact"])
        self.assertFalse(dict(
            (name, passed) for name, passed, _ in report["checks"]
        )["Rule conditions linked to known facts"])

    def test_identical_conditions_with_different_conclusions_are_flagged(self):
        conditions = ["phone_slow", "storage_full"]
        rules = [
            {
                "id": 1,
                "conditions": conditions,
                "conclusion": "diagnosis_one",
                "solution": "First action."
            },
            {
                "id": 2,
                "conditions": list(reversed(conditions)),
                "conclusion": "diagnosis_two",
                "solution": "Second action."
            },
        ]
        facts = [
            {
                "id": index,
                "fact": name,
                "description": name,
                "keywords": [name]
            }
            for index, name in enumerate(conditions, start=1)
        ]
        report = audit_knowledge_base(rules, facts)
        self.assertEqual(len(report["conflicting_condition_sets"]), 1)
        checks = dict((name, passed) for name, passed, _ in report["checks"])
        self.assertFalse(checks["No conflicting rule conclusions"])

    def test_duplicate_conditions_inside_one_rule_are_rejected(self):
        rules = [{
            "id": 1,
            "conditions": ["phone_slow", "phone_slow"],
            "conclusion": "slow_phone_diagnosis",
            "solution": "Restart the phone."
        }]
        facts = [{
            "id": 1,
            "fact": "phone_slow",
            "description": "The phone is slow.",
            "keywords": ["slow phone"]
        }]
        report = audit_knowledge_base(rules, facts)
        self.assertFalse(dict(
            (name, passed) for name, passed, _ in report["checks"]
        )["Rule structure"])


if __name__ == "__main__":
    unittest.main()
