"""Evidence-oriented summaries for rule-based diagnosis results."""


def summarize_diagnosis(trace, confirmed_facts):
    """Group activated diagnoses and show grounded conditions.

    This intentionally avoids numerical confidence claims: rule activation
    proves only that its conditions were available, not hardware certainty.
    """
    facts = set(confirmed_facts or [])
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
        entries.append({
            "rule_id": step.get("rule_id"),
            "conclusion": conclusion,
            "conditions": list(conditions),
            "confirmed_conditions": [
                condition for condition in conditions if condition in facts
            ],
            "derived_conditions": [
                condition for condition in conditions if condition not in facts
            ],
            "solution": step.get("solution", ""),
        })

    return {
        "entries": entries,
        "diagnosis_count": len(entries),
        "directly_supported_count": sum(
            not item["derived_conditions"] for item in entries
        ),
    }
