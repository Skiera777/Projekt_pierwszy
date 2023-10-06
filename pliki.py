# praca z plikami
# kontekst manager (with)

# with open('test.log', )

with open('test.log', 'w', encoding='utf-8') as fh:  # filehandler
    fh.write("Powitanie\n")
    fh.write("kolejne\n")
    fh.write("Powitanie\n")
    fh.write("Jeszcze jedno\n")

with open('test.log', 'w', encoding='utf-8') as file:
    file.write("Radek\n")

with open('test.log', 'a', encoding='utf-8') as f:
    f.write("dodane\n")
    f.write("dośąńdane\n")
    f.write("dożąńdane\n")

with open('test.log', 'r', encoding='utf-8') as file:
    lines = file.read()  # odczyt pliku

print(lines)  # wydruk pliku w konsoli
print(type(lines))