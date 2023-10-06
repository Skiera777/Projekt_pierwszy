# funkcje zwracajace wynik
# wywołanie fukcji: nazwa funkcji + (nawias) + podanie argumentu (##test)

def dodaj(a, b):
    return a + b # zwraca wynik do miejsca wywołania funkcji


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(5,7))
wyn = dodaj(5,6)
print(wyn)
print(dodaj(7,8) + dodaj(8,88))

print(oblicz_vat(1000))
print(oblicz_vat(1000,7))
print(oblicz_vat(vat=15, cena=5000))
zm = oblicz_vat(1000)
if zm == 1230:
    print("dziala")