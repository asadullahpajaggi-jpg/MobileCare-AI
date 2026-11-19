"""Convert rule-engine outputs into clear, user-friendly troubleshooting language."""

def _label(value):
    return str(value or "").replace("_", " ").strip().capitalize()

def build_user_report(result, fact_descriptions=None):
    """Build a plain-language report; internal rule identifiers are omitted."""
    fact_descriptions = fact_descriptions or {}
    describe = lambda fact: fact_descriptions.get(fact, _label(fact))
    contradictions = result.get("contradictions") or []
    ranked = result.get("ranked") or []
    evidence = result.get("evidence_report") or {}
    entries = {row.get("conclusion"): row for row in (evidence.get("entries") or [])}
    status = result.get("evidence_status") or {}

    if contradictions:
        conflicting = [" or ".join(describe(f) for f in item.get("facts", [])) for item in contradictions]
        return {
            "opening": "I noticed some conflicting details in what was reported. I won't use those conflicting details to decide the cause.",
            "conflicts": conflicting,
            "causes": [],
            "closing": "Please clarify which of these observations is correct, then start the diagnosis again.",
            "has_causes": bool(ranked),
        }

    causes = []
    for row in ranked:
        entry = entries.get(row.get("conclusion"), {})
        missing = entry.get("missing_conditions") or []
        direct = entry.get("confirmed_conditions") or []
        derived = entry.get("derived_conditions") or []
        if missing:
            explanation = "This is a possibility, but I still need to confirm: " + ", ".join(describe(f) for f in missing) + "."
            strength = "Possible explanation; more information needed"
        elif derived:
            explanation = "This explanation is supported by symptoms and by a condition inferred during the rule-based analysis."
            strength = "Supported by the current evidence"
        else:
            explanation = "The symptoms you reported match the conditions for this explanation in my troubleshooting knowledge."
            strength = "Supported by the reported symptoms"
        causes.append({
            "title": _label(row.get("conclusion")),
            "explanation": explanation,
            "strength": strength,
            "solution": row.get("solution") or "Try checking this condition carefully.",
            "confirmed": [describe(f) for f in direct],
            "inferred": [describe(f) for f in derived],
            "missing": [describe(f) for f in missing],
        })

    if not causes:
        opening = "I couldn't find a matching explanation in my troubleshooting knowledge from the details provided."
        closing = "Please describe what happens, when it happens, and any error message you see. I don't want to guess."
    elif status.get("status") == "competing":
        opening = "I found more than one explanation that matches the reported symptoms. I can't safely choose just one yet."
        closing = "Try the checks below one at a time. If the problem continues, a technician may need to inspect the phone."
    elif status.get("status") == "insufficient":
        opening = "I found some possible directions to investigate, but the details aren't enough to establish a cause."
        closing = "Please check the suggested conditions or provide more details before treating any of these as the cause."
    else:
        opening = "Based on the symptoms you described, I found a possible explanation."
        closing = "This is a rule-based suggestion, not a confirmed hardware diagnosis. If the problem continues, seek professional support."

    return {"opening": opening, "conflicts": [], "causes": causes, "closing": closing, "has_causes": bool(causes)}
