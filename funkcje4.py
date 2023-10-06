# funkcje zagnieżdzone

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")
    return fun2 # zwracamy tylko adres funkcji fun 2 dlatego bez nawiazow


x = fun1()
print(x)
print(type(x))
x()