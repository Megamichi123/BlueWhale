import sys
import os
import runpy
from configs.config import banner,tool_name
from time import sleep

tool_path = os.path.dirname(os.path.abspath(__file__))
setup_path = os.path.join(tool_path,"setup.py")
venv_path = os.path.join(tool_path,".venv")
if not os.name == "nt":venv_python_path = os.path.join(venv_path, "bin", "python3")
else:venv_python_path = os.path.join(venv_path, "Scripts", "python3.exe")


def Clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Start
Clear()
print(banner,f"\n\n#> Welcome to {tool_name}, the Setup will install everything in a Virtual Python Enviroment")

# Creating & Activating venv

if not os.path.exists(venv_path):
    print(f"#>     Creating .venv for {tool_name}:\n")
    os.system("python3 -m venv "+venv_path)
    sleep(2)
else:
    print("#>     Creation Sucessfully...\n")

if sys.executable != venv_python_path:
    print("#> Activating venv...\n\n")
    os.execv(venv_python_path, [venv_python_path, setup_path])
runpy.run_path(os.path.join(tool_path,"activate_venv_term.py"))

# Installing modules
os.system("python3 -m pip install --upgrade pip")
os.system("python3 -m pip install -r "+os.path.join(tool_path,"requirements.txt"))
if os.name == "nt":
    os.system("python3 -m pip install pywin32")  # because there is no pywin32 version for linux

if input(f"\n\n#> Launch {tool_name}e? (y/n): ") == "y":
    os.system("python3 "+os.path.join(tool_path,"BlueWhale.py"))
