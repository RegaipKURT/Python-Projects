from threading import Thread
import datetime

def Mukemmel_Bul():
    for i in range(1,10000):
        bolenler = []
        for k in range(1,i):
            if i % k == 0:
                bolenler.append(k)

        if sum(bolenler) == i:
            print(i)


def HEMukemmel_Bul(): # HAFİFÇE EKSİK MÜKEMMEL SAYI
    for i in range(1,10000):
        bolenler = []
        for k in range(1,i):
            if i % k == 0:
                bolenler.append(k)

        if sum(bolenler) == i-1:
            print(i)


def HAMukemmel_Bul(): # HAFİFÇE ARTIK MÜKEMMEL SAYI
    for i in range(1,10000):
        bolenler = []
        for k in range(1,i):
            if i % k == 0:
                bolenler.append(k)

        if sum(bolenler) == i+1:
            print(i)
    
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