import requests
from bs4 import BeautifulSoup
from termcolor import colored

imdburl = "https://www.imdb.com/chart/top"
r = requests.get(imdburl)

soup = BeautifulSoup(r.content, "html.parser")

gelenveri = soup.find_all("table", {"class": 'chart full-width'})

film_tablosu = (gelenveri[0].contents)[len(gelenveri[0].contents)-2]

film_tablosu = film_tablosu.find_all("tr")

for film in film_tablosu:
    film_basligi = film.find_all("td", {"class": 'titleColumn'})
    filmismi = film_basligi[0].text
    filmismi = filmismi.replace("\n","")
    print (colored(filmismi,"cyan"))
    