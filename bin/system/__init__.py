import installer
from tkinter import *

import colorama 
import os, platform

import pytch

pytch_cmds = pytch.commands()


from PIL import ImageTk, Image

using_desktop = False
AppsDatabase = {
      "desktop": {
                  "name": ("Pyndows Desktop", "DSK"),
                  "run": lambda: Apps.run('desktop'),
                  "close": lambda: Apps.close('desktop')
            }
}

def reboot():
      os.system("python main.py")

class Desktop(Tk):
      def __init__(self):
            super().__init__()
            self.geometry("640x480")
            self.title("Pyndows Desktop")

            taskbar = Frame(self, width=640, height=50)
            taskbar.grid(row=2,column=0)
            self.mainloop()
 
class Apps:
      def download(name):
            try:
                AppsDatabase.get(name)
            except ValueError:
                  return False
      def run(name):
            global using_desktop
            if name != "desktop" and not using_desktop:
                  print("[Error]: Graphical Shell not found.")
            elif name == "desktop":
                 Desktop()
      def close(name):
            pass
      
      def __init__(self):
            
            self.desktop = {
                  "name": ("Pyndows Desktop", "DSK"),
                  "run": lambda: Apps.run('desktop'),
                  "close": lambda: Apps.close('desktop')
            }

            self.browser = {
                  "name": ("Internet Explorer", "IE"),
                  "run": lambda: Apps.run('browser'),
                  "close": lambda: Apps.close('browser')
            }

            self.terminal = {
                  "name": ("Command Line", "CMD"),
                  "run": lambda: Apps.run('terminal'),
                  "close": lambda: Apps.close('terminal')
            }
            

def clear():
    if platform.system() == "Linux" or platform.system() == "Darwin":
                os.system("clear")
    else:
                os.system("cls")

def boot():
    def bootm():
        print(f"{colorama.Fore.WHITE}{colorama.Back.BLACK}")
        clear()
        pytch.pytch()
    
    if open("installed").read() == "n":
        print(f"{colorama.Fore.WHITE}{colorama.Back.BLACK}No bootable device found. System halted!")
    else:
        bootm()