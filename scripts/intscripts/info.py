from configs.util import *
from configs.term import *
from configs.config import *
from os import system, path

Title("Info")
try:
    import webbrowser

    print(
        f"\n{BEFORE + current_time_hour() + AFTER} {WAIT} Information Recovery..{reset}"
    )

    w_str = ""
    for w in Websites:
        w_str += f"   - {w}\n"
    Slow(
        f"""
    {INFO_ADD} Tool Name:  {white}{tool_name}
    {INFO_ADD} Tool Type:  {white}{type_tool}
    {INFO_ADD} Version  :  {white}{version}
    {INFO_ADD} Platform :  {white}{platform}
    {INFO_ADD} Github   :  {white}{github_url}
    {INFO_ADD} License  :  {white}{license}

    {INFO_ADD} Main-Dev :  {white}{main_dev}
    {INFO_ADD} creator  :  {white}{creator}
    Websites:
    {w_str}
    """
    )

    license_read = input(
        f"{BEFORE + current_time_hour() + AFTER} {INPUT} Open 'LICENSE' ? (y/n) -> {reset}"
    )
    if license_read in ["y", "Y", "Yes", "yes", "YES"]:
        if os_name == "Linux":
            system("sdg-open "+path.join(tool_path,license))
        else:
            system("start "+path.join(tool_path,license))


except Exception as e:
    Error(e)
