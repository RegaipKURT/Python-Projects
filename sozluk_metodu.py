# -*- coding: utf-8 -*-
sozluk={"a":0,"b":0,"c":0,"ç":0,"d":0,"e":0,"f":0,"g":0,"ğ":0,"h":0,"ı":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"ö":0,"p":0,"r":0,"s":0,"ş":0,"t":0,"u":0,"ü":0,"v":0,"w":0,"x":0,"y":0,"z":0}
metin=str(input("Metni giriniz: ")).lower()
liste=[]
for i in metin:
    if i in sozluk:
        sozluk[i] = sozluk[i] + 1
        
    if (not i in liste) and (i in sozluk):
        liste.append(i)

for j in liste:
    print (j," - ", sozluk[j])