import requests
from bs4 import BeautifulSoup
import operator
def sozlukolustur(tumkelimeler): #tüm kelimeleri bir sözlüğe atayıp kaç defa geçtiğini bulacağız.
    kelimesayisi = {} #kelimesayisi diye sozluk oluşturduk.
    for kelime in tumkelimeler:
        if kelime in kelimesayisi:
            kelimesayisi[kelime] += 1
        else:
            kelimesayisi[kelime] = 1
    return kelimesayisi
#işlemler tamamladıktan sonra kelimelerdeki ifadeleri temizlemek için
def temizle(tumkelimeler):
    sembolsuz = [] #temizlenen kelimeleri sembolsuz listesine ekleyeceğiz.
    semboller = "!@$+#^\"\',.;:`”’“©£<>/()[]{}=*?\\_-|é" #ifadelerimiz bunlar. Yani bunlardan temizleyeceğiz kelimeleri.
    for kelime in tumkelimeler: #tumkelimelerin içinde birer defa dönecek.
        for sembol in semboller: #sonra sembollerin içinde birer defa dönecek.
            if sembol in kelime: # eğer sembol kelimenin içinde varsa
                kelime = kelime.replace(sembol, "") #kelimenin içindeki sembolü boş karakterle değiştirecek.
        if (len(kelime) > 0): #kelime sadece temizlenecek ifadeden oluşuyosa almayacak. Çünkü onun uzunluğu "0" olacak
            sembolsuz.append(kelime) #sembolsüz kelimeleri sembolsuz listesine ekleyecek
    return sembolsuz # döndürdüğü bu listenin içindeki her bir kelimeyi tumkelimeler listesine for döngüsüyle ekleyeceğiz.
#URL'Yİ TANIMLAYALIM
url = "https://www.haberturk.com/son-dakika-feto-nun-eminyet-yapilanmasinin-iddianamesi-hazir-2091811"
#KELİME LİSTESİ OLUŞTURALIM. İLERDE KELİMELERİ APPEND İLE İÇİNE EKLEYECEĞİZ.
tumkelimeler = []
#REQUSETS MODÜLÜ İLE URL ADRESİNİN KAYNAK BİLGİLERİNİ ÇEKİYORUZ.
r = requests.get(url)
#SOUP İLE BUNLARI DAHA DÜZGÜN BİR HALE SOKUYORUZ. OKUNABİLİR OLMASI İÇİN
soup = BeautifulSoup(r.content, "html.parser")
#P ETİKETİ İLE BAŞLAYAN HER YERİ ALIP HER BİRİNE KELİME GURUBU DİYELİM
for kelimegrubu in soup.find_all("p"): #FIND_ALL FONKSİYONU O ETİKETLE BAŞLAYAN PROGRAMLARI BULACAK.
    icerik = kelimegrubu.text #.TEXT DİYEREK SADECE TEXT OLAN KISIMLARI ALDIK. YOKSA HTML BİLGİLERİNİ DE ALIRDI.
    kelimeler= icerik.lower().split() #SPLİT FONKSİYONU KELİMELE GRUPLARINI BOŞLUKLARA GÖRE AYIRIP LİSTEYE ATAR.
    # DAHA SONRA SPLİT FONKSİYONUYLA LİSTELERE ATANAN KELİMELERİ ÖNCEDEN TANIMLADIĞIMIZ LİSTEYE ATIYORUZ.
    for i in kelimeler: #TUM KELİMELERİ LİSTEYE TEKER TEKER EKLİYORUZ.
        tumkelimeler.append(i)

tumkelimeler = temizle(tumkelimeler) #TEMİZLE FONKSİYONUNU TUMKELİMELER LİSTESİ ÜZERİNDE ÇALIŞTIRDIK VE YENİ TUM KELİMELER LİSTESİNİ OLUŞTURDUK.
kelimesayisi =sozlukolustur(tumkelimeler) #TUM KELİMELERİ KELİMESAYISI SÖZLÜĞÜNÜ ATTIM. ÇÜNKÜ KELİMENİN KAÇ DEFA GEÇTİĞİNİ SÖZLÜKLE BULABİLİRİZ.

for kelime in tumkelimeler: #TUM KELİMELERİ EKRANA YAZDIRIYORUZ.
    print (kelime)

for anahtar,deger in sorted(kelimesayisi.items(), key=operator.itemgetter(1)):
    print(anahtar,":",deger)

""" BURADAN SONRASINI DOSYALARA YAZDIRMAK İÇİN YAPTIM!!!
b = open("kelime_frekansı.txt", "w")



#DAHA SONRA KELİMELER DİYE BİR TEXT DOSYASI OLUŞTURUP KELİMELERİ ORAYA YAZALIM...
a = open("kelimeler.txt", "w")

for kelime in tumkelimeler:
    a.write(kelime)
    a.write("\n")

metin2 = open("kelimeler.txt", "r")
a = metin2.read()
frekans = dict()

for karakter in a:
    if (karakter in frekans):
        frekans[karakter] += 1
    else:
        frekans[karakter] = 1
for i, j in frekans.items():
    print(i, ":", j)

sayi = len(frekans)

print("Toplam Harf sayısı: ", sayi)

sonuc = open("sonuc.txt","w")
sonuc.write("Toplam Harf Sayısı\n")
sonuc.write(str(sayi))
sonuc.write("\nToplam Kelime Sayısı\n")
sonuc.write(str(len(kelimesayisi)))
"""
