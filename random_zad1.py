import random

# importowanie biblioteki random - do generowania liczb pseudolosowych

print(random.randint(1, 6))  # 1...6
print(random.random())  # float 0.... 0.99999
print(random.random() * 6)  # float 0... 5.99999
print(random.randrange(6))  # int 0...5
print(random.randrange(1, 6))  # int 1...5

lista = [5, 7, 45, 34, 56]
print(random.choice(lista))

lista2 = list(range(1, 50))
print(lista2)
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))

wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)

print(random.choices(lista2, k=7))  # losuje z powtorzeniami
print(random.sample(lista2, 7))  # losuje bez powtorzen
