# # instrukcje warunkowe - instrukcja sterowania przeplywem programu
# if
# sterowana warunkie, jezeli warunek jest True to wykonuje dzialania z wydzielonego bloku

odp = True
if odp:
    print("Brawo")  # obowiązkowo wcięcie przy warunkach (4 spacje), conajmniej jedna komenda
else:
    print("Musisz sie dalej uczyc")
print("Działam dalej")

podatek = 0.0
zarobki = int(input("Podaj dochód"))
if zarobki < 10000:
    podatek = 0.0
elif zarobki < 30000:
    podatek = 0.2
elif zarobki < 100000:
    podatek = 0.4
else:
    podatek = 0.6

print(podatek)
print(f"Podatek wynosi {zarobki * podatek}")

# kolejnosc ma znaczenie

suma_zam = 250
if suma_zam > 150:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabat wynosi {rabacik}")  # f - string format

rabat = 25 if suma_zam > 150 else 0
print(f"Rabat wynosi {rabat}")

lista_bledow = []
alert_system = 'x'
error = 'inny'
error_message = "Stało się coś strasznego"

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    lista_bledow.append("email")
    if error == 'medium':
        lista_bledow.append('ostrzeżenie')
    elif error == 'critical':
        lista_bledow.append("krytyczny")
    else:
        lista_bledow.append("inny blad")
else:
    print("system nieznany")
print(lista_bledow)

a = 14
b = 3
print(f"Wynik porówniania {a} > {b}, {a > b}")
print(f"Wynik porówniania {a} < {b}, {a < b}")
print(f"Wynik porówniania {a} >= {b}, {a >= b}")
print(f"Wynik porówniania {a} <= {b}, {a <= b}")
print(f"Wynik porówniania {a} == {b}, {a == b}") # porownianie ==
print(f"Wynik porówniania {a} != {b}, {a != b}") # rozne !=


odp = input("Podaj rok wejscia PL do UE")
if odp == '2004':
    print("Dobrze!")
else:
    print("Zle!")


