"""Forward- and backward-chaining inference for MobileCare AI.

Public function signatures and result keys remain compatible with the app.
Malformed rules fail clearly, and recursive proof checks are cycle-safe.
"""

from collections.abc import Mapping


def normalize_facts(facts):
    """Convert fact names or assertion dictionaries into a clean set."""
    if facts is None:
        return set()
    if isinstance(facts, (str, bytes)):
        facts = [facts]
    result = set()
    for item in facts:
        if isinstance(item, Mapping):
            item = item.get("fact")
        if isinstance(item, str) and item.strip():
            result.add(item.strip())
    return result


def _validated_rule(rule):
    if not isinstance(rule, Mapping):
        raise ValueError("Each rule must be a dictionary-like object.")
    rule_id = rule.get("id")
    conditions = rule.get("conditions")
    conclusion = rule.get("conclusion")
    solution = rule.get("solution", "")
    if rule_id is None:
        raise ValueError("A rule is missing its 'id'.")
    if not isinstance(conditions, (list, tuple, set)) or not conditions:
        raise ValueError(f"Rule {rule_id} must have a non-empty conditions list.")
    if not all(isinstance(value, str) and value.strip() for value in conditions):
        raise ValueError(f"Rule {rule_id} contains an invalid condition.")
    if not isinstance(conclusion, str) or not conclusion.strip():
        raise ValueError(f"Rule {rule_id} has an invalid conclusion.")
    return rule_id, tuple(conditions), conclusion.strip(), solution


def _trace_entry(rule_id, conditions, conclusion, solution):
    return {
        "rule_id": rule_id,
        "conditions": list(conditions),
        "conclusion": conclusion,
        "solution": solution,
    }


def forward_chaining(facts, rules):
    """Apply rules until a complete pass adds no new facts."""
    known_facts = normalize_facts(facts)
    original_facts = set(known_facts)
    validated_rules = [_validated_rule(rule) for rule in rules]
    trace = []
    changed = True
    while changed:
        changed = False
        for rule_id, conditions, conclusion, solution in validated_rules:
            if set(conditions).issubset(known_facts) and conclusion not in known_facts:
                known_facts.add(conclusion)
                changed = True
                trace.append(_trace_entry(rule_id, conditions, conclusion, solution))
    return {
        "facts": known_facts,
        "diagnoses": known_facts - original_facts,
        "trace": trace,
    }


def backward_chaining(goal, facts, rules):
    """Prove a goal recursively while preventing cyclic rule evaluation."""
    if not isinstance(goal, str) or not goal.strip():
        return {"goal": goal, "success": False, "trace": []}
    known_facts = normalize_facts(facts)
    validated_rules = [_validated_rule(rule) for rule in rules]
    trace = []
    visiting = set()
    proven = set()
    rules_by_conclusion = {}
    for rule in validated_rules:
        rules_by_conclusion.setdefault(rule[2], []).append(rule)

    def prove(target):
        if target in known_facts or target in proven:
            return True
        if target in visiting:
            return False
        visiting.add(target)
        try:
            for rule_id, conditions, conclusion, solution in rules_by_conclusion.get(target, []):
                if all(prove(condition) for condition in conditions):
                    proven.add(target)
                    trace.append(_trace_entry(rule_id, conditions, conclusion, solution))
                    return True
            return False
        finally:
            visiting.remove(target)

    success = prove(goal.strip())
    return {"goal": goal, "success": success, "trace": trace}
