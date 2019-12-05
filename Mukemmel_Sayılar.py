from threading import Thread
import datetime

def Mukemmel_Bul():
    """
    Kendisi dışındaki pozitif bölenlerinin toplamı, kendisine eşittir.
    """
    for i in range(1,10000):
        bolenler = []
        for k in range(1,i):
            if i % k == 0:
                bolenler.append(k)

        if sum(bolenler) == i:
            print(i)


def HEMukemmel_Bul(): # HAFİFÇE EKSİK MÜKEMMEL SAYI
    """
    2'nin kuvvetleri böyle sayılardır. 
    Kendisi dışındaki pozitif bölenlerinin toplamı, kendisinden 1 eksiktir.
    """
    for i in range(1,10000):
        bolenler = []
        for k in range(1,i):
            if i % k == 0:
                bolenler.append(k)

        if sum(bolenler) == i-1:
            print(i)


def HAMukemmel_Bul(): # HAFİFÇE ARTIK MÜKEMMEL SAYI 
    """
    Kendisi dışındaki pozitif bölenlerinin toplamı, kendisinden 1 fazladır.
    Böyle bir sayı bugüne kadar bulunamamıştır ama yokluğu veya varlığı da kanıtlanamamıştır.
    """
    for i in range(1,10000):
        bolenler = []
        for k in range(1,i):
            if i % k == 0:
                bolenler.append(k)

        if sum(bolenler) == i+1:
            print(i)
        elif i % 10000 == 0:
            print(i, " sayısına kadar sonuç yok!")
    
thr1 = Thread(target=Mukemmel_Bul, name="Mukemmeller")
thr2 = Thread(target=HEMukemmel_Bul, name="Hafifçe Eksik Mükemmeller")

def sürehesap(thr=Thread()):
    print(thr.name, " başladı!")
    baslangic = datetime.datetime.now()
    thr.start()
    thr.join()
    son = datetime.datetime.now()
    
    print(thr.name, "sonlandı. \nToplam Geçen Süre: ", son-baslangic)
    
sürehesap(thr1)
sürehesap(thr2)
