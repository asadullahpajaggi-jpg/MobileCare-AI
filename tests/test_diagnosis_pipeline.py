from engine.diagnosis_pipeline import run_diagnosis


def test_pipeline_reports_supported_cause_and_verifies():
    rules = [
        {"id": 1, "conditions": ["a", "b"], "conclusion": "intermediate", "solution": ""},
        {"id": 2, "conditions": ["intermediate", "c"], "conclusion": "cause", "solution": "check"},
    ]
    report = run_diagnosis(["a", "b", "c"], rules)
    assert report["conclusions"] == ["cause"]
    assert report["verified"] == 1
    assert report["evidence_status"]["status"] == "supported"
    assert report["ranked"][0]["conclusion"] == "cause"


def test_pipeline_does_not_present_intermediate_as_final():
    rules = [
        {"id": 1, "conditions": ["a", "b"], "conclusion": "intermediate", "solution": ""},
        {"id": 2, "conditions": ["intermediate", "c"], "conclusion": "cause", "solution": "check"},
    ]
    report = run_diagnosis(["a", "b", "c"], rules)
    assert "intermediate" not in report["conclusions"]
    assert report["verification"][0]["success"]


def test_pipeline_rejects_missing_evidence():
    rules = [{"id": 1, "conditions": ["a", "b"], "conclusion": "cause", "solution": ""}]
    report = run_diagnosis(["a"], rules)
    assert report["conclusions"] == []
    assert report["evidence_status"]["status"] == "insufficient"
    assert report["verified"] == 0
