import os
import sys

for file in sys.argv[1:]:
    sozluk = {}
    print("*"*40)
    print(str(file) + " dosyası için sonuçlar:")
    with open(file, "r") as file:
        for i in file.readlines():
            if i not in sozluk:
                sozluk[i] = 1
            else:
                sozluk[i] +=1
    for i, j in enumerate(sozluk):
        if sozluk[j] > 1:
            print(str(sozluk[j]) + "\t" + j[:-1])
    print("*"*40 + "\n")