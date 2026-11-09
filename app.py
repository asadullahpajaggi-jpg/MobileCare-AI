
import re
import streamlit as st

from knowledge_base.rules import RULES
from knowledge_base.assertions import ASSERTIONS

from engine.inference_engine import (
    forward_chaining,
    backward_chaining
)

from engine.rule_tester import run_rule_tests


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="MobileCare AI",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# PROFESSIONAL THEME
# ==================================================

st.markdown("""
<style>
.stApp {
    background-color: #081321;
    color: #E8F1FA;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1, h2, h3 {
    color: #F1F7FF !important;
}

p, label {
    color: #C5D3E3;
}

.stButton > button,
.stFormSubmitButton > button {
    background: #087E9B;
    color: white;
    border: none;
    border-radius: 10px;
    min-height: 43px;
    font-weight: 600;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background: #10AFC0;
    color: white;
}

.stTextArea textarea {
    background: #102034;
    color: white;
    border: 1px solid #31516E;
    border-radius: 10px;
}

div[data-testid="stMetric"] {
    background: #10263B;
    border: 1px solid #23435E;
    padding: 14px;
    border-radius: 12px;
}

div[data-testid="stAlert"] {
    border-radius: 10px;
}

hr {
    border-color: #243B53;
}

@media (max-width: 640px) {
    .block-container {
        padding: 1rem 0.8rem 2rem 0.8rem;
    }
}
</style>
""", unsafe_allow_html=True)


# ==================================================
# KNOWLEDGE BASE
# ==================================================

FACT_LOOKUP = {
    item["fact"]: item
    for item in ASSERTIONS
}


def get_fact_description(fact):

    assertion = FACT_LOOKUP.get(fact, {})

    return assertion.get(
        "description",
        fact.replace("_", " ").title()
    )


# ==================================================
# NATURAL LANGUAGE PROCESSING
# ==================================================

def normalize_tokens(text):

    words = re.findall(r"[a-z0-9]+", text.lower())
    normalized = []

    for word in words:

        if word.endswith("ies") and len(word) > 4:
            word = word[:-3] + "y"

        elif word.endswith("ing") and len(word) > 5:
            word = word[:-3]

        elif word.endswith("ed") and len(word) > 4:
            word = word[:-2]

        elif word.endswith("es") and len(word) > 4:
            word = word[:-2]

        elif word.endswith("s") and len(word) > 3:
            word = word[:-1]

        normalized.append(word)

    return normalized


def phrase_matches(user_words, keyword):

    phrase_words = normalize_tokens(keyword)

    if len(phrase_words) < 2:
        return False

    negations = {"not", "no", "never", "without"}

    for start in range(len(user_words)):

        positions = []

        for word in phrase_words:

            found = None

            for index in range(
                start,
                min(start + 6, len(user_words))
            ):

                if (
                    index not in positions
                    and user_words[index] == word
                ):
                    found = index
                    break

            if found is None:
                break

            positions.append(found)

        if len(positions) != len(phrase_words):
            continue

        if (
            max(positions) - min(positions)
            > len(phrase_words) + 2
        ):
            continue

        nearby_words = user_words[
            max(0, min(positions) - 2):
            max(positions) + 1
        ]

        if (
            negations.intersection(nearby_words)
            and not negations.intersection(phrase_words)
        ):
            continue

        return True

    return False


def extract_facts(problem):

    user_words = normalize_tokens(problem)
    matched_facts = []

    extra_keywords = {
        "phone_overheating": [
            "getting hot",
            "gets hot",
            "becomes hot",
            "heating up",
            "phone is hot",
            "mobile is hot",
            "overheating"
        ]
    }

    for assertion in ASSERTIONS:

        fact_name = assertion["fact"]

        keywords = assertion.get("keywords", [])

        keywords = keywords + [
            fact_name.replace("_", " ")
        ]

        keywords += extra_keywords.get(
            fact_name,
            []
        )

        for keyword in keywords:

            if phrase_matches(user_words, keyword):

                matched_facts.append(fact_name)
                break

    return sorted(set(matched_facts))


