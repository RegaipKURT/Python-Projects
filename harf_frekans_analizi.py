#! usr/bin/env/ python
# -*- coding: utf-8 -*-

metin = input("Lütfen okunacak dosyanın adını uzantısı ile giriniz: ")
metin2 =  open(metin, "r")
a = metin2.read()
frekans = dict()

for karakter in a:
    if (karakter in frekans):
        frekans[karakter] += 1
    else:
        frekans[karakter] = 1
for i,j in frekans.items():
    
    print(i,":",j)

sayi = len(a)

print ("Toplam Harf sayısı: " , sayi)