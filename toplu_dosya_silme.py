import os

dosya_turu = str(input("\nSilmek istediğiniz dosyaların uzantısını giriniz: "))

if dosya_turu.startswith("."):
    dosya_turu = dosya_turu
else:
    dosya_turu = "." + dosya_turu

yol = str(input("\nİçindeki verilerin silineceği klasörün yolunu giriniz: "))

kabul = str(input("\n\nUYARI!!!\n\n{} klasöründeki, tüm {} uzantılı dosyalar silinecektir!!!\n\nKabul ediyor musunuz (Evet:y / Hayır: n): ".format(yol, dosya_turu)))

dir = os.chdir(yol)
dosyalar = os.listdir()
sayi = 0

if kabul == "y" or kabul == "Y":
    for i in dosyalar:
        if i.endswith(dosya_turu):
            if os.name == "posix":
                os.system("rm -r {}".format(i))
            elif os.name == "nt":
                os.system("del /f {}".format(i))
            sayi += 1
        else:
            pass
    print("Toplamda {} {} uzantılı dosya silindi\n".format(sayi, dosya_turu))
    if sayi == 0:
        print("Klasörde bu uzantıya sahip herhangi bir dosya bulunamadı.\n")
else:
    print("Programdan Çıkıldı!")
