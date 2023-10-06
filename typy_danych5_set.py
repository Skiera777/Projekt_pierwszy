# set, zbior - przechowuje niepotwarzajace sie elementy
# tracimy kolejnosc przy dodawaniu (losowa kolejnosc)

lista = [44, 55, 77, 33, 22, 11, 33, 11, 18]
zbior = set(lista)
print(zbior)
print(type(zbior))
zb2 = set()  # pusty zbior
print(zb2)

zbior.add(33)  # add()- dodawanie elementu do zbioru
zbior.add(18)
zbior.add(18)
print(zbior)

zbior.remove(55)  # usuiecie po elemencie
print(zbior)

print(zbior.pop())  # usuniecie pierwszego elementu
print(zbior)
print(len(zbior))  # dlugosc zbioru
zbior.pop()
print(zbior)
print(type(zbior))  # <class 'set'>

lista2 = list(zbior)
print(lista2)

zbior2 = {66, 11, 44, 18, 52, 62, 999, 999}
print(zbior2)
print(type(zbior2))

print(zbior | zbior2)  # suma zbiorów
print(zbior & zbior2)  # czesc wspolna
print(zbior - zbior2)  # róznica
print(zbior.difference((zbior2)))  # roznica
print(zbior2.difference((zbior)))  # roznica

print(zbior)
print(zbior2)