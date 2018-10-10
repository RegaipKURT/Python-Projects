from termcolor import cprint
import os
import time

def yukleme():
    i = 0
    while i < 10:
        cprint("Yükleniyor.",color="green")
        time.sleep(0.2)
        os.system("clear")
        cprint("Yükleniyor..",color="red")
        time.sleep(0.2)
        os.system("clear")
        cprint("Yükleniyor...",color="blue")
        time.sleep(0.2)
        os.system("clear")
        i = i + 1

def logo():
    cprint(" _  _____  ____      ____   _    ____  ____  ",color="green")
    time.sleep(0.5) 
    cprint("| |/ / _ \|  _ \ _  |  _ \ / \  |  _ \/ ___| ",color="green")
    time.sleep(0.5) 
    cprint("| ' / | | | | | (_) | |_) / _ \ | |_) \___ \ ",color="green")
    time.sleep(0.5) 
    cprint("| . \ |_| | |_| |_  |  __/ ___ \|  _ < ___) |",color="green")
    time.sleep(0.5) 
    cprint("|_|\_\___/|____/(_) |_| /_/   \_\_| \_\____/ ",color="green")
    time.sleep(0.5)
    cprint("                                             ",color="green")

