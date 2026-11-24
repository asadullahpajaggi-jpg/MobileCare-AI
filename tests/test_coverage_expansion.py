"""Regression tests for Stage 30 knowledge-base coverage expansion."""

import unittest

from engine.diagnosis_pipeline import run_diagnosis
from engine.nlp_engine import extract_facts
from knowledge_base.assertions import ASSERTIONS
from knowledge_base.rules import RULES


CASES = [
    ("Battery drains quickly and short battery backup.", ["battery_drains_fast", "phone_battery_not_holding_charge"], "battery_health_issue_possible"),
    ("Phone not turning on, but power key unresponsive.", ["phone_not_turning_on", "phone_power_button_unresponsive"], "power_button_fault"),
    ("Phone slow and low internal storage.", ["phone_slow", "phone_internal_storage_low"], "low_storage_performance_issue"),
    ("Phone slow and high RAM usage.", ["phone_slow", "phone_ram_usage_high"], "memory_overload"),
    ("Apps crashing and app freezing.", ["apps_crashing", "app_freezing"], "app_stability_issue_possible"),
    ("Camera not working, but camera access disabled.", ["camera_not_working", "camera_permission_disabled"], "camera_permission_problem"),
    ("Autofocus not working, but blurry camera.", ["phone_camera_blurry", "camera_focus_not_working"], "camera_focus_issue"),
    ("Mobile data not working, but wrong APN.", ["mobile_data_not_working", "mobile_data_apn_incorrect"], "mobile_data_apn_issue"),
    ("Wi-Fi not working, but incorrect Wi-Fi password.", ["wifi_not_working", "wifi_password_incorrect"], "wifi_authentication_problem"),
    ("Wi-Fi not working, but saved Wi-Fi problem.", ["wifi_not_working", "wifi_saved_network_issue"], "saved_wifi_configuration_problem"),
    ("Bluetooth problem, but pairing code incorrect.", ["bluetooth_not_working", "bluetooth_pairing_code_mismatch"], "bluetooth_pairing_problem"),
    ("Bluetooth connection problem, but device not visible.", ["bluetooth_not_working", "bluetooth_visibility_disabled"], "bluetooth_visibility_problem"),
    ("GPS not working, but GPS inaccurate.", ["gps_not_working", "gps_accuracy_low"], "gps_accuracy_problem"),
    ("USB not working, but USB port dirty.", ["usb_connection_not_working", "usb_port_dirty"], "usb_port_contact_problem"),
    ("Touchscreen not working, but ghost touch.", ["touchscreen_not_working", "ghost_touch_detected"], "ghost_touch_issue"),
    ("Incoming calls not received, but call forwarding enabled.", ["incoming_calls_not_received", "call_forwarding_enabled"], "call_forwarding_setting_issue"),
    ("Phone not charging, but charger connects and disconnects.", ["phone_not_charging", "phone_charging_disconnects"], "intermittent_charging_connection"),
    ("Phone heating, but charger getting hot.", ["phone_overheating", "charger_overheating"], "charging_adapter_heat_safety"),
    ("Backup not completed, but cloud backup disabled.", ["phone_backup_not_completed", "cloud_backup_disabled"], "cloud_backup_disabled_issue"),
    ("Backup not completed, but backup space insufficient.", ["phone_backup_not_completed", "backup_storage_insufficient"], "backup_storage_issue"),
    ("Proximity sensor not working, but proximity sensor blocked.", ["proximity_sensor_not_working", "proximity_sensor_blocked"], "proximity_sensor_obstruction"),
]


class CoverageExpansionTests(unittest.TestCase):
    def test_natural_language_extracts_expected_facts_and_diagnoses(self):
        for problem, expected_facts, expected_conclusion in CASES:
            with self.subTest(problem=problem):
                facts = extract_facts(problem, ASSERTIONS)
                self.assertTrue(
                    set(expected_facts).issubset(set(facts)),
                    msg=f"Missing facts: {set(expected_facts) - set(facts)}; extracted: {facts}",
                )
                report = run_diagnosis(facts, RULES)
                self.assertIn(expected_conclusion, report["conclusions"])


if __name__ == "__main__":
    unittest.main()
