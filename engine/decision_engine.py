"""Evidence-based prioritization for rule-driven diagnosis traces."""
def rank_diagnoses(trace, confirmed_facts):
    direct=set(confirmed_facts or [])
    derived={s.get("conclusion") for s in trace or [] if isinstance(s,dict) and s.get("conclusion")}
    rows=[]; seen=set()
    intermediate={condition for step in trace or [] if isinstance(step,dict) for condition in (step.get("conditions") or [])}\n    intermediate.intersection_update(derived)
    for step in trace or []:
        if not isinstance(step,dict): continue
        conclusion=step.get("conclusion")
        if not conclusion or conclusion in seen or conclusion in intermediate: continue
        seen.add(conclusion); cond=list(step.get("conditions") or [])
        direct_n=sum(f in direct for f in cond)
        derived_n=sum(f in derived and f not in direct for f in cond)
        # Deterministic ordering; score is a ranking aid, not a probability.
        score=direct_n*3+derived_n
        rows.append({"rule_id":step.get("rule_id"),"conclusion":conclusion,"conditions":cond,"solution":step.get("solution", ""),"direct_count":direct_n,"derived_count":derived_n,"rank_score":score,"evidence_label":"Direct evidence" if direct_n and not derived_n else "Mixed evidence" if direct_n else "Indirect evidence"})
    rows.sort(key=lambda x:(-x["rank_score"],-x["direct_count"],x["rule_id"] if isinstance(x["rule_id"],int) else 10**9))
    for idx,row in enumerate(rows,1): row["rank"]=idx
    return rows

def decision_summary(rows):
    if not rows:return {"top":None,"alternatives":[],"message":"No rule-based cause has been established."}
    top=rows[0]
    if len(rows)==1:return {"top":top,"alternatives":[],"message":"One rule matched the gathered evidence. This is a possible cause, not a confirmed hardware diagnosis."}
    tied=len(rows)>1 and rows[1]["rank_score"]==top["rank_score"]
    msg="Several possible causes remain similarly supported; the system cannot confidently distinguish them." if tied else "The leading cause has the strongest evidence match in the current rules, but alternatives remain possible."
    return {"top":top,"alternatives":rows[1:],"message":msg}
