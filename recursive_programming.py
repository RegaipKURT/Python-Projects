"""
İlk örneğimizi recursive programlama şeklinde yazalım.
Recursive kelimesi türkçeye "öz yinelemeli" olarak çevrilebilir.
Örnek verecek olursak 5! = 5 * 4! olarak yazılabilir. 4! = 4 * 3!, 3!=3*2!, 2!=2*1!, 1!=1*0!
Biz fak diye bir fonksiyon tanımlayıp özyinelemli olarak yazarsak ve 0!'in değerinin ne olduğunu
programa söylersek, recursive tanımlama sayesinde program geriye kalan değerleri 
yazdığmız program kendisi hesaplayabilecektir. Bu şekilde program yazmak insanın düşünme 
yapısına çok daha yakındır. İnsan beyni recursive düşünmeye daha yatkındır.
Şimdi bir recursive faktöryel hesaplama programı yazalım...
"""
import profile #bu modülü fonksiyonun çalışma süresini ölçmek için koyuyoruz.

def fak(n): #Fonksiyonumuzu fak ismiyle tanımladık
    if (n == 0): #burada eğer n 0 ise 1 döndür dedik.
        return 1 #eğer kodu if döngüsüyle 0'da kesmeseydik eksi sonsuza kadar aramaya devam edecekti
    return (n * fak(n-1)) #fonksiyon (n*(n-1)!) değerini döndürüyor.

a = int(input("Faktöryel alınacak sayi giriniz:"))
print ("Recursive Sonuç:",fak(a))

print ("\n\nRECURSİVE PROGRAMLAMA İÇİN FONKSİYONUN ÇALIŞTIRMA SÜRESİ DEĞERLERİ:")
profile.run('fak(a)')
#BURADA ÖENMLİ OLAN BİR ŞEY VAR!!! RECURSİVE MANTIK YÜKSEK HESAPLAMADA HATA VERİYOR.
#1000 SAYISINI FONKSİYONLARDA AYRI AYRI DENEYİNCE RECURSİVE FONKSİYONUN ÇALIŞMADIĞINI GÖRECEKSİNİZ!
"""SEBEP RECURSİVE FONKSİYONUN SADECE 995 KERE GERİYE VEYA İLERİYE DOĞRU ARAMA YAPMASIDIR..."""
#AYRICA RECURSİVE FONKSİYON DAHA UZUN SÜREDE ÇALIŞIYOR. BUNU DEĞERLERDE GÖREBİLİRSİNİZ.


"""
Aynı programı normal programlama mantığıyla yazdığımızda şu şekilde yazmamız gerekir. 
"""
def fac(n):
    sonuc = 1
    a = 1
    while (a <= n):
        if n ==0:
            sonuc = 1
            break
        sonuc = sonuc * a
        a += 1
    return sonuc

b = int(input("Faktöryel alınacak sayi giriniz:"))
print ("Listesiz Sonuç",fac(b))
#Gördüğünüz gibi burada hem daha uzun kod yazdık, hem de bazı değişkenler tanımlamak zorunda kaldık
#Üstelik bu kodun anlaşılması biraz daha zor
print ("\n\nNORMAL MANTIKTA PROGRAMLAMA İÇİN FONKSİYONUN ÇALIŞTIRMA SÜRESİ DEĞERLERİ:")
profile.run('fac(b)')


"""
Şimdi yine normal programlama mantığı ile aynı programı farklı şekilde yazalım 
"""
def fakto(n):  #bu sefer de bir liste oluşturarak yapacağız.
    liste = list(range(1,n+1)) # 1'den n'ye kadar olan sayılardan liste oluşturduk.
    carpım = 1
    for i in liste: # for döngüsüyle listenin elemamlarını birbiriyle çarparak sonucu bulacağız.
        carpım = carpım * i
    return carpım

c = int(input("Faktöryel alınacak sayi giriniz:"))
print ("Listeli Sonuç:",fakto(c))

print ("\n\nLİSTELERLE ÇALIŞILDIĞINDA FONKSİYONUN ÇALIŞTIRMA SÜRESİ DEĞERLERİ:")
profile.run('fakto(c)')