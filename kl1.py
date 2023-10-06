# klasa - szablon(formularz) wskazujacy jakie cechy bedzie mial obiekt
# cechy - pola (zmienne)
# działania - funkcje
# obiekt - budowany na podstawie klasy (instancja klasy)

# definicja klasy PEP8 - wskazuje, ze nazwy klas z duzej litery (da sie z malej, ale niezgodnie z PEP)
class Human:
    """
    Klasa opisujaca czlowieka w Pythonie

    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self): # jak piszemy w klasie obowiazkowo self
        print(self)
        print(f"Nazywam sie {self.imie}")

    def lata(self):
        print(f"Wiek: {self.wiek}")


print(Human.__doc__)  # wypisanie dokumentacji

print(print.__doc__)

help(print())

cz1 = Human()  # tworzenie obieku, uruchamianie klasy Human
print(cz1)
print(cz1.plec)
cz1.imie = "Kasia"
cz1.wiek = 29
print(cz1.imie)
print(cz1.wiek)
cz1.powitanie()

cz2 = Human()
cz2.imie = "Karol"
cz2.wiek = 33
cz2.plec = "m"
print(cz2.imie)
print(cz2.plec)
print(cz2.wiek)
cz2.powitanie()
cz1.lata()
cz2.lata()

