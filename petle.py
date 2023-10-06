# petle
# instrukcja sterowania przepływem
# for - petla iteracyjna
import random
from itertools import zip_longest

for i in range(10):
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):  # tzw. niema zmienna "_"
    pass

lista2 = list(range(1, 50))
for i in range(6):
    wyn = random.choice(lista2)
    lista2.remove(wyn)
    print(wyn)
print(lista2)

for i in range(10):
    print(i * 2)

for i in range(10):
    if i % 2 == 0:
        print(i, "Parzysta")

lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)

lista4 = []
for j in range(10):
    if j % 2 == 0:
        lista4.append(j)

print(lista4)

for c in lista4:
    if c == 2:
        c += 1  # c = c + 1
    print(c)

a = 1
a += 1  # a = a + 1
print(a)
a -= 1  # a = a - 1
print(a)
a *= 3  # a= a * 3
print(a)
a %= 2  # a = a % 2 reszta z dzielenia
print(a)
a /= 2  # a = a / 2 - dzielenie rzeczywiste zwraca zawsze float
print(a)

imiona = ['Radek', 'Asia', 'Zbyszek', 'Karolina']
for p in range(len(imiona)):
    print(p, imiona[p])

for p in imiona:
    print(imiona.index(p), p)

# enumerate() - zwraca ponumerowane elementy kolekcji
for p in enumerate(imiona):
    print(p)
a, b = (0, 'Radek')
print(a)
print(b)

for p, w in enumerate(imiona):
    print(p, w, sep=";", end='')  # zmiana separatora sep, usuniecie entera i wstawienie spacji end
# z automatu jest w print wstawiona spacja
print()

ludzie = ['Radek', 'Zenek', 'Andrzej', 'Karolina', 'Kasia']
wiek = [47, 67, 43, 32]

# for p,o in enumerate(ludzie):
# print(p,o, wiek[p])

# zip() - łączy kolekcje
for k in zip(ludzie, wiek):
    print(k)
# o,w = k gdzie k to krotka ('karolina', 32)
for o, w in zip(ludzie, wiek):
    print(o, w)

for p in enumerate(zip(ludzie, wiek)):
    print(p)
a, b = (3, ('Karolina', 32))
print(a, b)
c, d = b
print(a, c, d)

for a, (c, d) in enumerate(zip(ludzie, wiek)):
    print(a, c, d)

for a, (c, d) in enumerate(zip(ludzie, wiek), start=1): # start=1 zacznij numerowanie od 1, a nie od 0
    print(a, c, d)

jezyk = ['python', 'java']

zipped = zip_longest(ludzie, wiek, jezyk, fillvalue='Nan')
print(type(zipped))
zipped_list = list(zipped)

for item in zipped_list:
    print(item)

for o, w, j in zipped_list:
    print(o, w, j)