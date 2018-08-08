from selenium import webdriver
import time
import sys
browser = webdriver.Chrome()
browser.get("https://www.instagram.com/")

time.sleep(8)
#sayfanın yüklenmesi için bekliyoruz. ardından ben css selector kullandım.
#css selector yerine başka yintemler (xpath veya html veya name) kullanılabilir.
#ÖNEMLİ UYARI!!!!
#X_PATH İLE VERİ ALIRKEN "REACT ROOT" KISMINI STRİNG OLARAK TANITMAK İÇİN TEK TIRNAK '' İÇİNE AL!!!
giris = browser.find_element_by_css_selector("#react-root > section > main > article > div.rgFsT > div:nth-child(2) > p > a")
giris.click()
time.sleep(4)
user = browser.find_element_by_name("username")
psw = browser.find_element_by_name("password")
giris2 = browser.find_element_by_css_selector("#react-root > section > main > div > article > div > div:nth-child(1) > div > form > span > button")
a = str(input("Kullanıcı adı: "))
name = user.send_keys(a)
b = str(input("Şifre: "))
sifre = psw.send_keys(b)
giris2.click()
time.sleep(7)

browser.close()

sys.exit()
