# napisz funkcje obliczajaca srednia

def liczby(i=0, *cyfry):  # uzywamy * jezeli nie wiemy ile argumentow nam przyjdzie
    print(cyfry)
    suma = 0
    try:
        for c in cyfry:
            suma += c
        count = len(cyfry)
        avg = suma / count
    except Exception as e:
        print("Blad", e)
    else:
        print(f"Średnia dla ucznia {i} wynosi {avg}")


liczby()
liczby(1, 2, 3)
liczby("Radek", 2, 3, 4, 5, 6, 7) # string na pierwszym miejscu, bo i definiujemy jako pierwsze
