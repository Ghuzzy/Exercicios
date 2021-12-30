def é_hipotenusa(n):
    contadorb = 1
    contadorc = 1
    a = 1
    soma = 0
    verif = 0
    while a <= n:
        contadorb = 1
        while contadorb <= n and verif == 0:
            contadorc = 1
            while contadorc <= n:
                if a**2 == (contadorb**2 + contadorc**2):
                    soma = soma + a
                    verif = 1
                contadorc += 1
            contadorb += 1
        a += 1
        verif = 0
    return soma
