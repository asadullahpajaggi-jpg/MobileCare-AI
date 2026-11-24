
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
        "conditions": ["phone_restarting", "software_update_pending"],
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
    },
    {
        "id": 21,
        "conditions": ["camera_not_working", "camera_permission_denied"],
        "conclusion": "camera_permission_problem",
        "solution": "Allow camera permission in app settings."
    },
    {
        "id": 22,
        "conditions": ["camera_not_working", "camera_lens_dirty"],
        "conclusion": "dirty_camera_lens",
        "solution": "Clean the camera lens gently with a soft microfiber cloth."
    },
    {
        "id": 23,
        "conditions": ["camera_app_crashing", "camera_cache_corrupted"],
        "conclusion": "camera_cache_problem",
        "solution": "Clear the camera app cache and restart the app."
    },
    {
        "id": 24,
        "conditions": ["speaker_no_sound", "media_volume_low"],
        "conclusion": "low_media_volume",
        "solution": "Increase media volume using the volume buttons."
    },
    {
        "id": 25,
        "conditions": ["speaker_no_sound", "bluetooth_connected"],
        "conclusion": "audio_routed_to_bluetooth",
        "solution": "Disconnect Bluetooth and test the phone speaker."
    },
    {
        "id": 26,
        "conditions": ["microphone_not_working", "microphone_permission_denied"],
        "conclusion": "microphone_permission_problem",
        "solution": "Allow microphone permission for the affected app."
    },
    {
        "id": 27,
        "conditions": ["microphone_not_working", "microphone_blocked"],
        "conclusion": "microphone_obstruction",
        "solution": "Check that the microphone opening is not blocked."
    },
    {
        "id": 28,
        "conditions": ["phone_storage_full", "many_large_videos"],
        "conclusion": "videos_using_storage",
        "solution": "Back up and remove unnecessary large videos."
    },
    {
        "id": 29,
        "conditions": ["apps_crashing", "app_version_outdated"],
        "conclusion": "outdated_app_problem",
        "solution": "Update the affected application."
    },
    {
        "id": 30,
        "conditions": ["apps_crashing", "app_cache_corrupted"],
        "conclusion": "app_cache_problem",
        "solution": "Clear the affected app cache and reopen it."
    },
    {
        "id": 31,
        "conditions": ["phone_slow", "software_update_pending"],
        "conclusion": "outdated_system",
        "solution": "Check for and install available Android system updates."
    },
    {
        "id": 32,
        "conditions": ["phone_slow", "phone_not_restarted_recently"],
        "conclusion": "temporary_system_load",
        "solution": "Restart the phone and check its performance."
    },
    {
        "id": 33,
        "conditions": ["apps_not_installing", "storage_full"],
        "conclusion": "insufficient_installation_space",
        "solution": "Free up storage space before installing the app."
    },
    {
        "id": 34,
        "conditions": ["apps_not_installing", "internet_unavailable"],
        "conclusion": "download_connection_problem",
        "solution": "Connect to a stable internet connection and retry."
    },
    {
        "id": 35,
        "conditions": ["play_store_not_working", "play_store_cache_corrupted"],
        "conclusion": "play_store_cache_problem",
        "solution": "Clear Google Play Store cache and reopen it."
    },
    {
        "id": 36,
        "conditions": ["notifications_not_received", "do_not_disturb_on"],
        "conclusion": "notifications_silenced",
        "solution": "Turn off Do Not Disturb or adjust its exceptions."
    },
    {
        "id": 37,
        "conditions": ["notifications_not_received", "battery_saver_on"],
        "conclusion": "battery_saver_restricting_notifications",
        "solution": "Check battery optimization settings for the affected app."
    },
    {
        "id": 38,
        "conditions": ["phone_storage_full", "many_unused_apps"],
        "conclusion": "unused_apps_using_storage",
        "solution": "Uninstall applications you no longer use."
    },
    {
        "id": 39,
        "conditions": ["sim_not_detected", "sim_improperly_inserted"],
        "conclusion": "sim_insertion_problem",
        "solution": "Power off the phone and carefully reinsert the SIM card."
    },
    {
        "id": 40,
        "conditions": ["sim_not_detected", "sim_card_damaged"],
        "conclusion": "sim_card_fault",
        "solution": "Test the SIM in another compatible phone or contact your network provider."
    },
    {
        "id": 41,
        "conditions": ["phone_no_sound", "phone_muted"],
        "conclusion": "phone_is_muted",
        "solution": "Turn off Silent Mode and increase the ringtone volume."
    },
    {
        "id": 42,
        "conditions": ["incoming_calls_not_received", "do_not_disturb_on"],
        "conclusion": "calls_silenced_by_dnd",
        "solution": "Check Do Not Disturb settings and allowed callers."
    },
    {
        "id": 43,
        "conditions": ["outgoing_calls_failing", "insufficient_balance"],
        "conclusion": "insufficient_call_balance",
        "solution": "Check your mobile balance or active calling package."
    },
    {
        "id": 44,
        "conditions": ["phone_overheating", "direct_sunlight"],
        "conclusion": "sunlight_causes_overheating",
        "solution": "Move the phone away from direct sunlight and let it cool."
    },
    {
        "id": 45,
        "conditions": ["phone_overheating", "thick_phone_case"],
        "conclusion": "case_restricts_heat_dissipation",
        "solution": "Remove the case temporarily and check whether the phone cools down."
    },
    {
        "id": 46,
        "conditions": ["screen_flickering", "low_screen_brightness"],
        "conclusion": "low_brightness_flickering",
        "solution": "Increase brightness and check whether flickering continues."
    },
    {
        "id": 47,
        "conditions": ["screen_not_rotating", "auto_rotate_disabled"],
        "conclusion": "auto_rotate_is_off",
        "solution": "Enable Auto Rotate from Quick Settings."
    },
    {
        "id": 48,
        "conditions": ["fingerprint_not_working", "fingerprint_sensor_dirty"],
        "conclusion": "dirty_fingerprint_sensor",
        "solution": "Gently clean the fingerprint sensor and try again."
    },
    {
        "id": 49,
        "conditions": ["face_unlock_not_working", "front_camera_dirty"],
        "conclusion": "front_camera_obstructed",
        "solution": "Clean the front camera area and try face unlock again."
    },
    {
        "id": 50,
        "conditions": ["phone_boot_loop", "recent_system_update"],
        "conclusion": "possible_update_boot_problem",
        "solution": "Allow the phone time to restart. If the boot loop continues, seek authorized service support."
    },
    {
        "id": 51,
        "conditions": ["phone_not_turning_on", "battery_completely_empty"],
        "conclusion": "battery_depleted",
        "solution": "Charge the phone with a compatible charger and wait before turning it on."
    },
    {
        "id": 52,
        "conditions": ["phone_not_turning_on", "power_button_damaged"],
        "conclusion": "power_button_fault",
        "solution": "Have the power button inspected by a qualified technician."
    },
    {
        "id": 53,
        "conditions": ["phone_freezing", "storage_almost_full"],
        "conclusion": "storage_pressure",
        "solution": "Free up storage space and restart the phone."
    },
    {
        "id": 54,
        "conditions": ["phone_freezing", "recent_app_installed"],
        "conclusion": "possible_app_conflict",
        "solution": "Uninstall the recently installed app and check whether freezing stops."
    },
    {
        "id": 55,
        "conditions": ["internet_slow", "weak_wifi_signal"],
        "conclusion": "weak_wifi_connection",
        "solution": "Move closer to the router and check the connection."
    },
    {
        "id": 56,
        "conditions": ["internet_slow", "background_downloads"],
        "conclusion": "bandwidth_used_by_downloads",
        "solution": "Pause unnecessary downloads and test internet speed again."
    },
    {
        "id": 57,
        "conditions": ["gps_not_working", "location_disabled"],
        "conclusion": "location_service_is_off",
        "solution": "Enable Location services in Android settings."
    },
    {
        "id": 58,
        "conditions": ["gps_not_working", "location_permission_denied"],
        "conclusion": "gps_permission_problem",
        "solution": "Allow location permission for the affected app."
    },
    {
        "id": 59,
        "conditions": ["usb_connection_not_working", "usb_cable_damaged"],
        "conclusion": "usb_cable_fault",
        "solution": "Try a compatible USB cable that is known to work."
    },
    {
        "id": 60,
        "conditions": ["usb_connection_not_working", "usb_debugging_required"],
        "conclusion": "usb_debugging_disabled",
        "solution": "If the task requires USB debugging, enable it in Developer Options."
    },
    {
        "id": 61,
        "conditions": ["phone_vibrating_unexpectedly", "notification_alerts_enabled"],
        "conclusion": "notification_vibration",
        "solution": "Check notification settings and disable unnecessary vibration alerts."
    },
    {
        "id": 62,
        "conditions": ["phone_vibrating_unexpectedly", "vibration_motor_fault"],
        "conclusion": "possible_vibration_motor_fault",
        "solution": "If vibration continues without notifications, seek technician inspection."
    },
    {
        "id": 63,
        "conditions": ["headphones_no_sound", "headphone_volume_low"],
        "conclusion": "headphone_volume_problem",
        "solution": "Increase media volume while headphones are connected."
    },
    {
        "id": 64,
        "conditions": ["headphones_no_sound", "headphones_not_connected"],
        "conclusion": "headphone_connection_problem",
        "solution": "Reconnect the headphones and check the connection."
    },
    {
        "id": 65,
        "conditions": ["charging_slow", "incompatible_charger"],
        "conclusion": "charger_power_insufficient",
        "solution": "Use a compatible charger that supports your phone's charging requirements."
    },
    {
        "id": 66,
        "conditions": ["charging_slow", "phone_used_during_charging"],
        "conclusion": "phone_usage_slows_charging",
        "solution": "Avoid gaming or heavy tasks while charging."
    },
    {
        "id": 67,
        "conditions": ["battery_swelling", "back_cover_lifting"],
        "conclusion": "possible_swollen_battery",
        "solution": "Stop using and charging the phone. Do not press or puncture it. Seek professional battery replacement."
    },
    {
        "id": 68,
        "conditions": ["phone_wet", "liquid_exposure"],
        "conclusion": "possible_liquid_damage",
        "solution": "Power off the phone if safe. Do not charge it or use heat. Seek professional inspection."
    },
    {
        "id": 69,
        "conditions": ["screen_black", "phone_still_ringing"],
        "conclusion": "display_problem_possible",
        "solution": "The phone may be running despite a black screen. Seek display inspection if restarting does not help."
    },
    {
        "id": 70,
        "conditions": ["screen_cracked", "visible_display_damage"],
        "conclusion": "physical_screen_damage",
        "solution": "Protect the damaged screen from moisture and arrange professional screen repair."
    },
    {
        "id": 71,
        "conditions": ["phone_restarting", "battery_connection_loose"],
        "conclusion": "possible_battery_connection_fault",
        "solution": "Have the battery connection inspected by a qualified technician."
    },
    {
        "id": 72,
        "conditions": ["phone_slow", "too_many_home_screen_widgets"],
        "conclusion": "excessive_widget_load",
        "solution": "Remove unnecessary widgets and check phone performance."
    },
    {
        "id": 73,
        "conditions": ["app_not_opening", "app_data_corrupted"],
        "conclusion": "app_data_problem",
        "solution": "Back up important app data if possible, then clear app data or reinstall the app."
    },
    {
        "id": 74,
        "conditions": ["keyboard_not_working", "keyboard_app_crashed"],
        "conclusion": "keyboard_app_problem",
        "solution": "Restart the phone and update the keyboard application."
    },
    {
        "id": 75,
        "conditions": ["phone_language_wrong", "system_language_changed"],
        "conclusion": "system_language_setting",
        "solution": "Open Language settings and select your preferred language."
    },
    {
        "id": 76,
        "conditions": ["mobile_data_not_working", "data_limit_reached"],
        "conclusion": "mobile_data_limit_reached",
        "solution": "Check your data package and usage limit with your network provider."
    },
    {
        "id": 77,
        "conditions": ["wifi_disconnects", "router_signal_weak"],
        "conclusion": "weak_router_signal",
        "solution": "Move closer to the router or improve router placement."
    },
    {
        "id": 78,
        "conditions": ["bluetooth_disconnects", "bluetooth_device_low_battery"],
        "conclusion": "bluetooth_accessory_low_battery",
        "solution": "Charge the Bluetooth accessory and reconnect it."
    },
    {
        "id": 79,
        "conditions": ["phone_storage_full", "system_cache_accumulated"],
        "conclusion": "app_cache_consuming_storage",
        "solution": "Review app storage usage and clear unnecessary caches."
    },
    {
        "id": 80,
        "conditions": ["phone_screen_timeout", "screen_timeout_short"],
        "conclusion": "short_screen_timeout_setting",
        "solution": "Increase the screen timeout duration in Display settings."
    },
    {
        "id": 81,
        "conditions": ["phone_not_receiving_sms", "sms_service_center_wrong"],
        "conclusion": "sms_service_center_problem",
        "solution": "Contact your network provider to verify the SMS service center settings."
    },
    {
        "id": 82,
        "conditions": ["phone_not_receiving_sms", "sim_network_issue"],
        "conclusion": "sim_sms_network_problem",
        "solution": "Restart the phone and contact your network provider if SMS still fails."
    },
    {
        "id": 83,
        "conditions": ["hotspot_not_working", "hotspot_disabled"],
        "conclusion": "hotspot_is_off",
        "solution": "Enable Mobile Hotspot in your phone settings."
    },
    {
        "id": 84,
        "conditions": ["hotspot_not_working", "connected_device_limit"],
        "conclusion": "hotspot_device_limit_reached",
        "solution": "Disconnect an unused device or increase the allowed device limit."
    },
    {
        "id": 85,
        "conditions": ["phone_storage_full", "large_download_files"],
        "conclusion": "downloads_using_storage",
        "solution": "Review your Downloads folder and remove files you no longer need."
    },
    {
        "id": 86,
        "conditions": ["phone_restarts_during_gaming", "heavy_game_load"],
        "conclusion": "gaming_overloads_device",
        "solution": "Reduce game graphics settings and allow the phone to cool."
    },
    {
        "id": 87,
        "conditions": ["phone_screen_dim", "adaptive_brightness_enabled"],
        "conclusion": "adaptive_brightness_adjustment",
        "solution": "Check adaptive brightness settings and adjust brightness manually."
    },
    {
        "id": 88,
        "conditions": ["flashlight_not_working", "camera_in_use"],
        "conclusion": "camera_uses_flash_module",
        "solution": "Close the camera app and try turning on the flashlight again."
    },
    {
        "id": 89,
        "conditions": ["phone_not_detected_by_pc", "usb_connection_mode_wrong"],
        "conclusion": "usb_file_transfer_not_selected",
        "solution": "Unlock the phone and select File Transfer mode from the USB notification."
    },
    {
        "id": 90,
        "conditions": ["phone_not_detected_by_pc", "pc_usb_port_fault"],
        "conclusion": "computer_usb_port_problem",
        "solution": "Try another USB port or test the phone with another computer."
    },
    {
        "id": 91,
        "conditions": ["phone_not_updating", "internet_unavailable"],
        "conclusion": "update_download_connection_problem",
        "solution": "Connect to a stable Wi-Fi network and try downloading the update again."
    },
    {
        "id": 92,
        "conditions": ["phone_not_updating", "insufficient_storage"],
        "conclusion": "update_storage_insufficient",
        "solution": "Free up enough storage space before installing the update."
    },
    {
        "id": 93,
        "conditions": ["app_notifications_delayed", "background_restriction_enabled"],
        "conclusion": "background_activity_restricted",
        "solution": "Review battery and background activity restrictions for the affected app."
    },
    {
        "id": 94,
        "conditions": ["phone_clock_wrong", "automatic_time_disabled"],
        "conclusion": "incorrect_manual_time_setting",
        "solution": "Enable automatic date and time in Android settings."
    },
    {
        "id": 95,
        "conditions": ["phone_storage_full", "recycle_bin_full"],
        "conclusion": "deleted_files_still_using_space",
        "solution": "Review and empty the Gallery or Files recycle bin after checking its contents."
    },
    {
        "id": 96,
        "conditions": ["phone_audio_distorted", "speaker_opening_blocked"],
        "conclusion": "speaker_obstruction",
        "solution": "Check the speaker opening and gently remove visible external dust."
    },
    {
        "id": 97,
        "conditions": ["screen_brightness_not_adjusting", "brightness_slider_fault"],
        "conclusion": "brightness_control_problem",
        "solution": "Restart the phone and check Display settings."
    },
    {
        "id": 98,
        "conditions": ["phone_apps_show_ads", "suspicious_app_installed"],
        "conclusion": "possible_adware_app",
        "solution": "Review recently installed apps and uninstall suspicious applications."
    },
    {
        "id": 99,
        "conditions": ["phone_security_warning", "unknown_app_source"],
        "conclusion": "unknown_source_security_risk",
        "solution": "Avoid installing untrusted APK files and review app permissions."
    },
    {
        "id": 100,
        "conditions": ["phone_problem_persists", "basic_troubleshooting_failed"],
        "conclusion": "professional_diagnosis_required",
        "solution": "Back up important data and contact an authorized mobile repair service."
    }
