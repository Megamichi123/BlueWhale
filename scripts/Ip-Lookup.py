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
    import requests
except Exception as e:
    ErrorModule(e)

Title("Ip Lookup")

try:
    Slow(map_banner)
    ip = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Ip -> {reset}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search for information..")

    try:
        response = requests.get(f"https://{website}/api/ip/ip={ip}")
        api = response.json()

        ip = api.get("ip")
        status = api.get("status")
        country = api.get("country")
        country_code = api.get("country_code")
        region = api.get("region")
        region_code = api.get("region_code")
        zip = api.get("zip")
        city = api.get("city")
        latitude = api.get("latitude")
        longitude = api.get("longitude")
        timezone = api.get("timezone")
        isp = api.get("isp")
        org = api.get("org")
        as_host = api.get("as")

    except:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        api = response.json()

        status = "Valid" if api.get("status") == "success" else "Invalid"
        country = api.get("country", "None")
        country_code = api.get("countryCode", "None")
        region = api.get("regionName", "None")
        region_code = api.get("region", "None")
        zip = api.get("zip", "None")
        city = api.get("city", "None")
        latitude = api.get("lat", "None")
        longitude = api.get("lon", "None")
        timezone = api.get("timezone", "None")
        isp = api.get("isp", "None")
        org = api.get("org", "None")
        as_host = api.get("as", "None")

    Slow(
        f"""    
    {INFO_ADD} Status    : {white}{status}{blue}
    {INFO_ADD} Country   : {white}{country} ({country_code}){blue}
    {INFO_ADD} Region    : {white}{region} ({region_code}){blue}
    {INFO_ADD} Zip       : {white}{zip}{blue}
    {INFO_ADD} City      : {white}{city}{blue}
    {INFO_ADD} Latitude  : {white}{latitude}{blue}
    {INFO_ADD} Longitude : {white}{longitude}{blue}
    {INFO_ADD} Timezone  : {white}{timezone}{blue}
    {INFO_ADD} Isp       : {white}{isp}{blue}
    {INFO_ADD} Org       : {white}{org}{blue}
    {INFO_ADD} As        : {white}{as_host}{blue}{reset}
    """
    )

    Continue()

except Exception as e:
    Error(e)
