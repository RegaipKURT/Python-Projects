"""
Metaprogramlama birçok programlama dilinde bulunur. 

Metaprogramlama en basit haliyle bir tür kod denetleme aracıdır.
Yazdığımız kodun içeriğini program çalışırken içerden veya dışardan
değiştirmek veya denetlemek istediğimizde bu yapıyı kullanırız.

Bu programı çalıştırmak için bulunduğunuz dizinde deneme.py ve bos_dosya.py isimli 
iki adet python dosyası oluşturun. Daha sonra bu python programlarını bu dosya üzerinden programlayalım.

deneme.py içeriği şöyle olsun:
<--
def selamla(*args, **kwargs):
    print("Hoşgeldiniz", kwargs["isim"], kwargs["soyad"] + "!")

a = "Kemal"
def w():
    global a
    import os
    os.system("whoami")
    print(a)

if __name__ == '__main__':
    selamla(isim="Regaip", soyad="Kurt")

-->

"""

with open("bos_dosya.py","a") as f:
    f.close()

#oluşturduğumuz dosyaların import edilmesi
import deneme
import bos_dosya
import Metaprogramming # programın kendisini import etmesi



if __name__ == '__main__':
    #Yayıncı isminde bir değişkenim var. En altta nasıl olduğunu görebilirsin.
    print("Yayıncı:", Metaprogramming.Yayinci)
    #print(deneme.__dict__) # deneme dosyası içindeki tüm özellikler ve değişkenler

    # metaclass aracılığıyla oluşturacağımız insan sınıfı için yapıcı metod
    def insan_init(self, boy, kilo, isim):
        self.kilo = kilo
        self.boy = boy
        self.isim = isim

    # type fonksiyonuyla insan sınıfı oluşturma
    insan = type(
        "insan", #sınıfın adı
        (), #base class tanımlama (biz kullanmayacağız)
        # sınıf metodlarımızı tanımlama
        {"__init__": insan_init,
        "get_name": lambda self: print(self.isim),
        "VKI": lambda self: print(self.isim + " kişisinin Vücut/Kitle İndeksi: " + "{:.2f}".format(self.kilo/((self.boy/100)**2)))
        }
    )

    #deneme dosyasının gömülü metodlarına bakalım
    print(dir(deneme)) #henüz biz hiç bi şey tanımlamadık

    # deneme dosyasında yeni_nesne adında bir insan sınıfı oluşturalım
    deneme.__dict__["yeni_nesne"] = insan(175, 85, "Değişik insan") 
    deneme.yeni_nesne.get_name()  # isim alma
    deneme.yeni_nesne.VKI() # vücut kitle indeksi alma
    print("Orjinal değer: ", deneme.a) #deneme dosyası içinde tanımlanmış a değişkeninin değerini aldık
    deneme.a = "Atatürk"
    print("Değiştirdiğimiz değer: ", deneme.a)
    print(dir(deneme)) # deneme dosyasının gömülü metodlarında artık bizim oluşturduğumuz nesne görünecek.
    # print(deneme.__dict__["__file__"].split("\\")[-1])
    # print(deneme.__dict__["__cached__"])

    # bos_dosya.py isimli programda yeni listeler tanımlayalım

    # liste+number olacak şekilde 100 tane liste tanımlayalım ve 
    # içine o listenin sonundaki numaraya kadar olan sayıları ekleyelim
    # for i in range(100):
    #     bos_dosya.__dict__["liste" + str(i)] = [j for j in range(i)]

    # #bos_dosya.py içinde 20 ye kadar olan listelere bakalım
    # for i in range(20):
    #     print(bos_dosya.__dict__["liste"+str(i)])




    # METAPROGRAMMING YÖNTEMLERİYLE HİÇBİR İZNİMİZ OLMAYAN BİR PYTHON DOSYASINA DA ERİŞİP 
    # İÇİNDEKİLERİ OKUYABİLİR VEYA ÇALIŞTIRABİLİRİZ. BUNUN İÇİN __pycache__ dosyasının oluşturulmuş olması gerekir.
    #deneme.py dosyasının izinlerini değiştirip deneyebilirsiniz! 
    # __pycache__ içideki dosyayı okuma izniniz olmalıdır!
    import deneme #okuyamasak bile bu python dosyasını cache üzerinden import edebilecektir. Çünkü cache okunabilir durumda!

    def hello():
        print("HACKED!")

    deneme.__dict__["hello"] = hello
    deneme.hello()
    # DOSYA İÇİNDEN SELAMLA VE W İSİMLİ FONKSİYONLARI ÇALIŞTIRALIM
    # deneme.selamla(isim="Regaip", soyad="Kurt") 
    # deneme.w()

    # #DOSYANIN İÇİNDEKİLERİ CACHE'I OKUDUĞUMUZ İÇİN GÖREBİLDİK AMA AÇMAYA ÇALIŞTIĞIMIZDA HATA VERECEKTİR.
    # with open("deneme.py", "r") as f:
    #     print(f.readlines())


    # METAPROGRAMLAMANIN KULLANIMI
    # Metaprogramlamada metaclasslar kullanılır ve bir metaclass type dan kalıtım alır.
    # metaclass alan bir sınıfın özellikleri metaclass tarafından düzenlenebilir. Örnek verelim:
    class StringMeta(type):
        # bureda eğer bu metaclass ile oluşturulan sınıfın adı y ile başlıyorsa 
        # o sınıfa sınıfın adını yazdıran bir yaz fonksiyonu eklensin
        def __new__(cls, what, bases=None, dict=None):
            print(dict) # dict sınıfın özelliklerini barındırır.
            new_dict = {}
            if dict["__qualname__"].startswith("y"):
                print("Sınıf adı y ile başlıyor, yaz fonksiyonu ayarlanacak!")
                def yaz(self):
                    print(dict["__qualname__"])
                #Soru: Bu ne işe yarar? Diyebiiliriz.
                #Cevap: Örneğin IDE'ler bizim yazdığımız kodu metaprogramlama ile tıpkı böyle denetler. 
                # Böylece hatalı yerleri gösterirler mesela.
                new_dict["yaz"] = yaz
            return type.__new__(cls, what, bases, new_dict)
    class yreg(metaclass=StringMeta):
        pass
    class reg(metaclass=StringMeta):
        pass
    #yreg sınıfının adı y ile başladığı için yaz metodu olacak içinde.
    y = yreg()
    y.yaz()

    r = reg()
    # r.yaz çalışmaz çünkü r nesnesinin oluşturulduğu sınıfın adı y ile başlamıyor, yaz metodu tanımlanmadı!
    # dolayısıyla yaz fonksiyonuna sahip değil!
    #r.yaz() 


#Program çalışma zamanı içinde kendini de değiştirebilir!
Metaprogramming.__dict__["Yayinci"] = "Regaip KURT"

#program import edildiğinde Kemal değeri yazılırken en sonda Atatürk değeri yazacak.
eval("deneme.w()")
exec("deneme.w()")
