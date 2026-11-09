
import re
import streamlit as st

from knowledge_base.rules import RULES
from knowledge_base.assertions import ASSERTIONS

from engine.inference_engine import (
    forward_chaining,
    backward_chaining
)

from engine.rule_tester import run_rule_tests


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="MobileCare AI",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# --------------------------------------------------
# PROFESSIONAL UI DESIGN
# --------------------------------------------------

st.markdown("""
<style>

/* Main application */

.stApp {
    background: #081321;
    color: #E8F1FA;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Headings */

h1, h2, h3 {
    color: #F1F7FF !important;
}

p, label, .stMarkdown {
    color: #C5D3E3;
}

/* Main header */

.hero {
    background: linear-gradient(135deg, #102B49, #0B1D32);
    border: 1px solid #1C4567;
    border-radius: 20px;
    padding: 30px 25px;
    margin-bottom: 25px;
}

.hero-title {
    font-size: 34px;
    font-weight: 800;
    color: #FFFFFF;
    margin-bottom: 8px;
}

.hero-subtitle {
    font-size: 16px;
    color: #A9C7E5;
    line-height: 1.6;
}

.hero-tag {
    display: inline-block;
    background: #123B54;
    color: #5DE1E6;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
    margin-bottom: 15px;
}

/* Section headings */

.section-label {
    color: #54DDE6;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 5px;
}

/* Cards */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #102034;
    border: 1px solid #203B55;
    border-radius: 15px;
}

/* Buttons */

.stButton > button,
.stFormSubmitButton > button {
    background: linear-gradient(90deg, #087E9B, #11A9B5);
    color: white;
    border: none;
    border-radius: 10px;
    min-height: 45px;
    font-weight: 700;
    transition: 0.2s;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background: linear-gradient(90deg, #0B9BB5, #20C5CA);
    color: white;
    border: none;
}

/* Text area */

.stTextArea textarea {
    background: #0D1C2D;
    color: #FFFFFF;
    border: 1px solid #31516E;
    border-radius: 12px;
}

/* Multiselect */

.stMultiSelect [data-baseweb="select"] {
    background: #0D1C2D;
    border-radius: 10px;
}

/* Metrics */

div[data-testid="stMetric"] {
    background: #10263B;
    border: 1px solid #23435E;
    padding: 15px;
    border-radius: 12px;
}

/* Alerts */

div[data-testid="stAlert"] {
    border-radius: 12px;
}

/* Expanders */

.streamlit-expanderHeader {
    background: #10263B;
    border-radius: 10px;
    color: #DCEBFA;
    font-weight: 600;
}

/* Divider */

hr {
    border-color: #243B53;
}

/* Footer */

.footer {
    text-align: center;
    color: #7891AA;
    font-size: 13px;
    padding: 20px 5px;
    border-top: 1px solid #20364D;
    margin-top: 30px;
}

/* Mobile responsive design */

@media (max-width: 640px) {

    .block-container {
        padding: 1rem 0.8rem 2rem 0.8rem;
    }

    .hero {
        padding: 22px 17px;
        border-radius: 15px;
    }

    .hero-title {
        font-size: 27px;
    }

    .hero-subtitle {
        font-size: 14px;
    }

    h1 {
        font-size: 27px !important;
    }

    h2 {
        font-size: 22px !important;
    }

}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# KNOWLEDGE BASE LOOKUP
# --------------------------------------------------

FACT_LOOKUP = {
    item["fact"]: item
    for item in ASSERTIONS
}


# --------------------------------------------------
# NATURAL LANGUAGE PROCESSING
# --------------------------------------------------

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


def get_fact_description(fact):

    assertion = FACT_LOOKUP.get(fact, {})

    return assertion.get(
        "description",
        fact.replace("_", " ").title()
    )


# --------------------------------------------------
# HERO HEADER
# --------------------------------------------------

st.markdown("""
<div class="hero">

    <div class="hero-tag">
        AI POWERED TROUBLESHOOTING
    </div>

    <div class="hero-title">
        📱 MobileCare AI
    </div>

    <div class="hero-subtitle">
        Your intelligent Android mobile troubleshooting
        assistant. Describe your mobile problem and get
        rule-based diagnosis with recommended solutions.
    </div>

</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# PROJECT OVERVIEW
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Knowledge Base Rules", "100")

with col2:
    st.metric("Assertions / Facts", "300")

with col3:
    st.metric("Inference Methods", "2")


st.divider()


# --------------------------------------------------
# PROBLEM INPUT
# --------------------------------------------------

st.markdown(
    '<div class="section-label">STEP 01</div>',
    unsafe_allow_html=True
)

st.header("🔍 Describe Your Mobile Problem")

st.write(
    "Explain your Android mobile issue in simple English. "
    "The system will analyze your description and identify "
    "relevant facts."
)

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

    else:

        st.warning(
            "Please describe your mobile problem first."
        )


# --------------------------------------------------
# PROBLEM ANALYSIS
# --------------------------------------------------

if st.session_state.get("diagnosis_ready", False):

    matched_facts = st.session_state["matched_facts"]

    st.divider()

    st.markdown(
        '<div class="section-label">STEP 02</div>',
        unsafe_allow_html=True
    )

    st.header("🧠 Problem Analysis")

    if not matched_facts:

        st.warning(
            "No matching fact was identified. "
            "Please describe your issue using more specific "
            "words."
        )

    else:

        st.success(
            f"{len(matched_facts)} relevant fact(s) identified."
        )

        with st.container(border=True):

            st.subheader("Identified Facts")

            for fact in matched_facts:

                st.markdown(
                    f"✓ {get_fact_description(fact)}"
                )


        # --------------------------------------------------
        # FOLLOW-UP QUESTIONS
        # --------------------------------------------------

        followup_facts = get_followup_facts(
            matched_facts
        )

        st.divider()

        st.markdown(
            '<div class="section-label">STEP 03</div>',
            unsafe_allow_html=True
        )

        st.header("📋 Additional Information")

        st.write(
            "Select any additional statements that are true "
            "for your phone. These answers can help improve "
            "the diagnosis."
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


        # --------------------------------------------------
        # INFERENCE ENGINE
        # --------------------------------------------------

        if diagnose:

            all_facts = sorted(
                set(matched_facts + selected_facts)
            )

            forward_result = forward_chaining(
                all_facts,
                RULES
            )

            diagnosis_trace = forward_result["trace"]

            st.divider()

            st.markdown(
                '<div class="section-label">STEP 04</div>',
                unsafe_allow_html=True
            )

            st.header("🩺 Diagnosis Results")

            if diagnosis_trace:

                st.success(
                    "The expert system identified possible "
                    "causes and generated recommended solutions."
                )

                st.subheader(
                    "Detected Problems and Solutions"
                )

                shown_conclusions = set()

                for step in diagnosis_trace:

                    conclusion = step["conclusion"]

                    if conclusion in shown_conclusions:
                        continue

                    shown_conclusions.add(conclusion)

                    with st.container(border=True):

                        st.markdown(
                            "### 🔴 "
                            + conclusion.replace(
                                "_", " "
                            ).title()
                        )

                        st.write(
                            "**Recommended Solution**"
                        )

                        st.info(step["solution"])

                        st.caption(
                            f"Applied Knowledge Base Rule: "
                            f"{step['rule_id']}"
                        )


                # --------------------------------------------------
                # BACKWARD CHAINING VERIFICATION
                # --------------------------------------------------

                st.divider()

                st.subheader(
                    "🔎 Diagnosis Verification"
                )

                verified_count = 0

                for conclusion in shown_conclusions:

                    backward_result = backward_chaining(
                        conclusion,
                        all_facts,
                        RULES
                    )

                    if backward_result["success"]:
                        verified_count += 1

                st.metric(
                    "Backward Chaining Verification",
                    f"{verified_count}/{len(shown_conclusions)}"
                )

                if verified_count == len(shown_conclusions):

                    st.success(
                        "All generated diagnosis conclusions "
                        "were verified by Backward Chaining."
                    )

                else:

                    st.warning(
                        "Some diagnosis conclusions could not "
                        "be verified."
                    )


                # --------------------------------------------------
                # EXPLANATION TRACE
                # --------------------------------------------------

                with st.expander(
                    "📖 View Expert System Explanation Trace"
                ):

                    st.write(
                        "The following rules were activated "
                        "during Forward Chaining."
                    )

                    for step in diagnosis_trace:

                        st.markdown(
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
# DEVELOPER TOOLS
# --------------------------------------------------

st.divider()

st.markdown(
    '<div class="section-label">SYSTEM MANAGEMENT</div>',
    unsafe_allow_html=True
)

st.header("🛠️ Developer Tools")

st.caption(
    "Technical verification and testing tools for project evaluation."
)


# --------------------------------------------------
# KNOWLEDGE BASE VALIDATION
# --------------------------------------------------

with st.expander(
    "📚 Knowledge Base Verification"
):

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


# --------------------------------------------------
# INFERENCE ENGINE TESTING
# --------------------------------------------------

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
# AUTOMATIC 100 RULES TESTING
# --------------------------------------------------

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

        st.subheader("Individual Rule Results")

        with st.expander(
            "View All Rule Test Results"
        ):

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


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">

    <strong>MobileCare AI</strong><br>

    Android Mobile Troubleshooting Expert System<br>

    BS Artificial Intelligence Major Project

</div>
""", unsafe_allow_html=True)
