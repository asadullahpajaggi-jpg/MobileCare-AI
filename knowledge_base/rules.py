
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
    }
]
