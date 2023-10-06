dictionary = {'imie': 'Radek', 'nazwisko': 'Kowalski'}
print(type(dictionary))

# wypisuje klucze! w przypadku iteracji po slowniku
for k in dictionary:
    print(k)
# wypisanie kluczy
for k in dictionary.keys():
    print(k)
# wypisanie wartosci
for v in dictionary.values():
    print(v)
# wypisanie par
for i in dictionary.items():
    print(i)
# rozpakowana para klucz wartosc
for k, v in dictionary.items():
    print(k, '=>', v)

dictionary2 = {'name': 'imie', 'company': 'rozne'}  # zamiana kolejnosci key z value
print({value: key for key, value in dictionary2.items()})

# to samo co wyżej tylko w innym formacie
d2 = {}
for key, value in dictionary2.items():
    d2[value] = key
print(d2)
