#!/usr/bin/env python3
# GNU GENERAL PUBLIC LICENSE
# See the file 'LICENSE' for details
# ---------------------------------------------------------------------
# EN:
#     - Touch or modify the code below. If there is an error,
#     - please fix it and make a pull request ;)
from .config import *
from .term import *

try:
    import subprocess # used in other scripts...
    import colorama
    import ctypes
    import os
    import time
    import sys
    import datetime
    import sys
    import requests
    import random
except Exception as e:
    print(
        f'Modules of the python library required for {tool_name} are not installed, make sure you have correctly installed python and have launched the "setup.py" file which will install all the necessary modules.'
    )
    input(f"Error: {e}")

#tool_path = os.path.dirname(os.path.abspath(__file__))


#color_webhook = 0xA80505
#username_webhook = name_tool
#avatar_webhook = "https://media.discordapp.net/attachments/1369051349106430004/1369054652213231687/RedTiger-Logo-1-Large.png?ex=6821b740&is=682065c0&hm=fb74ee5ac9239dd15605a36bfde4da265ee788fe83b1938b0fc3b1dd6ffa8871&=&format=webp&quality=lossless&width=1032&height=1032"

color = colorama.Fore
reset = color.RESET
white = color.WHITE
blue = color.BLUE
red = color.RED
green = color.GREEN
yellow = color.YELLOW


if sys.platform.startswith("win") or os.name == "nt":
    os_name = "Windows"
elif sys.platform.startswith("linux") or sys.platform.startswith("Linux"):
    os_name = "Linux"
else:
    os_name = "Unknown"

def activate_venv(argv):
    if os_name == "Linux":
        venv_python = os.path.join(tool_path, ".venv", "bin", "python3")
    else:
        venv_python = os.path.join(tool_path, ".venv", "Scripts", "python3.exe")

    if not os.path.exists(venv_python):
        print("#>  Please run the setup.py")
    elif sys.executable != venv_python:
        os.execv(venv_python, [venv_python] + argv)


def current_time_day_hour():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def current_time_hour():
    return datetime.datetime.now().strftime("%H:%M:%S")


BEFORE = f"{blue}[{white}"
AFTER = f"{blue}]"

BEFORE_GREEN = f"{green}[{white}"
AFTER_GREEN = f"{green}]"

INPUT = f"{BEFORE}>{AFTER} |"
INFO = f"{BEFORE}!{AFTER} |"
ERROR = f"{BEFORE}x{AFTER} |"
ADD = f"{BEFORE}+{AFTER} |"
WAIT = f"{BEFORE}~{AFTER} |"
NOTE = f"{BEFORE}NOTE{AFTER} |"

GEN_VALID = f"{BEFORE_GREEN}+{AFTER_GREEN} |"
GEN_INVALID = f"{BEFORE}x{AFTER} |"

INFO_ADD = f"{white}[{blue}+{white}]{blue}"

def Title(title):
    if os_name == "Windows":
        ctypes.windll.kernel32.SetConsoleTitleW(f"{name_tool} {version} - {title}")
    elif os_name == "Linux":
        sys.stdout.write(f"\x1b]2;{tool_name} {version} - {title}\x07")


def Clear():
    if os_name == "Windows":
        os.system("cls")
    elif os_name == "Linux":
        os.system("clear")


def Slow(text):
    delay = 0.03
    lines = text.split("\n")
    for line in lines:
        print(line)
        time.sleep(delay)


def Continue():
    input(
        f"{BEFORE + current_time_hour() + AFTER} {INFO} Press to continue -> " + reset
    )


def Error(e):
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error: {white}{e}", reset)
    Continue()


# remove this fucking useless functions...


def ErrorChoice():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Choice !", reset)
    time.sleep(3)


def ErrorId():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid ID !", reset)
    time.sleep(3)


def ErrorUrl():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid URL !", reset)
    time.sleep(3)


def ErrorResponse():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Response !", reset)
    time.sleep(3)


def ErrorEdge():
    print(
        f"{BEFORE + current_time_hour() + AFTER} {ERROR} Edge not installed or driver not up to date !",
        reset,
    )
    time.sleep(3)


