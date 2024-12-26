import os, platform
import colorama 

import time
import survey

from pathlib import Path

def clear():
    if platform.system() == "Linux" or platform.system() == "Darwin":
                os.system("clear")
    else:
                os.system("cls")

def rm(file):
    if platform.system() == "Linux" or platform.system() == "Darwin":
                os.system(f"rm {file}")
    else:
                os.system(f"del {file}")

def create(file):
    if platform.system() == "Linux" or platform.system() == "Darwin":
                Path(file).touch()
    else:
                os.system(f"echo. 2>{file}")

global installed
installed = False

def install():
    global installed
    if not installed:
        clear()
        print("""
        Preparing Pyndows 1.0 Installer...
        [                                 ]
        """)
        time.sleep(3)
        clear()
        print("""
        Preparing Pyndows 1.0 Installer...
        [---------------------------------]
        """)
        time.sleep(0.5)
        clear()
        print("Pyndows 1.0 Installer")
        print("─────────────────────")
        time.sleep(3)
        print("[+] Formatting drive: pyndows_drive...")
        time.sleep(3)
        print("[+] Formatted drive: pyndows_drive. Installing Pyndows 1.0...")
        time.sleep(10)
        clear()
        print("Pyndows 1.0 Installer")
        print("─────────────────────")
        print("[+] Pyndows 1.0 has been installed to drive: pyndows_drive")
        time.sleep(1)
        name = input("[?] Enter username: ")
        print(f"Pyndows 1.0 is ready to boot. Rebooting in 3s.")
        create("username")
        open("username", "w").write(name)
        installed = True
        rm("installed")
        create("installed")
        open("installed", "w").write("y")
        time.sleep(3)
        clear()
        os.system("python main.py")

    else:
        pass