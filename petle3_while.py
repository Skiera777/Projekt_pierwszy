# while - petla sterowania warunkiem (nie licznikiem jak w przypadku for)
# instrukcja sterowania przepływem programu
# dopoki True petla sie wykonuje

licznik = 0
while True:
    licznik += 1
    print("Komunikat")
    if licznik > 10:
        break  # przerywa działanie tej pętli
print("Dalsza czesc programu")

print(licznik)
print("Dalsza czesc programu")
licznik = 0
while licznik <11:
    print("Komunikat")
    licznik += 1

lista = []
lista2 = []

while True:
    wej = input("Podaj liczbe") # input standardowo pobiera/wypluwa stringi
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista2.append(int(wej))

print(lista) # ['1', '2', '3', '4', '5', '6'] - oddzielone '' to stringi
print(lista2) # [1, 2, 3, 4, 5, 6] to int