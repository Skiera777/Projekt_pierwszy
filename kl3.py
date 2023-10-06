class Car:
    """
    Klasa samochód
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.predkosc = 0

    def gaz(self):
        self.predkosc += 10

    def licznik(self):
        print(f"Predkosc wynosi: {self.predkosc} km/h")

    def hamuj(self):
        self.predkosc -= 10


car1 = Car("Fiat", 2023)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
print(car1.predkosc) #50 - odczytujemy pole
car1.licznik()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()