# match case

lista = []
lang = input("Podaj znany jezyk programowania")

match lang.lower().replace(" ", ""):
    case "python":
        lista.append(lang)
    case "c++":
        lista.append(lang)
    case "java":
        lista.append(lang)
    case _:  # wartosc domyslna (odpowiednik else)
        print("nie znam takiego działania")
print(lista)
