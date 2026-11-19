"""Tests for multi-step rule dependency reasoning."""
from engine.inference_engine import forward_chaining, backward_chaining

CHAIN_RULES = [
    {"id": 1, "conditions": ["symptom_a", "symptom_b"], "conclusion": "intermediate_x", "solution": "step one"},
    {"id": 2, "conditions": ["intermediate_x", "symptom_c"], "conclusion": "final_y", "solution": "step two"},
]

def test_forward_chaining_reaches_nested_conclusion():
    result = forward_chaining(["symptom_a", "symptom_b", "symptom_c"], CHAIN_RULES)
    assert "intermediate_x" in result["facts"] and "final_y" in result["facts"]
    assert [step["rule_id"] for step in result["trace"]] == [1, 2]

def test_backward_chaining_proves_nested_goal():
    result = backward_chaining("final_y", ["symptom_a", "symptom_b", "symptom_c"], CHAIN_RULES)
    assert result["success"] and len(result["trace"]) == 2

def test_backward_chaining_rejects_missing_leaf_fact():
    result = backward_chaining("final_y", ["symptom_a", "symptom_b"], CHAIN_RULES)
    assert not result["success"]
