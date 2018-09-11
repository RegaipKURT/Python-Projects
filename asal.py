#! /usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input("Bir Sayi Giriniz:"))
liste = []

for i in range(1, n):
    flag = False
    for b in range(2, i):
        if (i % b == 0):
            flag = True
            pass
    if (flag == False):
        liste.append(i)

print (liste)
