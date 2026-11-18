"""Structural validation for the MobileCare AI knowledge base.

Run with: python validate_data.py
The validator is intentionally independent of Streamlit so it can run in CI.
"""
import ast
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).parent


def load_list(file_path, variable_name):
    """Safely load a Python list literal from a knowledge-base module."""
    source = file_path.read_text(encoding="utf-8")
    tree = ast.parse(source)

    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == variable_name:
                    value = ast.literal_eval(node.value)
                    if not isinstance(value, list):
                        raise ValueError(f"{variable_name} must be a list")
                    return value

        if isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name) and node.target.id == variable_name:
                value = ast.literal_eval(node.value)
                if not isinstance(value, list):
                    raise ValueError(f"{variable_name} must be a list")
                return value

    raise ValueError(f"{variable_name} was not found")


def _duplicates(values):
    """Return sorted duplicate values without assuming input order."""
    counts = Counter(values)
    return sorted(
        (value for value, count in counts.items() if count > 1),
        key=str
    )


def audit_knowledge_base(rules, assertions):
    """Audit rule/fact links and common knowledge-base data-quality issues."""
    checks = []
    missing_conditions = []
    malformed_rules = []
    malformed_facts = []
    duplicate_condition_sets = []
    conflicting_condition_sets = []

    rule_ids = [
        rule.get("id") for rule in rules if isinstance(rule, dict)
    ]
    fact_ids = [
        fact.get("id") for fact in assertions if isinstance(fact, dict)
    ]
    fact_names = [
        fact.get("fact") for fact in assertions if isinstance(fact, dict)
    ]

    duplicate_rule_ids = _duplicates(rule_ids)
    duplicate_fact_ids = _duplicates(fact_ids)
    duplicate_fact_names = _duplicates(fact_names)

    checks.append((
        "Unique rule IDs",
        not duplicate_rule_ids,
        "No duplicate rule IDs" if not duplicate_rule_ids
        else f"Duplicates: {duplicate_rule_ids}"
    ))
    checks.append((
        "Unique fact IDs",
        not duplicate_fact_ids,
        "No duplicate fact IDs" if not duplicate_fact_ids
        else f"Duplicates: {duplicate_fact_ids}"
    ))
    checks.append((
        "Unique fact names",
        not duplicate_fact_names,
        "No duplicate fact names" if not duplicate_fact_names
        else f"Duplicates: {duplicate_fact_names}"
    ))

    known_facts = {
        name for name in fact_names if isinstance(name, str) and name
    }
    condition_sets = {}

    for index, rule in enumerate(rules):
        if not isinstance(rule, dict):
            malformed_rules.append(f"Rule at position {index + 1} is not a dictionary")
            continue

        rule_id = rule.get("id", index + 1)
        conditions = rule.get("conditions")
        conclusion = rule.get("conclusion")
        solution = rule.get("solution")

        valid_conditions = (
            isinstance(conditions, list)
            and len(conditions) > 0
            and all(isinstance(item, str) and item.strip() for item in conditions)
            and len(conditions) == len(set(conditions))
        )
        if not valid_conditions:
            malformed_rules.append(
                f"Rule {rule_id}: conditions must be a non-empty list "
                "of unique, non-empty fact names"
            )
        elif isinstance(conclusion, str) and conclusion.strip():
            missing = sorted(set(conditions) - known_facts)
            if missing:
                missing_conditions.extend(missing)

            signature = tuple(sorted(conditions))
            condition_sets.setdefault(signature, []).append({
                "id": rule_id,
                "conclusion": conclusion
            })

        if not isinstance(rule_id, int) or rule_id <= 0:
            malformed_rules.append(f"Rule {rule_id}: ID must be a positive integer")
        if not isinstance(conclusion, str) or not conclusion.strip():
            malformed_rules.append(f"Rule {rule_id}: conclusion is missing")
        if not isinstance(solution, str) or not solution.strip():
            malformed_rules.append(f"Rule {rule_id}: solution is missing")

    for signature, entries in condition_sets.items():
        if len(entries) > 1:
            conclusions = {entry["conclusion"] for entry in entries}
            item = {
                "conditions": list(signature),
                "rule_ids": [entry["id"] for entry in entries],
                "conclusions": sorted(conclusions)
            }
            duplicate_condition_sets.append(item)
            if len(conclusions) > 1:
                conflicting_condition_sets.append(item)

    for index, fact in enumerate(assertions):
        if not isinstance(fact, dict):
            malformed_facts.append(f"Fact at position {index + 1} is not a dictionary")
            continue

        fact_id = fact.get("id")
        name = fact.get("fact")
        description = fact.get("description")
        keywords = fact.get("keywords")
        if not isinstance(fact_id, int) or fact_id <= 0:
            malformed_facts.append(f"Fact {name or index + 1}: ID must be a positive integer")
        if not isinstance(name, str) or not name.strip():
            malformed_facts.append(f"Fact at position {index + 1}: name is missing")
        if not isinstance(description, str) or not description.strip():
            malformed_facts.append(f"Fact {name or index + 1}: description is missing")
        if (
            not isinstance(keywords, list)
            or not all(isinstance(word, str) and word.strip() for word in keywords)
        ):
            malformed_facts.append(
                f"Fact {name or index + 1}: keywords must be a list of non-empty strings"
            )

    missing_conditions = sorted(set(missing_conditions))
    checks.extend([
        (
            "Rule conditions linked to known facts",
            not missing_conditions,
            "All rule conditions reference known facts"
            if not missing_conditions
            else f"Missing fact names: {missing_conditions}"
        ),
        (
            "Rule structure",
            not malformed_rules,
            "All rules have valid IDs, conditions, conclusions and solutions"
            if not malformed_rules
            else f"{len(malformed_rules)} rule issue(s)"
        ),
        (
            "Fact structure",
            not malformed_facts,
            "All facts have valid IDs, names, descriptions and keywords"
            if not malformed_facts
            else f"{len(malformed_facts)} fact issue(s)"
        ),
        (
            "No duplicate condition sets",
            not duplicate_condition_sets,
            "Every rule has a distinct condition set"
            if not duplicate_condition_sets
            else f"{len(duplicate_condition_sets)} repeated condition set(s)"
        ),
        (
            "No conflicting rule conclusions",
            not conflicting_condition_sets,
            "No identical condition set produces different conclusions"
            if not conflicting_condition_sets
            else f"{len(conflicting_condition_sets)} conflicting condition set(s)"
        ),
    ])

    return {
        "checks": checks,
        "missing_facts": missing_conditions,
        "rule_count": len(rules),
        "fact_count": len(assertions),
        "duplicate_condition_sets": duplicate_condition_sets,
        "conflicting_condition_sets": conflicting_condition_sets,
        "rule_issues": malformed_rules,
        "fact_issues": malformed_facts,
    }


