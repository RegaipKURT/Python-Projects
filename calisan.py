#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
import sys
class calisan():

    def __init__(self,isim = "Bilinmeyen Çalışan", maas = "Asgari Ücret", departman = "Şirket"):
        print ("\nÇalışan Sınıfı Yapıcı Fonksiyonu Çalıştırılıyor...")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def yazdir(self):
        print("Çalışan Bilgileri Gösteriliyor...\n---------------------------")
        print("İsim:",self.isim,"\nMaaş:",self.maas, "\nDepartman:",self.departman)
    
    def zamyap(self, zam = 0):
        zam = int(input("Lütfen Zam Miktarını Giriniz: "))
        self.maas += zam
        print("Maaşa Zam Yapıldı...\n")

    def departdegistir(self, yenidepart = "Şirket"):
        print ("Departman değiştiriliyor...")
        self.departman = yenidepart
        print ("Yeni Departman:",self.departman)


class yonetici(calisan):

    def __init__(self, isim = "Yönetici", maas = 3500, departman = "Şirket", sorumlu_sayisi = 5):
        print ("\nYönetici Sınıfı Fonksiyonu Çalıştırılıyor...")
        super().__init__(isim,maas,departman)
        super().yazdir()
        super().zamyap()
        super().departdegistir()
        self.sorumlu_sayisi = sorumlu_sayisi #Ek Özellik Ekledik!!!
        print ("Sorumlu Olunan Kişi Sayısı:",self.sorumlu_sayisi)

calisan1 = calisan("Mehmet Baltacı", 2500, "İnsan")
calisan1.yazdir()
#calisan2 = calisan(sys.argv[1],int(sys.argv[2]),sys.argv[3])
#calisan2.yazdir()
kel = yonetici()
kel.yazdir()
