
import re
import streamlit as st

from knowledge_base.rules import RULES
from knowledge_base.assertions import ASSERTIONS

from engine.inference_engine import (
    forward_chaining,
    backward_chaining
)


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="MobileCare AI",
    page_icon="📱",
    layout="wide"
)


# --------------------------------------------------
# KNOWLEDGE BASE LOOKUP
# --------------------------------------------------

FACT_LOOKUP = {
    item["fact"]: item
    for item in ASSERTIONS
}






def normalize_tokens(text):
    """Normalize text while preserving word order."""

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
    """Check phrase meaning without matching isolated words."""

    phrase_words = normalize_tokens(keyword)

    # Ignore single-word keywords to reduce false matches.
    if len(phrase_words) < 2:
        return False

    negations = {"not", "no", "never", "without"}

    for start in range(len(user_words)):

        positions = []

        for word in phrase_words:

            found = None

            for index in range(start, min(start + 6, len(user_words))):

                if index not in positions and user_words[index] == word:
                    found = index
                    break

            if found is None:
                break

            positions.append(found)

        if len(positions) != len(phrase_words):
            continue

        # Keep matched words reasonably close together.
        if max(positions) - min(positions) > len(phrase_words) + 2:
            continue

        # Do not match a positive fact when the user negates it.
        nearby_words = user_words[
            max(0, min(positions) - 2):max(positions) + 1
        ]

        if (
            negations.intersection(nearby_words)
            and not negations.intersection(phrase_words)
        ):
            continue

        return True

    return False


def extract_facts(problem):
    """Extract facts using phrase matching and negation handling."""

    user_words = normalize_tokens(problem)
    matched_facts = []

    for assertion in ASSERTIONS:

        fact_name = assertion["fact"]
        keywords = assertion.get("keywords", [])

        keywords = keywords + [
            fact_name.replace("_", " ")
        ]

        for keyword in keywords:

            if phrase_matches(user_words, keyword):

                matched_facts.append(fact_name)
                break

    return list(set(matched_facts))


def get_followup_facts(matched_facts):
    """Find relevant missing conditions without contradictions."""

    known_facts = set(matched_facts)
    additional_facts = set()

    for rule in RULES:

        conditions = set(rule["conditions"])

        if conditions.intersection(known_facts):

            for condition in conditions:

                if condition not in known_facts:
                    additional_facts.add(condition)

    # Avoid asking contradictory questions.
    if "phone_not_charging" in known_facts:
        additional_facts.discard("phone_charging")

    if "phone_charging" in known_facts:
        additional_facts.discard("phone_not_charging")

    return sorted(additional_facts)
        







# --------------------------------------------------
# APPLICATION HEADER
# --------------------------------------------------

st.title("📱 MobileCare AI")

st.subheader(
    "Android Mobile Troubleshooting Expert System"
)

st.write(
    "Welcome to MobileCare AI. "
    "Describe your Android mobile problem in simple English "
    "to receive an intelligent troubleshooting diagnosis."
)

st.divider()


# --------------------------------------------------
# NATURAL LANGUAGE INTERFACE
# --------------------------------------------------

st.header("🔍 Describe Your Mobile Problem")

