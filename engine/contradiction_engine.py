"""Detect explicitly conflicting symptom/settings observations conservatively."""
OPPOSITE_FACT_PAIRS = [
    ("phone_charging", "phone_not_charging"), ("airplane_mode_on", "airplane_mode_off"),
    ("mobile_data_disabled", "mobile_data_enabled"), ("bluetooth_disabled", "bluetooth_enabled"),
    ("phone_muted", "phone_unmuted"), ("wifi_not_working", "wifi_working"),
    ("phone_overheating", "phone_not_overheating"), ("screen_wet", "screen_dry"),
]

def detect_contradictions(facts):
    observed = set(facts or [])
    return [{"facts": [left, right], "message": "Conflicting observations supplied."}
             for left, right in OPPOSITE_FACT_PAIRS if left in observed and right in observed]

def remove_conflicted_facts(facts, conflicts):
    blocked = {fact for conflict in conflicts for fact in conflict["facts"]}
    return sorted(set(facts or []) - blocked)
