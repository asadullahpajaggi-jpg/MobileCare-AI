# MobileCare AI - Inference Engine

def normalize_facts(facts):
    """Convert input facts into a set of fact names."""
    result = set()

    for item in facts:
        if isinstance(item, dict):
            result.add(item["fact"])
        else:
            result.add(item)

    return result


def forward_chaining(facts, rules):
    """Apply rules repeatedly until no new facts are generated."""

    known_facts = normalize_facts(facts)
    original_facts = set(known_facts)
    trace = []

    changed = True

    while changed:
        changed = False

        for rule in rules:
            conditions = set(rule["conditions"])
            conclusion = rule["conclusion"]

            if conditions.issubset(known_facts):
                if conclusion not in known_facts:

                    known_facts.add(conclusion)
                    changed = True

                    trace.append({
                        "rule_id": rule["id"],
                        "conditions": rule["conditions"],
                        "conclusion": conclusion,
                        "solution": rule["solution"]
                    })

    return {
        "facts": known_facts,
        "diagnoses": known_facts - original_facts,
        "trace": trace
    }


def backward_chaining(goal, facts, rules):
    """Check whether a specific goal can be proven."""

    known_facts = normalize_facts(facts)
    trace = []
    visiting = set()
    proven = set()

    def prove(target):

        if target in known_facts:
            return True

        if target in proven:
            return True

        if target in visiting:
            return False

        visiting.add(target)

        for rule in rules:

            if rule["conclusion"] == target:

                conditions_proven = True

                for condition in rule["conditions"]:
                    if not prove(condition):
                        conditions_proven = False
                        break

                if conditions_proven:

                    trace.append({
                        "rule_id": rule["id"],
                        "conditions": rule["conditions"],
                        "conclusion": target,
                        "solution": rule["solution"]
                    })

                    visiting.remove(target)
                    proven.add(target)
                    return True

        visiting.remove(target)
        return False

    success = prove(goal)

    return {
        "goal": goal,
        "success": success,
        "trace": trace
    }