def ErrorToken():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Token !", reset)
    time.sleep(3)


def ErrorNumber():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Number !", reset)
    time.sleep(3)


def ErrorWebhook():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Webhook !", reset)
    time.sleep(3)


def ErrorCookie():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Cookie !", reset)
    time.sleep(3)


def ErrorUsername():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Username !", reset)
    time.sleep(3)


def ErrorPlateform():
    print(
        f"{BEFORE + current_time_hour() + AFTER} {ERROR} Unsupported Platform !", reset
    )
    time.sleep(3)


def ErrorModule(e):
    print(
        f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error Module: {white}{e}",
        reset,
    )
    Continue()



def ChoiceUserAgent():
    file_user_agent = os.path.join(tool_path, "2-Input", "Headers", "UserAgent.txt")

    with open(file_user_agent, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if lines:
        user_agent = random.choice(lines).strip()
    else:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36"

    return user_agent


def CheckWebhook(webhook):
    try:
        response = requests.get(webhook)
        if response.status_code == 200 or response.status_code == "200":
            return True
        else:
            return False
    except:
        return None


def Choice1TokenDiscord():
    def CheckToken(token_number, token):
        response = requests.get(
            "https://discord.com/api/v8/users/@me",
            headers={"Authorization": token, "Content-Type": "application/json"},
        )

        if response.status_code == 200:
            user = requests.get(
                "https://discord.com/api/v8/users/@me", headers={"Authorization": token}
            ).json()
            username_discord = user["username"]
            token_sensur = token[:-25] + "." * 3
            print(
                f" {BEFORE}{token_number}{AFTER} -> {blue}Status: {white}Valid{blue} | User: {white}{username_discord}{blue} | Token: {white}{token_sensur}"
            )
        else:
            print(
                f" {BEFORE}{token_number}{AFTER} -> {blue}Status: {white}Invalid{blue} | {blue}Token: {white}{token}"
            )

    file_token_discord_relative = "\\2-Input\\TokenDisc\\TokenDisc.txt"
    file_token_discord = os.path.join(
        tool_path, "2-Input", "TokenDisc", "TokenDisc.txt"
    )

    tokens = {}
    token_discord_number = 0

    with open(file_token_discord, "r") as file_token:
        print(
            f"{BEFORE + current_time_hour() + AFTER} {INFO} Token Discord ({white}{file_token_discord_relative}{blue}):\n"
        )
        for line in file_token:
            if not line.strip() or line.isspace():
                continue

            token_discord_number += 1
            modified_token = line.strip()
            tokens[token_discord_number] = modified_token
            CheckToken(token_discord_number, modified_token)

    if not tokens:
        print(
            f"{BEFORE + current_time_hour() + AFTER} {INFO} No Token Discord in file: {white}{file_token_discord_relative}{blue} Please add tokens to the file."
        )
        Continue()

        return None

    try:
        selected_token_number = int(
            input(
                f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Token Number -> {reset}"
            )
        )
    except:
        ErrorChoice()

    selected_token = tokens.get(selected_token_number)
    if selected_token:
        r = requests.get(
            "https://discord.com/api/v8/users/@me",
            headers={
                "Authorization": selected_token,
                "Content-Type": "application/json",
            },
        )
        if r.status_code == 200:
            pass
        else:
            ErrorToken()
    else:
        ErrorChoice()
    return selected_token





INFO_TXT  = [" ├─ [I] Info ",
             " └─┬─────────",
             "   │         "]

BACK_TXT  = [" ├─ [B] Back ",
             "─┴─┬─────────",
             "   │         "]


NEXT_TXT  = [" [N] Next ─┐ ",
             "───────────┴─",
             "             "]

END_TXT   =  ["            ",
              "─── --- -- -",
              "            "]

rt_error = StyleText(f"""[x] | RedTiger not Found, 
install it into the "scripts" directory via git:

> cd scripts
> git clone ...

* but DONT run the Setup.py from RedTiger,
  because {tool_name} will run the Setup.py
""",True,">*[x]|")

tor_banner = StyleText(
    r"""
                                                                       ..                                   
                                                                     .:@ :...                               
                .:::::::::::::::::::::::::::::::::.             ....-@@@+..                                 
               .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.           .-@@@@@-.                                    
               :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.          .=@@@@-.                                      
               :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.          -@@@@-.                                       
               :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.      @@ :@@#:.                                         
               :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.       %  @%+:                                          
                ::::::::-*@@@@@@@@@@@@@@@*-::::::::        @@ #:@@@                           ..::::::::    
                         -@@@@@@@@@@@@@@@=                 @@ @+@@@@                      .::+@@@@@@@@@@:   
                         -@@@@@@@@@@@@@@@                @@@  @+@%%@@                    -*@@@@@@@@@@@@@:   
                         :@@@@@@@@@@@@@@@            @@@@    @@+.@@=:@@@@              :*@@@@@@@@@@@@@@@:   
                         :@@@@@@@@@@@@@@@          @@@    ..@:@@+ @@%=-:=@@@          :*@@@@@@@@@@@@@@@@:   
                         :@@@@@@@@@@@@@@@       @@@    .-@@@::@#@# @@#@%*-:@@@       .*@@@@@@@@@@@@@@@@@:   
                         :@@@@@@@@@@@@@@@     @@@   ..@@@+:--=@#.@% @#%@@@#=:@@      *@@@@@@@@@@@@@*-::.    
                         :@@@@@@@@@@@@@@@    @@@  :.@@..-++=@@@@. @ =@+@@@@@#:@@@   -@@@@@@@@@@@@@*:        
                         :@@@@@@@@@@@@@@@    @@  :*@.:-=-+@@%-@@@# @ @:@@@@@@#:@@   -@@@@@@@@@@@@@-         
                         :@@@@@@@@@@@@@@@    @@ .-@ -+=@@@=++=@.-@ @ @-@@@@@@@-@@@  -@@@@@@@@@@@@@.         
                         :@@@@@@@@@@@@@@@    @@ .@@ *@@@:*%=.@@@ @-@ @-%@@@@@@-@@@  -@@@@@@@@@@@@@.         
                         :@@@@@@@@@@@@@@@    @@   @ :@@.%@.@ :@@@ @@@@-@@@@@*:@@@   -@@@@@@@@@@@@@.         
                         :@@@@@@@@@@@@@@@     @@  @@ @@ %@.@ :@@@ @@@@-@@@@@*:@@@   -@@@@@@@@@@@@@.         
                         :@@@@@@@@@@@@@@@      @@   @ @-.* @ -%@@-@ @@*@@@#=:@@     -@@@@@@@@@@@@@.         
                         :@@@@@@@@@@@@@@@       @@@  -@@@  @@ .%* #@@-%#=:-@@@      -@@@@@@@@@@@@@.         
                         -@@@@@@@@@@@@@@%         @@@@   @.  @ =*@@@...-@@@@        -@@@@@@@@@@@@@.         
                          .:::::::::::::.             @@@@@@@@@@@@-*@@@@             ::::::::::::.  
"""
)

discord_banner = StyleText(
    r"""
                                              @@@@                @%@@                                      
                                       @@@@@@@@@@@@               @@@@@@@@@@%                               
                                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          
                                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                         
                                %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                        
                               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                       
                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      
                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                     
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                    
                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                   
                          %@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@%                  
                          %@@@@@@@@@@@@@@@@        %@@@@@@@@@@@%@        @@@@@@@@@@@@@@@@@                  
                          %@@@@@@@@@@@@@@@          @@@@@@@@@@@@          @@@@@@@@@@@@@@@%                  
                         %@@@@@@@@@@@@@@@@          @@@@@@@@@@@%          %@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@%         @@@@@@@@@@@%         %@@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@@@      %@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@%                 
                         %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                           @%@@@@@@@@@@@@@%@@   @@@@%@@@@@@@@@%%%@%@@  @@@@@@@@@@@@@@@@@@                   
                              @@%@@@@@@@@@@@@@                        @%@@@@@@@@@@@%@@                      
                                   @%@@@@@@@                            @@@@@@%%@                           
                                         @@                              @@                           
"""
)

dox_banner = StyleText(
    r"""                                            
                  .:+*#%%#####*++++-.             
                :#%%*+*+-.....                    
             .=%%+++:..                           
           .=%#++=.                               
          -%%+++.                                 
      .  =%%++-          ....                     
      #%+#%++=.        .:#%%%*:                   
      :#@%#+=          :*+:-*%#:                  
       .*@@#.         .-%*::-%%#.                 
        .-%@@%-.      .=%%--%%%-                  
          .:--=*+-:.:-#%%%%%%%%*.                      ██████╗   ██████╗  ██╗  ██╗
               .:-*#%%%%%%%%%%%%%-                     ██╔══██╗ ██╔═══██╗ ╚██╗██╔╝
                  .+%%%*+*%%%%%%%%+...                 ██║  ██║ ██║   ██║  ╚███╔╝ 
                  .+%@@%%%%*#%%%%%%%%%*-.              ██║  ██║ ██║   ██║  ██╔██╗
                   .*%@%%%%%%%%%%%%%%%%%#-.            ██████╔╝ ╚██████╔╝ ██╔╝ ██╗
                   .*%%%%%%%%%%%+#%%%%%%%%%*-.         ╚═════╝   ╚═════╝  ╚═╝  ╚═╝
                  .=%%%%%%%%%%%%@%*%%%%%####=-==  
                  :*%%%%%%%%%%%%%%%*#%%%%#+=-==+  
                 .+=*%#%%%%%%%%%%%%%**%%#+**+-:-  
                .-=::*-%%%%%%%%%%%%###*-*%###+:   
                ...:..%%%%%%%%%%%%%%#:=*+-:.      
                     *%%%%%%%%%%%%%%%%.           
                    :#%%%%%%%%%%%%%%%%+           
                   .*%%%%%%%%%%%%%%%%%#.          
                  .=%%%%%%%%%%%%%%%%%%#:          
                  .+%%%%%%%%%%%%%%%%%%%*.         
                    :+*#%%%@%%%%%%%%%%%%#:.       
                      ..:==+*#%#*=-:.:-+***:."""
)


osint_banner = StyleText(
    r"""                                                                                                
                                          ...:----:...                                              
                                     .:=#@@@@@@@@@@@@@@%*-..                                        
                                  .:#@@@@@@@%#*****#%@@@@@@@+..                                     
                               ..-@@@@@%-...... ........+@@@@@@..                                   
                               :%@@@@=..   .#@@@@@@@@#=....+@@@@*.                                  
                             .+@@@@=.      .*@@@%@@@@@@@@=...*@@@@:.                                
                            .#@@@%.                 .=@@@@@=. .@@@@-.                               
                           .=@@@#.                    .:%@@@*. -@@@%:.                              
                           .%@@@-                       .*@@*. .+@@@=.                              
                           :@@@#.                              .-@@@#.                              
                           -@@@#                                :%@@@.                              
                           :@@@#.                              .-@@@#.                              
                           .%@@@-.                             .+@@@=.                              
                           .+@@@#.                             -@@@%:.                              
                            .*@@@%.                          .:@@@@-.                               
                             .+@@@@=..                     ..*@@@@:.                                
                               :%@@@@-..                ...+@@@@*.                                  
                               ..-@@@@@%=...         ...*@@@@@@@@#.                                 
                                  .:*@@@@@@@%*++++**@@@@@@@@=:*@@@@#:.                              
                                     ..=%@@@@@@@@@@@@@@%#-.   ..*@@@@%:.                            
                                        .....:::::::....       ...+@@@@%:                           
                                                                  ..+@@@@%-.                        
                                                                    ..=@@@@%-.                      
                                                                      ..=@@@@@=.                    
                                                                         .=%@@@@=.                  
                                                                          ..-%@@@-.                 
                                                                             ....
"""
)

wifi_banner = StyleText(
    r"""
                                                 @@@@@@@@@@@@@@@@@@@                                 
                                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                         
                                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                    
                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                
                             @@@@@@@@@@@@@@@@@@                       @@@@@@@@@@@@@@@@@@             
                           @@@@@@@@@@@@@@                                   @@@@@@@@@@@@@@@          
                        @@@@@@@@@@@@@              @@@@@@@@@@@@@@@              @@@@@@@@@@@@@        
                       @@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@          @@@@@@@@@@@       
                       @@@@@@@@         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         @@@@@@@@       
                        @@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@        
                                  @@@@@@@@@@@@@@@                   @@@@@@@@@@@@@@@                  
                                @@@@@@@@@@@@@                           @@@@@@@@@@@@@                
                               @@@@@@@@@@            @@@@@@@@@@@            @@@@@@@@@@               
                                @@@@@@@         @@@@@@@@@@@@@@@@@@@@@         @@@@@@@                
                                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@                            
                                          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          
                                         @@@@@@@@@@@             @@@@@@@@@@@                         
                                        @@@@@@@@@                   @@@@@@@@@                        
                                         @@@@@@        @@@@@@@        @@@@@@                         
                                                    @@@@@@@@@@@@@                                    
                                                   @@@@@@@@@@@@@@@                                   
                                                  @@@@@@@@@@@@@@@@@                                  
                                                  @@@@@@@@@@@@@@@@@                                  
                                                   @@@@@@@@@@@@@@@                                   
                                                    @@@@@@@@@@@@@                                    
                                                       @@@@@@@                                       
"""
)


phishing_banner = StyleText(
    r"""
                                                         .+#%@@%#+.                                     
                                                    .#@@@@@@@@@@@@@@@@#.                                
                                                  +@@@@@@@@@@@@@@@@@@@@@@*                              
                                                .%@@@@@@@@@@@@@@@@@@@@@@@@%.                            
                                                %@@@@@@@@@@@@@@@@@@@@@@@@@@%                            

                                               %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#                          
                                                -..........................-.                           
                                                %@@@@@@%%@@@@@@@@@@@%@@@@@@%                            
                                                %@@@#     .%@@@@%.     *@@@%                            
                                                . :+%%+--+%@#::#@%*--+%%+: .                            
                                                                           .                            
                                                 :                        :                             
                                                  -                      =                              
                                                    -                  -                                
                                                       -=          --                                   
                                               -+#%@@@@@@=        =@@@@@@%#+-                           
                                            *@@@@@@@@@@@@=        =@@@@@@@@@@@@*                        
                                          *@@@@@@@@@@@@@@+        +@@@@@@@@@@@@@@#                      
                                         *@@@@@@@@@@@@@@@@%=    -%@@@@@@@@@@@@@@@@#                     
                                        -@@@@@@@@@@@@@@@@@@@%#*%@@@@@@@@@@@@@@@@@@@-                    
                                        -@@@@@@@@@@@@@@@@@@@%::%@@@@@@@@@@@@@@@@@@@-                    
                                        -@@@@@@@@@@@@@@@@@@@%::%@@@@@@@@@@@@@@@@@@@-                    
                                        -@@@@@@@@@@@@@@@@@@@%::%@@@@@@@@@@@@@@@@@@@-  """
)

decrypted_banner = StyleText(
    r"""
                                         ^M@@@@@@@@@v                                    
                                      v@@@@@@@@@@@@@@@@@                                 
                                    _@@@@@@@}    ;a@@@@@@@                               
                                   M@@@@@            @@@@@@                              
                                  ;@@@@@              O@@@@@                             
                                  @@@@@v               @@@@@                             
                                  @@@@@;               @@@@@                             
                                  @@@@@;               @@@@@                             
                                  @@@@@;                                                 
                                  @@@@@;        v@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         
                                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       
                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@j     @@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@v       @@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@_   @@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|      
                                               ^@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@O  """
)


encrypted_banner = StyleText(
    r"""
                                                       j@@@@@^                                 
                           _@v   p@@@@j           j@@@@@@@@@@@@@@@;          |@@@@M   v@}      
                          @@@@@} >@@@@    v@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@p    @@@@_ _@@@@@     
                          >@@@v    @@     v@@@@@@@@@@@@      p@@@@@@@@@@@a     @@    j@@@_     
                           ^@@     @@@@   |@@@@@@@@@@^ @@@@@@; @@@@@@@@@@p   p@@@     M@;      
                           ^@@            >@@@@@@@@@@ p@@@@@@@ M@@@@@@@@@j            M@;      
                           ^@@@@@@@@@@@}   @@@@@@@@|            >@@@@@@@@;   @@@@@@@@@@@;      
                                           }@@@@@@@|    O@@@    >@@@@@@@M                      
                          |@@@@             @@@@@@@|     M@     >@@@@@@@^            @@@@j     
                          @@@@@@@@@@@@@@@>   @@@@@@|    O@@@    >@@@@@@    @@@@@@@@@@@@@@@     
                            ^                 @@@@@v            }@@@@@^                ^       
                                 p@@@@@@@@@^   M@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@p            
                                 p@_            ^@@@@@@@@@@@@@@@@@@>            >@a            
                                @@@@O              @@@@@@@@@@@@@@              J@@@@           
                               ;@@@@@                 J@@@@@@p                 @@@@@>          
                                  ;              p@              p@>  M@@_       ;             
                                          @@@@p  p@_  ;      j_  a@@@@@@@@j                    
                                         ^@@@@@@@@@   v@_   O@}       M@@_                     
                                            ;         p@|   O@}      }}                        
                                                    >@@@@@  O@@@@@@@@@@@J                      
                                                     p@@@j         ;@@@@^                      """
)


scan_banner = StyleText(
    r"""
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                   >|a@@@@@@@@@|                                                
                                              }@@@@@@@@@@@@@@@@| 000M|                                          
                                          ;@@@@@@O  @@@@@@@@@@@|  j000000_                                      
                                       }@@@@@v   |@@@@@@@@@@@@@| 00J  |00000j                                   
                                     @@@@@_     @@@@@@@@@@@@@@@| 0000    ;00000^                                
                                  ;@@@@v       _@@@@@@@     >@@| 0000v      }0000_                              
                                ^@@@@_         @@@@@@@      ^O@| 00000        ;0000_                            
                                 @@@@;         @@@@@@@      ;p@| 00000         0000^                            
                                   @@@@p       >@@@@@@@^    >@@| 0000v      J0000;                              
                                     O@@@@|     M@@@@@@@@@@@@@@| 0000    >00000                                 
                                       ;@@@@@J^  }@@@@@@@@@@@@@| 00v  j00000}                                   
                                          >@@@@@@@_;@@@@@@@@@@@| ;M000000_                                      
                                              >@@@@@@@@@@@@@@@@| 00000}                                          
                                                   ^jpM@@@@@@@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@| 
"""
)


sql_banner = StyleText(
    r"""
                                                                                   ^                      
                                                                                 J@@M                     
                                                                        ^         @@@@^                   
                                                                     ;@@@>         J@@@                   
                                                                      ;@@@J      ;j j@@@}                 
                                                                       ^@@@O  ^J@@@@^;@@@}                
                                                                   >@@@; @@@@^;@@@@@> ;@@@O               
                                                                >j _@@@@j p@@@^;@|      @@@>              
                                                              }@@@@  @@@@j J@@@>                          
                                                          ^a@@ _@@@@;_@@@@a }@@@>                         
                                                       ^} v@@@@^;@@@@@@@@@@@ >@@@v                        
                                                     |@@@@ ^@@@@J@@@@@@@@@@@@;^@@@J                       
                                                  J@M }@@@@ _@@@@@@@@@@@@@@j    @@j                       
                                               ; v@@@@ >@@@@@@@@@@@@@@@@j                                 
                                            ^@@@@ ;@@@@v@@@@@@@@@@@@@j^                                   
                                            a@@@@@ >@@@@@@@@@@@@@@a                                       
                                            |@@@@@@@@@@@@@@@@@@J                                          
                                          |a ;@@@@@@@@@@@@@@a;                                            
                                         @@@@ ;@@@@@@@@@@@;                                               
                                        |@@@@@> @@@@@@@>                                                  
                                     }@@@pO@MJ   >pp_                                                     
                                  ;@@@a                                                                   
                               ;@@@p;                                                                     
                            >p@@M>                                                                        
                           }@@>                                                                           
"""
)


map_banner = StyleText(
    r"""
                                      :**+ :::+*@@.                                                         
                              +: @ = =.  :#@@@@@@@@                 :     .=*@@#     -                      
                 @@@@-. :=: +@@.:% *=@@:   @@@@@@          :#=::     .:@=@@@@@@@@@@@@@@@@@@@@--.-:          
             .#@@@@@@@@@@@@@@@@@@:# .@@   #@@    :@-     +@@:@@@+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*        
             #*   :%@@@@@@@@@@:   .@@#*              ..  ##@ *#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-:- %=         
                   *@@@@@@@@@@@@%@@@@@@@            = @=+@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+   #.        
                   #@@@@@@@@@##@@@@@= =#              #@@@#@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=            
                  @@@@@@@@@@@#+#@@=                 :@@@-.#-*#@.  .@@.=%@@@@%@@@@@@@@@@@@@@@@@=  +          
                 :@@@@@@@@@@@@@@:                   :@@    # - @@@@@@@ =@@@*#*@@@@@@@@@@@@@=.=-  #:         
                  :@@@@@@@@@@@+                     @@@@@@@: :    @@@@@@@@@@@@@@@@@@@@@@@@@@@               
                   #@@@@@    @                     #%@@@@@@@@@@@@@@@@@:@@@@@@@@@@@@#@@@@@@@@@:              
                     @@@     .                    @@@@@@@@@@@@@@@@-%@@@%@#   @@@@@@#=@#@@@@@==              
                     =@@##@   =:*.                @@@@@@*@@@@@@@@@@-=@@@@.    +@@@:  %#@@#=   :             
                         .=@.                     #@@@@@@@@#@@@@@@@@+#:        %@      *%@=                 
                            . @@@@@@               @#@@*@@@@@@@@@@@@@@@=        :-     -       =.           
                             :@@@@@@@#=                   @@@@@@@@@@@@-               :+%  .@=              
                            -@@@@@@@@@@@@                 @+@@@@*+@@#                   @. @@.#   # :       
                             @@@@@@@@@@@@@@@               @@@@@*@@@                     :=.        @@@.    
                              @@@@@@@@@@@@@                #@@@@@@%@.                             :  :      
                               *@@@@@@@@@@%               :@@@@@@@@@ @@.                      .@@@@=:@      
                                :@@@@@@@@@                 #@@@@@@   @:                    .#@@@@@@@@@@     
                                :@@@@%@@                   .@@@@@-   .                     @@@@@@@@@@@@*    
                                :@@@@@@.                    *@@@-                          @@@@#@@@@@@@     
                                :@@@@@@@                     *@@@-                          @@@@#@@@@@@@     
                                .@@@@@                                                           =@@@:    @=
                                 =@@                                                              =    #+   
                                  @%                                                                        
"""
)


virus_banner = StyleText(
    r"""
                                                         ...                                       
                                                  +%@@@@@@@@@@@@@*.                                
                                               #@@@@@@@@@@@@@@@@@@@@@:                             
                                             %@@@@@@@@@@@@@@@@@@@@@@@@@:                           
                                           .@@@@@@@@@@@@@@@@@@@@@@@@@@@@:                          
                                           :@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                          
                                           =@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                          
                                           :@@@@@@@@@@@@@@@@@@@@@@@@@@@@*                          
                                            #@@@%.     .@@@@+      #@@@%                           
                                             +@@=      .@@@@=      .@@#                            
                                              @@@@%%%@@@@%*@@@@%%%@@@@=                            
                                             .@@@@@@@@@@*  -@@@@@@@@@@=                            
                                           .    .::-@@@@@@@@@@@@+::.    .                          
                                         *@@@@#     @@@@@@@@@@@@-    +@@@@@.                       
                                         #@@@@@%    -%@@@@@@@@%=.   *@@@@@@:                       
                                       @@@@@@@@@@@@:            .#@@@@@@@@@@@-                     
                                       +@@@@@*#@@@@@@@@*:  .+@@@@@@@@%*%@@@@#                      
                                                    *@@@@@@@@@@%.                                  
                                        .==.    .+%@@@@@@@%@@@@@@@+:     :=:                       
                                       @@@@@@@@@@@@@@*.       :@@@@@@@@@@@@@@=                     
                                       -@@@@@@@@%=                :#@@@@@@@@*                      
                                         *@@@@@:                     %@@@@@:                       
                                         :%@@%.                       *@@@=                       
"""
)
