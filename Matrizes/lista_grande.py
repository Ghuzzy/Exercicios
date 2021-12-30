
from random import randint


def lista_grande(n):
    lista = []
    for i in range(n):
        lista.append(randint(0, 5000))

    return lista


def ordena(lista):
    x = len(lista) - 1
    for i in range(x):
        posicaomin = i
        for j in range(i+1, x+1):
            if lista[j] < lista[posicaomin]:
                posicaomin = j
        lista[i], lista[posicaomin] = lista[posicaomin], lista[i]

    return lista
