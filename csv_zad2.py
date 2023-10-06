import csv

import dialect as dialect

filename = 'records.csv'

fields = []
rows = []

with open(filename, 'r') as csv_f:
    # wyszukanie automatyczne separatora dla csv
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)
    print(dialect)
    csv_f.seek(0)  # powrot na poczatek danych, ustawiamy licznik na 0
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)

    print(csvreader)

    fields = next(csvreader)  # odczyt pierwszego wiersza i ustawienie licznika na nastepny
    for row in csvreader:  # petla startuje od indeksu 1, czyli drugiego wiersza
        rows.append(row)

print(fields)
print(rows)
suma = 0
for i in rows:
    number = float(i[-1])
    suma += number

print(f"Średnia wynosi {suma / len(rows)}")
