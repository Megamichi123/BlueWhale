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
    import dns.resolver
    import requests
    import re
except Exception as e:
    ErrorModule(e)

Title("Email Lookup")

try:

    def get_email_info(email):
        info = {}
        try:
            domain_all = email.split("@")[-1]
        except:
            domain_all = None

        try:
            name = email.split("@")[0]
        except:
            name = None

        try:
            domain = re.search(r"@([^@.]+)\.", email).group(1)
        except:
            domain = None
        try:
            tld = f".{email.split('.')[-1]}"
        except:
            tld = None

        try:
            mx_records = dns.resolver.resolve(domain_all, "MX")
            mx_servers = [str(record.exchange) for record in mx_records]
            info["mx_servers"] = mx_servers
        except dns.resolver.NoAnswer:
            info["mx_servers"] = None
        except dns.resolver.NXDOMAIN:
            info["mx_servers"] = None

        try:
            spf_records = dns.resolver.resolve(domain_all, "SPF")
            info["spf_records"] = [str(record) for record in spf_records]
        except dns.resolver.NoAnswer:
            info["spf_records"] = None
        except dns.resolver.NXDOMAIN:
            info["spf_records"] = None

        try:
            dmarc_records = dns.resolver.resolve(f"_dmarc.{domain_all}", "TXT")
            info["dmarc_records"] = [str(record) for record in dmarc_records]
        except dns.resolver.NoAnswer:
            info["dmarc_records"] = None
        except dns.resolver.NXDOMAIN:
            info["dmarc_records"] = None

        if mx_servers:
            for server in mx_servers:
                if "google.com" in server:
                    info["google_workspace"] = True
                elif "outlook.com" in server:
                    info["microsoft_365"] = True

        return info, domain_all, domain, tld, name

    email = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Email -> {reset}")
    Censored(email)

    print(
        f"{BEFORE + current_time_hour() + AFTER} {WAIT} Information Recovery..{reset}"
    )
    info, domain_all, domain, tld, name = get_email_info(email)

    try:
        mx_servers = info["mx_servers"]
        mx_servers = " / ".join(mx_servers)
    except Exception as e:
        mx_servers = None

    try:
        spf_records = info["spf_records"]
    except:
        spf_records = None

    try:
        dmarc_records = info["dmarc_records"]
        dmarc_records = " / ".join(dmarc_records)
    except:
        dmarc_records = None

    try:
        google_workspace = info["google_workspace"]
    except:
        google_workspace = None

    try:
        mailgun_validation = info["mailgun_validation"]
        mailgun_validation = " / ".join(mailgun_validation)
    except:
        mailgun_validation = None

    print(
        f"""
    {INFO_ADD} Email      : {white}{email}{blue}
    {INFO_ADD} Name       : {white}{name}{blue}
    {INFO_ADD} Domain     : {white}{domain}{blue}
    {INFO_ADD} Tld        : {white}{tld}{blue}
    {INFO_ADD} Domain All : {white}{domain_all}{blue}
    {INFO_ADD} Servers    : {white}{mx_servers}{blue}
    {INFO_ADD} Spf        : {white}{spf_records}{blue}
    {INFO_ADD} Dmarc      : {white}{dmarc_records}{blue}
    {INFO_ADD} Workspace  : {white}{google_workspace}{blue}
    {INFO_ADD} Mailgun    : {white}{mailgun_validation}{blue}
    {color.RESET}"""
    )

    Continue()

except Exception as e:
    Error(e)
