import requests
import sys
access_key = "78e44fffb788ba4161909eff6b852181" 
#you can use this acces key or take another one from fixer.io

while True:

    try:

        print("""
        1 - ) Exhange Rate
        2 - ) Historical Data
        3 - ) Exit
        """)
        a = input("Choose a Value:")
        if int(a) == 1:
            from_curr = input("From currency: ").upper()
            to_curr = input("To currency: ").upper()
            amount = float(input("Amount: "))
            response = requests.get("http://data.fixer.io/api/latest?access_key={}".format(access_key))
            rate = response.json()['rates'][to_curr] / response.json()['rates'][from_curr]
            print("Exchange rate: "+ str(round(rate,4))+", "+str(amount)+" "+from_curr+" = " + str(round((rate * amount), 4)) + " " +to_curr)
        elif int(a) == 2:
            date = input("Date (YYYY-MM-DD): ")
            base = input("Currency Symbol: ").upper()
            response = requests.get("http://data.fixer.io/api/{}?access_key={}".format(date, access_key))
            rate = response.json()['rates'][base]
            print(date + " EURO based " + base + " value: " + str(rate))
        elif int(a) == 3:
            break

    except:
        print("Unknown value. Please Try Again!")
        continue
