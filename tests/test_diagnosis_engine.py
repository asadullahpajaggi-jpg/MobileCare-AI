import unittest

from engine.diagnosis_engine import summarize_diagnosis


class DiagnosisSummaryTests(unittest.TestCase):
    def test_reports_direct_evidence(self):
        trace = [{
            "rule_id": 7, "conditions": ["battery_drains_fast", "phone_old"],
            "conclusion": "battery_health_low", "solution": "Check battery health.",
        }]
        report = summarize_diagnosis(trace, ["battery_drains_fast", "phone_old"])
        self.assertEqual(report["diagnosis_count"], 1)
        self.assertEqual(report["directly_supported_count"], 1)
        self.assertEqual(report["entries"][0]["confirmed_conditions"],
                         ["battery_drains_fast", "phone_old"])
        self.assertEqual(report["entries"][0]["missing_conditions"], [])

    def test_marks_unestablished_conditions_missing(self):
        trace = [{
            "rule_id": 8, "conditions": ["battery_drains_fast", "phone_old"],
            "conclusion": "battery_health_low", "solution": "Check battery health.",
        }]
        report = summarize_diagnosis(trace, ["battery_drains_fast"])
        self.assertEqual(report["entries"][0]["missing_conditions"], ["phone_old"])
        self.assertEqual(report["directly_supported_count"], 0)

    def test_marks_intermediate_conclusion_as_inferred_evidence(self):
        trace = [
            {"rule_id": 1, "conditions": ["a"], "conclusion": "middle", "solution": ""},
            {"rule_id": 2, "conditions": ["middle", "b"], "conclusion": "final", "solution": ""},
        ]
        report = summarize_diagnosis(trace, ["a", "b"])
        self.assertEqual(report["entries"][1]["derived_conditions"], ["middle"])
        self.assertTrue(report["entries"][1]["evidence_complete"])

    def test_ignores_duplicate_conclusions(self):
        trace = [
            {"rule_id": 1, "conditions": ["a"], "conclusion": "cause", "solution": "s1"},
            {"rule_id": 2, "conditions": ["b"], "conclusion": "cause", "solution": "s2"},
        ]
        report = summarize_diagnosis(trace, ["a", "b"])
        self.assertEqual(report["diagnosis_count"], 1)


if __name__ == "__main__":
    unittest.main()
