'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

version:    24.12.29.12.30
'''


###################################################### LINKEDIN SEARCH PREFERENCES ######################################################

from modules.profile_loader import load_section

_search_overrides = load_section("search")

_DEFAULT_SEARCH_TERMS = [
    # Enterprise & Digital Architecture
    "Digital Architect",
    "Enterprise Architect",
    "Principal Enterprise Architect",
    "Director of Enterprise Architecture",

    # Cloud Architecture Leadership
    "Chief Cloud Architect",
    "Director of Cloud Architecture",
    "Director of Cloud Engineering",
    "Director of Cloud Infrastructure",
    "Director of Cloud Strategy",

    # Platform / DevOps / SRE
    "Head of Platform Engineering",
    "Director of Platform Engineering",
    "Director of Site Reliability Engineering",
    "Director of DevOps",
    "DevOps Transformation Lead",

    # Technology & Digital Strategy
    "Director of Technology Strategy",
    "Director of Digital Transformation",
    "Technology Strategy Director",
    "Infrastructure Modernization Lead",
    "Director of Digital Strategy",
    "Head of Digital Strategy",
    "Director of IT Strategy",
    "Information Technology Operations Manager",
    "Director of Technology Innovation",

    # Data & Integration Leadership
    "Enterprise Integration Director",
    "Director of Data Platforms",

    # IT Leadership
    "Head of IT Strategy",
    "Director of IT Operations",
]


def _sanitize_list(items: list) -> list[str]:
    cleaned: list[str] = []
    for item in items:
        if item is None:
            continue
        text = str(item).strip()
        if text:
            cleaned.append(text)
    return cleaned


def _get_list(key: str, fallback: list[str]) -> list[str]:
    value = _search_overrides.get(key, fallback)
    if isinstance(value, list):
        return _sanitize_list(value) or fallback
    if isinstance(value, str):
        return _sanitize_list(value.split(",")) or fallback
    return fallback


def _get_str(key: str, fallback: str = "") -> str:
    value = _search_overrides.get(key, fallback)
    if isinstance(value, str):
        return value.strip()
    if value is None:
        return fallback
    return str(value).strip()


def _get_bool(key: str, fallback: bool = False) -> bool:
    value = _search_overrides.get(key, fallback)
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
    value = _search_overrides.get(key, fallback)
    try:
        return int(value)
    except (TypeError, ValueError):
        return fallback


# Search criteria
search_terms = _get_list("search_terms", _DEFAULT_SEARCH_TERMS)
search_location = _get_str("search_location", "Ireland")
switch_number = _get_int("switch_number", 2)
randomize_search_order = _get_bool("randomize_search_order", True)

# Job search filters
sort_by = _get_str("sort_by", "")
date_posted = _get_str("date_posted", "Past week")
salary = _get_str("salary", "")

easy_apply_only = _get_bool("easy_apply_only", True)

experience_level = _get_list("experience_level", [])
job_type = _get_list("job_type", [])
on_site = _get_list("on_site", [])

companies = _get_list("companies", [])
location = _get_list("location", [])
industry = _get_list("industry", [])
job_function = _get_list("job_function", [])
job_titles = _get_list("job_titles", [])
benefits = _get_list("benefits", [])
commitments = _get_list("commitments", [])

under_10_applicants = _get_bool("under_10_applicants", False)
in_your_network = _get_bool("in_your_network", False)
fair_chance_employer = _get_bool("fair_chance_employer", False)

# Related settings
pause_after_filters = _get_bool("pause_after_filters", True)

# Skip logic
about_company_bad_words = _get_list("about_company_bad_words", ["Crossover"])
about_company_good_words = _get_list("about_company_good_words", [])
bad_words = _get_list("bad_words", ["US Citizen", "USA Citizen", "No C2C", "No Corp2Corp", "Embedded Programming", "Ruby", "CNC"])

security_clearance = _get_bool("security_clearance", False)
did_masters = _get_bool("did_masters", True)
current_experience = _get_int("current_experience", 20)


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
