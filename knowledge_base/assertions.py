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
    },
    {
        "id": 51,
        "fact": "phone_muted",
        "description": "Phone is in silent or muted mode",
        "category": "Audio",
        "keywords": ["phone muted", "silent mode"]
    },
    {
        "id": 52,
        "fact": "incoming_calls_not_received",
        "description": "Incoming calls are not being received",
        "category": "Calls",
        "keywords": ["incoming calls not received", "cannot receive calls"]
    },
    {
        "id": 53,
        "fact": "insufficient_balance",
        "description": "Mobile account has insufficient balance",
        "category": "Calls",
        "keywords": ["no balance", "insufficient balance"]
    },
    {
        "id": 54,
        "fact": "direct_sunlight",
        "description": "Phone is exposed to direct sunlight",
        "category": "Temperature",
        "keywords": ["direct sunlight", "phone in sunlight"]
    },
    {
        "id": 55,
        "fact": "thick_phone_case",
        "description": "Phone has a thick protective case",
        "category": "Device",
        "keywords": ["thick phone case", "heavy mobile cover"]
    },
    {
        "id": 56,
        "fact": "screen_flickering",
        "description": "Phone screen flickers repeatedly",
        "category": "Display",
        "keywords": ["screen flickering", "display blinking"]
    },
    {
        "id": 57,
        "fact": "low_screen_brightness",
        "description": "Screen brightness is set very low",
        "category": "Display",
        "keywords": ["low brightness", "screen too dim"]
    },
    {
        "id": 58,
        "fact": "screen_not_rotating",
        "description": "Screen does not rotate automatically",
        "category": "Display",
        "keywords": ["screen not rotating", "auto rotation problem"]
    },
    {
        "id": 59,
        "fact": "auto_rotate_disabled",
        "description": "Auto Rotate setting is disabled",
        "category": "Display",
        "keywords": ["auto rotate off", "rotation disabled"]
    },
    {
        "id": 60,
        "fact": "fingerprint_not_working",
        "description": "Fingerprint unlock is not working",
        "category": "Security",
        "keywords": ["fingerprint not working", "fingerprint unlock problem"]
    },
    {
        "id": 61,
        "fact": "fingerprint_sensor_dirty",
        "description": "Fingerprint sensor is dirty",
        "category": "Security",
        "keywords": ["dirty fingerprint sensor", "fingerprint sensor dirty"]
    },
    {
        "id": 62,
        "fact": "face_unlock_not_working",
        "description": "Face unlock feature is not working",
        "category": "Security",
        "keywords": ["face unlock not working", "face recognition problem"]
    },
    {
        "id": 63,
        "fact": "front_camera_dirty",
        "description": "Front camera area is dirty or obstructed",
        "category": "Camera",
        "keywords": ["front camera dirty", "selfie camera blocked"]
    },
    {
        "id": 64,
        "fact": "phone_boot_loop",
        "description": "Phone repeatedly restarts during startup",
        "category": "Software",
        "keywords": ["boot loop", "phone stuck restarting"]
    },
    {
        "id": 65,
        "fact": "recent_system_update",
        "description": "A system update was recently installed",
        "category": "Software",
        "keywords": ["recent system update", "updated phone recently"]
    },
    {
        "id": 66,
        "fact": "phone_not_turning_on",
        "description": "Phone does not turn on",
        "category": "Power",
        "keywords": ["phone not turning on", "mobile dead"]
    },
    {
        "id": 67,
        "fact": "battery_completely_empty",
        "description": "Battery charge is completely depleted",
        "category": "Battery",
        "keywords": ["battery empty", "battery completely dead"]
    },
    {
        "id": 68,
        "fact": "power_button_damaged",
        "description": "Power button is damaged",
        "category": "Hardware",
        "keywords": ["power button damaged", "broken power button"]
    },
    {
        "id": 69,
        "fact": "phone_freezing",
        "description": "Phone frequently freezes or becomes unresponsive",
        "category": "Performance",
        "keywords": ["phone freezing", "mobile hangs"]
    },
    {
        "id": 70,
        "fact": "storage_almost_full",
        "description": "Phone storage is almost full",
        "category": "Storage",
        "keywords": ["storage almost full", "low storage space"]
    },
    {
        "id": 71,
        "fact": "recent_app_installed",
        "description": "A new application was recently installed",
        "category": "Applications",
        "keywords": ["recent app installed", "new app installed"]
    },
    {
        "id": 72,
        "fact": "internet_slow",
        "description": "Internet connection speed is very slow",
        "category": "Network",
        "keywords": ["slow internet", "internet speed slow"]
    },
    {
        "id": 73,
        "fact": "weak_wifi_signal",
        "description": "Wi-Fi signal strength is weak",
        "category": "Network",
        "keywords": ["weak wifi signal", "wifi signal low"]
    },
    {
        "id": 74,
        "fact": "background_downloads",
        "description": "Files are downloading in the background",
        "category": "Network",
        "keywords": ["background downloads", "downloads running"]
    },
    {
        "id": 75,
        "fact": "gps_not_working",
        "description": "GPS location service is not working",
        "category": "Location",
        "keywords": ["gps not working", "location not accurate"]
    },
    {
        "id": 76,
        "fact": "location_disabled",
        "description": "Location services are disabled",
        "category": "Location",
        "keywords": ["location off", "gps disabled"]
    },
    {
        "id": 77,
        "fact": "location_permission_denied",
        "description": "Location permission is denied for an app",
        "category": "Location",
        "keywords": ["location permission denied", "app location access blocked"]
    },
    {
        "id": 78,
        "fact": "usb_connection_not_working",
        "description": "USB connection is not working",
        "category": "Connectivity",
        "keywords": ["usb not working", "usb connection problem"]
    },
    {
        "id": 79,
        "fact": "usb_cable_damaged",
        "description": "USB cable is damaged",
        "category": "Connectivity",
        "keywords": ["damaged usb cable", "broken usb wire"]
    },
    {
        "id": 80,
        "fact": "usb_debugging_required",
        "description": "A USB task requires USB debugging",
        "category": "Developer Settings",
        "keywords": ["usb debugging required", "enable usb debugging"]
    },
    {
        "id": 81,
        "fact": "phone_vibrating_unexpectedly",
        "description": "Phone vibrates unexpectedly",
        "category": "Hardware",
        "keywords": ["unexpected vibration", "phone vibrating randomly"]
    },
    {
        "id": 82,
        "fact": "notification_alerts_enabled",
        "description": "Apps have vibration alerts enabled",
        "category": "Notifications",
        "keywords": ["notification vibration", "vibration alerts"]
    },
    {
        "id": 83,
        "fact": "vibration_motor_fault",
        "description": "Phone vibration motor may be faulty",
        "category": "Hardware",
        "keywords": ["vibration motor problem", "vibration hardware fault"]
    },
    {
        "id": 84,
        "fact": "headphones_no_sound",
        "description": "Connected headphones produce no sound",
        "category": "Audio",
        "keywords": ["headphones no sound", "earphones not working"]
    },
    {
        "id": 85,
        "fact": "headphone_volume_low",
        "description": "Headphone media volume is low",
        "category": "Audio",
        "keywords": ["headphone volume low", "earphone sound low"]
    },
    {
        "id": 86,
        "fact": "headphones_not_connected",
        "description": "Headphones are not properly connected",
        "category": "Audio",
        "keywords": ["headphones not connected", "earphones disconnected"]
    },
    {
        "id": 87,
        "fact": "charging_slow",
        "description": "Phone charges more slowly than expected",
        "category": "Charging",
        "keywords": ["slow charging", "phone charging slowly"]
    },
    {
        "id": 88,
        "fact": "incompatible_charger",
        "description": "Charger may not support the phone's charging requirements",
        "category": "Charging",
        "keywords": ["incompatible charger", "wrong charger"]
    },
    {
        "id": 89,
        "fact": "phone_used_during_charging",
        "description": "Phone is being used heavily while charging",
        "category": "Charging",
        "keywords": ["using phone while charging", "gaming while charging"]
    },
    {
        "id": 90,
        "fact": "battery_swelling",
        "description": "Battery appears swollen",
        "category": "Battery Safety",
        "keywords": ["swollen battery", "battery bulging"]
    },
    {
        "id": 91,
        "fact": "back_cover_lifting",
        "description": "Phone back cover is lifting away from the body",
        "category": "Hardware",
        "keywords": ["back cover lifting", "phone back opening"]
    },
    {
        "id": 92,
        "fact": "phone_wet",
        "description": "Phone has become wet",
        "category": "Water Damage",
        "keywords": ["phone wet", "mobile got wet"]
    },
    {
        "id": 93,
        "fact": "liquid_exposure",
        "description": "Phone has been exposed to liquid",
        "category": "Water Damage",
        "keywords": ["liquid exposure", "water entered phone"]
    },
    {
        "id": 94,
        "fact": "screen_black",
        "description": "Phone screen remains black",
        "category": "Display",
        "keywords": ["black screen", "screen is black"]
    },
    {
        "id": 95,
        "fact": "phone_still_ringing",
        "description": "Phone still rings despite its black screen",
        "category": "Display",
        "keywords": ["phone rings but screen black", "black screen with sound"]
    },
    {
        "id": 96,
        "fact": "screen_cracked",
        "description": "Phone screen has visible cracks",
        "category": "Display",
        "keywords": ["cracked screen", "broken display glass"]
    },
    {
        "id": 97,
        "fact": "visible_display_damage",
        "description": "Display shows visible physical damage",
        "category": "Display",
        "keywords": ["display damaged", "screen physically damaged"]
    },
    {
        "id": 98,
        "fact": "battery_connection_loose",
        "description": "Battery connection may be loose",
        "category": "Hardware",
        "keywords": ["loose battery connection", "battery connector problem"]
    },
    {
        "id": 99,
        "fact": "too_many_home_screen_widgets",
        "description": "Many widgets are running on the home screen",
        "category": "Performance",
        "keywords": ["too many widgets", "home screen widgets"]
    },
    {
        "id": 100,
        "fact": "app_not_opening",
        "description": "An application does not open",
        "category": "Applications",
        "keywords": ["app not opening", "application won't open"]
    },
    {
        "id": 101,
        "fact": "app_data_corrupted",
        "description": "Application data may be corrupted",
        "category": "Applications",
        "keywords": ["app data corrupted", "application data problem"]
    },
    {
        "id": 102,
        "fact": "keyboard_not_working",
        "description": "Phone keyboard is not responding",
        "category": "Input",
        "keywords": ["keyboard not working", "mobile keyboard problem"]
    },
    {
        "id": 103,
        "fact": "keyboard_app_crashed",
        "description": "Keyboard application has crashed",
        "category": "Input",
        "keywords": ["keyboard app crashed", "keyboard keeps closing"]
    },
    {
        "id": 104,
        "fact": "phone_language_wrong",
        "description": "Phone displays an unwanted language",
        "category": "Settings",
        "keywords": ["wrong phone language", "mobile language changed"]
    },
    {
        "id": 105,
        "fact": "system_language_changed",
        "description": "System language setting has changed",
        "category": "Settings",
        "keywords": ["system language changed", "language setting changed"]
    },
    {
        "id": 106,
        "fact": "data_limit_reached",
        "description": "Mobile data usage limit has been reached",
        "category": "Network",
        "keywords": ["data limit reached", "mobile data limit exceeded"]
    },
    {
        "id": 107,
        "fact": "wifi_disconnects",
        "description": "Phone frequently disconnects from Wi-Fi",
        "category": "Network",
        "keywords": ["wifi keeps disconnecting", "wifi disconnects repeatedly"]
    },
    {
        "id": 108,
        "fact": "router_signal_weak",
        "description": "Router provides a weak Wi-Fi signal",
        "category": "Network",
        "keywords": ["router signal weak", "weak router coverage"]
    },
    {
        "id": 109,
        "fact": "bluetooth_disconnects",
        "description": "Bluetooth connection disconnects repeatedly",
        "category": "Connectivity",
        "keywords": ["bluetooth keeps disconnecting", "bluetooth connection drops"]
    },
    {
        "id": 110,
        "fact": "bluetooth_device_low_battery",
        "description": "Connected Bluetooth accessory has low battery",
        "category": "Connectivity",
        "keywords": ["bluetooth device low battery", "earbuds battery low"]
}
]
