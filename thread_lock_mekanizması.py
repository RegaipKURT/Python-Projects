import threading
import time

x = 0
count = 100000 
# işlemi bu sayıda tekrarlayacağız. Sadece 1 kerede istediğimiz sonucu almayabiliriz.
# tek bir sefer çalıştırıldığında işlem çok kısa süreceği için biri başlamadan diğeri
# bitmiş olacak ve aynı anda x değerine erilmesi zor olacaktır. Oysa uzun süren 
# bir işlem için aynı anda erişilmesi 

"""
        Aşağıda x değerine ekleme ve çıkarma yapan fonksiyonlar tanımlayacağız.
    Sırasıyla +3, +1, -1, -4 şeklinde ekleme ve çıkarmalar yapılacak.
    Ama x global değerine erişen fonksiyonlar aynı anda çalışacak ve aldıkları
    x değerine göre işlem yapacaklar. Bu da bir karışıklığa sebep olacak.
    Çünkü x değeri 4 thread'in aynı aynda çalışmasında dolayı sürekli değişmiş olacak!
    İlk önce fonksiyonları ard arda çalıştırıp başlangıçtaki değeri elde ettiğimizi
    göreceğiz. Fakat thread kullanıldığında x başlangıçtaki değere eşit olmayacak.
    Yüz bin kere tekrarlamamıza rağmen thread sonucu da 0 gelebilir. Fakat program
    birkaç kez çalıştırılırsa hatalı sonuçlar da görülecektir.
    
        Bu sorunu çözmenin yolu bir değişkene aynı anda sadece bir thread'in 
    erişip, yine sadece onun işlem yapmasına müsade eden thread lock mekanizmasını
    kullanmaktır. Aşağıda thread lock mekanizmasının kullanımı ve sonucu görülebilir.
"""

def add_3():
    global x
    for i in range(count):
        x += 3
    print("3 eklendi.")

def add_2():
    global x
    for i in range(count):
        x += 2
    print("2 eklendi.")
    
def subtract_1():
    global x
    for i in range(count):
        x -= 1
    print("1 çıkarıldı.")

def subtract_4():
    global x
    for i in range(count):
        x -= 4
    print("4 çıkarıldı.")

# sıralı çalıştırma ve sonucu
add_3()
add_2()
subtract_1()
subtract_4()
print("\nSıralı çalışmadan sonra x: {}\n".format(x))

#thread çalıştırılması ve sonucu
adding_2 = threading.Thread(target=add_2)
adding_3 = threading.Thread(target=add_3)
subtracting_4 = threading.Thread(target=subtract_4)
subtracting_1 = threading.Thread(target=subtract_1)

adding_2.start()
adding_3.start()
subtracting_1.start()
subtracting_4.start()

time.sleep(2) # yukarıdaki thread'ler bitmeden yazılmasın diye bekledik.

print("Thread çalışmasından sonra x: {}\n\n".format(x))



# LOCK MEKANİZMASININ KULLANILMASI
x = 0
count = 100000 
lock = threading.Lock()

# dosya işlemlerinde sıklıkla kullanılan with terimi burada da kullanılabilir.
# with open ile açılan dosya işlem bitince nasıl otomatik kapatılıyorsa
# with lock ile yapılan işlem bittikten sonra da lock kaldırılır.
# aşağıdaki thread'lerin çalışmasından sonra x daima 0 olacak.
# çünkü bir thread işlem yapılırken başka bir thread o değere erişip işlem yapamaz.
def add_3():
    global x
    with lock:
        for i in range(count):
            x += 3
    print("3 eklendi.")

def add_2():
    global x
    with lock:
        for i in range(count):
            x += 2
    print("2 eklendi.")
    
def subtract_1():
    global x
    with lock:
        for i in range(count):
            x -= 1
    print("1 çıkarıldı.")

def subtract_4():
    global x
    with lock:
        for i in range(count):
            x -= 4
    print("4 çıkarıldı.")

#lock tanımlı fonksiyonlarda thread çalıştırılması ve sonucu
adding_2 = threading.Thread(target=add_2)
adding_3 = threading.Thread(target=add_3)
subtracting_4 = threading.Thread(target=subtract_4)
subtracting_1 = threading.Thread(target=subtract_1)

adding_2.start()
adding_3.start()
subtracting_1.start()
subtracting_4.start()

time.sleep(2) # yukarıdaki thread'ler bitmeden yazılmasın diye bekledik.

print("\nLock tanıladığımız fonksiyonlarda thread çalışmasından sonra x: {}\n\n".format(x))









































