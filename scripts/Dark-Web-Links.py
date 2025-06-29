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

Title("Dark Web Links")

try:
    links = {
        "Search Engine": {
            "Torch": "http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/",
            "Danex": "http://danexio627wiswvlpt6ejyhpxl5gla5nt2tgvgm2apj2ofrgm44vbeyd.onion/",
            "Sentor": "http://e27slbec2ykiyo26gfuovaehuzsydffbit5nlxid53kigw3pvz6uosqd.onion/",
            "Hidden Answers": "http://answerszuvs3gg2l64e6hmnryudl5zgrmwm3vh65hzszdghblddvfiqd.onion/",
            "riseup searx": "http://ozmh2zkwx5cjuzopui64csb5ertcooi5vya6c2gm4e3vcvf2c2qvjiyd.onion/",
        },
        "Government": {
            "UK Passport Renewal": "http://3bp7szl6ehbrnitmbyxzvcm3ieu7ba2kys64oecf4g2b65mcgbafzgqd.onion/",
        },
    }

    def format_links(links):
        display_link = ""

        for category, sites in links.items():
            display_link += "\n" + category + "\n"

            def add_sites(prefix, sites_dict):
                nonlocal display_link
                for i, (site, url) in enumerate(sites_dict.items()):
                    if isinstance(url, dict):
                        display_link += f"{prefix}├─ {site}\n"
                        add_sites(prefix + "│   ", url)
                    else:
                        if i == len(sites_dict) - 1:
                            display_link += f"{prefix}└─ {site}: {url}" + "\n"
                        else:
                            display_link += f"{prefix}├─ {site}: {url}" + "\n"

            add_sites("", sites)

        return display_link

    formatted_links = format_links(links)
    Slow(tor_banner + StyleText(formatted_links, True))
    Continue()

except Exception as e:
    Error(e)
