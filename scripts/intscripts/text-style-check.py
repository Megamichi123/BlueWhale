from configs.util import *
from configs.term import *


texta = f"thats a {red}test{reset} for formating"

print("#>  text_a no formating: ",texta)
print("#>  text_a    formating: ",StyleText(texta),"\n\n")


textb = f"""
thats a 
{red}test{reset}
for formating"""

print("#>  text_b no formating: ",textb)
print("\n#>  text_b    formating: ",StyleText(textb))