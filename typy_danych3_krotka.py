# krotka (tupla) - niezmienna lista
# zmienna, niezmienna - jednoelementowa krotka
tupla = "radek", # musi mieć na końcu przecinek zeby byl type tuple
print(type(tupla))
temp = 37,5
print(type(temp))
print((temp))

tupla2 = "Tomek", "Radek", "Zenek", "Marek"
tupla2a = ("Tomek", "Radek", "Zenek", "Marek")
print(type(tupla2))
print(type(tupla2a))
print(tupla2)

# tupla moze byc traktowana tez jako zmienna (niezmienna)
tupla3 = 43, 55, 22.34, 11, 200
print(type(tupla3))

print(tupla2.index("Tomek"))
print(tupla2.count("Tomek"))

a, b = 1, 2
print(a)
print(b)
print(type((1,2))) # rozpakowanie tupli

a, *b = 1, 2, 3 # * (gwiazdka) - worek na pozostale elementy
print(a)
print(b)

print(tupla2)
imie1, *imie2, imie3 = tupla2
print(imie1)
print(imie2)
print(imie3)

lista = list(tupla3) # zamiana (rzutowanie) tupli na liste
print(lista)
print(type(lista))

