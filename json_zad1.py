# json - {"name":"Radek"}
# obiekty typu klucz:wartość
import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))

dict_json = json.dumps(person_dict)  # dumps ze słownika na stringa odpowiednika jsona
print(dict_json)
print(type(dict_json))  # zamiana na json to wyplucie stringa

with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)  # dump zapisanie do pliku jsona

with open('nasze_dane.json', 'r') as f:
    data = json.load(f)

print(data)
print(type(data))

print(data.keys())
print(data.values())
print(data.items())

print(data['name'])  # Radek - wypisanie wartości poprzez podanie nazwy klucza
