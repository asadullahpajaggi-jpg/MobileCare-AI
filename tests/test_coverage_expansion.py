"""Regression tests for Stage 30 knowledge-base coverage expansion."""

import unittest

from engine.diagnosis_pipeline import run_diagnosis
from engine.nlp_engine import extract_facts
from knowledge_base.assertions import ASSERTIONS
from knowledge_base.rules import RULES


CASES = [
    ("My battery is not holding charge and it drains quickly.", ["battery_drains_fast", "phone_battery_not_holding_charge"], "battery_health_issue_possible"),
    ("My phone will not turn on and the power button gives no response.", ["phone_not_turning_on", "phone_power_button_unresponsive"], "power_button_fault"),
    ("My phone is slow and internal storage is low.", ["phone_slow", "phone_internal_storage_low"], "low_storage_performance_issue"),
    ("My phone is slow and RAM usage is high.", ["phone_slow", "phone_ram_usage_high"], "memory_overload"),
    ("Apps keep crashing and the app freezes.", ["apps_crashing", "app_freezing"], "app_stability_issue_possible"),
    ("The camera is not working because camera access is disabled.", ["camera_not_working", "camera_permission_disabled"], "camera_permission_problem"),
    ("My camera photos are blurry and autofocus is not working.", ["phone_camera_blurry", "camera_focus_not_working"], "camera_focus_issue"),
    ("Mobile data is not working and APN settings are wrong.", ["mobile_data_not_working", "mobile_data_apn_incorrect"], "mobile_data_apn_issue"),
    ("Wi-Fi is not working because the password is incorrect.", ["wifi_not_working", "wifi_password_incorrect"], "wifi_authentication_problem"),
    ("Wi-Fi is not working and the saved network configuration has a problem.", ["wifi_not_working", "wifi_saved_network_issue"], "saved_wifi_configuration_problem"),
    ("Bluetooth is not working because the pairing code is incorrect.", ["bluetooth_not_working", "bluetooth_pairing_code_mismatch"], "bluetooth_pairing_problem"),
    ("Bluetooth is not working and my phone is not discoverable.", ["bluetooth_not_working", "bluetooth_visibility_disabled"], "bluetooth_visibility_problem"),
    ("GPS is not working and location accuracy is low.", ["gps_not_working", "gps_accuracy_low"], "gps_accuracy_problem"),
    ("USB connection is not working and the USB port is dirty.", ["usb_connection_not_working", "usb_port_dirty"], "usb_port_contact_problem"),
    ("The touchscreen is not working properly and the screen touches itself.", ["touchscreen_not_working", "ghost_touch_detected"], "ghost_touch_issue"),
    ("Incoming calls are not received and calls are being forwarded elsewhere.", ["incoming_calls_not_received", "call_forwarding_enabled"], "call_forwarding_setting_issue"),
    ("My phone is not charging and charging keeps stopping.", ["phone_not_charging", "phone_charging_disconnects"], "intermittent_charging_connection"),
    ("My phone is overheating and the charging adapter is getting hot.", ["phone_overheating", "charger_overheating"], "charging_adapter_heat_safety"),
    ("My phone backup is not completed and cloud backup is disabled.", ["phone_backup_not_completed", "cloud_backup_disabled"], "cloud_backup_disabled_issue"),
    ("My phone backup is not completed because backup storage is full.", ["phone_backup_not_completed", "backup_storage_insufficient"], "backup_storage_issue"),
    ("The proximity sensor is not working and the sensor is blocked.", ["proximity_sensor_not_working", "proximity_sensor_blocked"], "proximity_sensor_obstruction"),
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
