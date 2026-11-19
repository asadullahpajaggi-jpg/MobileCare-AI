from engine.reliability_audit import audit_reliability

def test_clean_chain_classifies_intermediate_and_terminal():
    rules=[{"id":1,"conditions":["a"],"conclusion":"middle"},{"id":2,"conditions":["middle"],"conclusion":"final"}]
    report=audit_reliability(rules,[{"fact":"a"}])
    assert "middle" in report["intermediate_conclusions"]
    assert "final" in report["terminal_conclusions"]
    assert not report["errors"]

def test_cycle_detected():
    rules=[{"id":1,"conditions":["b"],"conclusion":"a"},{"id":2,"conditions":["a"],"conclusion":"b"}]
    report=audit_reliability(rules,[])
    assert any(f["kind"]=="Reasoning cycle" for f in report["findings"])

def test_duplicate_ids_and_unknown_reference_detected():
    rules=[{"id":1,"conditions":["missing"],"conclusion":"x"},{"id":1,"conditions":["z"],"conclusion":"y"}]
    report=audit_reliability(rules,[])
    kinds={f["kind"] for f in report["findings"]}
    assert "Duplicate rule IDs" in kinds
    assert "Unknown condition reference" in kinds

def test_conflicting_signature_detected():
    rules=[{"id":1,"conditions":["a"],"conclusion":"x"},{"id":2,"conditions":["a"],"conclusion":"y"}]
    report=audit_reliability(rules,[{"fact":"a"}])
    assert any(f["kind"]=="Repeated condition signature" and f["severity"]=="error" for f in report["findings"])
