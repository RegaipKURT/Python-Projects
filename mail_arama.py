"""
emailharvester ile kullanılmakta ve linux için çalışmaktadır.
dolayısıyla emailharvester!ın yüklenmesi ve linux sistem gereklidir
"""

# -*- coding: utf-8 -*-
import os
import re
import string

UYARI = "\nSİTE İSİMLERİNİN OLDUĞU DOSYA PROGRAM İLE AYNI DİZİNDE OLMALI \nEĞER AYNI DİZİNDE DEĞİLSE DOSYA YOLU İLE BERABER GİRİLMELİDİR.\n"
print(UYARI)

dosya = str(input("Site isimlerinin olduğu dosyanın adını giriniz: "))

dosya = open(dosya, "r")

dosya = dosya.readlines()

yenidosya = open("yenisiteler.txt","w")

for i in dosya:
    i = i.replace("www.", "")
    print(i)
    yenidosya.write(i)

yenidosya.close()
okunan_siteler = open("yenisiteler.txt", "r")
okunan_siteler = okunan_siteler.readlines()
for i in okunan_siteler:
    a = "emailharvester -d {} -e google >> sonuc.txt".format(i.replace("\n",""))
    print(a)
    os.system(a)

okunan_siteler.close()

karisik = open("sonuc.txt","r")
karisik = karisik.read()
yeni = open("sonuc.txt","w")
yeni.write(karisik)
yeni.close()

oku = open("sonuc.txt","r")
oku = oku.readlines()

son_sonuc = open("son_sonuc.txt","w")

for i in oku:
    if "@" in i:
        son_sonuc.write(i)
    else:
        pass
son_sonuc.close()
