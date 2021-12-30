n = int(input("Digite um número inteiro:"))
digito1 = 0
digito2 = 0
contador = 0

while n > 0:
    digito1 = n % 10
    n = n//10
    digito2 = n % 10
    if digito1 == digito2:
        contador = contador + 1

if contador > 0:
    print("sim")
else:
    print("não")
