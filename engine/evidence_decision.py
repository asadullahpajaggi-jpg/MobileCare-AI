"""Evidence sufficiency and conservative stopping guidance."""
def assess_evidence(rows):
    """Classify evidence coverage and give a cautious next-step recommendation."""
    rows = rows or []
    complete, partial = [], []
    for row in rows:
        conditions = set(row.get("conditions") or [])
        direct = set(row.get("confirmed_conditions") or [])
        derived = set(row.get("derived_conditions") or [])
        missing = set(row.get("missing_conditions") or [])
        supported = direct | derived
        if conditions and not missing and conditions.issubset(supported):
            complete.append(row)
        elif supported:
            partial.append(row)

    if not complete:
        return {
            "status": "insufficient", "supported": [], "partial": partial,
            "message": "Required evidence is still missing for every matched cause.",
            "next_step": "Ask a relevant follow-up or gather more observations. Do not present partial matches as diagnoses.",
        }
    if len(complete) > 1:
        return {
            "status": "competing", "supported": complete, "partial": partial,
            "message": "More than one cause has complete rule evidence. The system cannot reliably select one.",
            "next_step": "Compare the suggested checks for each cause or seek professional inspection if the problem persists.",
        }
    top = complete[0]
    derived_used = bool(top.get("derived_conditions"))
    return {
        "status": "supported", "supported": complete, "partial": partial,
        "message": "One cause has complete evidence in the current rule set, but this is not a verified hardware diagnosis.",
        "next_step": "Try the safe recommended check. If the issue remains or the check is inconclusive, seek professional support.",
        "evidence_basis": "Includes inferred facts" if derived_used else "All required conditions directly confirmed",
    }
