import math
a = int(input("Digite o valor de a :"))
b = int(input("Digite o valor de b :"))
c = int(input("Digite o valor de c :"))

delta = (b**2 - (4*a*c))

if delta == 0:
    xI = (-b) / 2*a
    print("A equação possui apenas uma raíz, sendo esta: ", xI)

if delta < 0:
    print("A equação não possui raízes reais")

if delta > 0:
    xI = ((-b) + (math.sqrt(delta)))/2*a
    xII = ((-b) - (math.sqrt(delta)))/2*a
    print("O resultado da equação é: ")
    print("xI =", xI, "xII =", xII)
