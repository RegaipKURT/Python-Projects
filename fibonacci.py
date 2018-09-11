# -*- coding: utf-8 -*-
def fibonacci():
    a = 0
    b = 1
    sayi = int(input("Lütfen bir sayı giriniz:"))
    liste = [a, b]
    c = 0
    while c < sayi:
        c = liste[a] + liste[b]
        liste.append(c)
        a += 1
        b += 1
    print(liste)
    print(len(liste))
    altin_oran_dizi = float(liste[len(liste) - 1] / liste[(len(liste)) - 2])
    print("Dizinin altın oranı:" + str(altin_oran_dizi))

while True:
    try:
        fibonacci()
    except ValueError:
        print ("Yanlış değer girdiniz....")
    except KeyboardInterrupt:
        break