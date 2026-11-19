"""Conservative fallback candidates for rules that are not fully satisfied."""
def find_partial_rule_candidates(facts, rules, assertions, blocked_facts=None, limit=5):
    known=set(facts or []); blocked=set(blocked_facts or [])
    descriptions={a.get('fact'):a.get('description',a.get('fact','').replace('_',' ').title()) for a in assertions or [] if isinstance(a,dict)}
    candidates=[]
    for rule in rules or []:
        conditions=set(rule.get('conditions') or [])
        if not conditions or conditions.intersection(blocked): continue
        matched=conditions.intersection(known); missing=conditions-known
        if not matched or not missing: continue
        candidates.append({'rule_id':rule.get('id'),'conclusion':rule.get('conclusion'),'solution':rule.get('solution',''),'matched':[descriptions.get(f,f.replace('_',' ').title()) for f in sorted(matched)],'missing':[descriptions.get(f,f.replace('_',' ').title()) for f in sorted(missing)],'coverage':len(matched)/len(conditions),'matched_count':len(matched),'condition_count':len(conditions)})
    candidates.sort(key=lambda row:(-row['coverage'],-row['matched_count'],row['rule_id'] if isinstance(row['rule_id'],int) else 10**9))
    return [row for row in candidates if row['coverage']>=0.5][:limit]
