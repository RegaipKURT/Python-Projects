# -*- coding: utf-8 -*-
from tkinter import *
import matplotlib.pyplot as plt

sozluk={"a":0,"b":0,"c":0,"ç":0,"d":0,"e":0,"f":0,"g":0,"ğ":0,"h":0,"ı":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"ö":0,"p":0,"r":0,"s":0,"ş":0,"t":0,"u":0,"ü":0,"v":0,"w":0,"x":0,"y":0,"z":0}
sozluk2={"a":0,"b":0,"c":0,"ç":0,"d":0,"e":0,"f":0,"g":0,"ğ":0,"h":0,"ı":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"ö":0,"p":0,"r":0,"s":0,"ş":0,"t":0,"u":0,"ü":0,"v":0,"w":0,"x":0,"y":0,"z":0}

def olustur():
    global metin
    metin=acikentry.get(0.0, END).lower()
    global metin2
    metin2=sifrelientry.get(0.0, END).lower()
    def acik_metin():
        for i in metin:
            if i in sozluk:
                sozluk[i] = sozluk[i] + 1
            else:
                pass
        plt.bar(range(len(sozluk)), list(sozluk.values()), align='center')
        plt.xticks(range(len(sozluk)), list(sozluk.keys()))
        plt.ylabel('Harf Sayısı')
        plt.xlabel('Harfler')
        plt.title('Açık Metin Harf Frekansı Grafiği')
        plt.savefig("Acik_Metin_Grafik.png")
        plt.show()
        plt.close()
    def gizli_metin():
        for i in metin2:
            if i in sozluk2:
                sozluk2[i] = sozluk2[i] + 1
            else:
                pass
        plt.bar(range(len(sozluk2)), list(sozluk2.values()), align='center')
        plt.xticks(range(len(sozluk2)), list(sozluk2.keys()))
        plt.ylabel('Harf Sayısı')
        plt.xlabel('Harfler')
        plt.title('Şifreli Metin Harf Frekansı Grafiği')
        plt.savefig("Gizli_Metin_Grafik.png")
        plt.show()
        plt.close()
    acik_metin(), gizli_metin()

pencere = Tk()
pencere.title("Sezar Şifre Kırma")
pencere.geometry("400x450")

sifrelilabel = Label(pencere,text="Şifreli Metin:")
sifrelilabel.pack()
sifrelientry = Text(pencere,width=40,height=10)
sifrelientry.pack()

aciklabel=Label(pencere,text="Açık Dilde Metin Örneği:")
aciklabel.pack()
acikentry = Text(pencere,width=40,height=10)
acikentry.pack()

coz = Button(pencere,text="Grafikleri Oluştur")
coz.config(command=olustur)
coz.pack()

mainloop()
