def kantor(waluta):
    print("Uruchomienie kantoru")

    def usd():
        x = input("Podaj kwote usd")
        print(f"Wymieniam dolary: {x} usd = {int(int(x) * 4.3)} pln")

    def eur():
        x = input("Podaj kwote eur")
        print(f"Wymieniam euro: {x} eur = {int(int(x) * 4.6)} pln")

    if waluta == 'eur':
        return eur
    else:
        return usd

# kantor_usd = kantor('usd')
# print(kantor_usd)
# kantor_usd()
kantor_eur = kantor('eur')
print(kantor_eur)
kantor_eur()
