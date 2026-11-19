"""Deep structural reliability audit for the MobileCare AI rule graph."""
from collections import defaultdict

def audit_reliability(rules, assertions):
    facts={a.get("fact") for a in assertions if isinstance(a,dict) and isinstance(a.get("fact"),str)}
    conclusions={r.get("conclusion") for r in rules if isinstance(r,dict) and isinstance(r.get("conclusion"),str)}
    findings=[]
    ids=[]
    signatures=defaultdict(list)
    graph=defaultdict(set)
    valid_rules=[]
    for pos,r in enumerate(rules):
        if not isinstance(r,dict):
            findings.append({"severity":"error","kind":"Malformed rule","detail":f"Position {pos+1} is not a dictionary"});continue
        rid=r.get("id");ids.append(rid)
        cond=r.get("conditions");con=r.get("conclusion")
        if not isinstance(cond,list) or not cond or not all(isinstance(x,str) and x.strip() for x in cond):
            findings.append({"severity":"error","kind":"Invalid conditions","detail":f"Rule {rid}: conditions must be a non-empty list of strings"});continue
        if len(cond)!=len(set(cond)):
            findings.append({"severity":"error","kind":"Repeated condition","detail":f"Rule {rid}: condition list contains duplicates"})
        if not isinstance(con,str) or not con.strip():
            findings.append({"severity":"error","kind":"Invalid conclusion","detail":f"Rule {rid}: conclusion missing"});continue
        unknown=sorted(set(cond)-facts-conclusions)
        if unknown: findings.append({"severity":"error","kind":"Unknown condition reference","detail":f"Rule {rid}: {unknown}"})
        signatures[tuple(sorted(cond))].append(r)
        valid_rules.append(r)
        for c in cond:
            if c in conclusions: graph[con].add(c)
    duplicate_ids=sorted({x for x in ids if ids.count(x)>1},key=str)
    if duplicate_ids: findings.append({"severity":"error","kind":"Duplicate rule IDs","detail":str(duplicate_ids)})
    for sig,group in signatures.items():
        if len(group)>1:
            cs=sorted({str(r.get("conclusion")) for r in group})
            findings.append({"severity":"error" if len(cs)>1 else "review","kind":"Repeated condition signature","detail":f"Rules {[r.get('id') for r in group]} -> {cs}"})
    # DFS detects cycles only among intermediate conclusion dependencies.
    cyclic_nodes=set();visiting=[];visited=set()
    def dfs(node):
        if node in visiting:
            cyclic_nodes.update(visiting[visiting.index(node):]);return
        if node in visited:return
        visiting.append(node)
        for nxt in graph.get(node,()):
            dfs(nxt)
        visiting.pop();visited.add(node)
    for node in conclusions:dfs(node)
    if cyclic_nodes: findings.append({"severity":"error","kind":"Reasoning cycle","detail":"Cycle among intermediate conclusions: "+", ".join(sorted(cyclic_nodes))})
    intermediates=sorted(conclusions & {c for r in valid_rules for c in r.get("conditions",[])})
    terminals=sorted(conclusions-set(intermediates))
    return {"rule_count":len(rules),"fact_count":len(facts),"conclusion_count":len(conclusions),
            "intermediate_conclusions":intermediates,"terminal_conclusions":terminals,
            "findings":findings,"errors":sum(x["severity"]=="error" for x in findings),
            "reviews":sum(x["severity"]=="review" for x in findings)}
