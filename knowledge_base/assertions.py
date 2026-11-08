# MobileCare AI - Knowledge Base Assertions

ASSERTIONS = [
    {
        "id": 1,
        "fact": "battery_drains_fast",
        "description": "Phone battery drains unusually fast",
        "category": "Battery",
        "keywords": ["battery drain", "battery finishes quickly"]
    },
    {
        "id": 2,
        "fact": "phone_old",
        "description": "Phone is relatively old",
        "category": "Device",
        "keywords": ["old phone", "using phone for years"]
    },
    {
        "id": 3,
        "fact": "many_apps_running",
        "description": "Many applications are running in background",
        "category": "Performance",
        "keywords": ["many apps", "background apps"]
    },
    {
        "id": 4,
        "fact": "screen_brightness_high",
        "description": "Screen brightness is set very high",
        "category": "Display",
        "keywords": ["high brightness", "bright screen"]
    },
    {
        "id": 5,
        "fact": "phone_not_charging",
        "description": "Phone does not charge",
        "category": "Charging",
        "keywords": ["not charging", "charging problem"]
    },
    {
        "id": 6,
        "fact": "charger_damaged",
        "description": "Charging adapter is damaged",
        "category": "Charging",
        "keywords": ["damaged charger", "broken adapter"]
    },
    {
        "id": 7,
        "fact": "charging_port_dirty",
        "description": "Charging port contains dirt",
        "category": "Charging",
        "keywords": ["dirty charging port", "dust in port"]
    },
    {
        "id": 8,
        "fact": "charging_cable_damaged",
        "description": "Charging cable is damaged",
        "category": "Charging",
        "keywords": ["broken cable", "damaged charging wire"]
    },
    {
        "id": 9,
        "fact": "phone_overheating",
        "description": "Phone becomes unusually hot",
        "category": "Temperature",
        "keywords": ["phone heating", "mobile getting hot"]
    },
    {
        "id": 10,
        "fact": "heavy_gaming",
        "description": "User plays demanding mobile games",
        "category": "Usage",
        "keywords": ["heavy gaming", "playing games"]
    },
    {
        "id": 11,
        "fact": "wifi_not_working",
        "description": "Phone cannot connect to Wi-Fi",
        "category": "Network",
        "keywords": ["wifi not working", "cannot connect to wifi"]
    },
    {
        "id": 12,
        "fact": "airplane_mode_on",
        "description": "Airplane mode is enabled",
        "category": "Network",
        "keywords": ["airplane mode on", "flight mode enabled"]
    },
    {
        "id": 13,
        "fact": "router_not_working",
        "description": "Wi-Fi router is not working properly",
        "category": "Network",
        "keywords": ["router not working", "wifi router problem"]
    },
    {
        "id": 14,
        "fact": "mobile_data_not_working",
        "description": "Mobile internet data is not working",
        "category": "Network",
        "keywords": ["mobile data not working", "mobile internet problem"]
    },
    {
        "id": 15,
        "fact": "mobile_data_disabled",
        "description": "Mobile data is turned off",
        "category": "Network",
        "keywords": ["mobile data off", "data disabled"]
    },
    {
        "id": 16,
        "fact": "no_network_signal",
        "description": "Phone has no cellular network signal",
        "category": "Network",
        "keywords": ["no signal", "no network"]
    },
    {
        "id": 17,
        "fact": "bluetooth_not_working",
        "description": "Bluetooth connection is not working",
        "category": "Connectivity",
        "keywords": ["bluetooth not working", "bluetooth problem"]
    },
    {
        "id": 18,
        "fact": "bluetooth_disabled",
        "description": "Bluetooth is turned off",
        "category": "Connectivity",
        "keywords": ["bluetooth off", "bluetooth disabled"]
    },
    {
        "id": 19,
        "fact": "device_not_paired",
        "description": "Bluetooth device has not been paired",
        "category": "Connectivity",
        "keywords": ["device not paired", "not paired"]
    },
    {
        "id": 20,
        "fact": "phone_restarting",
        "description": "Phone restarts unexpectedly",
        "category": "Performance",
        "keywords": ["phone keeps restarting", "mobile restarts automatically"]
    },
    {
        "id": 21,
        "fact": "camera_not_working",
        "description": "Phone camera is not working",
        "category": "Camera",
        "keywords": ["camera not working", "camera problem"]
    },
    {
        "id": 22,
        "fact": "camera_permission_denied",
        "description": "Camera permission is denied",
        "category": "Camera",
        "keywords": ["camera permission denied", "camera access blocked"]
    },
    {
        "id": 23,
        "fact": "camera_lens_dirty",
        "description": "Camera lens is dirty",
        "category": "Camera",
        "keywords": ["dirty camera lens", "camera lens dirty"]
    },
    {
        "id": 24,
        "fact": "camera_app_crashing",
        "description": "Camera application crashes",
        "category": "Camera",
        "keywords": ["camera app crashing", "camera closes automatically"]
    },
    {
        "id": 25,
        "fact": "camera_cache_corrupted",
        "description": "Camera app cache may be corrupted",
        "category": "Camera",
        "keywords": ["camera cache problem", "camera app cache"]
    },
    {
        "id": 26,
        "fact": "speaker_no_sound",
        "description": "Phone speaker produces no sound",
        "category": "Audio",
        "keywords": ["speaker no sound", "no sound from speaker"]
    },
    {
        "id": 27,
        "fact": "media_volume_low",
        "description": "Media volume is too low",
        "category": "Audio",
        "keywords": ["low media volume", "media volume low"]
    },
    {
        "id": 28,
        "fact": "bluetooth_connected",
        "description": "Phone is connected to a Bluetooth audio device",
        "category": "Connectivity",
        "keywords": ["bluetooth connected", "connected to bluetooth"]
    },
    {
        "id": 29,
        "fact": "microphone_not_working",
        "description": "Phone microphone is not working",
        "category": "Audio",
        "keywords": ["microphone not working", "mic not working"]
    },
    {
        "id": 30,
        "fact": "microphone_permission_denied",
        "description": "Microphone permission is denied",
        "category": "Audio",
        "keywords": ["microphone permission denied", "mic access blocked"]
    },
    {
        "id": 31,
        "fact": "microphone_blocked",
        "description": "Microphone opening is blocked",
        "category": "Audio",
        "keywords": ["microphone blocked", "mic opening blocked"]
    },
    {
        "id": 32,
        "fact": "phone_storage_full",
        "description": "Phone storage is full",
        "category": "Storage",
        "keywords": ["storage full", "phone memory full"]
    },
    {
        "id": 33,
        "fact": "many_large_videos",
        "description": "Many large video files are stored on the phone",
        "category": "Storage",
        "keywords": ["large videos", "many videos taking space"]
    },
    {
        "id": 34,
        "fact": "apps_crashing",
        "description": "Applications close unexpectedly",
        "category": "Applications",
        "keywords": ["apps crashing", "apps closing automatically"]
    },
    {
        "id": 35,
        "fact": "app_version_outdated",
        "description": "Application version is outdated",
        "category": "Applications",
        "keywords": ["outdated app", "old app version"]
    },
    {
        "id": 36,
        "fact": "app_cache_corrupted",
        "description": "Application cache may be corrupted",
        "category": "Applications",
        "keywords": ["app cache corrupted", "app cache problem"]
    },
    {
        "id": 37,
        "fact": "software_update_pending",
        "description": "Android system update is available",
        "category": "Software",
        "keywords": ["software update pending", "system update available"]
    },
    {
        "id": 38,
        "fact": "phone_not_restarted_recently",
        "description": "Phone has not been restarted for a long time",
        "category": "Performance",
        "keywords": ["not restarted", "phone running for days"]
    },
    {
        "id": 39,
        "fact": "apps_not_installing",
        "description": "Applications cannot be installed",
        "category": "Applications",
        "keywords": ["apps not installing", "cannot install apps"]
    },
    {
        "id": 40,
        "fact": "internet_unavailable",
        "description": "Internet connection is unavailable",
        "category": "Network",
        "keywords": ["no internet", "internet unavailable"]
    },
    {
        "id": 41,
        "fact": "play_store_not_working",
        "description": "Google Play Store is not working",
        "category": "Applications",
        "keywords": ["play store not working", "play store problem"]
    },
    {
        "id": 42,
        "fact": "play_store_cache_corrupted",
        "description": "Google Play Store cache may be corrupted",
        "category": "Applications",
        "keywords": ["play store cache problem", "play store cache corrupted"]
    },
    {
        "id": 43,
        "fact": "notifications_not_received",
        "description": "Phone does not receive expected notifications",
        "category": "Notifications",
        "keywords": ["notifications not received", "no notifications"]
    },
    {
        "id": 44,
        "fact": "do_not_disturb_on",
        "description": "Do Not Disturb mode is enabled",
        "category": "Notifications",
        "keywords": ["do not disturb on", "dnd enabled"]
    },
    {
        "id": 45,
        "fact": "battery_saver_on",
        "description": "Battery Saver mode is enabled",
        "category": "Battery",
        "keywords": ["battery saver on", "power saving mode enabled"]
    },
    {
        "id": 46,
        "fact": "many_unused_apps",
        "description": "Many unused applications are installed",
        "category": "Storage",
        "keywords": ["unused apps", "too many installed apps"]
    },
    {
        "id": 47,
        "fact": "sim_not_detected",
        "description": "Phone does not detect the SIM card",
        "category": "Network",
        "keywords": ["sim not detected", "no sim card"]
    },
    {
        "id": 48,
        "fact": "sim_improperly_inserted",
        "description": "SIM card is not inserted correctly",
        "category": "Network",
        "keywords": ["sim inserted incorrectly", "sim not properly inserted"]
    },
    {
        "id": 49,
        "fact": "sim_card_damaged",
        "description": "SIM card may be physically damaged",
        "category": "Network",
        "keywords": ["damaged sim", "sim card broken"]
    },
    {
        "id": 50,
        "fact": "phone_no_sound",
        "description": "Phone produces no ringtone or system sound",
        "category": "Audio",
        "keywords": ["phone no sound", "no ringtone"]
}
]
