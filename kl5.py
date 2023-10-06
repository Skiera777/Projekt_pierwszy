# klasa abstrakcyjna - klasa z ktorej nie mozna stworzyc obiektu
from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    klasa opisujaca ptaka w Pythonie"""

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "lecę z szybkością", self.szybkosc)

    @abstractmethod # oznaczylismy metode jako abstrakcyjna
    def wydaj_odglos(self):
        pass

class Kura(Ptak): # dziedziczenie po Ptaku
    """
    Kura
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)
        self.gatunek = gatunek

    def latam(self):
        print(f"Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("kokokoko")

class Orzel(Ptak):
    """
    Orzel
    """
    def wydaj_odglos(self):
        print(f"piiiiii")

# po dodaniu @abstractmethod klasa Ptak staje sie abstrakcyjna, bo posiada metode abstrakcyjna
# nie mozna utworzyc takiej klasy
# orz1 = Ptak("orzeł", 15)
# orz1.latam()
# kur1 = Ptak("kura", 0)
# kur1.latam()
# kur1.wydaj_odglos()

kur2 = Kura("Kura")
print(kur2.gatunek)
kur2.latam()
kur2.wydaj_odglos()
orz2 = Orzel("Orzel", 34)
orz2.latam()
orz2.wydaj_odglos()