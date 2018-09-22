#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 10:03:40 2018

@author: regkr
"""

#1000'e kadar olan asal sayıları bulma
asallar = [2]
def asal():
    for i in range(3,1000,2):
        bolunur = False
        for x in range(2,i):
            if (i % x) == 0:
                bolunur = True
        if bolunur == False:
            asallar.append(i)
asal()
print("Asal Sayılar Listesi:\n", asallar,"\n")

# 3'e ve 5'e aynı anda bölünenleri bulma
bolunenler = []
def tamlar():
    for i in range(1,1000):
        if i % 3 == 0 and i % 5 == 0:
            bolunenler.append(i)
tamlar()
print("3 ve 5'e bolunenler:\n", bolunenler,"\n")

# 1000'e kadar fibonacci sayılarını bulma 
fibo = [0,1]
def fibonacci():
    a = 0
    while (fibo[(len(fibo)) - 1] < 1000):
        fibo.append(fibo[a]+ fibo[a+1])
        a = a + 1
    if fibo[(len(fibo)-1)] > 1000:
        fibo.remove(fibo[(len(fibo)-1)])
fibonacci()
print ("Fibonacci Listesi:\n",fibo)

# 1 ile 1000 arasında bir sayı alıp kaç rassal tahiminden sonra eşleştiğini bulma
import random
sayimiz = int(input("Lütfen Bir Sayı Giriniz:"))
rassal = random.randint(1,1000)
def rassaltahmin(rassal,sayimiz):
    a = 0
    while sayimiz != rassal:
        rassal = random.randint(1,1000)
        a += 1
    print (a,"rassal tahminde sayılar eşitlendi.")
rassaltahmin(rassal,sayimiz)

# öklid mesafesi bulma
a1 = float(input("1. noktanın x ekseni değeri:"))
a2 = float(input("1. noktanın y ekseni değeri:"))
b1 = float(input("2. noktanın x ekseni değeri:"))
b2 = float(input("2. noktanın y ekseni değeri:"))

y = abs(a1-b1)
x = abs(a2-b2)

import math
mesafe = math.sqrt((y*y)+(x*x))
print ("İki nokta arasındaki öklid mesafesi {}".format(mesafe))





