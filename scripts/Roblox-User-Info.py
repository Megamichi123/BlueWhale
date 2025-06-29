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

Title("Roblox User Info")

try:
    user_agent = ChoiceUserAgent()
    headers = {"User-Agent": user_agent}

    print(
        f"\n{BEFORE + current_time_hour() + AFTER} {INFO} Selected User-Agent: {white + user_agent}"
    )
    username_input = input(
        f"{BEFORE + current_time_hour() + AFTER} {INPUT} Username -> {color.RESET}"
    )
    print(
        f"{BEFORE + current_time_hour() + AFTER} {WAIT} Information Recovery..{reset}"
    )

    try:
        response = requests.post(
            "https://users.roblox.com/v1/usernames/users",
            headers=headers,
            json={"usernames": [username_input], "excludeBannedUsers": "true"},
        )

        data = response.json()

        user_id = data["data"][0]["id"]

        response = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
        api = response.json()

        userid = api.get("id", "None")
        display_name = api.get("displayName", "None")
        username = api.get("name", "None")
        description = api.get("description", "None")
        created_at = api.get("created", "None")
        is_banned = api.get("isBanned", "None")
        external_app_display_name = api.get("externalAppDisplayName", "None")
        has_verified_badge = api.get("hasVerifiedBadge", "None")

        print(
            f"""
    {INFO_ADD} Username       : {white}{username}{blue}
    {INFO_ADD} Id             : {white}{userid}{blue}
    {INFO_ADD} Display Name   : {white}{display_name}{blue}
    {INFO_ADD} Description    : {white}{description}{blue}
    {INFO_ADD} Created        : {white}{created_at}{blue}
    {INFO_ADD} Banned         : {white}{is_banned}{blue}
    {INFO_ADD} External Name  : {white}{external_app_display_name}{blue}
    {INFO_ADD} Verified Badge : {white}{has_verified_badge}{blue}
    """
        )
        Continue()

    except:
        ErrorUsername()
except Exception as e:
    Error(e)
