from engine.rule_audit import audit_rules

def test_duplicate_condition_conflict():
    report=audit_rules([{"id":1,"conditions":["a","b"],"conclusion":"x"},{"id":2,"conditions":["b","a"],"conclusion":"y"}],[{"fact":"a"},{"fact":"b"}])
    assert any(f["kind"]=="Duplicate condition sets" and f["severity"]=="error" for f in report["findings"])

def test_unknown_fact_flag():
    report=audit_rules([{"id":1,"conditions":["unknown"],"conclusion":"x"}],[])
    assert report["errors"]>=1

def test_safety_review_flag():
    report=audit_rules([{"id":1,"conditions":["a"],"conclusion":"battery_swelling","solution":"stop charging"}],[{"fact":"a"}])
    assert any(f["kind"]=="Safety wording review" for f in report["findings"])
