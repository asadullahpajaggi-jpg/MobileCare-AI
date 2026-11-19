"""Adaptive follow-up selection for MobileCare AI.

Select missing conditions that best distinguish the currently relevant rules.
Answers of No/Not sure and facts explicitly negated in the initial description
exclude rules that depend on those facts.
"""

def select_next_question(confirmed_facts, answered_facts, rules, assertions, excluded_facts=None):
    """Choose a question by rule coverage and how well it separates candidates."""
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
        if conditions.intersection(blocked | excluded):
            continue
        if conditions.intersection(known):
            active_rules.append(rule)

    if not active_rules:
        return None

    # Score candidate questions by how many active rules support Yes versus
    # remain alternatives if the answer is No. A balanced split is preferred.
    scores, rule_ids = {}, {}
    for rule in active_rules:
        conditions = set(rule.get("conditions") or [])
        for fact in conditions - known - set(answers) - excluded:
            if fact not in descriptions:
                continue
            scores.setdefault(fact, {"yes": 0, "coverage": 0})
            scores[fact]["yes"] += 1
            scores[fact]["coverage"] += 1
            rule_ids.setdefault(fact, []).append(rule.get("id"))

    if not scores:
        return None

    def score(fact):
        data = scores[fact]
        data["no"] = max(0, len(active_rules) - data["yes"])
        balance = min(data["yes"], data["no"])
        return (-balance, -data["coverage"], order.get(fact, 10**9), fact)

    chosen = sorted(scores, key=score)[0]
    return {
        "fact": chosen,
        "description": descriptions[chosen] or chosen.replace("_", " ").title(),
        "relevance_score": scores[chosen]["coverage"],
        "discrimination_score": min(scores[chosen]["yes"], scores[chosen]["no"]),
        "rule_ids": sorted(rid for rid in rule_ids[chosen] if isinstance(rid, int)),
    }
