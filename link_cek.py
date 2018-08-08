import requests
from bs4 import BeautifulSoup


r = requests.get("https://www.yellowpages.com/search?search_terms=cafe&geo_location_terms=ankara")
r.content
s = BeautifulSoup(r.content)

print (s.prettify)
linkler = s.find_all("a")

for link in linkler:
    print (link.get("href"))

for link in linkler:
    print ("---------------------------------------------------------------------")
    print("İsim: ",link.text,)
    print("Adres: ",link.get("href"))
    print ("---------------------------------------------------------------------")
