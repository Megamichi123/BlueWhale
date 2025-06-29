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
    import webbrowser
except Exception as e:
    ErrorModule(e)

Title("Python Obfuscator (Premium)")

try:
    print(StyleText("Comming soon"))
except Exception as e:
    Error(e)
