'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

version:    24.12.29.12.30
'''


###################################################### LOGIN & AI SETTINGS ######################################################

from modules.profile_loader import load_section

_secret_overrides = load_section("secrets")


def _get_str(key: str, fallback: str = "") -> str:
    value = _secret_overrides.get(key, fallback)
    if isinstance(value, str):
        return value.strip()
    if value is None:
        return fallback
    return str(value).strip()


def _get_bool(key: str, fallback: bool = False) -> bool:
    value = _secret_overrides.get(key, fallback)
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in {"true", "1", "yes", "y"}:
            return True
        if lowered in {"false", "0", "no", "n"}:
            return False
    return fallback


# LinkedIn credentials
username = _get_str("username")
password = _get_str("password")

# AI configuration
use_AI = _get_bool("use_AI")
ai_provider = _get_str("ai_provider", "openai")
llm_api_url = _get_str("llm_api_url", "")
llm_api_key = _get_str("llm_api_key", "")
llm_model = _get_str("llm_model", "")
llm_spec = _get_str("llm_spec", "openai")
stream_output = _get_bool("stream_output")


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
