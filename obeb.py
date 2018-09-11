def obeb(sayi1,sayi2):
    global liste
    liste = []
    ilerle = 1
    while ilerle < sayi1:
        if (sayi1 % ilerle == 0) and (sayi2 % ilerle == 0):
            liste.append(ilerle)
        else:
            pass
        ilerle += 1

sayi1 = int(input("Lütfen küçük sayıyı giriniz: "))
sayi2 = int(input("Lütfen büyük sayıyı giriniz: "))
obeb(sayi1,sayi2)
liste.sort()
print("Tam bölenlerinin listesi:",liste)
print("En büyük ortak bölenleri:",liste[len(liste) - 1])