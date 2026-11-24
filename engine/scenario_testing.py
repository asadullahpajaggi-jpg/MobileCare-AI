"""Scenario-based regression checks for the MobileCare AI diagnosis pipeline."""
from engine.diagnosis_pipeline import run_diagnosis

SCENARIOS = [
    {"id":"complete_battery","label":"Complete battery evidence","facts":["battery_drains_fast","phone_old"],"expected":"battery_health_low","type":"must_match"},
    {"id":"incomplete_battery","label":"Incomplete battery evidence","facts":["battery_drains_fast"],"expected":"battery_health_low","type":"must_not_match"},
    {"id":"complete_charger","label":"Damaged charger evidence","facts":["phone_not_charging","charger_damaged"],"expected":"charger_fault","type":"must_match"},
    {"id":"contradicted_charger","label":"Contradictory charging evidence","facts":["phone_not_charging","phone_charging","charger_damaged"],"expected":"charger_fault","type":"must_not_match"},
    {"id":"heat_gaming","label":"Overheating during gaming","facts":["phone_overheating","heavy_gaming"],"expected":"gaming_causes_overheating","type":"must_match"},
    {"id":"incomplete_wifi","label":"Incomplete Wi-Fi evidence","facts":["wifi_not_working"],"expected":"airplane_mode_blocks_wifi","type":"must_not_match"},
    {"id":"liquid_safety","label":"Liquid exposure reasoning","facts":["phone_wet","liquid_exposure"],"expected":"possible_liquid_damage","type":"must_match"},
    {"id":"conflict_network","label":"Conflicting Wi-Fi facts","facts":["wifi_not_working","wifi_working","airplane_mode_on"],"expected":"airplane_mode_blocks_wifi","type":"must_not_match"},

    # Stage 30 coverage-expansion regression scenarios
    {"id":"battery_not_holding","label":"Battery not holding charge","facts":["battery_drains_fast","phone_battery_not_holding_charge"],"expected":"battery_health_issue_possible","type":"must_match"},
    {"id":"unresponsive_power_button","label":"Unresponsive power button","facts":["phone_not_turning_on","phone_power_button_unresponsive"],"expected":"power_button_fault","type":"must_match"},
    {"id":"low_internal_storage","label":"Low internal storage with slow phone","facts":["phone_slow","phone_internal_storage_low"],"expected":"low_storage_performance_issue","type":"must_match"},
    {"id":"high_ram_usage","label":"High RAM usage with slow phone","facts":["phone_slow","phone_ram_usage_high"],"expected":"memory_overload","type":"must_match"},
    {"id":"app_freezing","label":"App freezing and crashing","facts":["apps_crashing","app_freezing"],"expected":"app_stability_issue_possible","type":"must_match"},
    {"id":"camera_permission_disabled","label":"Camera permission disabled","facts":["camera_not_working","camera_permission_disabled"],"expected":"camera_permission_problem","type":"must_match"},
    {"id":"camera_focus_failure","label":"Blurry camera with focus failure","facts":["phone_camera_blurry","camera_focus_not_working"],"expected":"camera_focus_issue","type":"must_match"},
    {"id":"mobile_apn_problem","label":"Mobile data APN problem","facts":["mobile_data_not_working","mobile_data_apn_incorrect"],"expected":"mobile_data_apn_issue","type":"must_match"},
    {"id":"wifi_password_problem","label":"Incorrect Wi-Fi password","facts":["wifi_not_working","wifi_password_incorrect"],"expected":"wifi_authentication_problem","type":"must_match"},
    {"id":"saved_wifi_problem","label":"Saved Wi-Fi configuration problem","facts":["wifi_not_working","wifi_saved_network_issue"],"expected":"saved_wifi_configuration_problem","type":"must_match"},
    {"id":"bluetooth_code_problem","label":"Bluetooth pairing code mismatch","facts":["bluetooth_not_working","bluetooth_pairing_code_mismatch"],"expected":"bluetooth_pairing_problem","type":"must_match"},
    {"id":"bluetooth_visibility_problem","label":"Bluetooth visibility disabled","facts":["bluetooth_not_working","bluetooth_visibility_disabled"],"expected":"bluetooth_visibility_problem","type":"must_match"},
    {"id":"gps_accuracy_problem","label":"Low GPS accuracy","facts":["gps_not_working","gps_accuracy_low"],"expected":"gps_accuracy_problem","type":"must_match"},
    {"id":"usb_port_dirty","label":"Dirty USB port","facts":["usb_connection_not_working","usb_port_dirty"],"expected":"usb_port_contact_problem","type":"must_match"},
    {"id":"ghost_touch","label":"Ghost touch","facts":["touchscreen_not_working","ghost_touch_detected"],"expected":"ghost_touch_issue","type":"must_match"},
    {"id":"call_forwarding","label":"Unexpected call forwarding","facts":["incoming_calls_not_received","call_forwarding_enabled"],"expected":"call_forwarding_setting_issue","type":"must_match"},
    {"id":"intermittent_charging_fact","label":"Intermittent charging connection","facts":["phone_not_charging","phone_charging_disconnects"],"expected":"intermittent_charging_connection","type":"must_match"},
    {"id":"hot_charger","label":"Overheating phone and charger","facts":["phone_overheating","charger_overheating"],"expected":"charging_adapter_heat_safety","type":"must_match"},
    {"id":"cloud_backup_disabled","label":"Cloud backup disabled","facts":["phone_backup_not_completed","cloud_backup_disabled"],"expected":"cloud_backup_disabled_issue","type":"must_match"},
    {"id":"backup_storage_full","label":"Insufficient backup storage","facts":["phone_backup_not_completed","backup_storage_insufficient"],"expected":"backup_storage_issue","type":"must_match"},
    {"id":"proximity_sensor_blocked","label":"Blocked proximity sensor","facts":["proximity_sensor_not_working","proximity_sensor_blocked"],"expected":"proximity_sensor_obstruction","type":"must_match"},
]

def run_scenario_suite(rules, scenarios=None):
    """Run fixed fact sets against the real pipeline and report expectations."""
    rows=[]
    for scenario in scenarios or SCENARIOS:
        report=run_diagnosis(scenario["facts"],rules)
        matched=scenario["expected"] in report["conclusions"]
        passed=(matched if scenario["type"]=="must_match" else not matched)
        rows.append({"id":scenario["id"],"label":scenario["label"],"expected":scenario["expected"],
                     "expectation":scenario["type"],"matched":matched,"passed":passed,
                     "contradictions":report["contradictions"],"status":"PASS" if passed else "FAIL"})
    return {"total":len(rows),"passed":sum(r["passed"] for r in rows),"failed":sum(not r["passed"] for r in rows),"results":rows}
