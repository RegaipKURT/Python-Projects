def fonksiyon():
    deger = "ilk değerdir."
    print("Fonksiyonda ilk tanımlanan değer: ",deger)
    def localdeger():
        deger = "Local değerdir."
    def nonlocaldeger():
        nonlocal deger
        deger = "Non-Local değerdir."
    def kuresel():
        global deger
        deger = "Global değerdir."
    localdeger()
    print("Local değer fonksiyonundan sonra:", deger)
    nonlocaldeger()
    print("Non-Local değer fonksiyonundan sonra:", deger)
    kuresel()
    print("Küresel değer fonksiyonundan sonra:", deger)

fonksiyon()
print("Fonksiyon dışından çalıştıralan değer:", deger)