"""Rule quality screening for the MobileCare AI knowledge base."""
from collections import defaultdict

SAFETY_TERMS = (
    "swelling", "swollen", "liquid", "wet", "water", "overheat",
    "hot", "smoke", "fire", "shock", "electric",
)


def audit_rules(rules, assertions):
    """Audit rule structure, references, duplicates and safety wording.

    Rule conclusions are valid symbols too: rules may use conclusions from
    earlier reasoning stages as conditions in a multi-level inference graph.
    """
    facts = {
        a.get("fact")
        for a in assertions or []
        if isinstance(a, dict) and isinstance(a.get("fact"), str)
    }
    conclusions = {
        r.get("conclusion")
        for r in rules or []
        if isinstance(r, dict) and isinstance(r.get("conclusion"), str)
        and r.get("conclusion").strip()
    }
    known_symbols = facts | conclusions
    findings = []
    signatures = defaultdict(list)

    for idx, rule in enumerate(rules or []):
        if not isinstance(rule, dict):
            findings.append({
                "severity": "error", "kind": "Malformed rule",
                "detail": f"Rule position {idx + 1} is not a dictionary",
            })
            continue

        rid = rule.get("id", idx + 1)
        cond = rule.get("conditions")
        conclusion = rule.get("conclusion")

        if not isinstance(cond, list) or not cond or not all(
            isinstance(item, str) and item.strip() for item in cond
        ):
            findings.append({
                "severity": "error", "kind": "Malformed conditions",
                "detail": f"Rule {rid}: conditions must be a non-empty list of fact/conclusion names",
            })
            continue

        unknown = sorted(set(cond) - known_symbols)
        if unknown:
            findings.append({
                "severity": "error", "kind": "Unknown facts",
                "detail": f"Rule {rid}: {', '.join(unknown)}",
            })

        signatures[tuple(sorted(cond))].append(rule)
        advice_text = (str(conclusion) + " " + str(rule.get("solution", ""))).lower()
        if any(term in advice_text for term in SAFETY_TERMS):
            findings.append({
                "severity": "review", "kind": "Safety wording review",
                "detail": f"Rule {rid} ({conclusion}): manually review advice for safety accuracy and escalation",
            })

    for signature, group in signatures.items():
        if len(group) > 1:
            conclusions_in_group = {r.get("conclusion") for r in group}
            ids = [r.get("id") for r in group]
            findings.append({
                "severity": "error" if len(conclusions_in_group) > 1 else "review",
                "kind": "Duplicate condition sets",
                "detail": f"Rules {ids} share conditions {list(signature)}; conclusions: {sorted(map(str, conclusions_in_group))}",
            })

    return {
        "rule_count": len(rules or []),
        "findings": findings,
        "errors": sum(item["severity"] == "error" for item in findings),
        "reviews": sum(item["severity"] == "review" for item in findings),
    }
