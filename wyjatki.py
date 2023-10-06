# kalkulator
while True:
    print(f"""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec""")

    odp = input("Podaj operacje")
    if odp >= '5':
        print("Nie znam takiego dzialania")
        break
    try:
        a = float(input("Podaj pierwszą liczbe"))
        b = float(input("Podaj drugą liczbę"))

        if odp == '1':
            print("Wynik", a + b)
        elif odp == '2':
            print("Wynik", a - b)
        elif odp == '3':
            print("Wynik", a * b)
        elif odp == '4':
            print("Wynik", a / b)
        else:
            print("Nie znam takiego dzialania")
    except  ZeroDivisionError:
        print("Nie dziel przez zero")
    except ValueError:
        print("Błąd wartości")
    except Exception as e:  # łapie pozostałe wyjątki
        print("Błąd", e)
    else:  # wykonuje sie tylko gdy nie ma błedu
        print("Gdy nie ma błedu")
    finally:  # wykonuje sie zawsze
        print("Zawsze")


while True:
    try:
        z = input("Podaj działanie + - * /")
        a = float(input("Podaj pierwszą liczbe"))
        b = float(input("Podaj drugą liczbę"))
        match z:
            case "+":
                print(f"Wynik dodawania {a} + {b} = {a + b}")
        match z:
            case "-":
                print(f"Wynik dodawania {a} - {b} = {a - b}")
        match z:
            case "*":
                print(f"Wynik dodawania {a} * {b} = {a * b}")
        match z:
            case "/":
                print(f"Wynik dodawania {a} / {b} = {a / b}")
            case _:
                break
    except  ZeroDivisionError:
        print("Nie dziel przez zero")
    except ValueError:
        print("Błąd wartości")
    except Exception as e:  # łapie pozostałe wyjątki
        print("Błąd", e)
    else:  # wykonuje sie tylko gdy nie ma błedu
        print("Gdy nie ma błedu")
    finally:  # wykonuje sie zawsze
        print("Zawsze")





#NA TEST