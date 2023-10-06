tekst = "Witaj Świecie"
print(tekst)
print(type(tekst)) # <class 'str'>

tekst2 = tekst.upper() # zamiana tekstu na duze litery
# przypisalismy do tekst2 wynik dzialania metody upper()

print(tekst)
print(tekst2)
# teksty sa immutable (niezmienne) niemutowalne
print(tekst.lower())

print(tekst.removeprefix("Witaj")) # swiecie
print(tekst.removesuffix("Świecie")) # witaj
print(tekst.removesuffix("Świecie").upper()) # WITAJ
print(tekst) # witaj swiecie
# ctrl d - kopiowanie linii kodu w ktorej ustawiony jest kursor

encoded_s = tekst.encode('utf-8')
print(encoded_s) # b'Witaj \xc5\x9awiecie'
print(type(encoded_s)) # <class 'bytes'>
print(encoded_s.decode('utf-8')) # Witaj Świecie
# indeksowane od 0
print(tekst[0]) # W
print(tekst.count("i"))
print(tekst.count("i",0,4)) #1
print(tekst.count("j",0,4)) # 0 z prawej strony zbior otwarty - 4 nie brane pod uwage

print(len(tekst)) # 13 dlugosc tekstu umieszczonego w tekst

imie = "Piotr"
tekst_format = f"Mam na imie {imie} i lubię Pythona"
print(tekst_format)
# f - fstringi - czyli sformatowane stringi
# w nawiasie {} umieszczamy nazwy zmiennych, ktorych zawartosc chcemy wyswietlic

tekst_format = f"\tMam na imie {imie}\n i lubię Pythona \b"
print(tekst_format)
# \t - tabulator/wciecie
# \n - nowa linia
# \b - backspace, skasowalo spacje

starszy = "Witaj %s"
# %s - oznacza wstaw w to miejsce string
print(starszy % imie)

print("""
    Tekst
wielolinijkowy""")

print("Witaj {}".format(imie))