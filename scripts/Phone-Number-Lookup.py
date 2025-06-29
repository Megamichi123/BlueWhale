#!/usr/bin/env python3
# GNU GENERAL PUBLIC LICENSE
# See the file 'LICENSE' for details
# ---------------------------------------------------------------------
# EN:
#     - Touch or modify the code below. If there is an error,
#     - please fix it and make a pull request ;)
from configs.util import *
from configs.term import *
from configs.config import *

try:
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
except Exception as e:
    ErrorModule(e)


Title("Phone Number Lookup")

try:
    phone_number = input(
        f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Phone Number -> {color.RESET}"
    )
    print(
        f"{BEFORE + current_time_hour() + AFTER} {WAIT} Information Recovery..{reset}"
    )
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        if phonenumbers.is_valid_number(parsed_number):
            status = "Valid"
        else:
            status = "Invalid"

        if phone_number.startswith("+"):
            country_code = "+" + phone_number[1:3]
        else:
            country_code = "None"
        try:
            operator = carrier.name_for_number(parsed_number, "fr")
        except:
            operator = "None"

        try:
            type_number = (
                "Mobile"
                if phonenumbers.number_type(parsed_number)
                == phonenumbers.PhoneNumberType.MOBILE
                else "Fixe"
            )
        except:
            type_number = "None"

        try:
            timezones = timezone.time_zones_for_number(parsed_number)
            timezone_info = timezones[0] if timezones else None
        except:
            timezone_info = "None"

        try:
            country = phonenumbers.region_code_for_number(parsed_number)
        except:
            country = "None"

        try:
            region = geocoder.description_for_number(parsed_number, "fr")
        except:
            region = "None"

        try:
            formatted_number = phonenumbers.format_number(
                parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL
            )
        except:
            formatted_number = "None"

        print(
            f"""
    {INFO_ADD} Phone        : {white}{phone_number}{blue}
    {INFO_ADD} Formatted    : {white}{formatted_number}{blue}
    {INFO_ADD} Status       : {white}{status}{blue}
    {INFO_ADD} Country Code : {white}{country_code}{blue}
    {INFO_ADD} Country      : {white}{country}{blue}
    {INFO_ADD} Region       : {white}{region}{blue}
    {INFO_ADD} Timezone     : {white}{timezone_info}{blue}
    {INFO_ADD} Operator     : {white}{operator}{blue}
    {INFO_ADD} Type Number  : {white}{type_number}{blue}
    """
        )
        Continue()

    except:
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Invalid Format !")
        Continue()

except Exception as e:
    Error(e)
