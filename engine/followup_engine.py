"""Adaptive follow-up selection that prioritizes diagnostic value over raw rule count.

Questions are selected from the currently active rules, grouped by distinct
conclusions so duplicated rules for one cause cannot dominate the score.
Answered No/Not sure and explicitly negated facts block dependent rules.
"""
def select_next_question(confirmed_facts, answered_facts, rules, assertions, excluded_facts=None):
    known = {f for f in (confirmed_facts or []) if isinstance(f, str) and f.strip()}
    answers = answered_facts or {}
    blocked = {f for f, answer in answers.items() if answer in ("no", "not_sure")}
    excluded = set(excluded_facts or [])
    descriptions = {item.get("fact"): item.get("description") for item in (assertions or []) if isinstance(item, dict) and item.get("fact")}
    order = {item.get("fact"): i for i, item in enumerate(assertions or []) if isinstance(item, dict) and item.get("fact")}

    active_rules = []
    for rule in rules or []:
        if not isinstance(rule, dict):
            continue
        conditions = set(rule.get("conditions") or [])
        if not conditions or conditions.intersection(blocked | excluded):
            continue
        if conditions.intersection(known):
            active_rules.append(rule)

    if not active_rules:
        return None

    # Group by diagnosis. Repeated rules for the same conclusion are not
    # treated as independent competing diagnoses.
    diagnosis_conditions = {}
    diagnosis_rule_ids = {}
    for rule in active_rules:
        conclusion = rule.get("conclusion")
        if not conclusion:
            continue
        diagnosis_conditions.setdefault(conclusion, []).append(set(rule.get("conditions") or []))
        diagnosis_rule_ids.setdefault(conclusion, []).append(rule.get("id"))

    candidates = {}
    for conclusion, condition_sets in diagnosis_conditions.items():
        for conditions in condition_sets:
            for fact in conditions - known - set(answers) - excluded:
                if fact not in descriptions:
                    continue
                entry = candidates.setdefault(fact, {"yes_diagnoses": set(), "rule_ids": set(), "coverage": 0})
                entry["yes_diagnoses"].add(conclusion)
                entry["coverage"] += 1
                entry["rule_ids"].update(rid for rid in diagnosis_rule_ids.get(conclusion, []) if isinstance(rid, int))

    if not candidates:
        return None

    total_diagnoses = len(diagnosis_conditions)
    def score(fact):
        entry = candidates[fact]
        yes = len(entry["yes_diagnoses"])
        no = max(0, total_diagnoses - yes)
        # A question affecting multiple distinct causes and splitting the
        # diagnosis set is useful. Coverage is a tie-breaker, not the main score.
        balance = min(yes, no)
        return (-balance, -yes, -entry["coverage"], order.get(fact, 10**9), fact)

    chosen = sorted(candidates, key=score)[0]
    entry = candidates[chosen]
    return {
        "fact": chosen,
        "description": descriptions[chosen] or chosen.replace("_", " ").title(),
        "relevance_score": entry["coverage"],
        "discrimination_score": min(len(entry["yes_diagnoses"]), max(0, total_diagnoses-len(entry["yes_diagnoses"]))),
        "diagnosis_count": total_diagnoses,
        "rule_ids": sorted(entry["rule_ids"]),
    }
