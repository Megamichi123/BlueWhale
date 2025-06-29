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
    import socket
    import concurrent.futures
    import requests
    from urllib.parse import urlparse
    import ssl
    import urllib3
    from requests.exceptions import RequestException
    from bs4 import BeautifulSoup
except Exception as e:
    ErrorModule(e)

Title("Website Scanner")

try:
    user_agent = ChoiceUserAgent()
    headers = {"User-Agent": user_agent}

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def WebsiteFoundUrl(url):
        website_url = f"https://{url}" if not urlparse(url).scheme else url
        print(
            f"{BEFORE + current_time_hour() + AFTER} {ADD} Website: {white}{website_url}{blue}"
        )
        return website_url

    def WebsiteDomain(website_url):
        domain = urlparse(website_url).netloc
        print(
            f"{BEFORE + current_time_hour() + AFTER} {ADD} Domain: {white}{domain}{blue}"
        )
        return domain

    def WebsiteIp(domain):
        try:
            ip = socket.gethostbyname(domain)
        except socket.gaierror:
            ip = "None"
        if ip != "None":
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} IP: {white}{ip}{blue}")
        return ip

    def IpType(ip):
        if ":" in ip:
            type = "ipv6"
        elif "." in ip:
            type = "ipv4"
        else:
            return
        print(
            f"{BEFORE + current_time_hour() + AFTER} {ADD} IP Type: {white}{type}{blue}"
        )

    def WebsiteSecure(website_url):
        print(
            f"{BEFORE + current_time_hour() + AFTER} {ADD} Secure: {white}{website_url.startswith('https://')}{blue}"
        )

    def WebsiteStatus(website_url):
        try:
            status_code = requests.get(
                website_url, timeout=5, headers=headers
            ).status_code
        except RequestException:
            status_code = 404
        print(
            f"{BEFORE + current_time_hour() + AFTER} {ADD} Status Code: {white}{status_code}{blue}"
        )

    def IpInfo(ip):
        try:
            api = requests.get(f"https://ipinfo.io/{ip}/json", headers=headers).json()
        except RequestException:
            api = {}
        for key in ["country", "hostname", "isp", "org", "asn"]:
            if key in api:
                print(
                    f"{BEFORE + current_time_hour() + AFTER} {ADD} Host {key.capitalize()}: {white}{api[key]}{blue}"
                )

    def IpDns(ip):
        try:
            dns = socket.gethostbyaddr(ip)[0]
        except:
            dns = "None"
        if dns != "None":
            print(
                f"{BEFORE + current_time_hour() + AFTER} {ADD} Host DNS: {white}{dns}{blue}"
            )

    def WebsitePort(ip):
        ports = [
            21,
            22,
            23,
            25,
            53,
            69,
            80,
            110,
            123,
            143,
            194,
            389,
            443,
            161,
            3306,
            5432,
            6379,
            1521,
            3389,
        ]
        port_protocol_map = {
            21: "FTP",
            22: "SSH",
            23: "Telnet",
            25: "SMTP",
            53: "DNS",
            69: "TFTP",
            80: "HTTP",
            110: "POP3",
            123: "NTP",
            143: "IMAP",
            194: "IRC",
            389: "LDAP",
            443: "HTTPS",
            161: "SNMP",
            3306: "MySQL",
            5432: "PostgreSQL",
            6379: "Redis",
            1521: "Oracle DB",
            3389: "RDP",
        }

        def ScanPort(ip, port):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(1)
                    if sock.connect_ex((ip, port)) == 0:
                        print(
                            f"{BEFORE + current_time_hour() + AFTER} {ADD} Port: {white}{port}{blue} Status: {white}Open{blue} Protocol: {white}{port_protocol_map.get(port, 'Unknown')}{blue}"
                        )
            except:
                pass

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(lambda p: ScanPort(ip, p), ports)

    def HttpHeaders(website_url):
        try:
            headers = requests.get(website_url, timeout=5).headers
            for header, value in headers.items():
                print(
                    f"{BEFORE + current_time_hour() + AFTER} {ADD} HTTP Header: {white}{header}{blue} Value: {white}{value}{blue}"
                )
        except RequestException:
            pass

    def CheckSslCertificate(website_url):
        try:
            with ssl.create_default_context().wrap_socket(
                socket.socket(), server_hostname=urlparse(website_url).hostname
            ) as sock:
                sock.settimeout(5)
                sock.connect((urlparse(website_url).hostname, 443))
                cert = sock.getpeercert()
            for key, value in cert.items():
                print(
                    f"{BEFORE + current_time_hour() + AFTER} {ADD} SSL Certificate Key: {white}{key}{blue} Value: {white}{value}{blue}"
                )
        except:
            pass

    def CheckSecurityHeaders(website_url):
        headers = [
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "X-XSS-Protection",
        ]
        try:
            response_headers = requests.get(website_url, timeout=5).headers
            for header in headers:
                print(
                    f"{BEFORE + current_time_hour() + AFTER} {ADD} {'Missing' if header not in response_headers else 'Security'} Header: {white}{header}{blue}"
                )
        except RequestException:
            pass

    def AnalyzeCookies(website_url):
        try:
            cookies = requests.get(website_url, timeout=5, headers=headers).cookies
            for cookie in cookies:
                secure = "Secure" if cookie.secure else "Not Secure"
                httponly = (
                    "HttpOnly"
                    if cookie.has_nonstandard_attr("HttpOnly")
                    else "Not HttpOnly"
                )
                print(
                    f"{BEFORE + current_time_hour() + AFTER} {ADD} Cookie: {white}{cookie.name}{blue} Secure: {white}{secure}{blue} HttpOnly: {white}{httponly}{blue}"
                )
        except RequestException:
            pass

    def DetectTechnologies(website_url):
        try:
            response = requests.get(website_url, timeout=5, headers=headers)
            headers = response.headers
            soup = BeautifulSoup(response.content, "html.parser")
            techs = []
            if "x-powered-by" in headers:
                techs.append(f"X-Powered-By: {headers['x-powered-by']}")
            if "server" in headers:
                techs.append(f"Server: {headers['server']}")
            for script in soup.find_all("script", src=True):
                if "jquery" in script["src"]:
                    techs.append("jQuery")
                if "bootstrap" in script["src"]:
                    techs.append("Bootstrap")
            for tech in techs:
                print(
                    f"{BEFORE + current_time_hour() + AFTER} {ADD} Detected Technology: {white}{tech}{blue}"
                )
        except:
            pass

    Slow(scan_banner)
    print(
        f"{BEFORE + current_time_hour() + AFTER} {INFO} Selected User-Agent: {white + user_agent}"
    )
    url = input(
        f"{BEFORE + current_time_hour() + AFTER} {INPUT} Website URL -> {reset}"
    )
    Censored(url)
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Scanning..{reset}")

    website_url = WebsiteFoundUrl(url)
    domain = WebsiteDomain(website_url)
    ip = WebsiteIp(domain)
    IpType(ip)
    WebsiteSecure(website_url)
    WebsiteStatus(website_url)
    IpInfo(ip)
    IpDns(ip)
    WebsitePort(ip)
    HttpHeaders(website_url)
    CheckSslCertificate(website_url)
    CheckSecurityHeaders(website_url)
    AnalyzeCookies(website_url)
    DetectTechnologies(website_url)
    Continue()


except Exception as e:
    Error(e)