with st.form("problem_form"):

    problem = st.text_area(
        "What problem are you experiencing?",
        placeholder=(
            "Example: My phone battery drains very fast..."
        ),
        height=120
    )

    submitted = st.form_submit_button(
        "Identify My Problem",
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

    else:

        st.warning("Please describe your mobile problem.")


# --------------------------------------------------
# DISPLAY IDENTIFIED FACTS
# --------------------------------------------------

if st.session_state.get("diagnosis_ready", False):

    matched_facts = st.session_state["matched_facts"]

    st.divider()

    st.header("🧠 Problem Analysis")

    if not matched_facts:

        st.warning(
            "The system could not identify a matching fact. "
            "Please describe your problem using different or "
            "more specific words."
        )

    else:

        st.success(
            f"Successfully identified {len(matched_facts)} "
            "relevant fact(s)."
        )

        st.subheader("Identified Facts")

        for fact in matched_facts:

            assertion = FACT_LOOKUP.get(fact, {})

            description = assertion.get(
                "description",
                fact.replace("_", " ").title()
            )

            st.write(f"✓ {description}")


        # --------------------------------------------------
        # ASK FOLLOW-UP QUESTIONS
        # --------------------------------------------------

        followup_facts = get_followup_facts(matched_facts)

        st.divider()

        st.header("📋 Additional Information")

        st.write(
            "The system may need some additional information "
            "to improve its diagnosis. Select the statements "
            "that are also true for your phone."
        )

        followup_labels = {}

        for fact in followup_facts:

            assertion = FACT_LOOKUP.get(fact, {})

            description = assertion.get(
                "description",
                fact.replace("_", " ").title()
            )

            followup_labels[fact] = description


        with st.form("followup_form"):

            selected_facts = st.multiselect(
                "Select applicable statements:",
                options=followup_facts,
                format_func=lambda fact: followup_labels.get(
                    fact,
                    fact.replace("_", " ").title()
                )
            )

            diagnose = st.form_submit_button(
                "🩺 Run Expert Diagnosis",
                type="primary",
                use_container_width=True
            )


        # --------------------------------------------------
        # FORWARD AND BACKWARD CHAINING
        # --------------------------------------------------

        if diagnose:

            all_facts = list(
                set(matched_facts + selected_facts)
            )

            forward_result = forward_chaining(
                all_facts,
                RULES
            )

            st.divider()

            st.header("🩺 Diagnosis Results")

            diagnosis_trace = forward_result["trace"]

            if diagnosis_trace:

                st.success(
                    "The expert system successfully identified "
                    "possible causes of your mobile problem."
                )

                st.subheader("Detected Problems and Solutions")

                shown_conclusions = set()

                for step in diagnosis_trace:

                    conclusion = step["conclusion"]

                    if conclusion in shown_conclusions:
                        continue

                    shown_conclusions.add(conclusion)

                    st.markdown(
                        f"### 🔴 "
                        f"{conclusion.replace('_', ' ').title()}"
                    )

                    st.write("**Recommended Solution:**")

                    st.info(step["solution"])

                    st.caption(
                        f"Applied Rule: {step['rule_id']}"
                    )


                # --------------------------------------------------
                # BACKWARD CHAINING VERIFICATION
                # --------------------------------------------------

                st.divider()

                st.subheader("🔎 Diagnosis Verification")

                verified_count = 0

                for conclusion in shown_conclusions:

                    backward_result = backward_chaining(
                        conclusion,
                        all_facts,
                        RULES
                    )

                    if backward_result["success"]:
                        verified_count += 1

                st.success(
                    f"Backward Chaining verified "
                    f"{verified_count}/{len(shown_conclusions)} "
                    "diagnosis conclusion(s)."
                )


                # --------------------------------------------------
                # EXPLANATION TRACE
                # --------------------------------------------------

                with st.expander(
                    "View Expert System Explanation Trace"
                ):

                    for step in diagnosis_trace:

                        st.write(
                            f"**Rule ID:** {step['rule_id']}"
                        )

                        st.write(
                            "**Conditions:**",
                            step["conditions"]
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
                    "No diagnosis rule was activated with the "
                    "available facts. Try selecting additional "
                    "applicable statements or describing the "
                    "problem in more detail."
                )


            st.caption(
                "MobileCare AI provides rule-based suggestions. "
                "For hardware damage or serious safety issues, "
                "consult a qualified mobile technician."
            )


# --------------------------------------------------
# DEVELOPER: KNOWLEDGE BASE VALIDATION
# --------------------------------------------------

with st.expander("🛠️ Developer Tools — Knowledge Base Verification"):

    from validate_data import validate_knowledge_base

    report = validate_knowledge_base()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Knowledge Base Rules",
            report["rule_count"]
        )

    with col2:
        st.metric(
            "Assertions / Facts",
            report["fact_count"]
        )

    st.subheader("Validation Results")

    for name, passed, details in report["checks"]:

        if passed:
            st.success(f"PASS: {name} — {details}")

        else:
            st.error(f"FAIL: {name} — {details}")

    if report["missing_facts"]:

        st.warning("Missing assertion facts:")

        for fact in report["missing_facts"]:
            st.write(f"- {fact}")


# --------------------------------------------------
# DEVELOPER: INFERENCE ENGINE TESTING
# --------------------------------------------------

with st.expander("🧪 Developer Tools — Inference Engine Tests"):

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
            st.json(forward["trace"])


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


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "MobileCare AI | BS Artificial Intelligence Major Project"
)
