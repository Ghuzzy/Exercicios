def soma_matriz(x, y):
    somalinha = []
    somamatriz = []
    j = 0
    for i in range(len(x)):
        somalinha = []
        j = 0
        for elementos in x[i]:
            somalinha.append(elementos + y[i][j])
            j += 1
        somamatriz.append(somalinha)
    return somamatriz
