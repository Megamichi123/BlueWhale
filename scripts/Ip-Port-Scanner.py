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
except Exception as e:
    ErrorModule(e)

Title("Ip Port Scanner")

try:

    def PortScanner(ip):
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
                    sock.settimeout(0.1)
                    result = sock.connect_ex((ip, port))
                    if result == 0:
                        protocol = IdentifyProtocol(ip, port)
                        print(
                            f"{BEFORE + current_time_hour() + AFTER} {ADD} Port: {white}{port}{blue} Status: {white}Open{blue} Protocol: {white}{protocol}{blue}"
                        )
            except Exception:
                pass

        def IdentifyProtocol(ip, port):
            if port in port_protocol_map:
                return port_protocol_map[port]
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(0.5)
                    sock.connect((ip, port))
                    sock.send(
                        b"GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(ip).encode("utf-8")
                    )
                    response = sock.recv(100).decode("utf-8")
                    if "HTTP" in response:
                        return "HTTP"
                    sock.send(b"\r\n")
                    response = sock.recv(100).decode("utf-8")
                    if "FTP" in response:
                        return "FTP"
                    sock.send(b"\r\n")
                    response = sock.recv(100).decode("utf-8")
                    if "SSH" in response:
                        return "SSH"
                    return "Unknown"
            except Exception:
                return "Unknown"

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(lambda port: ScanPort(ip, port), range(1, 65536))

    Slow(scan_banner)
    ip = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Ip -> {reset}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Scanning..")
    PortScanner(ip)
    Continue()

except Exception as e:
    Error(e)
