#! /usr/bin/env/ python
# -*- coding: utf-8 -*-
import requests
import json
from fixerio import Fixerio


url = "http://data.fixer.io/api/latest?access_key="

birinci = input("Birinci döviz girin:").upper()
ikinci = input("İkinci döviz girin:").upper()
miktar = float(input("Miktar  Giriniz:"))
api_key = "e9ce6ff2f2ba6a315b1f5d58fb977af0"
response = requests.get(url+api_key)
jsonverisi = response.json()
print (jsonverisi)

print (float(jsonverisi["rates"][ikinci]))

Fixerio.latest()
