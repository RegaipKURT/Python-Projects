import threading
import time

def thr(n, name):
    print("\nMerhaba, ben {}, {} saniye bekleyeceğim...\n".format(name, n))
    time.sleep(5)
    print("{} bekleme süresini tamamladı...\n".format(name))

t = threading.Thread(group=None, target=thr, name="thread_1", args=(5, "Thread Görevi") )
t.start()

print("\nThread şu anda çalışıyor, ama program da kodları okumaya devam ediyor...\n")
time.sleep(1)
print("Şimdi anladın mı?\n")

t.join() # join ile thread bitene kadar bekleme sağlanır


#------------------------------------------------#
#ŞİMDİ 5 TANE THREAD AYNI ANDA ÇALIŞIRSA VEYA AYRI AYRI ÇALIŞIRSA NE OLUR GÖRELİM!

thread_list = []

baslangic_thread = time.time() # thread kullanınca tamamlanma süresini çlçmek için zamanı aldık.

for i in range(5):
    t = threading.Thread(target=thr, name="thread{}".format(i),  args =(5,'thread{}'.format(i)))
    thread_list.append(t)
    t.start()

#KODUN KALAN KISMINA DEVAM ETMESİN DİYE GÖREVLERİN JOİN FONKSİYONUYLA BİTMESİNİ BEKLEYELİM.
for i in thread_list:
    i.join()

bitis_thread = time.time() # bütün görevler bittikten sonraki zaman

#--------------------------------------------------------------#

# THREAD OLMADAN GÖREVLER AYRIK OLARAK ÇALIŞIRSA NE KADAR ZAMAN ALACAK GÖRELİM!

baslangic = time.time()

for i in range(5):
    print('Görev{} Başladı \n'.format(i))
    thr(5, "Görev{}".format(i))

bitis = time.time()

print ("Tüm görevlerin ayrık tamamlanma süresi: {}".format(bitis-baslangic))
print ("Tüm thread görevlerinin tamamlanma süresi: {}".format(bitis_thread-baslangic_thread))

"""
Görüldüğü gibi thread kullanmak 5 fonksiyonu aynı anda çalıştırıp süreyi 5 kat kısalttı.
Sonuç olarak thread kullandığımızda herhangi bir görevin bitmesini beklemeden diğer görevi çalıştırabiliriz.
Böylece programın çalışma zamanı büyük ölçüde azalabilir.

Burada dikkat edilmesi gereken nokta ayrı thread görevlerinin birbirinden girdi alması durumunda
programın hata verebileceğine dikkat edilmeli ve görevler buna göre düzenlenmelidir.

Zaten join fonksiyonuyla başka bir görevden girdi alınması durumunda o girdinin diğer fonksiyondan
çıkması beklenebilir ve girdi çıktıktan sonra program çalışmaya devam eder.
Join fonksiyonu özelliklerine bakılarak bu daha iyi anlaşılabilir.
"""
