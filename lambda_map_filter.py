# -*- coding: utf-8 -*-
liste = list(range(11))
print ("Asıl liste:",liste)

"""
Filter Fonksiyonu: True ya da False olma durumuna göre, listelerin içinden eleme veya seçme yapar.
Map Fonksiyonu: Bir fonksiyonu verilen liste elemanlarına teker teker uygular.
Lambda Fonksiyonu: Fonksiyon tanımlamaya yarar.
"""

teksayilar = lambda x: x%2
tek_liste = list(filter (teksayilar, liste))
#teksayılar fonksiyonundan 0 veya 1 döneceği için, True değerleri yani 1 olanları aldı.
print ("Tek sayılar:",tek_liste)

kare = lambda x: x**2
#kare fonksiyonu içine x diye bir eleman alacak ve geriye karesini döndürecek.
kareliste = list(map(kare, liste))
print("Karelerin listesi:",kareliste)

#reduce fonksiyonu ise python 3 sürümünde builtin olarak yoktur yoktur. (2 ile built-in kullanabiliriz.)
#python 3 için functools kütüphanesinin import edilmesi gerekir
#reduce listenin ilk iki elemanını alıp, uyguladığı fonksiyondan döndürdüğü değerle,
#bir sonrakini işleme sokar. Lİste bitinceye kadar sırasıyla sonuna kadar ikişerli olarak gider.
"""
carp = lambda x,y: x*y
a = reduce(carp, liste)
print (a)
"""
