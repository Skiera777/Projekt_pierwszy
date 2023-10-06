# funkcja - wydzielony kod programu, ktory mozna wykonywac wielokrotnie

a = 6
b = 7


# definicja funkcji, tu funcja sie nie wykonuje
def dodaj():  # fukcja bezargumentowa
    print(a + b)


def dodaj2(a, b):  # funkcja z dwoma argumentami, obowiazkowe a i b
    print(a + b)


def odejmij(a, b, c=0):  # argument c ma wartosc domyslna
    print(a - b - c)


def odejmij2(liczba1, liczba2):  # argument c ma wartosc domyslna
    print(liczba1 - liczba2)


# wywołanie/uruchomienie funkcji
dodaj()
dodaj2(6, 10)
odejmij(1, 2, 7) # przekazywanie pozycyjne
odejmij(b=6, a=8, c=1) # argumenty nazwane
odejmij2(10,7)
odejmij2(liczba2=7, liczba1=10)
print(dodaj()) # None - funkcja nie zwraca wyniki (tylko wypisuje)
###NA TEST