def get_followup_facts(matched_facts):

    known_facts = set(matched_facts)
    additional_facts = set()

    for rule in RULES:

        conditions = set(rule["conditions"])

        if conditions.intersection(known_facts):

            for condition in conditions:

                if condition not in known_facts:
                    additional_facts.add(condition)

    if "phone_not_charging" in known_facts:
        additional_facts.discard("phone_charging")

    if "phone_charging" in known_facts:
        additional_facts.discard("phone_not_charging")

    return sorted(additional_facts)


# ==================================================
# SESSION STATE
# ==================================================

if "diagnosis_ready" not in st.session_state:
    st.session_state["diagnosis_ready"] = False

if "diagnosis_result" not in st.session_state:
    st.session_state["diagnosis_result"] = None


# ==================================================
# SIDEBAR NAVIGATION
# ==================================================

st.sidebar.title("📱 MobileCare AI")
st.sidebar.caption("Android Troubleshooting Expert System")

st.sidebar.divider()

page = st.sidebar.radio(
    "MAIN MENU",
    [
        "🏠 Home",
        "🩺 Troubleshooting",
        "ℹ️ About Project",
        "🛠️ Developer Dashboard"
    ],
    key="navigation"
)

st.sidebar.divider()

st.sidebar.caption("BS Artificial Intelligence Major Project")


# ==================================================
# PAGE 1 — HOME
# ==================================================

if page == "🏠 Home":

    st.title("📱 MobileCare AI")

    st.subheader(
        "Your Android Mobile Troubleshooting Assistant"
    )

    st.write(
        "Welcome to MobileCare AI. An intelligent "
        "rule-based expert system designed to identify "
        "Android mobile problems and recommend possible solutions."
    )

    st.divider()

    st.subheader("Your Mobile Support System")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Knowledge Base Rules", "100")

    with col2:
        st.metric("Assertions / Facts", "300")

    with col3:
        st.metric("Inference Methods", "2")

    st.divider()

    st.subheader("How Does It Work?")

    st.write("**1. Describe Your Problem**")
    st.write(
        "Enter your Android mobile issue in simple English."
    )

    st.write("**2. Intelligent Analysis**")
    st.write(
        "The system identifies relevant facts and asks "
        "additional questions."
    )

    st.write("**3. Expert Diagnosis**")
    st.write(
        "Forward Chaining and Backward Chaining are used "
        "to generate and verify possible diagnoses."
    )

    st.write("**4. Recommended Solution**")
    st.write(
        "Receive troubleshooting suggestions based on "
        "the knowledge base."
    )

    st.divider()

    st.info(
        "Select Troubleshooting from the sidebar to diagnose "
        "your Android mobile problem."
    )


# ==================================================
# PAGE 2 — TROUBLESHOOTING
# ==================================================