,
    {
      "id": 101,
      "conditions": [
        "battery_drains_fast",
        "battery_not_holding_charge"
      ],
      "conclusion": "battery_capacity_degraded",
      "solution": "Check battery health and consider qualified battery replacement if capacity is degraded."
    },
    {
      "id": 102,
      "conditions": [
        "battery_drains_fast",
        "battery_percentage_jumping"
      ],
      "conclusion": "battery_reading_unstable",
      "solution": "Restart the phone and observe battery readings; seek battery inspection if repeated."
    },
    {
      "id": 103,
      "conditions": [
        "phone_not_turning_on",
        "phone_shutdown_at_high_battery"
      ],
      "conclusion": "unexpected_power_shutdown",
      "solution": "Charge with a compatible charger and seek battery or power-system inspection if shutdowns continue."
    },
    {
      "id": 104,
      "conditions": [
        "phone_not_charging",
        "charging_disconnects"
      ],
      "conclusion": "intermittent_charging_connection",
      "solution": "Check cable and adapter using known-good compatible accessories; avoid manipulating a damaged port."
    },
    {
      "id": 105,
      "conditions": [
        "phone_not_charging",
        "charging_port_loose"
      ],
      "conclusion": "loose_charging_port_possible",
      "solution": "Avoid forcing the connector and arrange charging-port inspection."
    },
    {
      "id": 106,
      "conditions": [
        "wifi_not_working",
        "wifi_password_rejected"
      ],
      "conclusion": "wifi_authentication_problem",
      "solution": "Confirm the password and router security settings; forget and reconnect if appropriate."
    },
    {
      "id": 107,
      "conditions": [
        "wifi_not_working",
        "wifi_connected_no_internet"
      ],
      "conclusion": "wifi_internet_service_problem",
      "solution": "Check whether other devices have internet and restart the router if appropriate."
    },
    {
      "id": 108,
      "conditions": [
        "wifi_connected_no_internet",
        "vpn_enabled"
      ],
      "conclusion": "vpn_connection_interference",
      "solution": "Temporarily disconnect the VPN and test; restore it afterward if needed."
    },
    {
      "id": 109,
      "conditions": [
        "mobile_data_not_working",
        "mobile_data_roaming_disabled"
      ],
      "conclusion": "roaming_data_setting",
      "solution": "If roaming is expected and safe for your plan, review roaming settings and possible charges."
    },
    {
      "id": 110,
      "conditions": [
        "mobile_data_not_working",
        "network_mode_incompatible"
      ],
      "conclusion": "network_mode_mismatch",
      "solution": "Review preferred network mode and local carrier support."
    },
    {
      "id": 111,
      "conditions": [
        "apps_crashing",
        "apps_crash_after_update"
      ],
      "conclusion": "app_update_regression_possible",
      "solution": "Check for a newer app update; report the issue to the app developer if it persists."
    },
    {
      "id": 112,
      "conditions": [
        "apps_crashing",
        "app_force_stop"
      ],
      "conclusion": "app_stopped_by_system_or_user",
      "solution": "Reopen the app and restart the phone if needed."
    },
    {
      "id": 113,
      "conditions": [
        "app_not_opening",
        "app_login_failed"
      ],
      "conclusion": "application_login_problem",
      "solution": "Check credentials, connectivity and the service status; avoid repeated attempts if locked."
    },
    {
      "id": 114,
      "conditions": [
        "app_login_failed",
        "account_locked"
      ],
      "conclusion": "account_lockout",
      "solution": "Use the app's official account recovery process."
    },
    {
      "id": 115,
      "conditions": [
        "notifications_not_received",
        "notification_permission_denied"
      ],
      "conclusion": "notifications_permission_blocked",
      "solution": "Allow notification permission for the relevant app."
    },
    {
      "id": 116,
      "conditions": [
        "notifications_not_received",
        "notification_channel_muted"
      ],
      "conclusion": "notification_channel_silenced",
      "solution": "Review the affected notification category or channel settings."
    },
    {
      "id": 117,
      "conditions": [
        "phone_slow",
        "phone_accessibility_zoom_on"
      ],
      "conclusion": "display_accessibility_setting",
      "solution": "Review accessibility zoom settings if they were enabled unintentionally."
    },
    {
      "id": 118,
      "conditions": [
        "touchscreen_not_working",
        "screen_touch_delay"
      ],
      "conclusion": "touch_response_issue",
      "solution": "Remove gloves and test the screen clean and dry; seek service if delay persists."
    },
    {
      "id": 119,
      "conditions": [
        "phone_slow",
        "phone_memory_low"
      ],
      "conclusion": "memory_pressure_possible",
      "solution": "Close unused apps and restart; check whether performance improves."
    },
    {
      "id": 120,
      "conditions": [
        "phone_problem_persists",
        "phone_safe_mode"
      ],
      "conclusion": "safe_mode_diagnostic_state",
      "solution": "If Safe Mode was entered unintentionally, restart normally; use it as a diagnostic state, not a diagnosis."
    },
    {
      "id": 121,
      "conditions": [
        "phone_wet",
        "phone_water_warning"
      ],
      "conclusion": "liquid_warning_safety",
      "solution": "Do not charge the phone. Power it off if safe and seek professional inspection."
    },
    {
      "id": 122,
      "conditions": [
        "battery_swelling",
        "phone_overheating"
      ],
      "conclusion": "battery_swelling_safety",
      "solution": "Stop using and charging the device. Do not press it or attempt to puncture it; arrange professional handling."
    },
    {
      "id": 123,
      "conditions": [
        "phone_overheating",
        "phone_smoke_or_burning_smell"
      ],
      "conclusion": "thermal_emergency",
      "solution": "Stop using and charging it, move away if unsafe, and seek emergency assistance if fire or smoke presents danger."
    },
    {
      "id": 124,
      "conditions": [
        "phone_lost_or_stolen",
        "phone_security_warning"
      ],
      "conclusion": "lost_device_security",
      "solution": "Use the official device-finding service to secure or locate it and contact your carrier as needed."
    },
    {
      "id": 125,
      "conditions": [
        "screen_lock_unknown",
        "backup_not_available"
      ],
      "conclusion": "locked_device_data_caution",
      "solution": "Use official recovery options; avoid resets that may erase data unless you understand the consequences."
    },
    {
      "id": 126,
      "conditions": [
        "apps_crashing",
        "phone_storage_permission_denied"
      ],
      "conclusion": "media_permission_issue",
      "solution": "Review the app's media or storage permissions and grant only what is necessary."
    },
    {
      "id": 127,
      "conditions": [
        "microphone_not_working",
        "microphone_sound_low"
      ],
      "conclusion": "microphone_low_input",
      "solution": "Check microphone openings and app permissions; test in another app to compare."
    },
    {
      "id": 128,
      "conditions": [
        "speaker_no_sound",
        "speaker_sound_low"
      ],
      "conclusion": "speaker_output_low",
      "solution": "Check volume and audio routing, and inspect openings for visible debris."
    },
    {
      "id": 129,
      "conditions": [
        "phone_clock_wrong",
        "software_update_pending"
      ],
      "conclusion": "time_configuration_problem",
      "solution": "Enable automatic date and time and automatic time zone if available."
    },
    {
      "id": 130,
      "conditions": [
        "phone_not_charging",
        "phone_overheating"
      ],
      "conclusion": "charging_temperature_safety",
      "solution": "Disconnect power if the phone is unusually hot and let it cool in a safe place."
    }
]


