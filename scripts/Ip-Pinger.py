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
    import concurrent.futures
    import time
    import socket
except Exception as e:
    ErrorModule(e)

Title("Ip Pinger")

try:

    def PingIp(hostname, port, bytes):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(2)
                start_time = time.time()
                sock.connect((hostname, port))
                data = b"\x00" * bytes
                sock.sendall(data)
                end_time = time.time()
                elapsed_time = (end_time - start_time) * 1000
                print(
                    f"{BEFORE + current_time_hour() + AFTER} {ADD} Hostname: {white}{hostname}{blue} time: {white}{elapsed_time:.2f}ms{blue} port: {white}{port}{blue} bytes: {white}{bytes}{blue} status: {white}succeed{blue}"
                )
        except:
            elapsed_time = 0
            print(
                f"{BEFORE + current_time_hour() + AFTER} {ERROR} Hostname: {white}{hostname}{blue} time: {white}{elapsed_time}ms{blue} port: {white}{port}{blue} bytes: {white}{bytes}{blue} status: {white}fail{blue}"
            )

    Slow(wifi_banner)

    hostname = input(
        f"{BEFORE + current_time_hour() + AFTER} {INPUT} Ip -> " + color.RESET
    )

    try:
        port_input = input(
            f"{BEFORE + current_time_hour() + AFTER} {INPUT} Port (enter for default) -> "
            + color.RESET
        )
        port = int(port_input) if port_input else 80

        bytes_input = input(
            f"{BEFORE + current_time_hour() + AFTER} {INPUT} Bytes (enter for default) -> "
            + color.RESET
        )
        bytes = int(bytes_input) if bytes_input else 64
    except:
        ErrorNumber()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        while True:
            time.sleep(0.1)
            executor.submit(PingIp, hostname, port, bytes)

except Exception as e:
    Error(e)
