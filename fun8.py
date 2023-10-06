def allparams(a, b, c=42, *args, d=256, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print("args", args)
    print("kwargs", kwargs)


allparams(1, 2)
allparams(1, 2, 3)
allparams(1, 2, c=3)
allparams(b=1, a=2, c=3)

# slash / - oddziela argumenty pozycjyne od nazwanych
# a i b mogą być tylko po kolejnosci podane

allparams(1, 2, 3, 4, 4, 5, 6, 7, 8, 9)
allparams(1, 2, 3, 4, 4, 5, 6, 7, 8, 9)
allparams(1, 2, 3, 4, 4, 5, 6, 7, 8, 100, 106, 109987)
allparams(1, 2, 3, 4, 4, 5, 6, 7, 8, d=129)
allparams(1, 2, 3, 4, 4, 5, 6, 7, 8, d=129, klucz='wart')
allparams(1, 2, 3, 4, 4, 5, 6, 7, 8, d=129, klucz='wart')
allparams(1, 2, 3, 4, 4, 5, 6, 7, 8, d=129, klucz='wart', a=8)
