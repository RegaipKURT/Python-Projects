import threading
import time

def bekleme():
    print("ana thread için beklenecek thread başladı 5 saniye sürecek")
    time.sleep(5)
    print("beklenecek thread bitti")

def ana_thread():
    tr1.join()
    print("ana thread başladı")
    time.sleep(7)
    print("ana_thread bitti.")

def yan_gorev():
    print("yan görev başladı")
    time.sleep(9)
    print("yan görev bitti...")

tr1 = threading.Thread(target=bekleme, name="beklenecek_thr")
tr2 = threading.Thread(target=ana_thread, name="anathr")
tr3 = threading.Thread(target=yan_gorev, name="yan_thr")

tr1.start()
tr2.start()
tr3.start()