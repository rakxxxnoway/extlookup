#!/usr/bin/env python3
"""
    * Program is written by rax =3
    * Black/Slash 2025-... All rights reserved
    * Source: https://www.file-extension.info
"""
import argparse
import sys

from bs4 import BeautifulSoup as bs
from colorama import Fore, Back
import requests


# +--------------- Globals ---------------+
parse = argparse.ArgumentParser(
    prog="extlookup",
    description="A small program written in python for looking up file extentions. Written by rax : Black/Slash 2025",
    epilog="All data is taken from 'https://www.file-extension.info'" )
parse.add_argument("ext")
argv = parse.parse_args()


# +--------------- Function ---------------+
def main() -> int:
    url = "https://www.file-extension.info"
    urn = "/format/"
    resp = requests.get(url+urn+argv.ext)

    if resp.status_code != 200:
        return 1
    
    soup = bs(resp.text, "html.parser")

    data = {
        "title": soup.find("h1").text,
        "name": soup.find("h5").text,
        "dev": soup.find("div", class_="value").text.strip(),
        "description": soup.find("span", attrs={"itemprop": "description"}).find("p").text
    }

    for key, val in data.items():
        print("%s[i]%s %s: %s%s%s" % (Fore.GREEN, Fore.WHITE, key.capitalize(), Back.BLUE, val, Back.BLACK))


# +--------------- Main ---------------+
if __name__ == "__main__":
    try:
        if main():
            sys.exit("[!]: Couldn't reach the site!")
    except Exception as e:
        print(f"[!]: Something went wrong\n L->\t{e}")
