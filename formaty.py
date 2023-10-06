import sys

user = "Tomek"  # str
wiek = 39  # int
wersja = 3.110058  # float - liczby zmiennoprzecinkowe
liczba = 1345658874  # int
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
# sizeof_digit=4,
# default_max_str_digits=4300,
# str_digits_check_threshold=640)

print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308,
# max_exp=1024,
# max_10_exp=308,
# min=2.2250738585072014e-308,
# min_exp=-1021,
# min_10_exp=-307,
# dig=15, mant_dig=53, epsilon=2.220446049250313e-16,
# radix=2, rounds=1)

print("Witaj %s masz teraz %d lat" % (user, wiek))
# print("Witaj %s masz teraz %d lat" % (wiek, user)) # TypeError: %d format: a real number is required, not str
# %s - str
# %d - digit - liczby
# przy konwerncji z % python weryfikuje typ danych

print("Witaj %(user)s, masz teraz %(age)d lat." % {"user": user, "age": wiek})

print("Witaj {} masz teraz {} lat.".format(wiek, user))
# przy takim zapisie nie sprawdza typow

print(f"Witaj {user}, masz teraz {wiek} lat.")
# f - fstring - tekst sformatowany {} dla zmiennych

print("Uzywamy wersji Pythona %i" % 3)
print("Uzywamy wersji Pythona %f" % 3.11)
print("Uzywamy wersji Pythona %.1f" % 3.11)
print("Uzywamy wersji Pythona %.2f" % 3.11)
print("Uzywamy wersji Pythona %.0f" % 3.11)
print("Uzywamy wersji Pythona %.f" % 3.11)
print("Uzywamy wersji Pythona %.f" % 3.9)
#  zero miejsc po przecinku zaokragla podczas wyswietlania
x = 3.14
print("zero miejsc po przecinku %.f" % x)
print("oryginalny x=", x)
# zero miejsc po przecinku 3
# oryginalny x= 3.14

print(f"uzywamy wersji pythona {wersja}")
print(f"uzywamy wersji pythona {wersja:.1f}")
print(f"uzywamy wersji pythona {wersja:.0f}")

print(f"{user:>10}")  # Tomek - uzupelnilo spacjami z LEWEJ strony do 10 znakow
print(f"{user:>20}")
print(f"{user:<30}")  # Tomek - uzupelnilo spacjami z PRAWEJ strony do 10 znakow
print(f"{user:^30}")  # wysrodkowanie

print(liczba)
print("Nasza duża liczba {:,}".format(liczba))
print("Nasza duża liczba {:,}".format(liczba).replace(",", "."))

print(f"Nasza duza liczba {liczba:,}")
print(f"Nasza duza liczba {liczba:,}".replace(",", " "))

# ctrl alt L - wyrownanie tekstu
