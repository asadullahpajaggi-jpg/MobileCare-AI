
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




# Multiple Rules Testing

st.divider()
st.header("🧠 Advanced Inference Engine Testing")

test_cases = [
    {
        "name": "Battery Problem",
        "facts": ["battery_drains_fast", "phone_old"],
        "expected": "battery_health_low"
    },
    {
        "name": "Charging Problem",
        "facts": ["phone_not_charging", "charger_damaged"],
        "expected": "charger_fault"
    },
    {
        "name": "Wi-Fi Problem",
        "facts": ["wifi_not_working", "airplane_mode_on"],
        "expected": "airplane_mode_blocks_wifi"
    },
    {
        "name": "Outgoing Calls Problem",
        "facts": ["outgoing_calls_failing", "insufficient_balance"],
        "expected": "insufficient_call_balance"
    },
    {
        "name": "Storage Problem",
        "facts": ["phone_storage_full", "system_cache_accumulated"],
        "expected": "app_cache_consuming_storage"
    }
]

passed = 0

for test in test_cases:

    st.subheader(test["name"])

    forward = forward_chaining(test["facts"], RULES)

    backward = backward_chaining(
        test["expected"],
        test["facts"],
        RULES
    )

    forward_pass = test["expected"] in forward["diagnoses"]
    backward_pass = backward["success"]

    if forward_pass and backward_pass:
        st.success("PASS: Both inference methods working.")
        passed += 1
    else:
        st.error("FAIL: Test needs investigation.")

    st.write("Input Facts:", test["facts"])
    st.write("Expected Diagnosis:", test["expected"])
    st.write("Forward Chaining:", "PASS" if forward_pass else "FAIL")
    st.write("Backward Chaining:", "PASS" if backward_pass else "FAIL")

    with st.expander("View Explanation Trace"):
        st.json(forward["trace"])


st.divider()

st.subheader("Negative Test")

negative_result = backward_chaining(
    "battery_health_low",
    ["battery_drains_fast"],
    RULES
)

if not negative_result["success"]:
    st.success("PASS: System correctly rejected insufficient evidence.")
else:
    st.error("FAIL: System accepted an incomplete diagnosis.")

st.divider()

st.subheader("Final Test Summary")

st.metric("Successful Test Cases", f"{passed}/5")

if passed == 5 and not negative_result["success"]:
    st.success("All inference engine tests passed!")
else:
    st.warning("Some tests need further investigation.")
