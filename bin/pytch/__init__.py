import system
import shlex

import time

import platform 
import os

import sys

from pathlib import Path

PYTCH_VERSION = "1.00"

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

class commands:
    def get():
        cmds = {}
        def sfw(back, other, str):
            if other[1].lower() == "list":
                 for i in system.Apps().__dict__.items():
                    print(f"""
[{i[1]['name'][1]}]
""")
            elif other[1].lower() == "install":
                 #other.remove("sfw")
                 #other.remove("install")

                 #print("Installing software:")
                 #for i in other:
                      #print(f"└ {i}")
                 #time.sleep(5)
                 #for i in other:
                      #system.Apps().download(i)
                      #print(f"Installed {i}.")
                print("[Error]: sfw install is in development. Use default apps instead.")
                      
                      
            back()

        cmds['sfw'] = sfw

        def exitc(back, other, str):
            exit()

        cmds['shutdown'] = exitc

        def pynver(back, other, str):
            print(f"Pyndows 1.0")
            print(f"━━━━━━━━━━━━━━━━━━━━━━")
            print(f"Kernel: python-{platform.python_version()}")
            back()

        cmds['pynver'] = pynver

        def pyndows_desktop(back, other, str):
              system.Apps.run("desktop")
        cmds['pyndows-desktop'] = pyndows_desktop

        def reboot(back, other, str):
            time.sleep(3)
            system.reboot()

        cmds['reboot'] = reboot

        def reinstall(back, other, str):
            time.sleep(3)
            rm("installed")
            create("installed")
            open("installed", "w").write("n")
            system.reboot()

        cmds['reinstall'] = reinstall

        def pytch(back, other: list, str):
              try:
                    if other[1] == 'version':
                        print(PYTCH_VERSION) 
                        back()
              except IndexError:
                    print("pytch")
                    print("┕ version")
                    back()
        
        cmds['pytch'] = pytch

        def echo(back, other, str):
            print(other[1])
            back()

        cmds['echo'] = echo
        cmds['print'] = echo

        return cmds

class pytch:
      cmds = [
            'sfw',
            'shutdown',
            'print',
            'echo'
            'open',
            'reboot',
            'pytch',
            'reinstall',
            'pynver',
            'pyndows-desktop'
      ]
      cfuncs = commands.get()
      def __init__(self):
            cmd = input(f"[{open("username", "r").read()}@pyndows]: ")

            for i in pytch.cmds:
                  if cmd.lower().split()[0] == i:
                        pytch.cfuncs.get(i)(pytch, shlex.split(cmd), cmd)

            try:
                  pytch.cmds.index(cmd.lower().split()[0])
            except ValueError:
                  print(f"Command {cmd.split()[0]} doesn't exist.")
                  pytch()
            
     