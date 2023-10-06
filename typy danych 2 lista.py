# lista - kolekcja przechowujaca dowolna ilosc danych
# przechowuje rozne typy danych  w jednej kolekcji
# zachowuje kolejnosc dodawania elementow

lista = [] # definicja pustej listy
print(lista)
print(type(lista))

print(bool(lista))

lista.append("Radek")
print(lista)
lista.append("maciek")
lista.append("jasko")
lista.append("zenek)")
lista.append("marta)")

print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])
print(lista[-5])

lista.insert(1, "Marcin")
print(lista)

ind = lista.index("Marcin")
print(ind)
#usuniecie elementu po indeksie

a = 1
b = 3
a = b
print(a)
print(b)
a = 7
print(b)

lista2 = lista

tekst = "Python"
lista_1 = list(tekst) #rozpakowanie sekwencji
print(lista_1)

lista2 = [tekst]
print(lista2)

print(lista_1 + lista2)

krotka = tuple(liczby)
print(krotka)