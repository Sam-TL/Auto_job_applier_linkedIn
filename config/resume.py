'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

version:    24.12.29.12.30
'''


###################################################### RESUME SETTINGS ######################################################

from modules.profile_loader import load_section
from config.personals import *  # Re-export personal details for backward compatibility

_resume_overrides = load_section("resume")
_resume_ingestion_overrides = load_section("resume_ingestion")


def _get_str(source: dict, key: str, fallback: str = "") -> str:
    value = source.get(key, fallback)
    if isinstance(value, str):
        return value.strip()
    if value is None:
        return fallback
    return str(value).strip()


def _get_list(source: dict, key: str) -> list[str]:
    value = source.get(key, [])
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str):
        return [item.strip() for item in value.split(",") if item.strip()]
    return []


# General resume configuration (optional section)
resume_template_path = _get_str(_resume_overrides, "template_path")
resume_output_path = _get_str(_resume_overrides, "output_path")
resume_filename_pattern = _get_str(_resume_overrides, "filename_pattern", "{full_name}_resume.pdf")

# Resume ingestion details (used by resume parser / AI helpers)
resume_text_path = _get_str(_resume_ingestion_overrides, "text_path")
resume_skill_keywords = _resume_ingestion_overrides.get("skill_keywords", {})
resume_fallbacks = _resume_ingestion_overrides.get("fallbacks", {})
resume_highlights = _get_list(_resume_ingestion_overrides, "highlights")
resume_question_keyword_answers = _resume_ingestion_overrides.get("question_keyword_answers", {})
resume_textarea_keyword_answers = _resume_ingestion_overrides.get("textarea_keyword_answers", {})


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
