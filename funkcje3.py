a = 10
b = 10


def dodaj():
    a = 6  # zmienne lokalne, maja zakres lokalny (scope) zdefiniowane wewnatrz funkcji nie zmieniaja wartosci globalnej
    b = 7
    print(a + b)


def dodaj2():
    print(a + b)  # wykona sie na wartosciach globalnych


def dodaj3():
    global a  # brane do funkcji a globalne
    a = 6
    b = 7
    print(a + b)


print("zmienna a z gory", a)
dodaj()
print("Zmienna a z gory", a)
dodaj2()
print("Zmienna a z gory", a)
dodaj3()
print("Zmienna a z gory", a)
dodaj2()
