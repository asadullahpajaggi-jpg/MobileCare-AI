import unittest
from engine.evidence_decision import assess_evidence

class EvidenceAdequacyTests(unittest.TestCase):
    def test_incomplete_conditions_not_presented_as_supported(self):
        row={"conditions":["a","b"],"confirmed_conditions":["a"],"derived_conditions":[],"missing_conditions":["b"],"rank_score":3}
        result=assess_evidence([row])
        self.assertEqual(result["status"],"insufficient")
        self.assertEqual(result["supported"],[])

    def test_complete_evidence_supported(self):
        row={"conditions":["a","b"],"confirmed_conditions":["a"],"derived_conditions":["b"],"missing_conditions":[],"rank_score":4}
        self.assertEqual(assess_evidence([row])["status"],"supported")

    def test_tied_complete_causes_flagged(self):
        rows=[{"conditions":["a"],"confirmed_conditions":["a"],"derived_conditions":[],"missing_conditions":[],"rank_score":3},{"conditions":["b"],"confirmed_conditions":["b"],"derived_conditions":[],"missing_conditions":[],"rank_score":3}]
        self.assertEqual(assess_evidence(rows)["status"],"competing")

    def test_empty_input_is_insufficient(self):
        self.assertEqual(assess_evidence([])["status"],"insufficient")

if __name__ == "__main__":
    unittest.main()
