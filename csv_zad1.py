# pliki csv
import csv

row = ['radek', 'coe', 3, '9.1']
fields = ['name', 'branch', 'year', 'cgpa']
dict2 = dict(zip(fields, row))
print(dict2)

dict_x = [
    {'name': 'radek', 'branch': 'coe', 'year': 3, 'cgpa': '9.10'},
    {'name': 'tomek', 'branch': 'coe', 'year': 2, 'cgpa': '9.0'},
    {'name': 'kasia', 'branch': 'coe', 'year': 1, 'cgpa': '9'},
]

filename = 'records.csv'
with open(filename, 'w', encoding='utf-8', newline='') as csv_f:  # nazwa zmiennej
    # csvwriter = csv.writer(csv_f) # bibiloteka csv, funkcja writer
    # csvwriter.writerow(row)
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields, delimiter=';')
    csvwriter.writeheader()  # zapisanie nazw kolumn
    # csvwriter.writerow((dict2))  # zapisanie wiersza ze słownika
    csvwriter.writerows(dict_x)