elif page == "🩺 Troubleshooting":

    st.title("🩺 Mobile Troubleshooting")

    st.write(
        "Describe your Android mobile problem to begin "
        "the intelligent diagnosis process."
    )

    st.divider()









    # NEW DIAGNOSIS / RESET BUTTON

   if st.button("🔄 New Diagnosis", key="reset_diagnosis"):

       st.session_state["diagnosis_ready"] = False
       st.session_state["diagnosis_result"] = None

       for key in [
           "problem_text",
           "matched_facts",
           "followup_facts",
           "selected_facts"
       ]:
           st.session_state.pop(key, None)

       st.rerun()
    













    
    with st.form("problem_form"):

        problem = st.text_area(
            "What problem are you experiencing?",
            placeholder=(
                "Example: My phone battery drains very fast "
                "and my phone is getting hot..."
            ),
            height=120
        )

        submitted = st.form_submit_button(
            "🔎 Analyze My Problem",
            type="primary",
            use_container_width=True
        )

    if submitted:

        if problem.strip():

            st.session_state["problem_text"] = problem

            st.session_state["matched_facts"] = extract_facts(
                problem
            )

            st.session_state["diagnosis_ready"] = True

            st.session_state["diagnosis_result"] = None

        else:

            st.warning(
                "Please describe your mobile problem first."
            )

    if st.session_state["diagnosis_ready"]:

        matched_facts = st.session_state["matched_facts"]

        st.divider()

        st.header("🧠 Problem Analysis")

        if not matched_facts:

            st.warning(
                "No matching fact was identified. "
                "Try describing your issue using more specific words."
            )

        else:

            st.success(
                f"{len(matched_facts)} relevant fact(s) identified."
            )

            st.subheader("Identified Facts")

            for fact in matched_facts:
                st.write(
                    "✓ " + get_fact_description(fact)
                )

            followup_facts = get_followup_facts(
                matched_facts
            )

            st.divider()

            st.header("📋 Additional Information")

            st.write(
                "Select any additional statements that are "
                "also true for your phone."
            )

            followup_labels = {
                fact: get_fact_description(fact)
                for fact in followup_facts
            }

            with st.form("followup_form"):

                selected_facts = st.multiselect(
                    "Select applicable statements:",
                    options=followup_facts,
                    format_func=lambda fact: followup_labels.get(
                        fact,
                        fact.replace("_", " ").title()
                    ),
                    placeholder="Choose applicable statements..."
                )

                diagnose = st.form_submit_button(
                    "🩺 Run Expert Diagnosis",
                    type="primary",
                    use_container_width=True
                )

            if diagnose:

                all_facts = sorted(
                    set(matched_facts + selected_facts)
                )

                forward_result = forward_chaining(
                    all_facts,
                    RULES
                )

                diagnosis_trace = forward_result["trace"]

                shown_conclusions = []

                for step in diagnosis_trace:

                    conclusion = step["conclusion"]

                    if conclusion not in shown_conclusions:
                        shown_conclusions.append(conclusion)

                verified_count = 0

                for conclusion in shown_conclusions:

                    backward_result = backward_chaining(
                        conclusion,
                        all_facts,
                        RULES
                    )

                    if backward_result["success"]:
                        verified_count += 1

                st.session_state["diagnosis_result"] = {
                    "trace": diagnosis_trace,
                    "conclusions": shown_conclusions,
                    "verified": verified_count,
                    "total": len(shown_conclusions)
                }

            # DISPLAY SAVED DIAGNOSIS

            result = st.session_state["diagnosis_result"]

            if result is not None:

                st.divider()

                st.header("🩺 Diagnosis Results")

                if result["trace"]:

                    st.success(
                        "The expert system identified possible "
                        "causes and recommended solutions."
                    )

                    st.subheader(
                        "Detected Problems and Solutions"
                    )

                    for step in result["trace"]:

                        conclusion = step["conclusion"]

                        st.markdown(
                            "### 🔴 "
                            + conclusion.replace(
                                "_", " "
                            ).title()
                        )

                        st.write("**Recommended Solution:**")

                        st.info(step["solution"])

                        st.caption(
                            f"Applied Rule: {step['rule_id']}"
                        )

                    st.divider()

                    st.subheader("🔎 Diagnosis Verification")

                    st.metric(
                        "Backward Chaining Verification",
                        f"{result['verified']}/{result['total']}"
                    )

                    if result["verified"] == result["total"]:

                        st.success(
                            "All diagnosis conclusions were "
                            "verified by Backward Chaining."
                        )

                    else:

                        st.warning(
                            "Some conclusions could not be verified."
                        )

                    with st.expander(
                        "📖 View Expert System Explanation Trace"
                    ):

                        for step in result["trace"]:

                            st.write(
                                f"**Rule ID:** {step['rule_id']}"
                            )

                            st.write(
                                "**Conditions:**",
                                ", ".join(step["conditions"])
                            )

                            st.write(
                                "**Conclusion:**",
                                step["conclusion"]
                            )

                            st.write(
                                "**Solution:**",
                                step["solution"]
                            )

                            st.divider()

                else:

                    st.warning(
                        "No diagnosis rule was activated. "
                        "Try selecting additional applicable "
                        "statements or describing the problem "
                        "in more detail."
                    )

                st.caption(
                    "MobileCare AI provides rule-based suggestions. "
                    "For hardware damage or serious safety issues, "
                    "consult a qualified mobile technician."
                )


