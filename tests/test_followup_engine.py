import unittest

from engine.followup_engine import select_next_question


ASSERTIONS = [
    {"fact": "battery_drains_fast", "description": "Battery drains fast"},
    {"fact": "phone_old", "description": "Phone is old"},
    {"fact": "many_apps_running", "description": "Many apps are running"},
    {"fact": "screen_brightness_high", "description": "Screen brightness is high"},
    {"fact": "phone_overheating", "description": "Phone is overheating"},
    {"fact": "heavy_gaming", "description": "Heavy gaming is happening"},
]


RULES = [
    {
        "id": 1,
        "conditions": ["battery_drains_fast", "phone_old"],
        "conclusion": "battery_health_low",
        "solution": "Check battery health.",
    },
    {
        "id": 2,
        "conditions": ["battery_drains_fast", "many_apps_running"],
        "conclusion": "background_apps_cause_drain",
        "solution": "Close background apps.",
    },
    {
        "id": 3,
        "conditions": ["battery_drains_fast", "screen_brightness_high"],
        "conclusion": "high_brightness_causes_drain",
        "solution": "Reduce brightness.",
    },
    {
        "id": 4,
        "conditions": ["phone_overheating", "heavy_gaming"],
        "conclusion": "gaming_causes_overheating",
        "solution": "Take a break.",
    },
]


class FollowUpEngineTests(unittest.TestCase):

    def test_selects_a_missing_condition_from_a_relevant_rule(self):
        question = select_next_question(
            ["battery_drains_fast"], {}, RULES, ASSERTIONS
        )
        self.assertIsNotNone(question)
        self.assertEqual(question["fact"], "phone_old")

    def test_does_not_ask_about_unrelated_rules(self):
        question = select_next_question(
            ["phone_overheating"], {}, RULES, ASSERTIONS
        )
        self.assertEqual(question["fact"], "heavy_gaming")

    def test_skips_already_answered_and_negated_facts(self):
        question = select_next_question(
            ["battery_drains_fast"],
            {"phone_old": "no"},
            RULES,
            ASSERTIONS,
            excluded_facts=["many_apps_running"],
        )
        self.assertEqual(question["fact"], "screen_brightness_high")

    def test_returns_none_when_no_relevant_unknown_fact_remains(self):
        question = select_next_question(
            ["battery_drains_fast"],
            {
                "phone_old": "not_sure",
                "many_apps_running": "no",
                "screen_brightness_high": "yes",
            },
            RULES,
            ASSERTIONS,
        )
        self.assertIsNone(question)

    def test_does_not_continue_rule_when_required_fact_is_denied(self):
        question = select_next_question(
            ["battery_drains_fast"],
            {"phone_old": "no"},
            RULES, ASSERTIONS
        )
        self.assertEqual(question["fact"], "many_apps_running")\n\n    def test_does_not_create_questions_without_confirmed_symptoms(self):
        question = select_next_question(
            [], {}, RULES, ASSERTIONS
        )
        self.assertIsNone(question)


if __name__ == "__main__":
    unittest.main()
