def n_primos(n):
    contador = 1
    while n > 2:
        if primos(n) == True:
            contador += 1
        n -= 1
    return contador


def primos(n):
    i = n//2
    verif = 0
    eprimo = False
    if n > 2 and (n % 2 != 0):
        while i > 1:
            if n % i == 0:
                verif += 1
            i -= 1
        if not verif > 0:
            eprimo = True
    if n == 1 or n == 2 or n == 0:
        eprimo = True

    return eprimo


print(n_primos(2))
print(n_primos(4))
print(n_primos(121))
