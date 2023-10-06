# REST API - GET, POST, PUT, DELETE, HEAD (pobiera tylko nagłowki)
# odpowiednik w bazie danych select, insert, update, delete
# CRUD - create, read, update, delete
import requests as re
# pip install requests

#url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/'
url = 'http://api.nbp.pl/api/exchangerates/rates/A/EUR/'
response = re.get(url)
print(response)
# <Response [200]> - ok
# 3XX - bledy konfiguracji np. przekierowania
# 4XX - np. 404 - brak zasobu, 400 bad request
# 5XX - wewnetrzne błedy serwera np. blad bazy danych

table = response.json()
print(table)

print(table['table'])
print(table['currency'])
print(table['code'])
print(table['rates'])
print(table['rates'][0])
print(table['rates'][0]['no'])
print(table['rates'][0]['effectiveDate'])
print(table['rates'][0]['mid'])


