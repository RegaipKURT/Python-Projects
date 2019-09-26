#! /usr/bin/python3

import hashlib
import sys
from termcolor import colored
import time

sifre_asil = "b74d04ca135c86e95f82d058f6999d65"

def sor():
    global a
    a += 1
    girilen = str(input(colored("Lütfen şifrenizi giriniz: ", "blue")))
    girilen_sifre = hashlib.md5(girilen.encode('utf-8')).hexdigest()
    if girilen_sifre == sifre_asil:
        pass
    elif girilen_sifre != sifre_asil and a < 3:
        print(colored("\nŞifreniz Hatalıydı! Lütfen Tekrar Deneyin...", "red"))
        sor()
    else:
        print(colored("\nŞifrenizi 3 Kere Yanlış Girdiniz! Çıkış Yapılıyor...", "red"))
        time.sleep(0.8)
        sys.exit()
a=0
sor()
print(colored("TEBRİKLER BAŞARILI BİR ŞEKİLDE GİRİŞ YAPILDI...\n", "green"))




