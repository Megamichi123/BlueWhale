#!/usr/bin/env python3
# GNU GENERAL PUBLIC LICENSE
# See the file 'LICENSE' for details
# ---------------------------------------------------------------------
# EN:
#     - Touch or modify the code below. If there is an error,
#     - please fix it and make a pull request ;)

from configs.config import *
from configs.util import *
from configs.term import *
from configs.menu_builder import *
import os
import sys
import re
try:
    import requests
except:
    ErrorModule(e)

tool_path = os.path.dirname(os.path.abspath(__file__))
scripts_path = os.path.join(tool_path, "scripts")

line_len = os.get_terminal_size().columns#120
t_len = (line_len//3)-2
# tab len

# activating venv
if os_name == "Linux":venv_python = os.path.join(tool_path, ".venv", "bin", "python3")
else:venv_python = os.path.join(tool_path, ".venv", "Scripts", "python3.exe")
if not os.path.exists(venv_python):print("#>  Please run the setup.py")
elif sys.executable != venv_python:os.execv(venv_python, [venv_python] + sys.argv)

#variables

options = [
    [ # Menu 0
        [
            (0,"venv Test ($ env)"),
            (0,"formating test ($ text)"),
        ],
        [
            (1, "Website-Vulnerability-Scanner"),
            (2, "Website-Info-Scanner"),
            (3, "Website-Url-Scanner"),
            (4, "Ip-Scanner"),
            (5, "Ip-Port-Scanner"),
            (6, "Ip-Pinger"),
        ],
        [
            (11, "Get-Image-Exif"),
            (12, "Username-Tracker"),
            (13, "Email-Lookup"),
            (14, "Phone-Number-Lookup"),
            (15, "Ip-Lookup"),
        ],
    ],
    [ # Menu 1
        [
            (21, "Password-Zip-Cracked-Attack"),
            (22, "Password-Hash-Decrypted-Attack"),
            (23, "Password-Hash-Encrypted"),
            (24, "Search-In-DataBase"),
            (25, "Dark-Web-Links"),
            (26, "Ip-Generator"),
        ],
        [
            (31, "Roblox-Cookie-Info"),
            (32, "Roblox-Id-Info"),
            (32, "Roblox-User-Info"),
        ],
        [
            (41, "Discord-Server-Info"),
            (42, "Discord-Webhook-Info"),
            (43, "Discord-Webhook-Generator"),
        ],
    ],
]
men_h_txt = [[" Intern "," Network Scanner "," Osint "],[" Utilities "," Roblox "," Discord "]]

def get_tool_script_name(id):
    for menu in options:
        for tab in menu:
            for function in tab:
                if id == function[0]:
                    return function[1]
    return None  # Falls nichts gefunden wird

def StartScript(script_name,cwd=tool_path):
    env = os.environ.copy()
    env["PYTHONPATH"] = tool_path
    command = [sys.executable, os.path.join(tool_path, "scripts", script_name + ".py")]
    subprocess.run(command, env=env, cwd=cwd)



def menu_head_builder(menu_index):
    categorys = men_h_txt[menu_index]
    if menu_index == 0:
        start_txt, end_txt = INFO_TXT, NEXT_TXT
    elif menu_index + 1 == len(options):
        start_txt, end_txt = BACK_TXT, END_TXT
    else:
        start_txt, end_txt = BACK_TXT, NEXT_TXT

    rendered_tabs = []
    for cat in categorys:
        l = len(cat)
        a, b, c = f"┌{'─'*l}┐", f"┤{cat}├", f"└{'─'*l}┘"
        blub = t_len - len(a)
        mod = blub % 2
        spacea, spaceb = (blub // 2) - 1, (blub // 2) + mod
        rendered_tabs.append([
            " " * (spacea + 1) + a + " " * spaceb,
            "┬" + "─" * spacea + b + "─" * spaceb,
            "│" + " " * spacea + c + " " * spaceb
        ])

    outa = "".join(tab[0] for tab in rendered_tabs)
    outb = "".join(tab[1] for tab in rendered_tabs)
    outc = "".join(tab[2] for tab in rendered_tabs)

    txt_len = len(start_txt[0])
    outa = "   " + outa
    outb = "   " + outb
    outc = "   " + outc
    outa = start_txt[0] + outa[txt_len:-txt_len] + end_txt[0]
    outb = start_txt[1] + outb[txt_len:-txt_len] + end_txt[1]
    outc = start_txt[2] + outc[txt_len:-txt_len] + end_txt[2]
    return StyleText(" .\n" + outa + "\n" + outb + "\n" + outc,True)

def menu_builder(menu_index):
    menu = "   "
    site_tabs = len(options[menu_index])
    biggest_tab_len = len(max(options[menu_index], key=len))
    for i in range(biggest_tab_len):  # lines == option
        for ti in range(site_tabs):  # tab index
            options_count = len(options[menu_index][ti])
            if not i >= options_count:
                if i + 1 == options_count:
                    sym = "└"
                else:
                    sym = "├"

                id, option_name = options[menu_index][ti][i]
                if not id == 0:
                    if id < 10:id_str = "0" + str(id)
                    else:id_str = str(id)
                else:id_str = ".."
                    # └─ [..]
                option_string = f"[{id_str}] {option_name}{" "*(t_len-8-len(option_name))}".replace(
                    "-", " "
                )
                menu += f"{sym}─ {option_string}"
            else:
                menu += "-".center(t_len)
        menu += "\n   "
    return StyleText(menu, True)


# REDTIGER
rt_detected = os.path.exists(os.path.join(scripts_path,"RedTiger-Tools"))
print(rt_detected)
if rt_detected:
    options[0][0].append((0,"RedTiger ($ rt)"))


# UPDATE
try:
    #new_version = re.search(r'version\s*=\s*"([^"]+)"', requests.get(config_url).text).group(1)
    new_version = "0.1.0"
except: new_version = version

if new_version != version:
    options[0][0].append((0,"Update available! ($ up)"))
    #webbrowser.open(github_url)
    #input(f"{BEFORE + current_time_hour() + AFTER} {INFO} Please install the new version of the tool: {white + version_tool + red} -> {white + new_version} ")
    v = f"New Version: {version} -> {new_version}"
    Clear()
else: v = version

menu_index = 0
if __name__ == "__main__":
    while True:
        Clear()

        Title(f"Menu {menu_index}")
        print(StyleText(CenterMultilineText(banner,line_len)))
        print(StyleText(CenterMultilineText(v,line_len)))
        print(menu_head_builder(menu_index))
        print(menu_builder(menu_index))
        choice = input(
            StyleText(
                f""" ┌──(user@{tool_name})─[~/{os_name}/Menu-{menu_index}]\n └─$ """,
                True,
                " └┌─()[]~",
            )
            + reset
        )

        if choice in ["N", "n", "NEXT", "Next", "next"]:
            menu_index = (menu_index + 1) % len(options)
        elif choice in ["B", "b", "BACK", "Back", "back"]:
            menu_index = (menu_index - 1) % len(options)
        
        elif choice in ["Q", "q", "exit", "quit"]:
            exit()

        elif choice in ["I", "i", "INFO", "Info", "info"]:
            StartScript(os.path.join("intscripts", "info"))
            Continue()

        elif choice.isdigit():
            StartScript(get_tool_script_name(int(choice)))
        
        elif choice == "rt":
            if rt_detected:
                print(StyleText("Launching RedTiger..."))
                # LAUNCH RT
                StartScript(os.path.join("RedTiger-Tools", "Setup"),os.path.join(tool_path, "scripts", "RedTiger-Tools"))
            else:
                print(rt_error)
            Continue()

        elif choice == "env":
            print(f"Inside {tool_name}:",sys.executable)
            StartScript(os.path.join("intscripts", "env-check"))
            Continue()

        elif choice == "text":
            StartScript(os.path.join("intscripts", "text-style-check"))
            Continue()

