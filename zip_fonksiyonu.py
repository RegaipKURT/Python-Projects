"""
    Zip fonksiyonu birçok listenin elemanlarına aynı anda ulaşmamızı sağlar.
Örneğin birden fazla liste üzerinde aynı anda işlem yapmak istiyorsak
bu listelerin içinde for döngüsüyle dönmemiz gerekir. her ne kadar çeşitli
yolları olsa da bunu yapmanın en kolay yolu zip fonksiyonunu kullanmaktır.

    Zip fonksiyonu python içinden gömülü olarak veya itertool içinden
kullanılabilir. Default haliyle en kısa uzunluktaki listenin eleman
sayısı kadar bir döngü gerçekleştirir. (Uzun olan için de itertools'da var!)
"""

import itertools  

# listelerimizi tanımlayalım.
num = [1, 2, 3] 
color = ['red', 'while', 'black'] 
value = [255, 256]


# aşağıda üç liste üzerinde en kısanın eleman sayısı kadar dönecek
# geri döndürdüğü değer her döngüde listelerin içinden alınan elemanlar olacak.

print("Gömülü (Normal) zip fonksiyonu!")
for (a, b, c) in zip(num, color, value): 
     print (a, b, c) 


# Eğer kısa olan liste bittikten sonra da devam etsin istersek zip_longest
# yani zip uzun fonksiyonunu kullanabiliriz.
print("En uzun liste bitene kadar çalışan zip_longest fonksiyonu!")
for (a, b, c) in itertools.zip_longest(num, color, value): 
    print (a, b, c)

#yetmeyen eleman None olarak belirlenecek.
