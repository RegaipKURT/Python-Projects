import time
import sys
i = 0
dosya = open("zamanlamadosyasi.txt","a",encoding="utf-8")
yaz = str(time.tzname)
dosya.write(yaz)
dosya.close
while i < 5:
    dosya = open("zamanlamadosyasi.txt","a",encoding="utf-8")
    a = str(time.asctime())
    dosya.write(a)
    dosya.write("\n")
    print ("Zaman dosyaya yazıldı\n")
    time.sleep(1)
    dosya.close()
    i += 1
dosya = open("zamanlamadosyasi.txt","a",encoding="utf-8")
dosya.write("\n")
dosya.close()
sys.exit()