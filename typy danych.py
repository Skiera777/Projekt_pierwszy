wiek = 47
rok = 2023
temp = 36.6
wiek2 = 37.5

print(wiek)
print(type(wiek))

print(5 *"wiek")

print (wiek * rok)
print (wiek + rok)
print (wiek - rok)
print (wiek / rok) # zawsze wynikiem dzielenia jest float
print(wiek // rok) # czesc calkowita dzielenia
print(wiek % rok) # modulo - reszta z dzielenia
print(5 % 2) # 1 bo 2 * 2 = 4 - 5 =
print(wiek ** rok) # potegowanie

print (54 - 5 * 43 + 4/2 + 4/2)
print (54 - (5 * 43) + (4/2 + 4)/2)

print(0.2 + 0.8)
print(0.2 + 0.7)

#float - przechowywane w pamieci jako mantysta i wykladnik

print(0.2 + 0.7 + 0.7)

czy_znasz_pythona = False # obowiazkowo z duzej litery
print(czy_znasz_pythona)

print(int(czy_znasz_pythona)) # int() zamiana na typ int tzw. rzutowanie
# 1 - True, 0 - False

x = 1
print(bool(x)) # bool() zamiana na typ logiczny
x = 100
print(bool(x))
# wszystko czego nie mozna zdefiniowac jako 0 to blad False
x= 'radek'
print(bool(x))

# and - i
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# or - lub
print(True or True)
print(True or False)
print(False or True)
print(False or False)
# True
# True
# True
# False

#not - negacja
print(not True)
print(not False)
# False
# True