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
    },
    {
        "id": 111,
        "fact": "phone_screen_timeout",
        "description": "Phone screen turns off too quickly.",
        "category": "display",
        "keywords": ["screen timeout", "screen turns off", "screen off quickly"]
    },
    {
        "id": 112,
        "fact": "screen_timeout_short",
        "description": "Screen timeout duration is set too short.",
        "category": "display",
        "keywords": ["short timeout", "timeout setting", "screen timeout duration"]
    },
    {
        "id": 113,
        "fact": "phone_not_receiving_sms",
        "description": "Phone is not receiving text messages.",
        "category": "network",
        "keywords": ["not receiving sms", "no text messages", "sms not received"]
    },
    {
        "id": 114,
        "fact": "sms_service_center_wrong",
        "description": "SMS service center number may be incorrect.",
        "category": "network",
        "keywords": ["sms service center", "message center number", "sms settings"]
    },
    {
        "id": 115,
        "fact": "sim_network_issue",
        "description": "SIM card has a possible network-related issue.",
        "category": "network",
        "keywords": ["sim network issue", "sim network problem", "sim signal issue"]
    },
    {
        "id": 116,
        "fact": "hotspot_not_working",
        "description": "Mobile hotspot is not working correctly.",
        "category": "network",
        "keywords": ["hotspot not working", "cannot share internet", "hotspot problem"]
    },
    {
        "id": 117,
        "fact": "hotspot_disabled",
        "description": "Mobile hotspot is turned off.",
        "category": "network",
        "keywords": ["hotspot disabled", "hotspot off", "portable hotspot off"]
    },
    {
        "id": 118,
        "fact": "connected_device_limit",
        "description": "Hotspot has reached its maximum connected device limit.",
        "category": "network",
        "keywords": ["device limit", "too many connected devices", "hotspot limit"]
    },
    {
        "id": 119,
        "fact": "large_download_files",
        "description": "Large downloaded files are consuming phone storage.",
        "category": "storage",
        "keywords": ["large downloads", "downloaded files", "downloads taking space"]
    },
    {
        "id": 120,
        "fact": "phone_restarts_during_gaming",
        "description": "Phone restarts while playing games.",
        "category": "performance",
        "keywords": ["restarts during gaming", "restart while gaming", "phone restarts in game"]
    },
    {
        "id": 121,
        "fact": "heavy_game_load",
        "description": "A demanding game is placing a heavy load on the phone.",
        "category": "performance",
        "keywords": ["heavy game", "demanding game", "high game load"]
    },
    {
        "id": 122,
        "fact": "phone_screen_dim",
        "description": "Phone screen appears unusually dim.",
        "category": "display",
        "keywords": ["screen dim", "display too dark", "screen brightness low"]
    },
    {
        "id": 123,
        "fact": "adaptive_brightness_enabled",
        "description": "Adaptive brightness is automatically adjusting screen brightness.",
        "category": "display",
        "keywords": ["adaptive brightness", "auto brightness", "automatic brightness"]
    },
    {
        "id": 124,
        "fact": "flashlight_not_working",
        "description": "Phone flashlight is not turning on.",
        "category": "hardware",
        "keywords": ["flashlight not working", "torch not working", "torch won't turn on"]
    },
    {
        "id": 125,
        "fact": "camera_in_use",
        "description": "Another application is currently using the camera.",
        "category": "camera",
        "keywords": ["camera in use", "camera occupied", "another app using camera"]
    },
    {
        "id": 126,
        "fact": "phone_not_detected_by_pc",
        "description": "Computer does not detect the connected phone.",
        "category": "connectivity",
        "keywords": ["phone not detected by pc", "computer cannot detect phone", "usb phone connection"]
    },
    {
        "id": 127,
        "fact": "usb_connection_mode_wrong",
        "description": "USB connection mode is not set to the required option.",
        "category": "connectivity",
        "keywords": ["usb mode wrong", "file transfer mode", "usb connection mode"]
    },
    {
        "id": 128,
        "fact": "pc_usb_port_fault",
        "description": "Computer USB port may be faulty.",
        "category": "connectivity",
        "keywords": ["pc usb port", "computer usb port faulty", "usb port problem"]
    },
    {
        "id": 129,
        "fact": "phone_not_updating",
        "description": "Phone cannot complete a system update.",
        "category": "software",
        "keywords": ["phone not updating", "system update failed", "update not installing"]
    },
    {
        "id": 130,
        "fact": "insufficient_storage",
        "description": "Available storage is insufficient for an operation.",
        "category": "storage",
        "keywords": ["insufficient storage", "not enough space", "storage required"]
    },
    {
        "id": 131,
        "fact": "app_notifications_delayed",
        "description": "Notifications from an application arrive late.",
        "category": "software",
        "keywords": ["delayed notifications", "notifications arrive late", "late app alerts"]
    },
    {
        "id": 132,
        "fact": "background_restriction_enabled",
        "description": "Background activity is restricted for an application.",
        "category": "software",
        "keywords": ["background restriction", "background activity restricted", "app background limit"]
    },
    {
        "id": 133,
        "fact": "phone_clock_wrong",
        "description": "Phone displays an incorrect date or time.",
        "category": "system",
        "keywords": ["wrong phone time", "incorrect clock", "wrong date and time"]
    },
    {
        "id": 134,
        "fact": "automatic_time_disabled",
        "description": "Automatic date and time setting is disabled.",
        "category": "system",
        "keywords": ["automatic time disabled", "auto date time off", "manual time setting"]
    },
    {
        "id": 135,
        "fact": "recycle_bin_full",
        "description": "Deleted files remain in the recycle bin and consume storage.",
        "category": "storage",
        "keywords": ["recycle bin full", "trash folder full", "deleted files taking space"]
    },
    {
        "id": 136,
        "fact": "phone_audio_distorted",
        "description": "Phone speaker audio sounds distorted or unclear.",
        "category": "audio",
        "keywords": ["distorted audio", "crackling sound", "unclear speaker sound"]
    },
    {
        "id": 137,
        "fact": "speaker_opening_blocked",
        "description": "Dust or debris may be blocking the speaker opening.",
        "category": "audio",
        "keywords": ["speaker blocked", "speaker opening dirty", "dust in speaker"]
    },
    {
        "id": 138,
        "fact": "screen_brightness_not_adjusting",
        "description": "Screen brightness does not change when adjusted.",
        "category": "display",
        "keywords": ["brightness not adjusting", "brightness not changing", "screen brightness stuck"]
    },
    {
        "id": 139,
        "fact": "brightness_slider_fault",
        "description": "Brightness slider or its control may not be responding.",
        "category": "display",
        "keywords": ["brightness slider problem", "slider not working", "brightness control stuck"]
    },
    {
        "id": 140,
        "fact": "phone_apps_show_ads",
        "description": "Unexpected advertisements appear on the phone.",
        "category": "security",
        "keywords": ["apps showing ads", "unexpected ads", "pop up advertisements"]
    },
    {
        "id": 141,
        "fact": "suspicious_app_installed",
        "description": "An application from an untrusted source may be installed.",
        "category": "security",
        "keywords": ["suspicious app", "unknown application", "untrusted app"]
    },
    {
        "id": 142,
        "fact": "phone_security_warning",
        "description": "Phone displays a security warning.",
        "category": "security",
        "keywords": ["security warning", "phone security alert", "security notification"]
    },
    {
        "id": 143,
        "fact": "unknown_app_source",
        "description": "An application was installed from an unknown source.",
        "category": "security",
        "keywords": ["unknown source", "unknown app source", "sideloaded application"]
    },
    {
        "id": 144,
        "fact": "phone_problem_persists",
        "description": "The phone problem continues after initial troubleshooting.",
        "category": "general",
        "keywords": ["problem persists", "problem continues", "issue still exists"]
    },
    {
        "id": 145,
        "fact": "basic_troubleshooting_failed",
        "description": "Basic troubleshooting steps did not resolve the problem.",
        "category": "general",
        "keywords": ["basic troubleshooting failed", "restart did not help", "basic fixes failed"]
    },
    {
        "id": 146,
        "fact": "phone_slow",
        "description": "Phone responds slowly to user actions.",
        "category": "performance",
        "keywords": ["phone slow", "mobile lagging", "slow response"]
    },
    {
        "id": 147,
        "fact": "storage_full",
        "description": "Phone storage has no sufficient free space.",
        "category": "storage",
        "keywords": ["storage full", "no storage space", "memory full"]
    },
    {
        "id": 148,
        "fact": "phone_charging",
        "description": "Phone is currently connected to a charger.",
        "category": "charging",
        "keywords": ["phone charging", "connected to charger", "charging now"]
    },
    {
        "id": 149,
        "fact": "power_button_stuck",
        "description": "Power button is physically stuck or continuously pressed.",
        "category": "hardware",
        "keywords": ["power button stuck", "stuck power key", "power button jammed"]
    },
    {
        "id": 150,
        "fact": "touchscreen_not_working",
        "description": "Touchscreen does not respond properly.",
        "category": "display",
        "keywords": ["touchscreen not working", "touch not responding", "screen touch problem"]
    },
    {
        "id": 151,
        "fact": "screen_protector_damaged",
        "description": "Screen protector is damaged or interfering with touch.",
        "category": "display",
        "keywords": ["damaged screen protector", "protector cracked", "screen guard damaged"]
    },
    {
        "id": 152,
        "fact": "screen_wet",
        "description": "Water or moisture is present on the screen surface.",
        "category": "display",
        "keywords": ["screen wet", "water on screen", "moisture on display"]
    },
    {
        "id": 153,
        "fact": "phone_battery_not_holding_charge",
        "description": "Battery loses charge quickly after charging.",
        "category": "battery",
        "keywords": ["battery not holding charge", "battery drains quickly", "short battery backup"]
    },
    {
        "id": 154,
        "fact": "battery_percentage_jumping",
        "description": "Battery percentage changes unexpectedly.",
        "category": "battery",
        "keywords": ["battery percentage jumping", "battery percentage changing", "incorrect battery level"]
    },
    {
        "id": 155,
        "fact": "phone_charging_disconnects",
        "description": "Charging repeatedly connects and disconnects.",
        "category": "charging",
        "keywords": ["charging disconnects", "charging keeps stopping", "charger connects disconnects"]
    },
    {
        "id": 156,
        "fact": "charging_icon_not_visible",
        "description": "Charging icon does not appear when charger is connected.",
        "category": "charging",
        "keywords": ["charging icon missing", "no charging symbol", "charging sign not showing"]
    },
    {
        "id": 157,
        "fact": "phone_power_button_unresponsive",
        "description": "Power button does not respond when pressed.",
        "category": "hardware",
        "keywords": ["power button not working", "power key unresponsive", "power button no response"]
    },
    {
        "id": 158,
        "fact": "phone_random_shutdown",
        "description": "Phone shuts down unexpectedly.",
        "category": "system",
        "keywords": ["random shutdown", "phone turns off itself", "unexpected shutdown"]
    },
    {
        "id": 159,
        "fact": "phone_booting_slowly",
        "description": "Phone takes unusually long to start.",
        "category": "system",
        "keywords": ["slow boot", "phone starts slowly", "long startup time"]
    },
    {
        "id": 160,
        "fact": "system_ui_crashing",
        "description": "Android system interface repeatedly stops responding.",
        "category": "software",
        "keywords": ["system ui crashing", "system interface stopped", "system ui not responding"]
    },
    {
        "id": 161,
        "fact": "app_freezing",
        "description": "An application becomes unresponsive during use.",
        "category": "software",
        "keywords": ["app freezing", "application not responding", "app hangs"]
    },
    {
        "id": 162,
        "fact": "phone_ram_usage_high",
        "description": "A large amount of RAM is being used.",
        "category": "performance",
        "keywords": ["high ram usage", "memory usage high", "ram almost full"]
    },
    {
        "id": 163,
        "fact": "phone_internal_storage_low",
        "description": "Very little internal storage space is available.",
        "category": "storage",
        "keywords": ["low internal storage", "internal memory low", "little free space"]
    },
    {
        "id": 164,
        "fact": "phone_sd_card_not_detected",
        "description": "Phone cannot detect the inserted memory card.",
        "category": "storage",
        "keywords": ["sd card not detected", "memory card missing", "phone cannot read sd card"]
    },
    {
        "id": 165,
        "fact": "phone_camera_blurry",
        "description": "Camera captures blurry or unclear photographs.",
        "category": "camera",
        "keywords": ["blurry camera", "photos out of focus", "camera image unclear"]
    },
    {
        "id": 166,
        "fact": "camera_permission_disabled",
        "description": "Camera access is disabled for an application.",
        "category": "camera",
        "keywords": ["camera access disabled", "camera permission off", "camera access blocked"]
    },
    {
        "id": 167,
        "fact": "phone_front_camera_not_working",
        "description": "Front-facing camera does not work correctly.",
        "category": "camera",
        "keywords": ["front camera not working", "selfie camera problem", "front camera failed"]
    },
    {
        "id": 168,
        "fact": "phone_earpiece_no_sound",
        "description": "No sound comes from the earpiece during calls.",
        "category": "audio",
        "keywords": ["earpiece no sound", "call speaker not working", "cannot hear during calls"]
    },
    {
        "id": 169,
        "fact": "phone_call_microphone_low",
        "description": "Voice sounds very quiet to the other person during calls.",
        "category": "audio",
        "keywords": ["low microphone volume", "voice too quiet on calls", "other person cannot hear clearly"]
    },
    {
        "id": 170,
        "fact": "phone_network_keeps_dropping",
        "description": "Mobile network connection repeatedly disconnects.",
        "category": "network",
        "keywords": ["network keeps dropping", "signal disconnects", "mobile network unstable"]
    },
    {
        "id": 171,
        "fact": "wifi_connected_no_internet",
        "description": "Phone is connected to Wi-Fi but cannot access the internet.",
        "category": "network",
        "keywords": ["wifi connected no internet", "connected without internet", "wifi has no internet"]
    },
    {
        "id": 172,
        "fact": "wifi_password_incorrect",
        "description": "The entered Wi-Fi password is incorrect.",
        "category": "network",
        "keywords": ["wrong wifi password", "incorrect wifi password", "wifi authentication failed"]
    },
    {
        "id": 173,
        "fact": "wifi_saved_network_issue",
        "description": "A saved Wi-Fi network configuration may be incorrect.",
        "category": "network",
        "keywords": ["saved wifi problem", "wifi configuration issue", "saved network not connecting"]
    },
    {
        "id": 174,
        "fact": "mobile_data_apn_incorrect",
        "description": "Mobile data APN settings may be incorrect.",
        "category": "network",
        "keywords": ["wrong apn", "apn settings problem", "mobile data apn"]
    },
    {
        "id": 175,
        "fact": "network_mode_incompatible",
        "description": "Selected network mode may not be supported in the current area.",
        "category": "network",
        "keywords": ["network mode problem", "4g not working", "preferred network type issue"]
    },
    {
        "id": 176,
        "fact": "sim_airplane_mode_conflict",
        "description": "Airplane mode is preventing mobile network connectivity.",
        "category": "network",
        "keywords": ["airplane mode network", "sim no signal airplane mode", "mobile signal airplane mode"]
    },
    {
        "id": 177,
        "fact": "bluetooth_pairing_code_mismatch",
        "description": "Bluetooth pairing fails because the pairing code does not match.",
        "category": "connectivity",
        "keywords": ["bluetooth code mismatch", "pairing code incorrect", "bluetooth pairing rejected"]
    },
    {
        "id": 178,
        "fact": "bluetooth_visibility_disabled",
        "description": "Phone is not discoverable to nearby Bluetooth devices.",
        "category": "connectivity",
        "keywords": ["bluetooth not discoverable", "device not visible", "bluetooth visibility off"]
    },
    {
        "id": 179,
        "fact": "bluetooth_cache_problem",
        "description": "Bluetooth system cache may be causing connection problems.",
        "category": "connectivity",
        "keywords": ["bluetooth cache", "bluetooth connection glitch", "bluetooth cache problem"]
    },
    {
        "id": 180,
        "fact": "gps_accuracy_low",
        "description": "GPS location accuracy is lower than expected.",
        "category": "location",
        "keywords": ["gps inaccurate", "wrong location", "location accuracy low"]
    },
    {
        "id": 181,
        "fact": "location_accuracy_mode_disabled",
        "description": "Enhanced location accuracy settings are disabled.",
        "category": "location",
        "keywords": ["location accuracy disabled", "improve location accuracy off", "gps accuracy setting"]
    },
    {
        "id": 182,
        "fact": "gps_signal_blocked",
        "description": "Buildings or surroundings may be blocking GPS signals.",
        "category": "location",
        "keywords": ["gps signal blocked", "gps weak indoors", "location signal blocked"]
    },
    {
        "id": 183,
        "fact": "usb_file_transfer_permission_missing",
        "description": "Required USB file transfer access has not been allowed.",
        "category": "connectivity",
        "keywords": ["usb permission missing", "file transfer permission", "usb access denied"]
    },
    {
        "id": 184,
        "fact": "usb_port_dirty",
        "description": "Dust or debris may be present inside the USB port.",
        "category": "hardware",
        "keywords": ["usb port dirty", "dust in charging port", "debris in usb port"]
    },
    {
        "id": 185,
        "fact": "usb_device_not_supported",
        "description": "Connected USB accessory may not be supported by the phone.",
        "category": "connectivity",
        "keywords": ["usb device unsupported", "accessory not supported", "usb compatibility issue"]
    },
    {
        "id": 186,
        "fact": "system_update_download_paused",
        "description": "System update download has been paused.",
        "category": "software",
        "keywords": ["update download paused", "system update stopped downloading", "update paused"]
    },
    {
        "id": 187,
        "fact": "system_update_installation_failed",
        "description": "Android system update installation has failed.",
        "category": "software",
        "keywords": ["update installation failed", "system update error", "update failed to install"]
    },
    {
        "id": 188,
        "fact": "phone_date_incorrect",
        "description": "Phone date is incorrect.",
        "category": "system",
        "keywords": ["wrong phone date", "incorrect date", "phone date incorrect"]
    },
    {
        "id": 189,
        "fact": "system_cache_accumulated",
        "description": "Temporary system files have accumulated.",
        "category": "system",
        "keywords": ["system cache", "temporary system files", "system cache accumulated"]
    },
    {
        "id": 190,
        "fact": "phone_accessibility_feature_enabled",
        "description": "An accessibility feature may be changing normal phone behavior.",
        "category": "system",
        "keywords": ["accessibility feature enabled", "accessibility settings", "unexpected accessibility behavior"]
    },
    {
        "id": 191,
        "fact": "screen_reader_enabled",
        "description": "Screen reader is enabled and may affect touch interaction.",
        "category": "accessibility",
        "keywords": ["screen reader on", "talkback enabled", "phone reads everything"]
    },
    {
        "id": 192,
        "fact": "magnification_enabled",
        "description": "Screen magnification feature is enabled.",
        "category": "accessibility",
        "keywords": ["screen magnification", "magnifier enabled", "zoomed phone screen"]
    },
    {
        "id": 193,
        "fact": "gesture_navigation_conflict",
        "description": "Navigation gestures may be conflicting with application controls.",
        "category": "system",
        "keywords": ["gesture navigation problem", "navigation gesture conflict", "back gesture issue"]
    },
    {
        "id": 194,
        "fact": "app_compatibility_issue",
        "description": "An application may not be compatible with the Android version.",
        "category": "software",
        "keywords": ["app compatibility issue", "app not compatible", "android version unsupported"]
    },
    {
        "id": 195,
        "fact": "app_permission_missing",
        "description": "An application does not have a required permission.",
        "category": "software",
        "keywords": ["app permission missing", "permission denied", "application access blocked"]
    },
    {
        "id": 196,
        "fact": "google_account_sync_disabled",
        "description": "Google account synchronization is disabled.",
        "category": "account",
        "keywords": ["google sync disabled", "account sync off", "sync not working"]
    },
    {
        "id": 197,
        "fact": "google_account_sign_in_failed",
        "description": "Phone cannot complete Google account sign-in.",
        "category": "account",
        "keywords": ["google sign in failed", "google account login problem", "cannot sign in google"]
    },
    {
        "id": 198,
        "fact": "play_store_account_issue",
        "description": "Google Play Store may have an account-related problem.",
        "category": "account",
        "keywords": ["play store account problem", "google account play store", "play store sign in issue"]
    },
    {
        "id": 199,
        "fact": "phone_date_time_mismatch",
        "description": "Phone date and time settings do not match the network time.",
        "category": "system",
        "keywords": ["date time mismatch", "incorrect network time", "phone time mismatch"]
    },
    {
        "id": 200,
        "fact": "phone_restart_required",
        "description": "A restart may be required to complete a system or application change.",
        "category": "system",
        "keywords": ["restart required", "phone needs restart", "pending restart"]
    },
    {
        "id": 201,
        "fact": "outgoing_calls_failing",
        "description": "Outgoing calls cannot be completed from the phone.",
        "category": "calling",
        "keywords": ["outgoing calls failing", "cannot make calls", "calls not going through"]
    },
    {
        "id": 202,
        "fact": "android_version_outdated",
        "description": "The installed Android version is outdated.",
        "category": "software",
        "keywords": ["old android version", "outdated android", "android version old"]
    },
    {
        "id": 203,
        "fact": "phone_security_patch_outdated",
        "description": "The phone is running an outdated security patch.",
        "category": "security",
        "keywords": ["old security patch", "security update outdated", "security patch old"]
    },
    {
        "id": 204,
        "fact": "developer_options_enabled",
        "description": "Android developer options are enabled.",
        "category": "system",
        "keywords": ["developer options enabled", "developer mode on", "developer settings"]
    },
    {
        "id": 205,
        "fact": "usb_debugging_enabled",
        "description": "USB debugging is enabled in developer options.",
        "category": "system",
        "keywords": ["usb debugging enabled", "debugging turned on", "android usb debugging"]
    },
    {
        "id": 206,
        "fact": "battery_saver_restricts_performance",
        "description": "Battery saver mode is limiting background or device performance.",
        "category": "battery",
        "keywords": ["battery saver performance", "power saving restrictions", "battery saver slows phone"]
    },
    {
        "id": 207,
        "fact": "extreme_power_saving_enabled",
        "description": "Extreme power saving mode is enabled.",
        "category": "battery",
        "keywords": ["extreme power saving", "ultra power saving", "maximum battery saving"]
    },
    {
        "id": 208,
        "fact": "battery_temperature_high",
        "description": "Battery temperature is higher than normal.",
        "category": "battery",
        "keywords": ["battery temperature high", "hot battery", "battery overheating"]
    },
    {
        "id": 209,
        "fact": "phone_temperature_normal",
        "description": "Phone temperature is within its normal operating range.",
        "category": "hardware",
        "keywords": ["normal phone temperature", "device temperature normal", "phone not hot"]
    },
    {
        "id": 210,
        "fact": "charging_port_loose",
        "description": "Charging cable connection feels loose in the phone port.",
        "category": "charging",
        "keywords": ["loose charging port", "charger connection loose", "cable moves in port"]
    },
    {
        "id": 211,
        "fact": "wireless_charging_not_supported",
        "description": "Phone model does not support wireless charging.",
        "category": "charging",
        "keywords": ["wireless charging unsupported", "phone has no wireless charging", "wireless charging compatibility"]
    },
    {
        "id": 212,
        "fact": "wireless_charging_not_working",
        "description": "Wireless charging is not functioning correctly.",
        "category": "charging",
        "keywords": ["wireless charging not working", "wireless charger problem", "phone not charging wirelessly"]
    },
    {
        "id": 213,
        "fact": "fast_charging_not_enabled",
        "description": "Fast charging option is disabled or unavailable.",
        "category": "charging",
        "keywords": ["fast charging disabled", "fast charge not enabled", "fast charging setting"]
    },
    {
        "id": 214,
        "fact": "charger_overheating",
        "description": "Charging adapter becomes unusually hot during use.",
        "category": "charging",
        "keywords": ["charger getting hot", "adapter overheating", "hot charging adapter"]
    },
    {
        "id": 215,
        "fact": "screen_auto_lock_disabled",
        "description": "Automatic screen locking is disabled or incorrectly configured.",
        "category": "display",
        "keywords": ["auto lock disabled", "screen not locking automatically", "automatic lock setting"]
    },
    {
        "id": 216,
        "fact": "screen_burn_in_visible",
        "description": "A persistent image or shadow is visible on the display.",
        "category": "display",
        "keywords": ["screen burn in", "display shadow", "image retention"]
    },
    {
        "id": 217,
        "fact": "display_color_mode_changed",
        "description": "Display color mode has been changed from the preferred setting.",
        "category": "display",
        "keywords": ["screen colors changed", "display color mode", "wrong screen colors"]
    },
    {
        "id": 218,
        "fact": "night_light_enabled",
        "description": "Night light or eye comfort mode is enabled.",
        "category": "display",
        "keywords": ["night light enabled", "eye comfort mode", "blue light filter"]
    },
    {
        "id": 219,
        "fact": "screen_refresh_rate_low",
        "description": "Display refresh rate is set to a lower option.",
        "category": "display",
        "keywords": ["low refresh rate", "screen refresh rate", "display feels less smooth"]
    },
    {
        "id": 220,
        "fact": "screen_resolution_changed",
        "description": "Display resolution has been changed from its normal setting.",
        "category": "display",
        "keywords": ["screen resolution changed", "wrong display resolution", "display resolution setting"]
    },
    {
        "id": 221,
        "fact": "proximity_sensor_blocked",
        "description": "Proximity sensor may be blocked by dirt or an accessory.",
        "category": "sensors",
        "keywords": ["proximity sensor blocked", "screen stays on during call", "sensor covered"]
    },
    {
        "id": 222,
        "fact": "proximity_sensor_not_working",
        "description": "Proximity sensor does not respond correctly.",
        "category": "sensors",
        "keywords": ["proximity sensor not working", "call screen sensor problem", "proximity detection failed"]
    },
    {
        "id": 223,
        "fact": "accelerometer_not_working",
        "description": "Accelerometer sensor may not be responding correctly.",
        "category": "sensors",
        "keywords": ["accelerometer problem", "motion sensor not working", "phone motion detection failed"]
    },
    {
        "id": 224,
        "fact": "gyroscope_not_working",
        "description": "Gyroscope sensor is not providing correct orientation data.",
        "category": "sensors",
        "keywords": ["gyroscope not working", "gyro sensor problem", "gyro calibration issue"]
    },
    {
        "id": 225,
        "fact": "compass_calibration_needed",
        "description": "Compass sensor may need calibration.",
        "category": "sensors",
        "keywords": ["compass inaccurate", "compass calibration", "wrong compass direction"]
    },
    {
        "id": 226,
        "fact": "fingerprint_enrollment_failed",
        "description": "Phone cannot register a new fingerprint successfully.",
        "category": "security",
        "keywords": ["fingerprint registration failed", "cannot add fingerprint", "fingerprint enrollment problem"]
    },
    {
        "id": 227,
        "fact": "face_unlock_lighting_poor",
        "description": "Poor lighting may prevent face unlock from recognizing the user.",
        "category": "security",
        "keywords": ["face unlock poor lighting", "face recognition in dark", "face unlock lighting issue"]
    },
    {
        "id": 228,
        "fact": "screen_lock_password_incorrect",
        "description": "The entered screen lock password or PIN is incorrect.",
        "category": "security",
        "keywords": ["wrong phone pin", "incorrect screen password", "wrong lock password"]
    },
    {
        "id": 229,
        "fact": "biometric_unlock_temporarily_locked",
        "description": "Biometric unlock is temporarily unavailable and requires the device PIN or password.",
        "category": "security",
        "keywords": ["fingerprint temporarily locked", "biometric locked", "use pin after restart"]
    },
    {
        "id": 230,
        "fact": "screen_lock_timeout_after_restart",
        "description": "Phone requires its primary PIN or password after restarting.",
        "category": "security",
        "keywords": ["pin required after restart", "password after reboot", "unlock after restart"]
    },
    {
        "id": 231,
        "fact": "app_auto_start_disabled",
        "description": "An application is prevented from starting automatically.",
        "category": "software",
        "keywords": ["app auto start disabled", "automatic startup blocked", "app does not start automatically"]
    },
    {
        "id": 232,
        "fact": "app_background_data_disabled",
        "description": "Background mobile data usage is disabled for an application.",
        "category": "network",
        "keywords": ["background data disabled", "app background internet blocked", "background data restriction"]
    },
    {
        "id": 233,
        "fact": "app_mobile_data_restricted",
        "description": "Mobile data access is restricted for an application.",
        "category": "network",
        "keywords": ["app mobile data blocked", "mobile data restricted", "application cannot use mobile data"]
    },
    {
        "id": 234,
        "fact": "app_storage_permission_denied",
        "description": "An application does not have permission to access storage.",
        "category": "software",
        "keywords": ["storage permission denied", "app cannot access files", "file access permission"]
    },
    {
        "id": 235,
        "fact": "app_camera_permission_denied",
        "description": "Camera permission is denied for a specific application.",
        "category": "camera",
        "keywords": ["app camera permission denied", "camera access not allowed", "application camera permission"]
    },
    {
        "id": 236,
        "fact": "app_microphone_permission_denied",
        "description": "Microphone permission is denied for a specific application.",
        "category": "audio",
        "keywords": ["app microphone permission", "microphone access denied", "app cannot use microphone"]
    },
    {
        "id": 237,
        "fact": "app_location_permission_denied",
        "description": "An application does not have permission to access location.",
        "category": "location",
        "keywords": ["app location permission denied", "location access blocked", "application cannot access location"]
    },
    {
        "id": 238,
        "fact": "app_notification_permission_denied",
        "description": "An application is not allowed to send notifications.",
        "category": "software",
        "keywords": ["app notification permission denied", "notifications permission off", "app alerts blocked"]
    },
    {
        "id": 239,
        "fact": "app_disabled_by_user",
        "description": "An application has been disabled in phone settings.",
        "category": "software",
        "keywords": ["app disabled", "application turned off", "disabled app"]
    },
    {
        "id": 240,
        "fact": "app_updates_pending",
        "description": "Updates are available for installed applications.",
        "category": "software",
        "keywords": ["app updates pending", "applications need updates", "apps outdated"]
    },
    {
        "id": 241,
        "fact": "app_installation_from_unknown_source_blocked",
        "description": "Android security settings block installation from an unknown source.",
        "category": "security",
        "keywords": ["unknown app installation blocked", "install unknown apps disabled", "apk installation blocked"]
    },
    {
        "id": 242,
        "fact": "google_play_protect_warning",
        "description": "Google Play Protect has displayed a security warning.",
        "category": "security",
        "keywords": ["play protect warning", "google security warning", "play protect detected app"]
    },
    {
        "id": 243,
        "fact": "phone_storage_usage_high",
        "description": "A large proportion of phone storage is currently occupied.",
        "category": "storage",
        "keywords": ["storage usage high", "phone memory almost full", "storage nearly full"]
    },
    {
        "id": 244,
        "fact": "duplicate_photos_present",
        "description": "Duplicate photographs are consuming additional storage.",
        "category": "storage",
        "keywords": ["duplicate photos", "same pictures repeated", "duplicate images"]
    },
    {
        "id": 245,
        "fact": "large_video_files_present",
        "description": "Large video files are occupying substantial storage.",
        "category": "storage",
        "keywords": ["large video files", "videos taking space", "big videos in storage"]
    },
    {
        "id": 246,
        "fact": "cloud_backup_disabled",
        "description": "Cloud backup is disabled for phone data.",
        "category": "backup",
        "keywords": ["cloud backup disabled", "phone backup off", "online backup turned off"]
    },
    {
        "id": 247,
        "fact": "backup_storage_insufficient",
        "description": "There is insufficient cloud storage to complete a backup.",
        "category": "backup",
        "keywords": ["backup storage full", "not enough cloud storage", "backup space insufficient"]
    },
    {
        "id": 248,
        "fact": "photo_backup_sync_paused",
        "description": "Photo backup or synchronization is paused.",
        "category": "backup",
        "keywords": ["photo backup paused", "photos not syncing", "gallery backup stopped"]
    },
    {
        "id": 249,
        "fact": "phone_backup_not_completed",
        "description": "The latest phone backup did not complete successfully.",
        "category": "backup",
        "keywords": ["backup failed", "phone backup incomplete", "backup not completed"]
    },
    {
        "id": 250,
        "fact": "cloud_account_storage_full",
        "description": "Cloud account storage has reached its available limit.",
        "category": "backup",
        "keywords": ["cloud storage full", "google storage full", "online storage limit reached"]
    },
    {
        "id": 251,
        "fact": "private_dns_misconfigured",
        "description": "Private DNS settings may be incorrectly configured.",
        "category": "network",
        "keywords": ["private dns problem", "private dns not connecting", "dns configuration error"]
    },
    {
        "id": 252,
        "fact": "vpn_connection_active",
        "description": "A VPN connection is active on the phone.",
        "category": "network",
        "keywords": ["vpn enabled", "vpn connected", "active vpn connection"]
    },
    {
        "id": 253,
        "fact": "vpn_server_unreachable",
        "description": "The configured VPN server cannot be reached.",
        "category": "network",
        "keywords": ["vpn server unreachable", "vpn connection failed", "vpn server offline"]
    },
    {
        "id": 254,
        "fact": "data_roaming_disabled",
        "description": "Data roaming is disabled while roaming data access is needed.",
        "category": "network",
        "keywords": ["data roaming disabled", "roaming data off", "mobile data while roaming"]
    },
    {
        "id": 255,
        "fact": "network_settings_changed",
        "description": "Network configuration was recently changed.",
        "category": "network",
        "keywords": ["network settings changed", "recent network configuration", "changed mobile network settings"]
    },
    {
        "id": 256,
        "fact": "wifi_frequency_incompatible",
        "description": "Phone may not support the Wi-Fi frequency used by the router.",
        "category": "network",
        "keywords": ["wifi frequency incompatible", "5ghz wifi unsupported", "wifi band compatibility"]
    },
    {
        "id": 257,
        "fact": "wifi_mac_randomization_enabled",
        "description": "Wi-Fi MAC randomization is enabled for the connected network.",
        "category": "network",
        "keywords": ["random mac address", "mac randomization", "wifi mac settings"]
    },
    {
        "id": 258,
        "fact": "router_access_control_blocking_phone",
        "description": "Router access control may be blocking the phone.",
        "category": "network",
        "keywords": ["router blocking phone", "mac filtering", "wifi access control blocked"]
    },
    {
        "id": 259,
        "fact": "phone_network_settings_corrupted",
        "description": "Saved network settings may be corrupted.",
        "category": "network",
        "keywords": ["network settings corrupted", "network configuration damaged", "saved network settings problem"]
    },
    {
        "id": 260,
        "fact": "phone_safe_mode_enabled",
        "description": "Phone is currently running in Android Safe Mode.",
        "category": "system",
        "keywords": ["safe mode enabled", "phone in safe mode", "android safe mode"]
    },
    {
        "id": 261,
        "fact": "phone_safe_mode_problem_resolved",
        "description": "A problem disappears when the phone runs in Safe Mode.",
        "category": "system",
        "keywords": ["problem gone in safe mode", "works in safe mode", "safe mode fixes issue"]
    },
    {
        "id": 262,
        "fact": "third_party_app_causing_issue",
        "description": "A third-party application may be causing a phone problem.",
        "category": "software",
        "keywords": ["third party app issue", "installed app causing problem", "external app conflict"]
    },
    {
        "id": 263,
        "fact": "recent_app_update",
        "description": "An application was recently updated before the problem appeared.",
        "category": "software",
        "keywords": ["recent app update", "problem after app update", "updated application"]
    },
    {
        "id": 264,
        "fact": "recent_system_settings_change",
        "description": "System settings were changed shortly before the problem started.",
        "category": "system",
        "keywords": ["recent settings change", "changed phone settings", "problem after settings change"]
    },
    {
        "id": 265,
        "fact": "factory_reset_recently_performed",
        "description": "Phone has recently undergone a factory reset.",
        "category": "system",
        "keywords": ["recent factory reset", "phone reset recently", "after factory reset"]
    },
    {
        "id": 266,
        "fact": "phone_data_not_backed_up",
        "description": "Important phone data has not been backed up.",
        "category": "backup",
        "keywords": ["data not backed up", "no phone backup", "important files not backed up"]
    },
    {
        "id": 267,
        "fact": "screen_touch_delay",
        "description": "Touchscreen responds with a noticeable delay.",
        "category": "display",
        "keywords": ["touch delay", "slow touchscreen response", "delayed touch response"]
    },
    {
        "id": 268,
        "fact": "ghost_touch_detected",
        "description": "Screen registers touches that the user did not make.",
        "category": "display",
        "keywords": ["ghost touch", "screen touches itself", "random screen touches"]
    },
    {
        "id": 269,
        "fact": "screen_dead_pixels_visible",
        "description": "One or more pixels on the display appear permanently defective.",
        "category": "display",
        "keywords": ["dead pixels", "black spots on screen", "display pixel defect"]
    },
    {
        "id": 270,
        "fact": "screen_color_tint_abnormal",
        "description": "Display has an unusual color tint.",
        "category": "display",
        "keywords": ["screen yellow tint", "display color tint", "abnormal screen colors"]
    },
    {
        "id": 271,
        "fact": "phone_water_damage_suspected",
        "description": "Phone may have internal damage following water exposure.",
        "category": "hardware",
        "keywords": ["water damage suspected", "phone damaged by water", "liquid damage symptoms"]
    },
    {
        "id": 272,
        "fact": "phone_dropped_recently",
        "description": "Phone was recently dropped or experienced physical impact.",
        "category": "hardware",
        "keywords": ["phone dropped", "mobile fell down", "recent physical impact"]
    },
    {
        "id": 273,
        "fact": "phone_frame_bent",
        "description": "Phone frame appears bent or physically deformed.",
        "category": "hardware",
        "keywords": ["bent phone frame", "mobile body bent", "phone physically deformed"]
    },
    {
        "id": 274,
        "fact": "camera_flash_not_working",
        "description": "Camera flash does not activate when taking photographs.",
        "category": "camera",
        "keywords": ["camera flash not working", "flash not turning on", "photo flash problem"]
    },
    {
        "id": 275,
        "fact": "camera_focus_not_working",
        "description": "Camera cannot focus properly on nearby or distant objects.",
        "category": "camera",
        "keywords": ["camera focus problem", "autofocus not working", "camera cannot focus"]
    },
    {
        "id": 276,
        "fact": "camera_storage_permission_missing",
        "description": "Camera application cannot save photographs because storage access is unavailable.",
        "category": "camera",
        "keywords": ["camera cannot save photos", "camera storage permission", "photos not saving"]
    },
    {
        "id": 277,
        "fact": "video_recording_stops",
        "description": "Video recording stops unexpectedly.",
        "category": "camera",
        "keywords": ["video recording stops", "camera stops recording", "video capture interrupted"]
    },
    {
        "id": 278,
        "fact": "speaker_volume_distortion_high",
        "description": "Speaker sound becomes distorted at high volume.",
        "category": "audio",
        "keywords": ["speaker distortion at high volume", "crackling at high volume", "speaker sounds bad loudly"]
    },
    {
        "id": 279,
        "fact": "headphone_jack_dirty",
        "description": "Dust or debris may be blocking the headphone jack.",
        "category": "audio",
        "keywords": ["dirty headphone jack", "dust in audio jack", "headphone port blocked"]
    },
    {
        "id": 280,
        "fact": "audio_balance_changed",
        "description": "Left and right audio balance settings have been changed.",
        "category": "audio",
        "keywords": ["audio balance changed", "left right sound imbalance", "sound balance setting"]
    },
    {
        "id": 281,
        "fact": "notification_sound_disabled",
        "description": "Notification sound is disabled in phone settings.",
        "category": "audio",
        "keywords": ["notification sound off", "no notification tone", "notification volume disabled"]
    },
    {
        "id": 282,
        "fact": "ringer_volume_low",
        "description": "Phone ringtone volume is set too low.",
        "category": "audio",
        "keywords": ["ringer volume low", "ringtone too quiet", "incoming call sound low"]
    },
    {
        "id": 283,
        "fact": "media_audio_output_wrong",
        "description": "Media sound is routed to an unintended audio output.",
        "category": "audio",
        "keywords": ["wrong audio output", "sound playing on wrong device", "audio output selected incorrectly"]
    },
    {
        "id": 284,
        "fact": "microphone_noise_cancellation_issue",
        "description": "Microphone noise cancellation may be affecting voice quality.",
        "category": "audio",
        "keywords": ["microphone noise cancellation", "voice noise issue", "call audio processing problem"]
    },
    {
        "id": 285,
        "fact": "call_forwarding_enabled",
        "description": "Incoming calls are being forwarded to another number.",
        "category": "calling",
        "keywords": ["call forwarding enabled", "calls forwarded", "incoming calls going elsewhere"]
    },
    {
        "id": 286,
        "fact": "call_barring_enabled",
        "description": "Call barring settings are restricting certain calls.",
        "category": "calling",
        "keywords": ["call barring enabled", "outgoing calls barred", "incoming calls barred"]
    },
    {
        "id": 287,
        "fact": "sim_pin_locked",
        "description": "SIM card is locked and requires its PIN.",
        "category": "calling",
        "keywords": ["sim pin locked", "sim requires pin", "sim card locked"]
    },
    {
        "id": 288,
        "fact": "sim_registration_failed",
        "description": "SIM card cannot register with the mobile network.",
        "category": "network",
        "keywords": ["sim registration failed", "not registered on network", "sim cannot register"]
    },
    {
        "id": 289,
        "fact": "phone_carrier_settings_outdated",
        "description": "Mobile carrier configuration may be outdated.",
        "category": "network",
        "keywords": ["carrier settings outdated", "operator configuration old", "carrier configuration problem"]
    },
    {
        "id": 290,
        "fact": "mobile_network_maintenance",
        "description": "Mobile network service may be temporarily unavailable due to maintenance.",
        "category": "network",
        "keywords": ["network maintenance", "operator service outage", "mobile network temporarily unavailable"]
    },
    {
        "id": 291,
        "fact": "phone_manufacturer_service_issue",
        "description": "A manufacturer-specific service or software component may be causing a problem.",
        "category": "system",
        "keywords": ["manufacturer service issue", "brand software problem", "phone manufacturer service"]
    },
    {
        "id": 292,
        "fact": "system_app_disabled",
        "description": "An important built-in Android system application has been disabled.",
        "category": "system",
        "keywords": ["system app disabled", "built in app disabled", "android system application turned off"]
    },
    {
        "id": 293,
        "fact": "phone_date_time_auto_sync_failed",
        "description": "Automatic date and time synchronization has failed.",
        "category": "system",
        "keywords": ["automatic time sync failed", "date time sync problem", "network time not syncing"]
    },
    {
        "id": 294,
        "fact": "phone_storage_permission_restricted",
        "description": "System settings are restricting storage access.",
        "category": "storage",
        "keywords": ["storage access restricted", "file access restricted", "storage permission limitation"]
    },
    {
        "id": 295,
        "fact": "phone_app_data_usage_high",
        "description": "An application is consuming unusually high mobile data.",
        "category": "network",
        "keywords": ["high app data usage", "application using too much data", "unexpected data consumption"]
    },
    {
        "id": 296,
        "fact": "phone_wifi_sleep_policy",
        "description": "Wi-Fi behavior is affected by a power or sleep-related setting.",
        "category": "network",
        "keywords": ["wifi sleep policy", "wifi disconnects during sleep", "wifi turns off screen locked"]
    },
    {
        "id": 297,
        "fact": "phone_system_resource_overload",
        "description": "Multiple active processes are placing excessive load on system resources.",
        "category": "performance",
        "keywords": ["system resource overload", "too many processes", "high system load"]
    },
    {
        "id": 298,
        "fact": "phone_hardware_diagnostic_needed",
        "description": "Further hardware testing is required to identify the fault.",
        "category": "hardware",
        "keywords": ["hardware diagnostic needed", "hardware test required", "device needs hardware inspection"]
    },
    {
        "id": 299,
        "fact": "phone_software_diagnostic_needed",
        "description": "Further software testing is required to identify the problem.",
        "category": "software",
        "keywords": ["software diagnostic needed", "software testing required", "system software inspection"]
    },
    {
        "id": 300,
        "fact": "professional_repair_recommended",
        "description": "The phone may require inspection or repair by a qualified technician.",
        "category": "general",
        "keywords": ["professional repair", "technician required", "mobile repair recommended"]
}
]
