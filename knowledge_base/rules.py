
# MobileCare AI - Knowledge Base
# Android Mobile Troubleshooting Rules

RULES = [
    {
        "id": 1,
        "conditions": ["battery_drains_fast", "phone_old"],
        "conclusion": "battery_health_low",
        "solution": "Check battery health. If battery condition is poor, replace it."
    },
    {
        "id": 2,
        "conditions": ["battery_drains_fast", "many_apps_running"],
        "conclusion": "background_apps_cause_drain",
        "solution": "Close unnecessary background apps."
    },
    {
        "id": 3,
        "conditions": ["battery_drains_fast", "screen_brightness_high"],
        "conclusion": "high_brightness_causes_drain",
        "solution": "Reduce screen brightness or enable adaptive brightness."
    },
    {
        "id": 4,
        "conditions": ["phone_not_charging", "charger_damaged"],
        "conclusion": "charger_fault",
        "solution": "Try a compatible working charger."
    },
    {
        "id": 5,
        "conditions": ["phone_not_charging", "charging_port_dirty"],
        "conclusion": "charging_port_blocked",
        "solution": "Inspect the charging port and have it safely cleaned."
    },
    {
        "id": 6,
        "conditions": ["phone_not_charging", "charging_cable_damaged"],
        "conclusion": "cable_fault",
        "solution": "Replace the damaged charging cable."
    },
    {
        "id": 7,
        "conditions": ["phone_overheating", "heavy_gaming"],
        "conclusion": "gaming_causes_overheating",
        "solution": "Take a break from gaming and allow the phone to cool."
    },
    {
        "id": 8,
        "conditions": ["phone_overheating", "phone_charging"],
        "conclusion": "charging_heat",
        "solution": "Avoid heavy phone use while charging."
    },
    {
        "id": 9,
        "conditions": ["phone_slow", "storage_full"],
        "conclusion": "low_storage_performance_issue",
        "solution": "Free up storage by removing unnecessary files and apps."
    },
    {
        "id": 10,
        "conditions": ["phone_slow", "many_apps_running"],
        "conclusion": "memory_overload",
        "solution": "Close unused applications and restart the phone."
    },
    {
        "id": 11,
        "conditions": ["wifi_not_working", "airplane_mode_on"],
        "conclusion": "airplane_mode_blocks_wifi",
        "solution": "Turn off Airplane Mode and check Wi-Fi again."
    },
    {
        "id": 12,
        "conditions": ["wifi_not_working", "router_not_working"],
        "conclusion": "router_connection_problem",
        "solution": "Restart the Wi-Fi router and reconnect."
    },
    {
        "id": 13,
        "conditions": ["mobile_data_not_working", "mobile_data_disabled"],
        "conclusion": "mobile_data_is_off",
        "solution": "Enable mobile data in phone settings."
    },
    {
        "id": 14,
        "conditions": ["mobile_data_not_working", "no_network_signal"],
        "conclusion": "network_coverage_problem",
        "solution": "Move to an area with better network coverage."
    },
    {
        "id": 15,
        "conditions": ["bluetooth_not_working", "bluetooth_disabled"],
        "conclusion": "bluetooth_is_off",
        "solution": "Enable Bluetooth and try connecting again."
    },
    {
        "id": 16,
        "conditions": ["bluetooth_not_working", "device_not_paired"],
        "conclusion": "bluetooth_pairing_problem",
        "solution": "Pair the Bluetooth device again."
    },
    {
        "id": 17,
        "conditions": ["phone_restarting", "system_update_pending"],
        "conclusion": "software_update_issue",
        "solution": "Install available system updates after backing up important data."
    },
    {
        "id": 18,
        "conditions": ["phone_restarting", "power_button_stuck"],
        "conclusion": "power_button_problem",
        "solution": "Check whether the power button is stuck or damaged."
    },
    {
        "id": 19,
        "conditions": ["touchscreen_not_working", "screen_protector_damaged"],
        "conclusion": "screen_protector_interference",
        "solution": "Inspect the screen protector and replace it if damaged."
    },
    {
        "id": 20,
        "conditions": ["touchscreen_not_working", "screen_wet"],
        "conclusion": "moisture_affecting_touchscreen",
        "solution": "Turn off the phone if safe, dry its exterior, and seek service if the issue continues."
    }
]
