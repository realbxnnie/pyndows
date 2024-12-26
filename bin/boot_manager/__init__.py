import os

import installer
import sys, system, platform
import time

import requests

from PIL import Image
from colorama import Fore, Back
from pyfiglet import figlet_format

def clear():
    if platform.system() == "Linux" or platform.system() == "Darwin":
                os.system("clear")
    else:
                os.system("cls")

class boot_manager:
    cmds = {
        'i': 'Install Pyndows 1.0',
        'b': 'Boot an existing OS'
    }
    cmds2 = {
        'b': 'Boot Pyndows 1.0',
    }
    def start():
        clear()
        print(f"{Back.BLUE}{Fore.YELLOW}")
        print("""

╔═══════════════════════╗
║                       ║
║    PYNDOWS BOOT MGR   ║
║                       ║
╚═══════════════════════╝ 
""")
        if open("installed").read() == "n":
         for c in boot_manager.cmds:
            print(f"> {c} - {boot_manager.cmds.get(c)}")
        else:
         for c in boot_manager.cmds2:
            print(f"> {c} - {boot_manager.cmds2.get(c)}")
        
        print('\n')
        cmd = input("> ")
        if not boot_manager.cmds.get(cmd.lower()):
            clear()
            boot_manager.start()
        else:
            if cmd.lower() == "i" and open("installed").read() == "n":
                installer.install()
            elif cmd.lower() == "b":
                system.boot()
