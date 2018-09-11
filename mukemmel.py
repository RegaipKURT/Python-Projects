def mukemmel(sayi):
    i = 1
    global liste
    liste = []
    global mukemmelliste
    mukemmelliste = []
    while i < sayi:
        if sayi % i == 0:
            liste.append(i)
            i = i + 1
        else:
            i = i + 1
    #print("Bölenler Listesi: ",liste)
    toplam = 0
    for bolen in liste:
        toplam = toplam +bolen
    if toplam == sayi:
        mukemmelliste.append(sayi)
    if len(mukemmelliste) > 0:
        print(sayi)

sayimiz = int(input("Lütfen bir sayi giriniz: "))
"""
mukemmel(sayimiz)
if len(mukemmelliste) == 0:
    print(sayimiz,"mükemmel sayı değildir.")
else:
    print(sayimiz, "mükemmel bir sayıdır.")
"""
for sayi in list(range(1,sayimiz)):
    mukemmel(sayi)
