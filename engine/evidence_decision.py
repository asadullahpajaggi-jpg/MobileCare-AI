"""Evidence adequacy assessment for conservative expert-system decisions."""

def assess_evidence(rows):
    """Separate complete, partial and competing explanations without probabilities."""
    rows = rows or []
    complete, partial = [], []
    for row in rows:
        conditions = row.get("conditions") or []
        direct = set(row.get("confirmed_conditions") or [])
        derived = set(row.get("derived_conditions") or [])
        missing = set(row.get("missing_conditions") or [])
        supported = direct | derived
        # Prefer explicit classification fields from diagnosis summaries.
        if not missing and conditions and set(conditions).issubset(supported):
            complete.append(row)
        elif supported:
            partial.append(row)

    if not complete:
        return {
            "status": "insufficient",
            "supported": [],
            "partial": partial,
            "message": "No diagnosis has all required conditions established. Treat partial matches as possibilities only.",
        }
    top = complete[0]
    tied = len(complete) > 1 and complete[1].get("rank_score", 0) == top.get("rank_score", 0)
    if tied:
        status = "competing"
        message = "Multiple diagnoses have complete evidence and similar ranking. Further distinction may require additional checks."
    else:
        status = "supported"
        message = "At least one diagnosis has all required conditions established by direct or inferred evidence. This remains a rule-based possibility."
    return {"status": status, "supported": complete, "partial": partial, "message": message}
