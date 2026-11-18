import unittest

from engine.nlp_engine import (
    extract_facts,
    extract_negated_facts,
    normalize_tokens,
)


ASSERTIONS = [
    {
        "fact": "phone_overheating",
        "description": "Phone becomes unusually hot",
        "keywords": ["phone heating", "mobile getting hot"],
    },
    {
        "fact": "battery_drains_fast",
        "description": "Battery drains unusually fast",
        "keywords": ["battery drain", "battery finishes quickly"],
    },
    {
        "fact": "phone_not_charging",
        "description": "Phone does not charge",
        "keywords": ["not charging", "charging problem"],
    },
    {
        "fact": "wifi_connected_no_internet",
        "description": "Wi-Fi is connected but internet is unavailable",
        "keywords": ["wifi connected no internet"],
    },
    {
        "fact": "no_network_signal",
        "description": "No mobile network signal",
        "keywords": ["no network signal"],
    },
]


class NLPExtractionTests(unittest.TestCase):

    def test_inflected_words_are_normalized(self):
        self.assertEqual(
            normalize_tokens("My phone gets hot and batteries are draining"),
            ["my", "phone", "get", "hot", "and", "battery", "are", "drain"],
        )

    def test_overheating_alias_is_detected(self):
        facts = extract_facts("My phone gets hot while gaming", ASSERTIONS)
        self.assertIn("phone_overheating", facts)

    def test_negated_overheating_is_not_extracted(self):
        problem = "My phone is not overheating"
        self.assertNotIn(
            "phone_overheating",
            extract_facts(problem, ASSERTIONS),
        )
        self.assertIn(
            "phone_overheating",
            extract_negated_facts(problem, ASSERTIONS),
        )

    def test_battery_drain_is_detected(self):
        facts = extract_facts("The battery drains very fast", ASSERTIONS)
        self.assertIn("battery_drains_fast", facts)

    def test_contrast_clause_does_not_inherit_previous_negation(self):
        problem = "My phone is not overheating but the battery drains fast"
        facts = extract_facts(problem, ASSERTIONS)
        self.assertNotIn("phone_overheating", facts)
        self.assertIn("battery_drains_fast", facts)

    def test_contraction_for_not_charging_is_detected(self):
        facts = extract_facts("My phone won't charge", ASSERTIONS)
        self.assertIn("phone_not_charging", facts)

    def test_wifi_connected_without_internet_is_detected(self):
        facts = extract_facts(
            "Wi-Fi is connected but no internet",
            ASSERTIONS,
        )
        self.assertIn("wifi_connected_no_internet", facts)

    def test_no_signal_is_detected_as_a_symptom(self):
        facts = extract_facts("There is no network signal", ASSERTIONS)
        self.assertIn("no_network_signal", facts)

    def test_empty_input_returns_no_facts(self):
        self.assertEqual(extract_facts("", ASSERTIONS), [])
        self.assertEqual(extract_negated_facts("", ASSERTIONS), [])


if __name__ == "__main__":
    unittest.main()
