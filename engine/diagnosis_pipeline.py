"""Orchestrate diagnosis inference, contradiction handling, and evidence verification."""
from engine.inference_engine import forward_chaining, backward_chaining
from engine.diagnosis_engine import summarize_diagnosis
from engine.decision_engine import rank_diagnoses, decision_summary
from engine.evidence_decision import assess_evidence
from engine.contradiction_engine import detect_contradictions, remove_conflicted_facts

def run_diagnosis(facts, rules):
    observed = sorted(set(facts or []))
    conflicts = detect_contradictions(observed)
    reasoning_facts = remove_conflicted_facts(observed, conflicts)
    forward = forward_chaining(reasoning_facts, rules)
    trace = forward["trace"]
    evidence = summarize_diagnosis(trace, reasoning_facts)
    ranked = rank_diagnoses(trace, reasoning_facts)
    entries_by_conclusion = {entry["conclusion"]: entry for entry in evidence["entries"]}
    evidence_rows = [{**entries_by_conclusion.get(row["conclusion"], {}), **row} for row in ranked]
    adequacy = assess_evidence(evidence_rows)
    summary = decision_summary(ranked)
    verified = [{"conclusion": row["conclusion"], "success": backward_chaining(row["conclusion"], reasoning_facts, rules)["success"],
                 "trace": backward_chaining(row["conclusion"], reasoning_facts, rules)["trace"]} for row in ranked]
    return {"observed_facts": observed, "reasoning_facts": reasoning_facts, "contradictions": conflicts,
            "trace": trace, "conclusions": [row["conclusion"] for row in ranked],
            "evidence_report": evidence, "ranked": ranked, "summary": summary,
            "evidence_status": adequacy, "verified": sum(item["success"] for item in verified),
            "total": len(verified), "verification": verified}
