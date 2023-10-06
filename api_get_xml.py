import requests as re
import xml.etree.ElementTree as ET

url = 'http://api.nbp.pl/api/exchangerates/tables/A/?format=xml'

response = re.get(url)
print(response)
xml_data = response.content
print(xml_data)

root = ET.fromstring(xml_data)

table_name = root.find(".//Table").text
print(table_name)
date = root.find(".//EffectiveDate").text
print(date)
no = root.find(".//No").text
print(f"Numer tabeli: {no}")
rates = root.findall(".//Rate")
print(rates)
print(type(rates))

for rate in rates:
    currency = rate.find("Currency").text
    code = rate.find("Code").text
    mid = rate.find("Mid").text
    print(f"{code}: {currency} - {mid}")
