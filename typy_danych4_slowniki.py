# słownik - {klucz:wartość}
# typ danych para: klucz - wartość
# odwzorowanie jsona w Pythonie
# {"name":"Radek"}
# klucz nie moze sie powtarzać

dictionary = {}  # pusty slownik takie klamerki
print(dictionary)

dictionary['imie'] = 'Radek'
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 39
print(dictionary)
print(type(dictionary))

print(dictionary.values())
print(dictionary.keys())
print(dictionary.items())

dictionary.update({'date': '12-12-2023'})
print(dictionary)

dictionary1 = {'x': 2}
dictionary1.update([('y', 3), ('z', 5)])
print(dictionary1)

print(dictionary1['x'])  # wypisanie elementu ze słownika

dictionary3 = {'jesc': 'eat', 'kot': 'cat', 'pies': 'dog'}
print(dictionary3['kot'])

print('Mam w słowniku', dictionary3.keys())
key = input("Podaj słowo do przetłymaczenia")  # input - odczytaj np. z klawiatury
print(dictionary3[key.replace(" ", "").lower()])

a = int(input("Podaj liczbe a"))
b = float(input("Podaj liczbe b"))
print(type(a))
print(a + b)
print(a + int(b))