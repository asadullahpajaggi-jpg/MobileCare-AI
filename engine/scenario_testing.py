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