# ==================================================
# PAGE 3 — ABOUT PROJECT
# ==================================================

elif page == "ℹ️ About Project":

    st.title("ℹ️ About MobileCare AI")

    st.subheader(
        "Android Mobile Troubleshooting Expert System"
    )

    st.write(
        "MobileCare AI is a knowledge-based expert system "
        "developed as a BS Artificial Intelligence major project."
    )

    st.divider()

    st.subheader("Project Objectives")

    st.write(
        "- Identify common Android mobile problems."
    )

    st.write(
        "- Use a structured knowledge base of facts and rules."
    )

    st.write(
        "- Apply Forward Chaining for diagnosis."
    )

    st.write(
        "- Apply Backward Chaining for goal verification."
    )

    st.write(
        "- Provide recommended troubleshooting solutions."
    )

    st.divider()

    st.subheader("Core Technologies")

    st.write("**Python:** Main programming language.")

    st.write("**Streamlit:** Web application interface.")

    st.write("**Knowledge Base:** 100 IF-THEN rules and 300 facts.")

    st.write(
        "**Inference Engine:** Forward Chaining and "
        "Backward Chaining."
    )

    st.write(
        "**Natural Language Interface:** Extracts relevant "
        "facts from user descriptions."
    )

    st.divider()

    st.subheader("Project Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rules", len(RULES))

    with col2:
        st.metric("Facts", len(ASSERTIONS))

    with col3:
        st.metric("Inference Methods", 2)

    st.info(
        "This system provides educational, rule-based "
        "troubleshooting suggestions. It does not replace "
        "professional mobile hardware diagnosis."
    )


# ==================================================
# PAGE 4 — DEVELOPER DASHBOARD
# ==================================================