# Stage 14: Multi-level dependency and intermediate reasoning rules
RULES.extend([
    {
        "id": 131,
        "conditions": [
            "charger_power_insufficient",
            "phone_used_during_charging"
        ],
        "conclusion": "charging_load_exceeds_supply",
        "solution": "Reduce phone workload while charging and use a compatible charger."
    },
    {
        "id": 132,
        "conditions": [
            "charging_load_exceeds_supply",
            "phone_overheating"
        ],
        "conclusion": "charging_heat_and_load_combined",
        "solution": "Stop intensive use during charging and allow the phone to cool."
    },
    {
        "id": 133,
        "conditions": [
            "memory_pressure_possible",
            "low_storage_performance_issue"
        ],
        "conclusion": "multiple_performance_constraints",
        "solution": "Free storage and reduce background workload, then restart."
    },
    {
        "id": 134,
        "conditions": [
            "weak_wifi_connection",
            "wifi_internet_service_problem"
        ],
        "conclusion": "wifi_link_and_service_issue",
        "solution": "Test another device and move closer to the router to isolate the issue."
    },
    {
        "id": 135,
        "conditions": [
            "application_login_problem",
            "account_lockout"
        ],
        "conclusion": "login_recovery_required",
        "solution": "Use official account recovery and avoid repeated login attempts."
    },
    {
        "id": 136,
        "conditions": [
            "battery_capacity_degraded",
            "battery_reading_unstable"
        ],
        "conclusion": "battery_health_concerns_combined",
        "solution": "Back up data and arrange professional battery inspection."
    },
    {
        "id": 137,
        "conditions": [
            "intermittent_charging_connection",
            "loose_charging_port_possible"
        ],
        "conclusion": "charging_connection_instability",
        "solution": "Stop forcing the connector and have the port inspected."
    },
    {
        "id": 138,
        "conditions": [
            "notifications_permission_blocked",
            "notification_channel_silenced"
        ],
        "conclusion": "notification_configuration_blocked",
        "solution": "Review both app permission and notification channel settings."
    },
    {
        "id": 139,
        "conditions": [
            "possible_app_conflict",
            "app_update_regression_possible"
        ],
        "conclusion": "app_compatibility_issue_possible",
        "solution": "Check app updates and test in Safe Mode where appropriate."
    },
    {
        "id": 140,
        "conditions": [
            "possible_liquid_damage",
            "liquid_warning_safety"
        ],
        "conclusion": "liquid_exposure_high_concern",
        "solution": "Do not charge the device; seek qualified inspection."
    },
    {
        "id": 141,
        "conditions": [
            "gaming_overloads_device",
            "sunlight_causes_overheating"
        ],
        "conclusion": "multiple_heat_sources",
        "solution": "Stop intensive use and remove the phone from direct sunlight."
    },
    {
        "id": 142,
        "conditions": [
            "speaker_obstruction",
            "speaker_output_low"
        ],
        "conclusion": "speaker_output_obstruction_possible",
        "solution": "Check volume and routing, and have the speaker cleaned if needed."
    }
])


