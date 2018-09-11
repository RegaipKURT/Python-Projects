#! /usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib #Kullanacağımız kütüphaneyi import ettik.
gonderen = str(input("Mail Adresinizi Giriniz:"))
sifre = str(input("Şifrenizi Giriniz:"))
alan = str(input ("Alıcının mail adresini giriniz:"))
mesaj = str(input("Lütfen mesajınızı yazınız:"))

mail = smtplib.SMTP("smtp.gmail.com",587) #bağlanmak istediğimiz mail serverını ve o serverın kullandığı portu girdik.
mail.ehlo() #Mail göndermek istediğimizi belirten fonksiyon.
mail.starttls() #Server'a bağlanırken şifremizi kript ediyor.
mail.login(gonderen, sifre) #Login İşlemi...
mail.sendmail(gonderen,alan,mesaj) #Son olarak mail gönderme işlemi

"""
Bu kodların çalışabilmesi için Google'dan daha az güvenli uygulamalardan erişime
izin ver seçeneğini açmamız lazım. Bunun için şu linkten izin verebiliriz:
https://myaccount.google.com/lesssecureapps?pli=1
Ayrıca türkçe karakter kullandığımda sıkıntı çıkardı.(Python 3 ile denemedim.)
"""
