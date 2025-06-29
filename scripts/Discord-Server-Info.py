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

Title("Discord Server Info")

try:
    Slow(discord_banner)
    invite = input(
        f"{BEFORE + current_time_hour() + AFTER} {INPUT} Server Invitation -> {reset}"
    )
    try:
        invite_code = invite.split("/")[-1]
    except:
        invite_code = invite

    response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")

    if response.status_code == 200:
        api = response.json()

        type_value = api.get("type", "None")
        code_value = api.get("code", "None")
        inviter_info = api.get("inviter", {})
        inviter_id = inviter_info.get("id", "None")
        inviter_username = inviter_info.get("username", "None")
        inviter_avatar = inviter_info.get("avatar", "None")
        inviter_discriminator = inviter_info.get("discriminator", "None")
        inviter_public_flags = inviter_info.get("public_flags", "None")
        inviter_flags = inviter_info.get("flags", "None")
        inviter_banner = inviter_info.get("banner", "None")
        inviter_accent_color = inviter_info.get("accent_color", "None")
        inviter_global_name = inviter_info.get("global_name", "None")
        inviter_banner_color = inviter_info.get("banner_color", "None")
        expires_at = api.get("expires_at", "None")
        flags = api.get("flags", "None")
        server_info = api.get("guild", {})
        server_id = server_info.get("id", "None")
        server_name = server_info.get("name", "None")
        server_icon = server_info.get("icon", "None")
        server_features = server_info.get("features", "None")
        if server_features != "None":
            server_features = " / ".join(server_features)
        server_verification_level = server_info.get("verification_level", "None")
        server_nsfw_level = server_info.get("nsfw_level", "None")
        server_descritpion = server_info.get("description", "None")
        server_nsfw = server_info.get("nsfw", "None")
        server_premium_subscription_count = server_info.get(
            "premium_subscription_count", "None"
        )
        channel_info = api.get("channel", {})
        channel_id = channel_info.get("id", "None")
        channel_type = channel_info.get("type", "None")
        channel_name = channel_info.get("name", "None")
    else:
        ErrorUrl()

    print(
        f"""{blue}
    Invitation Information:
    {INFO_ADD} Invitation         : {white}{invite}{blue}
    {INFO_ADD} Type               : {white}{type_value}{blue}
    {INFO_ADD} Code               : {white}{code_value}{blue}
    {INFO_ADD} Expired            : {white}{expires_at}{blue}
    {INFO_ADD} Server ID          : {white}{server_id}{blue}
    {INFO_ADD} Server Name        : {white}{server_name}{blue}
    {INFO_ADD} Channel ID         : {white}{channel_id}{blue}
    {INFO_ADD} Channel Name       : {white}{channel_name}{blue}
    {INFO_ADD} Channel Type       : {white}{channel_type}{blue}
    {INFO_ADD} Server Description : {white}{server_descritpion}{blue}
    {INFO_ADD} Server Icon        : {white}{server_icon}{blue}
    {INFO_ADD} Server Features    : {white}{server_features}{blue}
    {INFO_ADD} Server NSFW Level  : {white}{server_nsfw_level}{blue}
    {INFO_ADD} Server NSFW        : {white}{server_nsfw}{blue}
    {INFO_ADD} Flags              : {white}{flags}{blue}
    {INFO_ADD} Server Verification Level         : {white}{server_verification_level}{blue}
    {INFO_ADD} Server Premium Subscription Count : {white}{server_premium_subscription_count}{blue}
"""
    )

    if inviter_info:
        print(
            f"""    {blue}Inviter Information:
    {INFO_ADD} ID            : {white}{inviter_id}{blue}
    {INFO_ADD} Username      : {white}{inviter_username}{blue}
    {INFO_ADD} Global Name   : {white}{inviter_global_name}{blue}
    {INFO_ADD} Avatar        : {white}{inviter_avatar}{blue}
    {INFO_ADD} Discriminator : {white}{inviter_discriminator}{blue}
    {INFO_ADD} Public Flags  : {white}{inviter_public_flags}{blue}
    {INFO_ADD} Flags         : {white}{inviter_flags}{blue}
    {INFO_ADD} Banner        : {white}{inviter_banner}{blue}
    {INFO_ADD} Accent Color  : {white}{inviter_accent_color}{blue}
    {INFO_ADD} Banner Color  : {white}{inviter_banner_color}{blue}
    """
        )
    Continue()

except Exception as e:
    Error(e)