elif page == "🛠️ Developer Dashboard":

    st.title("🛠️ Developer Dashboard")

    st.write(
        "Technical verification, knowledge base validation "
        "and inference engine testing."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Knowledge Base Rules", len(RULES))

    with col2:
        st.metric("Assertions / Facts", len(ASSERTIONS))

    with col3:
        st.metric("Inference Methods", 2)

    # KNOWLEDGE BASE VALIDATION

    with st.expander(
        "📚 Knowledge Base Verification",
        expanded=True
    ):

        from validate_data import validate_knowledge_base

        report = validate_knowledge_base()

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Rules",
                report["rule_count"]
            )

        with col2:
            st.metric(
                "Facts",
                report["fact_count"]
            )

        st.subheader("Validation Results")

        for name, passed, details in report["checks"]:

            if passed:
                st.success(
                    f"PASS: {name} — {details}"
                )

            else:
                st.error(
                    f"FAIL: {name} — {details}"
                )

        if report["missing_facts"]:

            st.warning("Missing assertion facts:")

            for fact in report["missing_facts"]:
                st.write(f"- {fact}")

    # INFERENCE ENGINE TESTS

    with st.expander(
        "🧪 Inference Engine Tests"
    ):

        test_cases = [

            {
                "name": "Battery Problem",
                "facts": [
                    "battery_drains_fast",
                    "phone_old"
                ],
                "expected": "battery_health_low"
            },

            {
                "name": "Charging Problem",
                "facts": [
                    "phone_not_charging",
                    "charger_damaged"
                ],
                "expected": "charger_fault"
            },

            {
                "name": "Wi-Fi Problem",
                "facts": [
                    "wifi_not_working",
                    "airplane_mode_on"
                ],
                "expected": "airplane_mode_blocks_wifi"
            },

            {
                "name": "Outgoing Calls Problem",
                "facts": [
                    "outgoing_calls_failing",
                    "insufficient_balance"
                ],
                "expected": "insufficient_call_balance"
            },

            {
                "name": "Storage Problem",
                "facts": [
                    "phone_storage_full",
                    "system_cache_accumulated"
                ],
                "expected": "app_cache_consuming_storage"
            }
        ]

        passed = 0

        for test in test_cases:

            st.subheader(test["name"])

            forward = forward_chaining(
                test["facts"],
                RULES
            )

            backward = backward_chaining(
                test["expected"],
                test["facts"],
                RULES
            )

            forward_pass = (
                test["expected"] in forward["diagnoses"]
            )

            backward_pass = backward["success"]

            if forward_pass and backward_pass:

                st.success(
                    "PASS: Both inference methods working."
                )

                passed += 1

            else:

                st.error(
                    "FAIL: Test needs investigation."
                )

            st.write(
                "Forward Chaining:",
                "PASS" if forward_pass else "FAIL"
            )

            st.write(
                "Backward Chaining:",
                "PASS" if backward_pass else "FAIL"
            )

            with st.expander("View Test Explanation"):
                st.write(forward["trace"])

        negative_result = backward_chaining(
            "battery_health_low",
            ["battery_drains_fast"],
            RULES
        )

        st.subheader("Negative Test")

        if not negative_result["success"]:

            st.success(
                "PASS: Insufficient evidence correctly rejected."
            )

        else:

            st.error(
                "FAIL: Incomplete diagnosis was accepted."
            )

        st.divider()

        st.subheader("Final Test Summary")

        st.metric(
            "Successful Test Cases",
            f"{passed}/5"
        )

        if passed == 5 and not negative_result["success"]:

            st.success(
                "All inference engine tests passed!"
            )

        else:

            st.warning(
                "Some tests need further investigation."
            )

    # AUTOMATIC 100 RULE TESTING

    with st.expander(
        "🔬 Automatic 100 Rules Testing"
    ):

        st.write(
            "Test all knowledge base rules using "
            "Forward Chaining and Backward Chaining."
        )

        if st.button(
            "🚀 Run All Rule Tests",
            use_container_width=True
        ):

            test_report = run_rule_tests(RULES)

            st.divider()

            st.subheader("Automatic Testing Results")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Total Rules",
                    test_report["total"]
                )

            with col2:
                st.metric(
                    "Passed",
                    test_report["passed"]
                )

            with col3:
                st.metric(
                    "Failed",
                    test_report["failed"]
                )

            if (
                test_report["passed"] == test_report["total"]
                and test_report["total"] == 100
            ):

                st.success(
                    "All 100 rules passed Forward and "
                    "Backward Chaining tests."
                )

            else:

                st.warning(
                    "Some rules failed or the rule count "
                    "is different from 100."
                )

            with st.expander("View All Rule Test Results"):

                for result in test_report["results"]:

                    status = (
                        "PASS"
                        if result["passed"]
                        else "FAIL"
                    )

                    st.write(
                        f"Rule {result['rule_id']} — "
                        f"{result['conclusion']} — {status}"
                    )

                    st.caption(
                        f"Forward: "
                        f"{'PASS' if result['forward'] else 'FAIL'}"
                        f" | Backward: "
                        f"{'PASS' if result['backward'] else 'FAIL'}"
                    )

            failed_rules = [
                result
                for result in test_report["results"]
                if not result["passed"]
            ]

            if failed_rules:

                st.subheader(
                    "Rules Requiring Investigation"
                )

                for result in failed_rules:

                    st.error(
                        f"Rule {result['rule_id']}: "
                        f"{result['conclusion']}"
                    )


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "MobileCare AI | BS Artificial Intelligence Major Project"
)
