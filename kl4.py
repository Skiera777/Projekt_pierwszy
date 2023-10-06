class Dom:
    """
    klasa opisujca dom
    """

    def __init__(self, metraz, kolor, liczba_okien): # __init__ konstruktor
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def mam_kolor(self):
        print(f"Mam kolor: {self.__kolor}")

    def mam_metraz(self):
        print((f"Mam metraz {self.__metraz}"))

    def mam_okna(self):
        print(f"Mam okien {self.__liczba_okien}")

    def zmien_kolor(self):
        wybor = input("podaj kolor")
        self.__kolor = wybor
        self.mam_kolor()
        self.__farba()

    def zmien_okna(self):
        wybor = int(input("podaj liczbe okien"))
        self.__liczba_okien = wybor
        self.mam_okna()

    def zmien_metraz(self):
        wybor = int(input("podaj metraz"))
        self.__metraz = wybor
        self.mam_metraz()

    def __farba(self):
        print("Skonczyla sie farba")



dom1 = Dom(150, "biały", 10)
dom1.mam_okna()
dom1.mam_metraz()
dom1.mam_kolor()
dom1.zmien_metraz()
dom1.zmien_kolor()