# Stage 23: Expanded slow/intermittent charging diagnosis coverage
RULES.extend([
    {"id": 145, "conditions": ["charging_slow", "phone_charging_disconnects"], "conclusion": "unstable_slow_charging", "solution": "Check the cable and adapter connections. If charging repeatedly stops, inspect the cable and port; do not force the connector."},
    {"id": 146, "conditions": ["phone_charging_disconnects", "charging_cable_damaged"], "conclusion": "intermittent_cable_fault", "solution": "Replace the damaged or unreliable cable with a compatible one."},
    {"id": 147, "conditions": ["phone_charging_disconnects", "charging_port_dirty"], "conclusion": "intermittent_port_contact", "solution": "Inspect the port for visible debris. Do not insert metal objects; seek safe cleaning or inspection."},
    {"id": 148, "conditions": ["charging_slow", "battery_drains_fast"], "conclusion": "charging_and_battery_performance_issue", "solution": "Check battery usage and charging behavior. If battery life and charging are both poor, arrange battery health inspection."},
    {"id": 149, "conditions": ["phone_charging_disconnects", "charger_damaged"], "conclusion": "intermittent_adapter_fault", "solution": "Try a known-good compatible adapter and inspect the adapter for damage."},
    {"id": 150, "conditions": ["charging_slow", "charging_port_dirty"], "conclusion": "slow_charging_port_contact", "solution": "Inspect the charging port for debris or damage and arrange safe cleaning if needed."},
    {"id": 151, "conditions": ["charging_slow", "charging_cable_damaged"], "conclusion": "slow_charging_cable_fault", "solution": "Try a compatible cable known to work and replace the damaged cable."},
    {"id": 152, "conditions": ["charging_slow", "phone_charging_disconnects", "battery_drains_fast"], "conclusion": "multiple_charging_battery_symptoms", "solution": "Because charging and battery behavior are both affected, check the cable and port first, then arrange battery and charging hardware inspection if it persists."}
])


