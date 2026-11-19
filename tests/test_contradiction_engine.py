from engine.contradiction_engine import detect_contradictions, remove_conflicted_facts
from engine.diagnosis_pipeline import run_diagnosis

def test_conflicts_detected_without_picking_side():
    conflicts = detect_contradictions(["phone_charging", "phone_not_charging"])
    assert len(conflicts) == 1
    assert set(conflicts[0]["facts"]) == {"phone_charging", "phone_not_charging"}

def test_conflicted_facts_excluded_from_reasoning():
    conflicts = detect_contradictions(["phone_charging", "phone_not_charging", "a"])
    assert remove_conflicted_facts(["phone_charging", "phone_not_charging", "a"], conflicts) == ["a"]

def test_pipeline_blocks_conflict_based_diagnosis():
    rules = [{"id": 1, "conditions": ["phone_not_charging", "charger_damaged"], "conclusion": "charger_fault", "solution": ""}]
    report = run_diagnosis(["phone_not_charging", "phone_charging", "charger_damaged"], rules)
    assert report["contradictions"]
    assert "charger_fault" not in report["conclusions"]