def validate_knowledge_base():
    """Load repository data and return a backward-compatible validation report."""
    try:
        rules = load_list(BASE_DIR / "knowledge_base" / "rules.py", "RULES")
    except Exception as error:
        return {
            "checks": [("Rules file syntax and structure", False, str(error))],
            "missing_facts": [],
            "rule_count": 0,
            "fact_count": 0,
        }

    try:
        assertions = load_list(
            BASE_DIR / "knowledge_base" / "assertions.py", "ASSERTIONS"
        )
    except Exception as error:
        return {
            "checks": [
                ("Rules file syntax and structure", True, "Loaded successfully"),
                ("Assertions file syntax and structure", False, str(error)),
            ],
            "missing_facts": [],
            "rule_count": len(rules),
            "fact_count": 0,
        }

    report = audit_knowledge_base(rules, assertions)
    report["checks"].insert(
        0, ("Rules file syntax and structure", True, "Loaded successfully")
    )
    report["checks"].insert(
        1, ("Assertions file syntax and structure", True, "Loaded successfully")
    )
    return report


if __name__ == "__main__":
    report = validate_knowledge_base()
    print("MobileCare AI - Knowledge Base Validation")
    print(f"Rules: {report['rule_count']} | Facts: {report['fact_count']}")
    for name, passed, details in report["checks"]:
        status = "PASS" if passed else "FAIL"
        print(f"[{status}] {name}: {details}")

    failed = sum(1 for _, passed, _ in report["checks"] if not passed)
    print(f"\nResult: {len(report['checks']) - failed} passed, {failed} failed")
    if failed:
        raise SystemExit(1)
