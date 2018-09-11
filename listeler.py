rakamlar = list(range(0,10)) # 0 ile 10 arasındaki sayılardan liste oluşturduk.
print (rakamlar)

rakamlar.append(10) # append listenin sonuna verilen elemanı ekler
print (rakamlar)

rakamlar.insert(1,45) #insert verilen index numarasına verilen elemanı ekler
print (rakamlar)

rakamlar.remove(2) # remove verilen elemanı kaldırır.
print (rakamlar)

rakamlar.pop() # pop verilen index numarasındaki elemanı kaldırır.

print(rakamlar.index(4)) # index o sıra numrasındaki elemana işlem yapar.

rehber = ["regaip","kemal", "salih", "şamil", "kadir"]
print (rehber)

print(rehber.count(1)) #verilen değerden listede kaç tane olduğunu gösterir.

rehber.sort() #sort fonksiyonu listede alfabetik ya da numerik olarak sıralama yapar.
print (rehber)

rakamlar.sort()
rehber.extend(rakamlar) #extend listeleri birleştirmeye yarar
rehber.append(rakamlar) # eğer append ile eklersek bir eleman gibi tüm listeyi ekler.
print(rehber)

rakamlar.clear() #listenin içindeki tüm elemları siler.
print (rakamlar)

sayilar = []
sayilar = rakamlar
#bu sığ kopyalamdır. Hafızadaki tek eleman her iki listede gösterili(shallow copy)
#örneğin:
sayilar.append(999) #aslında her iki listeye de eklendi. sayılar ve rakamlara.
print(sayilar) #sebep hafızadaki aynı varlıklar olarak yer almalarıdır.
print(rakamlar)
rakamlar = sayilar.copy() # şimdi hafızada bir kopyası DAHA oluşturuldu.
rakamlar.append(111)
print (rakamlar)
print(sayilar)

"""
silmek için iki fonksiyon yazarsak ya silmek istediğimiz değişkeni fonksiyon
dışında tanımlayıp fonksiyona o değeri veririz ya da fonksiyonun içinde tanımlayıp
o değeri fonksiyona girdi olarak vermeden yaparız.
"""
#değer dışardan alırsak
a = input("Silmek istediğiniz elemanı giriniz:")

def sil(a):
    rehber.remove(a)

#değeri fonksiyon içinden alırsak
def silme():
    b = input("Silmek İstediğniz elemanı giriniz:")
    rehber.remove(b)

