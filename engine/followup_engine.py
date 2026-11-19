"""Select focused follow-up questions from MobileCare AI rules.

Only facts explicitly confirmed as positive can activate rules. A No or Not
sure answer blocks a rule that depends on that unresolved condition.
"""

def select_next_question(confirmed_facts, answered_facts, rules, assertions, excluded_facts=None):
    """Return the highest-priority useful missing condition, or None."""
    known = {f for f in (confirmed_facts or []) if isinstance(f, str) and f.strip()}
    answers = answered_facts or {}
    answered = set(answers)
    blocked = {f for f, answer in answers.items() if answer in ("no", "not_sure")}
    excluded = set(excluded_facts or [])
    descriptions = {item.get("fact"): item.get("description") for item in (assertions or []) if isinstance(item, dict) and item.get("fact")}
    order = {item.get("fact"): i for i, item in enumerate(assertions or []) if isinstance(item, dict) and item.get("fact")}
    scores, rule_ids = {}, {}

    for rule in rules or []:
        if not isinstance(rule, dict):
            continue
        conditions = set(rule.get("conditions") or [])
        # Do not pursue a rule when any of its required facts were explicitly
        # denied, or negated in the original problem.
        if conditions.intersection(blocked | excluded):
            continue
        if not conditions.intersection(known):
            continue
        for fact in conditions - known - answered - excluded:
            if fact not in descriptions:
                continue
            scores[fact] = scores.get(fact, 0) + 1
            rule_ids.setdefault(fact, []).append(rule.get("id"))

    if not scores:
        return None
    chosen = sorted(scores, key=lambda fact: (-scores[fact], order.get(fact, 10**9), fact))[0]
    return {
        "fact": chosen,
        "description": descriptions[chosen] or chosen.replace("_", " ").title(),
        "relevance_score": scores[chosen],
        "rule_ids": sorted(rid for rid in rule_ids[chosen] if isinstance(rid, int)),
    }
