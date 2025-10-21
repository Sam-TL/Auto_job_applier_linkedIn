'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

version:    24.12.29.12.30
'''


###################################################### CONFIGURE YOUR BOT HERE ######################################################

from modules.profile_loader import load_section

_settings_overrides = load_section("settings")


def _get_str(key: str, fallback: str = "") -> str:
    value = _settings_overrides.get(key, fallback)
    if isinstance(value, str):
        return value.strip()
    if value is None:
        return fallback
    return str(value).strip()


def _get_bool(key: str, fallback: bool = False) -> bool:
    value = _settings_overrides.get(key, fallback)
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in {"true", "1", "yes", "y"}:
            return True
        if lowered in {"false", "0", "no", "n"}:
            return False
    return fallback


def _get_int(key: str, fallback: int = 0) -> int:
    value = _settings_overrides.get(key, fallback)
    try:
        return int(value)
    except (TypeError, ValueError):
        return fallback


# >>>>>>>>>>> LinkedIn Settings <<<<<<<<<<<

close_tabs = _get_bool("close_tabs", False)
follow_companies = _get_bool("follow_companies", False)
run_non_stop = _get_bool("run_non_stop", False)
alternate_sortby = _get_bool("alternate_sortby", True)
cycle_date_posted = _get_bool("cycle_date_posted", True)
stop_date_cycle_at_24hr = _get_bool("stop_date_cycle_at_24hr", True)

# Application pacing controls
application_budget_per_run = _get_int("application_budget_per_run", 20)  # 0 = unlimited
confirm_after_budget = _get_bool("confirm_after_budget", True)
stagger_applications = _get_bool("stagger_applications", True)
stagger_min_delay = _get_int("stagger_min_delay", 10)
stagger_max_delay = _get_int("stagger_max_delay", 25)
if stagger_max_delay < stagger_min_delay:
    stagger_max_delay = stagger_min_delay

# >>>>>>>>>>> RESUME GENERATOR (Experimental & In Development) <<<<<<<<<<<

generated_resume_path = _get_str("generated_resume_path", "all resumes/")

# >>>>>>>>>>> Global Settings <<<<<<<<<<<

file_name = _get_str("file_name", "all excels/all_applied_applications_history.csv")
failed_file_name = _get_str("failed_file_name", "all excels/all_failed_applications_history.csv")
logs_folder_path = _get_str("logs_folder_path", "logs/")

click_gap = _get_int("click_gap", 0)
run_in_background = _get_bool("run_in_background", False)
disable_extensions = _get_bool("disable_extensions", False)
safe_mode = _get_bool("safe_mode", True)
smooth_scroll = _get_bool("smooth_scroll", False)
keep_screen_awake = _get_bool("keep_screen_awake", True)
stealth_mode = _get_bool("stealth_mode", False)
showAiErrorAlerts = _get_bool("showAiErrorAlerts", True)


############################################################################################################
'''
THANK YOU for using my tool ??! Wishing you the best in your job hunt ????!

Sharing is caring! If you found this tool helpful, please share it with your peers ??. Your support keeps this project alive.

Support my work on <PATREON_LINK>. Together, we can help more job seekers.

As an independent developer, I pour my heart and soul into creating tools like this, driven by the genuine desire to make a positive impact.

Your support, whether through donations big or small or simply spreading the word, means the world to me and helps keep this project alive and thriving.

Gratefully yours ????,
Sai Vignesh Golla
'''
############################################################################################################
