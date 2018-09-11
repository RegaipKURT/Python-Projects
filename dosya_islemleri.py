dosya =open("deneme.txt","w")
dosya.write("Bu bir deneme dosyasıdır.\n")
dosya.close()
dosya =open("deneme.txt","r")
oku =dosya.read()
print(oku)
print(type(oku))
tip = dosya.readlines()
print(type(tip))
print(tip)
dosya.close()
dosya = open("deneme.txt","a")
dosya.write("Regaip\n")
dosya = open("deneme.txt","r")
print(dosya.readlines())
dosya = open("deneme.txt","a")
dosya.write("Kemal\n")
dosya =open("deneme.txt","r")
print(dosya.readlines())
dosya.close()

"""
Burada önemli olan eski verileri kaybetmeden dosyanın içine bir şeyler yazmak
istiyorsak -a modunda açmamız gerekiyor. Çünkü -w modu dosyanın içindeki verileri
silerek yeni bir dosya açıyor. Dolayısıyla -a modunu kullanmaya diikkat etmek
gerekiyor. Bunun yanında readlines liste olarak okurken read metodu string olarak
dosyayı okur ve alır. Bu da verilerin kullanımında önem arz edebilir.
Ayrıca dosya -w ve -a modunda açılmışsa okumanaz. Okumak için -r moduna geçmek
gerekiyor. Tekrar yazmak için de yine -w veya -a moduna geçilmeli.
İşlem bittikten sonra dosyayı kapatmak veri kaybını önlemek açısından önemli. 
"""