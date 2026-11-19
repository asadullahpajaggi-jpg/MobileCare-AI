"""Orchestrate diagnosis inference, ranking, evidence adequacy, and goal verification."""
from engine.inference_engine import forward_chaining, backward_chaining
from engine.diagnosis_engine import summarize_diagnosis
from engine.decision_engine import rank_diagnoses, decision_summary
from engine.evidence_decision import assess_evidence


def run_diagnosis(facts, rules):
    """Return a consistent diagnosis pipeline report from observed facts."""
    observed = sorted(set(facts or []))
    forward = forward_chaining(observed, rules)
    trace = forward["trace"]
    evidence = summarize_diagnosis(trace, observed)
    ranked = rank_diagnoses(trace, observed)
    entries_by_conclusion = {entry["conclusion"]: entry for entry in evidence["entries"]}
    evidence_rows = [{**entries_by_conclusion.get(row["conclusion"], {}), **row}
                     for row in ranked]
    adequacy = assess_evidence(evidence_rows)
    summary = decision_summary(ranked)
    verified = []
    for row in ranked:
        proof = backward_chaining(row["conclusion"], observed, rules)
        verified.append({"conclusion": row["conclusion"], "success": proof["success"],
                         "trace": proof["trace"]})
    return {
        "observed_facts": observed, "trace": trace,
        "conclusions": [row["conclusion"] for row in ranked],
        "evidence_report": evidence, "ranked": ranked,
        "summary": summary, "evidence_status": adequacy,
        "verified": sum(item["success"] for item in verified),
        "total": len(verified), "verification": verified,
    }
