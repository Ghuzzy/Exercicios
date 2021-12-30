import math
a, b, c = float(input("Escreva a: ")), float(
    input("Escreva b: ")), float(input("Escreva c: "))

delta = (b**2) - (4*a*c)

if delta < 0:
    print("esta equação não possui raízes reais")
else:
    xI = (-b + (math.sqrt(delta)))/2*a
    xII = (-b - (math.sqrt(delta)))/2*a
    if (delta == 0):
        print("a raiz desta equação é", xI)
    if (xI == xII):
        print("a raiz dupla desta equação é", xI)
    if (xI > xII):
        print("as raízes da equação são", xI, "e", xII)
    else:
        print("as raízes da equação são", xII, "e", xI)