# Stage 30: Conservative coverage expansion for previously unused facts.
# Each rule requires a primary symptom plus a specific supporting fact.
RULES.extend([
    {
        "id": 153,
        "conditions": ["battery_drains_fast", "phone_battery_not_holding_charge"],
        "conclusion": "battery_health_issue_possible",
        "solution": "Review battery usage and charging behavior. If the battery still loses charge unusually quickly, arrange a professional battery health check."
    },
    {
        "id": 154,
        "conditions": ["phone_not_turning_on", "phone_power_button_unresponsive"],
        "conclusion": "power_button_fault",
        "solution": "Check for a case obstructing the button. Do not force it; arrange technician inspection if it remains unresponsive."
    },
    {
        "id": 155,
        "conditions": ["phone_slow", "phone_internal_storage_low"],
        "conclusion": "low_storage_performance_issue",
        "solution": "Review storage usage and back up important files before removing anything."
    },
    {
        "id": 156,
        "conditions": ["phone_slow", "phone_ram_usage_high"],
        "conclusion": "memory_overload",
        "solution": "Close unused apps and restart the phone. Check whether performance improves."
    },
    {
        "id": 157,
        "conditions": ["apps_crashing", "app_freezing"],
        "conclusion": "app_stability_issue_possible",
        "solution": "Update the affected app, restart it, and check whether the problem continues. Back up important app data before reinstalling."
    },
    {
        "id": 158,
        "conditions": ["camera_not_working", "camera_permission_disabled"],
        "conclusion": "camera_permission_problem",
        "solution": "Review camera permission for the affected app and allow access only if you trust the app."
    },
    {
        "id": 159,
        "conditions": ["phone_camera_blurry", "camera_focus_not_working"],
        "conclusion": "camera_focus_issue",
        "solution": "Clean the camera lens gently with a microfiber cloth and test focus in good lighting. Seek service if focus still fails."
    },
    {
        "id": 160,
        "conditions": ["mobile_data_not_working", "mobile_data_apn_incorrect"],
        "conclusion": "mobile_data_apn_issue",
        "solution": "Ask your mobile network provider for the correct APN settings before changing or resetting them."
    },
    {
        "id": 161,
        "conditions": ["wifi_not_working", "wifi_password_incorrect"],
        "conclusion": "wifi_authentication_problem",
        "solution": "Confirm the current Wi-Fi password with the network owner, then reconnect."
    },
    {
        "id": 162,
        "conditions": ["wifi_not_working", "wifi_saved_network_issue"],
        "conclusion": "saved_wifi_configuration_problem",
        "solution": "Forget only the affected Wi-Fi network and reconnect using its current password."
    },
    {
        "id": 163,
        "conditions": ["bluetooth_not_working", "bluetooth_pairing_code_mismatch"],
        "conclusion": "bluetooth_pairing_problem",
        "solution": "Confirm the pairing code shown on both devices and retry pairing."
    },
    {
        "id": 164,
        "conditions": ["bluetooth_not_working", "bluetooth_visibility_disabled"],
        "conclusion": "bluetooth_visibility_problem",
        "solution": "Make the phone discoverable during pairing, then turn visibility off again if your device provides that option."
    },
    {
        "id": 165,
        "conditions": ["gps_not_working", "gps_accuracy_low"],
        "conclusion": "gps_accuracy_problem",
        "solution": "Move to an open area, enable the appropriate location accuracy setting, and test again."
    },
    {
        "id": 166,
        "conditions": ["usb_connection_not_working", "usb_port_dirty"],
        "conclusion": "usb_port_contact_problem",
        "solution": "Disconnect the cable. Do not insert metal objects or liquid into the port; arrange safe cleaning if debris is present."
    },
    {
        "id": 167,
        "conditions": ["touchscreen_not_working", "ghost_touch_detected"],
        "conclusion": "ghost_touch_issue",
        "solution": "Keep the screen dry, remove any damaged screen protector, and restart the phone. Seek service if touches continue without contact."
    },
    {
        "id": 168,
        "conditions": ["incoming_calls_not_received", "call_forwarding_enabled"],
        "conclusion": "call_forwarding_setting_issue",
        "solution": "Review call-forwarding settings with your carrier or phone settings and disable forwarding only if you did not intend to use it."
    },
    {
        "id": 169,
        "conditions": ["phone_not_charging", "phone_charging_disconnects"],
        "conclusion": "intermittent_charging_connection",
        "solution": "Test with a compatible known-good cable and adapter. Do not force or wiggle a damaged connector; arrange port inspection if disconnections continue."
    },
    {
        "id": 170,
        "conditions": ["phone_overheating", "charger_overheating"],
        "conclusion": "charging_adapter_heat_safety",
        "solution": "Stop charging if the adapter or phone becomes unusually hot. Unplug safely, let equipment cool, and stop using damaged accessories."
    },
    {
        "id": 171,
        "conditions": ["phone_backup_not_completed", "cloud_backup_disabled"],
        "conclusion": "cloud_backup_disabled_issue",
        "solution": "Review the cloud backup setting and account selection, then start a backup when connected to a trusted network."
    },
    {
        "id": 172,
        "conditions": ["phone_backup_not_completed", "backup_storage_insufficient"],
        "conclusion": "backup_storage_issue",
        "solution": "Check the cloud account's storage usage and available space before retrying the backup."
    },
    {
        "id": 173,
        "conditions": ["proximity_sensor_not_working", "proximity_sensor_blocked"],
        "conclusion": "proximity_sensor_obstruction",
        "solution": "Clean the area around the proximity sensor and remove any case or protector covering it. Seek service if it still does not respond."
    }
])
