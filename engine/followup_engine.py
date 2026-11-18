"""Select focused follow-up questions from MobileCare AI rules.

Only facts already confirmed by the user can activate a rule as a candidate.
Answers are stored separately; a No or Not sure answer is never a positive fact.
"""


def select_next_question(
    confirmed_facts,
    answered_facts,
    rules,
    assertions,
    excluded_facts=None,
):
    """Return the most useful unresolved condition, or None.

    Candidate conditions must belong to a rule that already has at least one
    confirmed condition. Repeated support across active rules ranks a question
    higher. Ties are resolved by assertion order for predictable UI behavior.
    """
    known = {
        fact for fact in (confirmed_facts or [])
        if isinstance(fact, str) and fact.strip()
    }
    answered = set((answered_facts or {}).keys())
    excluded = set(excluded_facts or [])

    descriptions = {
        item.get("fact"): item.get("description")
        for item in (assertions or [])
        if isinstance(item, dict) and item.get("fact")
    }
    assertion_order = {
        item.get("fact"): index
        for index, item in enumerate(assertions or [])
        if isinstance(item, dict) and item.get("fact")
    }

    scores = {}
    supporting_rules = {}

    for rule in rules or []:
        if not isinstance(rule, dict):
            continue
        conditions = rule.get("conditions") or []
        condition_set = set(conditions)

        # A rule is relevant only after at least one of its conditions
        # has been explicitly confirmed.
        if not condition_set.intersection(known):
            continue

        for fact in condition_set - known - answered - excluded:
            if fact not in descriptions:
                continue
            scores[fact] = scores.get(fact, 0) + 1
            supporting_rules.setdefault(fact, []).append(rule.get("id"))

    if not scores:
        return None

    selected = sorted(
        scores,
        key=lambda fact: (
            -scores[fact],
            assertion_order.get(fact, 10**9),
            fact,
        ),
    )[0]

    return {
        "fact": selected,
        "description": descriptions[selected] or selected.replace("_", " ").title(),
        "relevance_score": scores[selected],
        "rule_ids": sorted(
            rule_id for rule_id in supporting_rules[selected]
            if isinstance(rule_id, int)
        ),
    }
