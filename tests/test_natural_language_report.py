import unittest
from engine.natural_language_report import build_user_report

class NaturalLanguageReportTests(unittest.TestCase):
    def test_report_for_supported_cause_is_plain_language(self):
        result = {
            "ranked": [{"conclusion":"charger_fault","solution":"Try a working compatible charger."}],
            "evidence_report":{"entries":[{"conclusion":"charger_fault","confirmed_conditions":["phone_not_charging","charger_damaged"],"derived_conditions":[],"missing_conditions":[]}]},
            "evidence_status":{"status":"supported"},
            "contradictions":[],
        }
        report=build_user_report(result,{"phone_not_charging":"Phone is not charging","charger_damaged":"Charger is damaged"})
        self.assertIn("possible explanation",report["opening"].lower())
        self.assertEqual(report["causes"][0]["solution"],"Try a working compatible charger.")
        self.assertEqual(report["causes"][0]["missing"],[])

    def test_insufficient_report_does_not_claim_certain_diagnosis(self):
        result={"ranked":[{"conclusion":"charger_fault","solution":"Try another charger."}],"evidence_report":{"entries":[{"conclusion":"charger_fault","confirmed_conditions":["phone_not_charging"],"derived_conditions":[],"missing_conditions":["charger_damaged"]}]},"evidence_status":{"status":"insufficient"},"contradictions":[]}
        report=build_user_report(result,{"charger_damaged":"Charger is damaged"})
        self.assertIn("not enough",report["opening"].lower())
        self.assertEqual(report["causes"][0]["missing"],["Charger is damaged"])

    def test_contradictions_are_explained_without_cause_claim(self):
        result={"ranked":[],"evidence_report":{"entries":[]},"evidence_status":{},"contradictions":[{"facts":["phone_charging","phone_not_charging"]}]}
        report=build_user_report(result,{"phone_charging":"Phone is charging","phone_not_charging":"Phone is not charging"})
        self.assertFalse(report["has_causes"])
        self.assertIn("conflicting",report["opening"].lower())

    def test_no_match_asks_for_more_description(self):
        result={"ranked":[],"evidence_report":{"entries":[]},"evidence_status":{"status":"insufficient"},"contradictions":[]}
        report=build_user_report(result)
        self.assertIn("couldn't find",report["opening"].lower())
        self.assertIn("don't want to guess",report["closing"].lower())

if __name__=="__main__":
    unittest.main()
