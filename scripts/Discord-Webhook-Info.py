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


Title("Discord Webhook Info")

try:

    def info_webhook(webhook_url):
        headers = {
            "Content-Type": "application/json",
        }

        response = requests.get(webhook_url, headers=headers)
        webhook_info = response.json()

        webhook_id = webhook_info.get("id", "None")
        webhook_token = webhook_info.get("token", "None")
        webhook_name = webhook_info.get("name", "None")
        webhook_avatar = webhook_info.get("avatar", "None")
        webhook_type = "bot" if webhook_info.get("type") == 1 else "webhook utilisateur"
        channel_id = webhook_info.get("channel_id", "None")
        guild_id = webhook_info.get("guild_id", "None")

        print(
            f"""
    {INFO_ADD} ID         : {white}{webhook_id}{blue}
    {INFO_ADD} Token      : {white}{webhook_token}{blue}
    {INFO_ADD} Name       : {white}{webhook_name}{blue}
    {INFO_ADD} Avatar     : {white}{webhook_avatar}{blue}
    {INFO_ADD} Type       : {white}{webhook_type}{blue}
    {INFO_ADD} Channel ID : {white}{channel_id}{blue}
    {INFO_ADD} Server ID  : {white}{guild_id}{blue}
    """
        )

        if "user" in webhook_info:
            user_info = webhook_info["user"]

            user_id = user_info.get("id", "None")
            username = user_info.get("username", "None")
            display_name = user_info.get("global_name", "None")
            discriminator = user_info.get("discriminator", "None")
            user_avatar = user_info.get("avatar", "None")
            user_flags = user_info.get("flags", "None")
            accent_color = user_info.get("accent_color", "None")
            avatar_decoration = user_info.get("avatar_decoration_data", "None")
            banner_color = user_info.get("banner_color", "None")

            print(
                f"""
    {blue}User information associated with the Webhook:
    {INFO_ADD} ID          : {white}{user_id}{blue}
    {INFO_ADD} Name        : {white}{username}{blue}
    {INFO_ADD} DisplayName : {white}{display_name}{blue}
    {INFO_ADD} Number      : {white}{discriminator}{blue}
    {INFO_ADD} Avatar      : {white}{user_avatar}{blue}
    {INFO_ADD} Flags       : {white}{user_flags} Publique: {user_flags}{blue}
    {INFO_ADD} Color       : {white}{accent_color}{blue}
    {INFO_ADD} Decoration  : {white}{avatar_decoration}{blue}
    {INFO_ADD} Banner      : {white}{banner_color}{blue}
    """
            )

    webhook_url = input(
        f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Webhook URL -> {color.RESET}"
    )
    if CheckWebhook(webhook_url) == False:
        ErrorWebhook()
    info_webhook(webhook_url)
    Continue()

except Exception as e:
    Error(e)
