'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

version:    24.12.29.12.30
'''


###################################################### PERSONAL DETAILS ######################################################


from modules.profile_loader import load_section

_personal_overrides = load_section("personals")


def _get(key: str, fallback: str = "") -> str:
    value = _personal_overrides.get(key, fallback)
    return value.strip() if isinstance(value, str) else fallback


# Your legal name
first_name = _get("first_name")
middle_name = _get("middle_name")
last_name = _get("last_name")

# Phone number (required)
phone_number = _get("phone_number")

# Location details
current_city = _get("current_city")
street = _get("street")
state = _get("state")
zipcode = _get("zipcode")
country = _get("country")
phone_country_code = _get("phone_country_code")
preferred_email = _get("preferred_email")
preferred_location = _get("preferred_location", current_city)

## US Equal Opportunity questions
ethnicity = _get("ethnicity")
gender = _get("gender")
disability_status = _get("disability_status")
veteran_status = _get("veteran_status")


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
