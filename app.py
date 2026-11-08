
import streamlit as st

st.set_page_config(
    page_title="MobileCare AI",
    page_icon="📱",
    layout="wide"
)

st.title("📱 MobileCare AI")
st.subheader("Android Mobile Troubleshooting Expert System")

st.write(
    "Welcome to MobileCare AI. "
    "Your intelligent assistant for Android mobile problems."
)

st.divider()

st.header("How can we help you?")

problem = st.text_area(
    "Describe your mobile problem:",
    placeholder="Example: My phone battery drains very fast..."
)

if st.button("Diagnose Problem"):
    if problem.strip():
        st.info("Your problem has been received.")
        st.write("Expert System diagnosis will be integrated here.")
    else:
        st.warning("Please describe your mobile problem.")

st.divider()

st.caption("MobileCare AI | BS Artificial Intelligence Major Project")


# Knowledge Base Validation

from validate_data import validate_knowledge_base

st.divider()
st.header("Knowledge Base Verification")

report = validate_knowledge_base()

col1, col2 = st.columns(2)

with col1:
    st.metric("Knowledge Base Rules", report["rule_count"])

with col2:
    st.metric("Assertions / Facts", report["fact_count"])

st.subheader("Validation Results")

for name, passed, details in report["checks"]:
    if passed:
        st.success(f"PASS: {name} — {details}")
    else:
        st.error(f"FAIL: {name} — {details}")

if report["missing_facts"]:
    st.warning("These rule conditions do not have matching assertion facts:")

    for fact in report["missing_facts"]:
        st.write(f"- {fact}")


# Inference Engine Testing

from knowledge_base.rules import RULES
from engine.inference_engine import (
    forward_chaining,
    backward_chaining
)

st.divider()
st.header("🧠 Inference Engine Testing")

test_facts = [
    "battery_drains_fast",
    "phone_old"
]

test_goal = "battery_health_low"

st.subheader("Test Facts")
st.write(test_facts)

# Forward Chaining Test
st.subheader("1. Forward Chaining")

forward_result = forward_chaining(test_facts, RULES)

if test_goal in forward_result["diagnoses"]:
    st.success("PASS: Forward Chaining generated the expected diagnosis.")
else:
    st.error("FAIL: Forward Chaining did not generate the expected diagnosis.")

st.write("Generated Diagnoses:")
st.write(list(forward_result["diagnoses"]))

# Backward Chaining Test
st.subheader("2. Backward Chaining")

backward_result = backward_chaining(
    test_goal,
    test_facts,
    RULES
)

if backward_result["success"]:
    st.success("PASS: Backward Chaining verified the diagnosis.")
else:
    st.error("FAIL: Backward Chaining could not verify the diagnosis.")

# Explanation Trace
st.subheader("3. Rule Explanation")

st.write("Forward Chaining Trace:")
st.json(forward_result["trace"])

st.write("Backward Chaining Trace:")
st.json(backward_result["trace"])
