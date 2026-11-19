"""Evidence-oriented summaries for rule-based diagnosis results."""

def summarize_diagnosis(trace, confirmed_facts):
    """Classify each rule condition as directly confirmed or inferred."""
    direct = set(confirmed_facts or [])
    derived = {step.get("conclusion") for step in (trace or [])
               if isinstance(step, dict) and step.get("conclusion")}
    entries = []
    seen = set()
    for step in trace or []:
        if not isinstance(step, dict):
            continue
        conclusion = step.get("conclusion")
        conditions = step.get("conditions") or []
        if not conclusion or conclusion in seen:
            continue
        seen.add(conclusion)
        direct_conditions = [condition for condition in conditions if condition in direct]
        derived_conditions = [condition for condition in conditions if condition in derived and condition not in direct]
        missing_conditions = [condition for condition in conditions if condition not in direct and condition not in derived]
        entries.append({
            "rule_id": step.get("rule_id"),
            "conclusion": conclusion,
            "conditions": list(conditions),
            "confirmed_conditions": direct_conditions,
            "derived_conditions": derived_conditions,
            "missing_conditions": missing_conditions,
            "solution": step.get("solution", ""),
            "evidence_complete": not missing_conditions,
        })
    return {
        "entries": entries,
        "diagnosis_count": len(entries),
        "directly_supported_count": sum(not item["derived_conditions"] and not item["missing_conditions"] for item in entries),
    }
