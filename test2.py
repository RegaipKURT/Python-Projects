from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path='drivers/geckodriver') #mozilla için geckodiriver
# chrome ile kullanılacaksa chromedriver olması gereki
#internetten ndirilip path içine atılmalı


#bir dosyadan adres okuyup sayfa sourrce code almak
dosya = open("new2.txt","r")
siteler = dosya.readlines()

time.sleep(5)

sonuc = open("sonuc.txt", "w")

for i in siteler:
    print(i)
    time.sleep(1)
    driver.get("https://www.google.com/search?source=hp&ei=oK9aXYyIEcX66QSM4regDw&q=mail+%40+{}&oq".format(i))
    time.sleep(2)
    sonuc.write(driver.page_source)
    
sonuc.close()
