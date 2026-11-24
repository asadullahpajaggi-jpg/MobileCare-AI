
import streamlit as st

from knowledge_base.rules import RULES
from knowledge_base.assertions import ASSERTIONS

from engine.inference_engine import (
    forward_chaining,
    backward_chaining
)

from engine.rule_tester import run_rule_tests
from engine.nlp_engine import extract_facts, extract_negated_facts


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
/* Theme colors: preserve the existing design while adapting to Streamlit mode. */
:root {
    --app-bg: #081321;
    --app-text: #E8F1FA;
    --heading-text: #F1F7FF;
    --muted-text: #C5D3E3;
    --sidebar-bg: #102034;
    --sidebar-text: #E8F1FA;
    --surface-bg: #10263B;
    --field-bg: #102034;
    --field-text: #FFFFFF;
    --border-color: #31516E;
    --soft-border: #23435E;
    --divider-color: #243B53;
}

html[data-theme="light"] {
    --app-bg: #F7F9FC;
    --app-text: #243447;
    --heading-text: #102A43;
    --muted-text: #526579;
    --sidebar-bg: #EAF0F6;
    --sidebar-text: #243447;
    --surface-bg: #FFFFFF;
    --field-bg: #FFFFFF;
    --field-text: #243447;
    --border-color: #C5D1DE;
    --soft-border: #D5DEE8;
    --divider-color: #D5DEE8;
}

.stApp {
    background-color: var(--app-bg);
    color: var(--app-text);
}

[data-testid="stSidebar"] {
    background-color: var(--sidebar-bg) !important;
}

[data-testid="stSidebar"] [data-testid="stMarkdown"],
[data-testid="stSidebar"] [data-testid="stMarkdown"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] [data-testid="stWidgetLabel"],
[data-testid="stSidebar"] [data-testid="stCaptionContainer"],
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p,
[data-testid="stSidebar"] [data-testid="stRadio"] label,
[data-testid="stSidebar"] [data-testid="stRadio"] p,
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] div {
    color: var(--sidebar-text) !important;
}

