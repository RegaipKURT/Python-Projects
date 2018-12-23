from tkinter import *
from tkinter import messagebox
#PENCERE OLUŞTURMA
pencere = Tk()
pencere.title("Program")
pencere.geometry("650x650")

"""
# alt ve üst frameler oluşturup ilerde bu bölgelere bi şeyler koyacağız.
#"INVISIBLE CONTAINERS" deniliyor bu frame'lere. Bu terim mantığını anlamamı sağlıyor.
üstframe = Frame(pencere)
üstframe.pack()
altframe = Frame(pencere)
altframe.pack(side=BOTTOM)

#LABEL OLUŞTURMA
metin = Label(pencere, text="Metin 1", bg="red",fg="white")
metin.pack() #pack yerine place kullanılırsa yerini de belirleriz. 
#metin.pack() #pack kullanıldığında bulduğu ilk boşluğa nesnemizi yerleştirir.
metin2 = Label(pencere, text="Metin 2", bg="blue",fg="white")
metin2.pack(fill=X)
metin3 = Label(pencere, text="Metin 3", bg="black",fg="green")
metin3.pack(fill=Y, side=LEFT)
"""

"""
#ENTRY (GİRİŞ) OLUŞTURMA
isim = Label(pencere, text="İsim:")
isimgiris = Entry(pencere)
sifre = Label(pencere, text="Şifre Giriniz:")
sifregir = Entry(pencere)

#grid parametresi ile ızgara mantığı gibi yerleştirme yapılabilir. satır ve sütunlar oluşturur.
isim.grid(row=0, sticky="w") # sticky yazıyı  yaslama yönünü belirtir.( 4 yön: n,s,w,e)
sifre.grid(row=1, sticky="w")
isimgiris.grid(row=0,column=1)
sifregir.grid(row=1, column=1)
#dikkat et pack kullanamıyoruz grid yaptığımız zaman. yeri belirtmeliyiz her şey için.

c = Checkbutton(pencere, text="Keep me Logged In")
c.grid(columnspan=2)
"""

"""
#BUTON OLUŞTURMA
buton1 = Button(altframe, text = "Buton", fg="green", bg="black",COMMAND=None)
buton1.pack()
"""

"""
#FONKSİYONLARI KULLANMA!!!
def yazdir(event):
    print("Fonksiyon Çalıştı...")

buton1 = Button(pencere, text="Çalıştır-1", command=yazdir)
buton1.pack()
#buton1.bind("<Button-1>", yazdir) 
# <Button-1> mouse da sol tık demek bu. Ayrıca bind kullanırken komutu sadece buraya yaz.

#Çoklu görev atama. bir tuşa birden fazla fonksiyon.
def sag(Event):
    print("sağ")
def sol(Event):
    print("sol")
def middle(Event):
    print("orta")

#bu sefer içine tıkladığımızda yazdıracağımız bir frame olsun.
frame1 = Frame(pencere, width=150, height=200)
frame1.bind("<Button-1>", sol) #BUTON AYARLANIRSA SADECE BUTONA TIKLANDIĞINDA ÇALIŞIR...
frame1.bind("<Button-2>", middle) # BUTON AYARLANMAZSA PROGRAM AÇILDIĞINDA ÇALIŞIR.
frame1.bind("<Button-3>", sag) #BUTONA FONKSİYON ATANACAKSA CLICK YAPISI KULLANILMALI Kİ HEMEN ÇALIŞMASIN.
frame1.pack()

buton2 = Button(pencere, text="Çalıştır-2")
"""

"""
#CLASS YAPISI İLE ÇALIŞMA!!!
#ilk başta bir pencere ve butonlar self olarak çalıştırılacak ve gerisi sınıfın fonksiyonlarıyla yapılacak.
class Butonlar:
    def __init__(self, master): #master dediğimizşey aslında pencere objesi. ismini öyle koyduk sadece.
        frame1 = Frame(master)
        frame1.pack()

        self.yazdirmabutonu = Button(frame1, text="Mesajı Yazdır")
        self.yazdirmabutonu.bind("<Button-1>", self.yazdir)
        self.yazdirmabutonu.pack(side=LEFT)

        self.cikisbuton = Button(frame1, text="ÇIKIŞ", command=frame1.quit)
        self.cikisbuton.pack(side= BOTTOM)

    def yazdir(self, Event):
        print("Yazı Yazdırıldı...")
        uyari = messagebox.showwarning("Uyarı!", "Konsola Bak!!!")
        
Butonlar(pencere)
"""

"""
#PROGRAMDA ÜST MENÜ ÇUBUĞU VE STATUS BAR OLUŞTURMA 
def calis():
    print("Tamam, yapmadık be!")

menu = Menu(pencere)
pencere.config(menu=menu)

#şimdi bu menunun içine bi şyler koyalım
altmenu = Menu(menu)
#üstte görünen menüler oluşturalım.
menu.add_cascade(label="File", menu=altmenu)

#üstteki menülerin içine alt açılır menüler koyalım.
altmenu.add_command(label="New", command=calis)
altmenu.add_command(label="Save", command=calis)

#ayrıcı çizgi ekleyelim.
altmenu.add_separator()
altmenu.add_command(label="Exit", command=quit)

#ikinci bir menü objesi daha ekleyelim
menu2 = Menu(menu)
menu.add_cascade(label="Edit", menu=menu2)
menu2.add_command(label="Ekle", command=calis)

#ŞİMDİ SIRA STATUS BAR OLUŞTURMADA(DURUM ÇUBUĞU)
status = Label(pencere, text="Yükleme Başarılı...", bd=1, relief=SUNKEN, anchor="w")
status.pack(side=BOTTOM, fill=X)
"""

"""
#MESSAGEBOX OLUŞTURMA
# from tkinter import messagebox #bu modülü import  etmek zorundayız.
import sys
messagebox.showinfo(title="Bilgi", message="Hoşgeldiniz...") #bilgi penceresi

#çıkış sorusu
answer = messagebox.askokcancel(title="Çıkış", message="Emin misiniz?")
if answer == TRUE:
    print("Çıkış Yapıldı...")
    sys.exit()
"""

"""
#ŞEKİL VE GRAFİK ALANLARI
#grafik, şekil, metin koymak için bi canvas objesi oluşturalım.
canvas = Canvas(pencere, width=200, height=300)
canvas.pack()

yesilkure = canvas.create_oval(0,0,50,50, fill="green") 
kırmızıcizgi = canvas.create_line(60,50,40,80, fill="red")
mavikare = canvas.create_rectangle(100,150,200,250, fill="blue")

#silmek istediğimiz obje olursa
#canvas.delete(kırmızıcizgi) #hepsini silmek için delete(ALL) diyebiliriz.
"""

#RESİM VE İKONLAR
foto = PhotoImage(file="ai.png")
label1 = Label(pencere, image=foto)
label1.pack(fill=BOTH)

mainloop() #PENCEREYİ SÜREKLİ EKRANDA TUTMAK İÇİN BİR LOOP OLUŞTURDUK.