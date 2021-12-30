def primo(n):
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


def maior_primo(n):
    teste = primo(n)
    maiorprimo = 0

    while teste == False:
        n -= 1
        teste = primo(n)

    if teste == True:
        maiorprimo = n

    return maiorprimo
