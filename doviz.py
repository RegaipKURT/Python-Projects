import requests
from_curr = input("From currency: ").upper()
to_curr = input("To currency: ").upper()
amount = float(input("Amount: "))
response = requests.get("http://api.fixer.io/latest?base="+from_curr+"&amp;symbols="+to_curr)
rate = response.json()['rates'][to_curr]
print("Exchange rate: "+ str(round(rate,4))+", "+str(amount)+" "+from_curr+" = " + str(round((rate * amount), 2)) + " " +to_curr)