[data-testid="stSidebar"] hr {
    border-color: var(--border-color) !important;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1, h2, h3 {
    color: var(--heading-text) !important;
}

p, label {
    color: var(--muted-text);
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
    background: var(--field-bg);
    color: var(--field-text);
    border: 1px solid var(--border-color);
    border-radius: 10px;
}

div[data-testid="stMetric"] {
    background: var(--surface-bg);
    color: var(--app-text);
    border: 1px solid var(--soft-border);
    padding: 14px;
    border-radius: 12px;
}

div[data-testid="stAlert"] {
    border-radius: 10px;
}

hr {
    border-color: var(--divider-color);
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
# FOLLOW-UP FACT SELECTION
# ==================================================

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
# NAVIGATION CALLBACK
# ==================================================

def go_to_troubleshooting():
    st.session_state["navigation"] = "🩺 Troubleshooting"


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
        st.metric("Knowledge Base Rules", len(RULES))

    with col2:
        st.metric("Assertions / Facts", len(ASSERTIONS))

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

    st.button(
        "🚀 Enter MobileCare AI",
        key="enter_troubleshooting",
        type="primary",
        use_container_width=True,
        on_click=go_to_troubleshooting,
    )





# ==================================================
# PAGE 2 — TROUBLESHOOTING
# ==================================================



elif page == "🩺 Troubleshooting":

    # --------------------------------------------------
    # SESSION STATE
    # --------------------------------------------------

    st.session_state.setdefault("diagnosis_ready", False)
    st.session_state.setdefault("diagnosis_result", None)
    st.session_state.setdefault("problem_text", "")
    st.session_state.setdefault("semantic_candidates", [])
    st.session_state.setdefault("semantic_review_pending", False)
    st.session_state.setdefault("semantic_error", False)
    st.session_state.setdefault("confirmed_facts", [])

    st.title("🩺 Mobile Troubleshooting")



    # --------------------------------------------------
    # NEW DIAGNOSIS / RESET
    # --------------------------------------------------

    if st.button("🔄 New Diagnosis", key="reset_diagnosis"):

        st.session_state["diagnosis_ready"] = False
        st.session_state["diagnosis_result"] = None
        st.session_state["problem_text"] = ""

        st.session_state["semantic_candidates"] = []
        st.session_state["semantic_review_pending"] = False
        st.session_state["semantic_error"] = False
        st.session_state["confirmed_facts"] = []
        st.session_state["negated_facts"] = []
        st.session_state["followup_answers"] = {}

        st.session_state["problem_input"] = ""
        st.session_state["semantic_candidate_selection"] = []
        st.session_state["selected_facts_input"] = []

        st.rerun()

    # --------------------------------------------------
    # NATURAL LANGUAGE PROBLEM INPUT
    # --------------------------------------------------

    with st.form("problem_form"):

        problem = st.text_area(
            "What problem are you experiencing?",
            placeholder=(
                "Example: My phone battery drains very fast "
                "and my phone gets hot while gaming..."
            ),
            height=120,
            key="problem_input"
        )

        submitted = st.form_submit_button(
            "🔎 Analyze My Problem",
            type="primary",
            use_container_width=True
        )

    if submitted:

        if problem.strip():

            try:

                # First use precise phrase matching, then semantic retrieval
                # to find possible meanings expressed with different wording.
                explicit_facts = extract_facts(problem, ASSERTIONS)
                negated_facts = set(extract_negated_facts(problem, ASSERTIONS))
                semantic_candidates = []
                semantic_error = False

                try:
                    from engine.semantic_matcher import search_similar_facts

                    semantic_results = search_similar_facts(
                        problem,
                        ASSERTIONS,
                        top_k=8,
                        min_score=0.42,
                    )
                    semantic_candidates = [
                        item["fact"]
                        for item in semantic_results
                        if item.get("fact")
                        and item["fact"] not in explicit_facts
                        and item["fact"] not in negated_facts
                    ]
                except Exception:
                    # Keep exact NLP available if the embedding model cannot load.
                    semantic_error = True

                st.session_state["problem_text"] = problem
                st.session_state["semantic_candidates"] = semantic_candidates
                st.session_state["semantic_review_pending"] = bool(semantic_candidates)
                st.session_state["semantic_error"] = semantic_error
                st.session_state["negated_facts"] = sorted(negated_facts)

                st.session_state["confirmed_facts"] = list(explicit_facts)
                st.session_state["followup_answers"] = {}
                st.session_state["diagnosis_result"] = None

                st.session_state["semantic_candidate_selection"] = []
                st.session_state["selected_facts_input"] = []

                st.session_state["diagnosis_ready"] = True

            except Exception as error:

                st.error("Problem analysis could not be completed.")
                st.code(str(error))

        else:

            st.warning(
                "Please describe your mobile problem first."
            )

    # --------------------------------------------------
    # AUTOMATIC FACT UNDERSTANDING + CONVERSATIONAL FOLLOW-UP
    # --------------------------------------------------

    if st.session_state["diagnosis_ready"]:

        # Semantic matches are suggestions only. The user confirms their meaning
        # before any suggested fact can enter the inference engine.
        if st.session_state.get("semantic_error"):
            st.warning(
                "Semantic language matching is currently unavailable. "
                "The system will still use direct phrase matching."
            )

        if st.session_state.get("semantic_review_pending"):
            fact_descriptions = {
                item["fact"]: item.get("description", item["fact"].replace("_", " ").title())
                for item in ASSERTIONS
                if isinstance(item, dict) and item.get("fact")
            }
            st.subheader("Did we understand your description?")
            st.write(
                "I found these possible meanings in your words. "
                "Select only the ones that correctly describe your problem."
            )
            selected_semantic_facts = st.multiselect(
                "Possible meanings",
                options=st.session_state.get("semantic_candidates", []),
                format_func=lambda fact: fact_descriptions.get(
                    fact, fact.replace("_", " ").title()
                ),
                key="semantic_candidate_selection",
            )
            confirm_col, skip_col = st.columns(2)
            with confirm_col:
                if st.button(
                    "Confirm selected meanings",
                    key="confirm_semantic_facts",
                    type="primary",
                    use_container_width=True,
                ):
                    current = set(st.session_state.get("confirmed_facts", []))
                    current.update(selected_semantic_facts)
                    st.session_state["confirmed_facts"] = sorted(current)
                    st.session_state["semantic_review_pending"] = False
                    st.rerun()
            with skip_col:
                if st.button(
                    "None of these",
                    key="skip_semantic_facts",
                    use_container_width=True,
                ):
                    st.session_state["semantic_review_pending"] = False
                    st.rerun()
            st.stop()

        confirmed_facts = st.session_state.get("confirmed_facts", [])
        negated = st.session_state.get("negated_facts", [])



        if not confirmed_facts:
            st.warning(
                "I could not confidently identify a direct symptom from your description. "
                "Please describe the problem with more details (what happens, when it happens, "
                "and what you notice). The system will not guess a diagnosis."
            )
        else:
            from engine.followup_engine import select_next_question

            followup_answers = st.session_state.setdefault("followup_answers", {})
            followup_limit = 5
            question = None
            if len(followup_answers) < followup_limit:
                question = select_next_question(
                    confirmed_facts=confirmed_facts,
                    answered_facts=followup_answers,
                    rules=RULES,
                    assertions=ASSERTIONS,
                    excluded_facts=negated,
                )

            if question:
                st.subheader(question["description"])
                answer = st.radio(
                    "Your answer:",
                    ["Yes", "No", "Not sure"],
                    horizontal=True,
                    key="followup_answer_" + question["fact"],
                )
                if st.button(
                    "Submit Answer",
                    key="submit_followup_" + question["fact"],
                    type="primary",
                    use_container_width=True,
                ):
                    followup_answers[question["fact"]] = answer.lower().replace(" ", "_")
                    if answer == "Yes" and question["fact"] not in confirmed_facts:
                        confirmed_facts.append(question["fact"])
                        st.session_state["confirmed_facts"] = confirmed_facts
                    st.session_state["followup_answers"] = followup_answers
                    st.session_state["diagnosis_result"] = None
                    st.rerun()
                st.caption(f"Follow-up question {len(followup_answers) + 1} of {followup_limit}")
            elif len(followup_answers) >= followup_limit:
                st.info("The follow-up limit has been reached.")
            else:
                st.info("No more relevant questions are available from the current rules.")

            if st.button(
                "🩺 Show Diagnosis",
                key="run_expert_diagnosis",
                type="primary",
                use_container_width=True,
                disabled=bool(question),
            ):
                from engine.diagnosis_pipeline import run_diagnosis
                all_facts = sorted(set(st.session_state["confirmed_facts"]))
                answers = st.session_state.get("followup_answers", {})
                blocked = {fact for fact, answer in answers.items() if answer in ("no", "not_sure")}
                blocked.update(st.session_state.get("negated_facts", []))
                pipeline_report = run_diagnosis(all_facts, RULES, blocked_facts=blocked)
                st.session_state["diagnosis_result"] = pipeline_report

            result = st.session_state.get("diagnosis_result")
            if result is not None:
                from engine.natural_language_report import build_user_report
                descriptions = {item["fact"]: item.get("description", item["fact"].replace("_", " ").title()) for item in ASSERTIONS}
                user_report = build_user_report(result, descriptions)
                st.subheader("🩺 Diagnosis")
                st.write(user_report["opening"])
                if user_report["conflicts"]:
                    st.warning("Please clarify:")
                    for conflict in user_report["conflicts"]:
                        st.write("• " + conflict)
                for index, cause in enumerate(user_report["causes"], 1):
                    st.markdown("**" + str(index) + ". " + cause["title"] + "**")
                    st.markdown("**Try:** " + cause["solution"])
                if not user_report["causes"] and result.get("partial_candidates"):
                    st.write("Possible areas to check (not confirmed diagnoses):")
                    for candidate in result["partial_candidates"]:
                        st.markdown("**" + str(candidate["conclusion"]).replace("_", " ").title() + "**")
                        st.markdown("**Try:** " + candidate["solution"])
                st.caption(user_report["closing"])
                with st.expander("Technical details (project demonstration)"):
                    st.write("Inference method: Forward Chaining and Backward Chaining.")
                    st.write(f"Backward verification: {result.get('verified', 0)} of {result.get('total', 0)} candidate(s).")
                    if result.get("trace"):
                        st.write("Rule trace:")
                        for step in result["trace"]:
                            st.write(f"Rule {step.get('rule_id')}: {step.get('conclusion', '').replace('_', ' ').title()}")
                            st.caption("Conditions: " + ", ".join(descriptions.get(f, f.replace("_", " ").title()) for f in step.get("conditions", [])))

        if st.session_state.get("diagnosis_result") is not None:
            st.caption("Suggestions are not a confirmed repair diagnosis.")


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

    st.write(f"**Knowledge Base:** {len(RULES)} IF-THEN rules and {len(ASSERTIONS)} facts.")

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





    # SEMANTIC NLP TESTING

    with st.expander(
        "🧠 Semantic NLP Testing",
        expanded=True
    ):

        st.write(
            "Test whether the semantic engine can identify "
            "mobile problems from different natural-language sentences."
        )

        st.info(
            "The multilingual embedding model compares sentence "
            "meaning with the 300 knowledge-base assertions."
        )

        sample_questions = [
            "My phone becomes very hot when I play games.",
            "My mobile battery loses power very quickly.",
            "I cannot connect my phone to the wireless network.",
            "My device takes too long to charge.",
            "My phone keeps restarting automatically."
        ]

        selected_sample = st.selectbox(
            "Choose a sample question:",
            ["Write my own question"] + sample_questions,
            key="semantic_sample"
        )

        default_question = (
            ""
            if selected_sample == "Write my own question"
            else selected_sample
        )

        question = st.text_area(
            "Enter a mobile problem in natural language:",
            value=default_question,
            placeholder=(
                "Example: My mobile gets extremely warm "
                "whenever I play games."
            ),
            height=100,
            key="semantic_question"
        )

        if st.button(
            "🔍 Find Similar Facts",
            key="run_semantic_test",
            use_container_width=True
        ):

            if not question.strip():

                st.warning(
                    "Please enter a mobile problem first."
                )

            else:

                try:

                    from engine.semantic_matcher import (
                        search_similar_facts
                    )

                    with st.spinner(
                        "Understanding your question and "
                        "searching the knowledge base..."
                    ):

                        semantic_results = search_similar_facts(
                            question,
                            ASSERTIONS,
                            top_k=10,
                            min_score=0.35
                        )

                    st.divider()

                    st.subheader(
                        "Semantic Matching Results"
                    )

                    if semantic_results:

                        st.success(
                            f"{len(semantic_results)} similar "
                            "fact(s) found."
                        )

                        for index, item in enumerate(
                            semantic_results,
                            start=1
                        ):

                            st.markdown(
                                f"**{index}. "
                                f"{item['fact'].replace('_', ' ').title()}**"
                            )

                            st.write(
                                item["description"]
                            )

                            st.caption(
                                f"Similarity Score: "
                                f"{item['score']:.4f}"
                            )

                            st.divider()

                    else:

                        st.warning(
                            "No sufficiently similar facts found. "
                            "Try explaining the problem differently."
                        )

                    st.caption(
                        "Note: Similarity scores measure semantic "
                        "closeness. They are not diagnosis confidence "
                        "or proof that a fact is true."
                    )

                except Exception as error:

                    st.error(
                        "Semantic NLP testing failed."
                    )

                    st.code(
                        str(error)
                    )

                    st.info(
                        "Check the Streamlit deployment logs "
                        "and model installation."
                    )

    

    # RULE QUALITY AUDIT

    with st.expander("🧭 Rule Quality Audit", expanded=True):
        from engine.rule_audit import audit_rules
        audit_report = audit_rules(RULES, ASSERTIONS)
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("Rules audited", audit_report["rule_count"])
        col_b.metric("Structural findings", audit_report["errors"])
        col_c.metric("Manual review flags", audit_report["reviews"])
        if not audit_report["findings"]:
            st.success("No findings from this automated audit.")
        else:
            for finding in audit_report["findings"]:
                if finding["severity"] == "error": st.error(f"{finding['kind']}: {finding['detail']}")
                else: st.warning(f"{finding['kind']}: {finding['detail']}")
        st.caption("Automated flags are screening aids, not proof of correctness. Safety findings require expert review.")

    
    # DEEP REASONING GRAPH AUDIT
    with st.expander("🧬 Reasoning Graph Reliability Audit", expanded=False):
        from engine.reliability_audit import audit_reliability
        reliability_report = audit_reliability(RULES, ASSERTIONS)
        ra1, ra2, ra3, ra4 = st.columns(4)
        ra1.metric("Conclusions", reliability_report["conclusion_count"])
        ra2.metric("Intermediate", len(reliability_report["intermediate_conclusions"]))
        ra3.metric("Terminal", len(reliability_report["terminal_conclusions"]))
        ra4.metric("Structural flags", reliability_report["errors"])
        if not reliability_report["findings"]:
            st.success("No structural issues detected by this graph audit.")
        else:
            for finding in reliability_report["findings"]:
                if finding["severity"] == "error": st.error(f"{finding['kind']}: {finding['detail']}")
                else: st.warning(f"{finding['kind']}: {finding['detail']}")
        with st.expander("Intermediate conclusions list"):
            st.write(reliability_report["intermediate_conclusions"])
        with st.expander("Terminal conclusion list"):
            st.write(reliability_report["terminal_conclusions"])
        st.caption("Graph screening is structural only; it does not prove a rule or repair recommendation is medically or technically correct.")

    
    # DIAGNOSTIC SCENARIO REGRESSION SUITE
    with st.expander("🧪 Diagnostic Scenario & False-Positive Testing", expanded=False):
        st.write("Regression scenarios check complete evidence, missing evidence, contradictory inputs, and safety-relevant rules.")
        from engine.scenario_testing import run_scenario_suite
        if st.button("Run Diagnostic Scenarios", key="run_diagnostic_scenarios"):
            scenario_report = run_scenario_suite(RULES)
            s1, s2, s3 = st.columns(3)
            s1.metric("Scenarios", scenario_report["total"])
            s2.metric("Passed", scenario_report["passed"])
            s3.metric("Failed", scenario_report["failed"])
            if scenario_report["failed"] == 0: st.success("All scenario expectations passed.")
            else: st.warning("Regression failures detected. Inspect the cases before trusting the related rules.")
            for case in scenario_report["results"]:
                if case["passed"]: st.success(f"{case['label']}: PASS")
                else: st.error(f"{case['label']}: FAIL")
                st.caption(f"Expected {case['expectation']} for {case['expected']}; conclusion matched: {case['matched']}")
                if case["contradictions"]: st.warning("Contradictions detected and passed into the pipeline safeguards.")

    # AUTOMATIC 100 RULE TESTING

    with st.expander(
        "🔬 Automatic Rule Testing"
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

            if test_report["passed"] == test_report["total"]:

                st.success(
                    f"All {test_report['total']} rules passed Forward and "
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
