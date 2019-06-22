# *args ve **kwargs kullanımının farkı

from threading import Thread
from termcolor import colored

class yazilar:
    
    def yaz_renkli(**kwargs): 
        # ** ile keyword argümanlar aldığımızda sonuç sözlük olarak döner
        print(kwargs) # ** ile alınca sözlük döndüğünü görelim
        
        for i in kwargs:
            print("{}: {}".format(i, kwargs[i]))
        
        print(colored("{} \n".format(kwargs["yazi"]),
                      color=kwargs["renk"]))
    
    def yaz(*args):
        # * ile alınan argüümanlar tupple oalrak döner
        print("{}".format(args))# args ı yazdırıp tupple olduğunu görelim

        for i in args:
            print(i) #her elemanı teker teker yazdıralım
        
        
yaz = yazilar.yaz_renkli(yazi="Yazılan ifade sözlük olarak görünüyor!", renk="green")
#yaz_renkli içine keyword değerler verdik (renk ve yazi şeklinde)
thr_renkli = Thread(target=yaz)
thr_renkli.start()

yaz2 = yazilar.yaz("Yazı ", "bir ", "demet ", "görüldüğü ", "gibi...")
thr_normal = Thread(target=yaz2)
thr_normal.start()

