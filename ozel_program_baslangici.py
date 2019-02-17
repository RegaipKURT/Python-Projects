# -*- coding: utf-8 -*-
from termcolor import cprint
import os
import time
import sys

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
    
class giris:

    @staticmethod
    def yukleme():
        i = 1
        while i < 10:
            cprint("Yükleniyor.",color="green")
            time.sleep(0.2)
            sys.stdout.write(CURSOR_UP_ONE)
            sys.stdout.write(ERASE_LINE)
            cprint("Yükleniyor..",color="red")
            time.sleep(0.2)
            sys.stdout.write(CURSOR_UP_ONE)
            sys.stdout.write(ERASE_LINE)
            cprint("Yükleniyor...",color="blue")
            time.sleep(0.2)
            i = i + 1
            sys.stdout.write(CURSOR_UP_ONE)
            sys.stdout.write(ERASE_LINE)

    @staticmethod
    def logo():
        cprint(r" _  _____  ____      ____   _    ____  ____  ",color="green")
        time.sleep(0.3)
        cprint(r"| |/ / _ \|  _ \ _  |  _ \ / \  |  _ \/ ___| ",color="green")
        time.sleep(0.3)
        cprint(r"| ' / | | | | | (_) | |_) / _ \ | |_) \___ \ ",color="green")
        time.sleep(0.3)
        cprint(r"| . \ |_| | |_| |_  |  __/ ___ \|  _ < ___) |",color="green")
        time.sleep(0.3)
        cprint(r"|_|\_\___/|____/(_) |_| /_/   \_\_| \_\____/ ",color="green")
        time.sleep(0.3)
        cprint("                                             ",color="green")
    
    @staticmethod
    def uyari():
            cprint("BU PROGRAMI KULLANARAK SORUMLULUĞU ÜSTLENMİŞ OLURSUNUZ!!!\n",
                   color="red", attrs=["bold",'underline'])
            time.sleep(1)


if __name__ == "__main__":
    giris.yukleme()
    giris.logo()
    giris.uyari()
