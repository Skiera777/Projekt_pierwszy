import csv

lista = []

with open('dane.csv', 'r') as file:
    reader = csv.reader(file)

    for i in reader:
        lista.append(i)

print(lista)
print(lista[1][1])

lista[1][1] = "Kasia"
print(lista)

with open('dane.csv', 'w', newline='') as file:  # otworzenie pliku
    writer = csv.writer(file)  # stworzenie urzadzenia co umie zapisac csv do pliku
    writer.writerows(lista)  # zaisanie do pliku
