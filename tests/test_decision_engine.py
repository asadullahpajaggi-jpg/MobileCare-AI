from engine.decision_engine import rank_diagnoses, decision_summary

def test_rank_direct_evidence_ahead_of_derived():
    trace=[{"rule_id":2,"conditions":["x","derived"],"conclusion":"b"},{"rule_id":1,"conditions":["x","y"],"conclusion":"a"}]
    ranked=rank_diagnoses(trace,["x","y"])
    assert ranked[0]["conclusion"]=="a"

def test_equal_support_is_not_called_confidence():
    rows=rank_diagnoses([{"rule_id":1,"conditions":["x"],"conclusion":"a"},{"rule_id":2,"conditions":["x"],"conclusion":"b"}],["x"])
    assert "similarly supported" in decision_summary(rows)["message"]

def test_empty_trace_summary():
    assert decision_summary([])["top"] is None
