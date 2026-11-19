import unittest
from engine.evidence_decision import assess_evidence

class EvidenceDecisionTests(unittest.TestCase):
    def row(self, direct=None, derived=None, missing=None, score=1):
        return {"conditions":["a","b"],"confirmed_conditions":direct or [],"derived_conditions":derived or [],"missing_conditions":missing or [],"rank_score":score,"conclusion":"cause"}

    def test_incomplete_evidence(self):
        result=assess_evidence([self.row(direct=["a"],missing=["b"])])
        self.assertEqual(result["status"],"insufficient")
        self.assertIn("Do not present partial",result["next_step"])

    def test_multiple_complete_causes_remain_competing(self):
        result=assess_evidence([self.row(direct=["a","b"],score=5),self.row(direct=["a","b"],score=1)])
        self.assertEqual(result["status"],"competing")

    def test_single_complete_direct_evidence(self):
        result=assess_evidence([self.row(direct=["a","b"])])
        self.assertEqual(result["status"],"supported")
        self.assertIn("professional",result["next_step"])

    def test_complete_inferred_evidence_disclosed(self):
        result=assess_evidence([self.row(derived=["a","b"])])
        self.assertEqual(result["status"],"supported")
        self.assertEqual(result["evidence_basis"],"Includes inferred facts")

    def test_empty_rows(self):
        self.assertEqual(assess_evidence([])["status"],"insufficient")

if __name__=="__main__":
    unittest.main()
