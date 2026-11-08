import ast
from pathlib import Path

BASE_DIR = Path(__file__).parent


def load_list(file_path, variable_name):
    source = file_path.read_text(encoding="utf-8")
    tree = ast.parse(source)

    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == variable_name:
                    return ast.literal_eval(node.value)

        if isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name) and node.target.id == variable_name:
                return ast.literal_eval(node.value)

    raise ValueError(f"{variable_name} was not found")


def validate_knowledge_base():
    checks = []
    rules = []
    assertions = []

    try:
        rules = load_list(
            BASE_DIR / "knowledge_base" / "rules.py",
            "RULES"
        )
        checks.append(("Rules file syntax and structure", True, "Loaded successfully"))
    except Exception as error:
        checks.append(("Rules file syntax and structure", False, str(error)))

    try:
        assertions = load_list(
            BASE_DIR / "knowledge_base" / "assertions.py",
            "ASSERTIONS"
        )
        checks.append(("Assertions file syntax and structure", True, "Loaded successfully"))
    except Exception as error:
        checks.append(("Assertions file syntax and structure", False, str(error)))

    if rules and assertions:
        rule_ids = [r.get("id") for r in rules]
        fact_ids = [a.get("id") for a in assertions]
        fact_names = [a.get("fact") for a in assertions]

        checks.append((
            "100 rules count",
            len(rules) == 100,
            f"Found: {len(rules)}"
        ))

        checks.append((
            "300 facts count",
            len(assertions) == 300,
            f"Found: {len(assertions)}"
        ))

        checks.append((
            "Unique rule IDs",
            len(rule_ids) == len(set(rule_ids)),
            "Duplicate rule IDs found" if len(rule_ids) != len(set(rule_ids)) else "No duplicates"
        ))

        checks.append((
            "Unique fact IDs",
            len(fact_ids) == len(set(fact_ids)),
            "Duplicate fact IDs found" if len(fact_ids) != len(set(fact_ids)) else "No duplicates"
        ))

        checks.append((
            "Unique fact names",
            len(fact_names) == len(set(fact_names)),
            "Duplicate fact names found" if len(fact_names) != len(set(fact_names)) else "No duplicates"
        ))

        known_facts = set(fact_names)
        used_conditions = set()

        for rule in rules:
            used_conditions.update(rule.get("conditions", []))

        missing = sorted(used_conditions - known_facts)

        checks.append((
            "Rule conditions linked to facts",
            len(missing) == 0,
            f"{len(missing)} missing fact names"
        ))

        valid_rules = all(
            isinstance(rule.get("conditions"), list)
            and len(rule.get("conditions", [])) > 0
            and bool(rule.get("conclusion"))
            and bool(rule.get("solution"))
            for rule in rules
        )

        checks.append((
            "Rule structure",
            valid_rules,
            "Conditions, conclusions and solutions checked"
        ))

        valid_facts = all(
            bool(fact.get("fact"))
            and bool(fact.get("description"))
            and isinstance(fact.get("keywords"), list)
            for fact in assertions
        )

        checks.append((
            "Fact structure",
            valid_facts,
            "Fact names, descriptions and keywords checked"
        ))

        return {
            "checks": checks,
            "missing_facts": missing,
            "rule_count": len(rules),
            "fact_count": len(assertions)
        }

    return {
        "checks": checks,
        "missing_facts": [],
        "rule_count": len(rules),
        "fact_count": len(assertions)
          }
      
