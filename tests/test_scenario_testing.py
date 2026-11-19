from engine.scenario_testing import run_scenario_suite

def test_scenario_suite_passes_with_expected_rules():
    rules=[
        {"id":1,"conditions":["battery_drains_fast","phone_old"],"conclusion":"battery_health_low","solution":""},
        {"id":2,"conditions":["phone_not_charging","charger_damaged"],"conclusion":"charger_fault","solution":""},
        {"id":3,"conditions":["phone_overheating","heavy_gaming"],"conclusion":"gaming_causes_overheating","solution":""},
        {"id":4,"conditions":["wifi_not_working","airplane_mode_on"],"conclusion":"airplane_mode_blocks_wifi","solution":""},
        {"id":5,"conditions":["phone_wet","liquid_exposure"],"conclusion":"possible_liquid_damage","solution":""},
    ]
    report=run_scenario_suite(rules)
    assert report["total"] == 8
    assert report["passed"] == 8
    assert report["failed"] == 0

def test_scenario_runner_reports_a_regression():
    rules=[{"id":1,"conditions":["battery_drains_fast"],"conclusion":"battery_health_low","solution":""}]
    report=run_scenario_suite(rules,[{"id":"one","label":"must not trigger incomplete evidence","facts":["battery_drains_fast"],"expected":"battery_health_low","type":"must_not_match"}])
    assert report["failed"] == 1
    assert not report["results"][0]["passed"]
