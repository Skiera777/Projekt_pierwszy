class Human:
    """
    Klasa opisujaca czlowieka w Pythonie
    """

    # konstruktor/ inicjalizator
    def __init__(self, imie, wiek, wzrost, plec='k'):
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self): # jak piszemy w klasie obowiazkowo self
        print(self)
        print(f"Nazywam sie {self.imie}")

    def lata(self):
        print(f"Wiek: {self.wiek}")

    def ile_wzrostu(self):
        print(f"Wzrost:", self.wzrost, "cm")

    def jaka_plec(self):
        print(f"Plec:", self.plec)

    def ruszaj(self):
        if self.plec == 'k':
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


cz1 = Human("Kasia", 29, "178")
print(cz1.wiek)
print(cz1.imie)
print(cz1.wzrost)
print(cz1.plec)
cz1.ile_wzrostu()

cz2 = Human("Staszek", 33, "198", "m")
print(cz2.wiek)
print(cz2.imie)
print(cz2.wzrost)
print(cz2.plec)
cz2.ile_wzrostu()
cz1.ruszaj()
cz2.ruszaj()
cz1.jaka_plec()
cz2.jaka_plec()