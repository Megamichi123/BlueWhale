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
    import tkinter as tk
    from tkinter import filedialog
except Exception as e:
    ErrorModule(e)

Title("Search DataBase")

try:

    def ChooseFolder():
        try:
            print(
                f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Enter database folder path -> {reset}"
            )
            if sys.platform.startswith("win"):
                root = tk.Tk()
                root.iconbitmap(os.path.join(tool_path, "Img", "incon.ico"))
                root.withdraw()
                root.attributes("-topmost", True)
                folder_database = filedialog.askdirectory(
                    parent=root, title=f"{name_tool} {version} - Choose a folder"
                )
            elif sys.platform.startswith("linux"):
                folder_database = filedialog.askdirectory(
                    title=f"{name_tool} {version} - Choose a folder"
                )
            print(
                f"{BEFORE + current_time_hour() + AFTER} {INFO} Folder path: {white + folder_database}"
            )
        except:
            folder_database = input(
                f"{BEFORE + current_time_hour() + AFTER} {INPUT} Enter database folder path -> {reset}"
            )

        return folder_database

    folder_database = ChooseFolder()
    search = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Search -> {reset}")

    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in DataBase..")

    def TitleSearch(files_searched, element):
        Title(f"Search DataBase - File Total: {files_searched} - File: {element}")

    try:
        files_searched = 0

        def Check(folder):
            global files_searched
            results_found = False
            folder = os.path.join(folder)
            print(
                f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in {white}{folder}"
            )
            for element in os.listdir(folder):
                chemin_element = os.path.join(folder, element)
                if os.path.isdir(chemin_element):
                    Check(chemin_element)
                elif os.path.isfile(chemin_element):
                    try:
                        with open(chemin_element, "r", encoding="utf-8") as file:
                            line_number = 0
                            files_searched += 1
                            TitleSearch(files_searched, element)
                            for line in file:
                                line_number += 1
                                if search in line:
                                    results_found = True
                                    line_info = line.strip().replace(
                                        search, f"{color.YELLOW}{search}{white}"
                                    )
                                    print(
                                        f"""{blue}
- Folder : {white}{folder}{blue}
- File   : {white}{element}{blue}
- Line   : {white}{line_number}{blue}
- Result : {white}{line_info}
    """
                                    )
                    except UnicodeDecodeError:
                        try:
                            with open(chemin_element, "r", encoding="latin-1") as file:
                                files_searched += 1
                                line_number = 0
                                TitleSearch(files_searched, element)
                                for line in file:
                                    line_number += 1
                                    if search in line:
                                        results_found = True
                                        line_info = line.strip().replace(
                                            search, f"{color.YELLOW}{search}{white}"
                                        )
                                        print(
                                            f"""{blue}
- Folder : {white}{folder}{blue}
- File   : {white}{element}{blue}
- Line   : {white}{line_number}{blue}
- Result : {white}{line_info}
    """
                                        )
                        except Exception as e:
                            print(
                                f'{BEFORE + current_time_hour() + AFTER} {ERROR} Error reading file "{white}{element}{blue}": {white}{e}'
                            )
                    except Exception as e:
                        print(
                            f'{BEFORE + current_time_hour() + AFTER} {ERROR} Error reading file "{white}{element}{blue}": {white}{e}'
                        )
            return results_found

        results_found = Check(folder_database)
        if not results_found:
            print(
                f'{BEFORE + current_time_hour() + AFTER} {INFO} No result found for "{white}{search}{blue}".'
            )

        print(
            f"{BEFORE + current_time_hour() + AFTER} {INFO} Total files searched: {white}{files_searched}"
        )

    except Exception as e:
        print(
            f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error during search: {white}{e}"
        )

    Continue()

except Exception as e:
    Error(e)
