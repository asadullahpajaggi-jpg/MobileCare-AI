"""Additional rule quality audit for MobileCare AI."""
from collections import defaultdict

SAFETY_TERMS = ("swelling", "swollen", "liquid", "wet", "water", "overheat", "hot", "smoke", "fire", "shock", "electric")

def audit_rules(rules, assertions):
    facts = {a.get("fact") for a in assertions if isinstance(a, dict)}
    findings = []
    signatures = defaultdict(list)
    for idx, rule in enumerate(rules):
        if not isinstance(rule, dict):
            findings.append({"severity":"error","kind":"Malformed rule","detail":f"Rule position {idx+1} is not a dictionary"}); continue
        rid=rule.get("id",idx+1); cond=rule.get("conditions",[]); conclusion=rule.get("conclusion")
        if not isinstance(cond,list) or not cond:
            findings.append({"severity":"error","kind":"Malformed conditions","detail":f"Rule {rid}: conditions missing or not a list"}); continue
        unknown=sorted(set(cond)-facts)
        if unknown: findings.append({"severity":"error","kind":"Unknown facts","detail":f"Rule {rid}: {', '.join(unknown)}"})
        signatures[tuple(sorted(cond))].append(rule)
        if any(term in (str(conclusion)+" "+str(rule.get("solution",""))).lower() for term in SAFETY_TERMS):
            findings.append({"severity":"review","kind":"Safety wording review","detail":f"Rule {rid} ({conclusion}): manually review advice for safety accuracy and escalation"})
    for sig,group in signatures.items():
        if len(group)>1:
            cs={r.get("conclusion") for r in group}; ids=[r.get("id") for r in group]
            findings.append({"severity":"error" if len(cs)>1 else "review","kind":"Duplicate condition sets","detail":f"Rules {ids} share conditions {list(sig)}; conclusions: {sorted(map(str,cs))}"})
    return {"rule_count":len(rules),"findings":findings,"errors":sum(f["severity"]=="error" for f in findings),"reviews":sum(f["severity"]=="review" for f in findings)}
