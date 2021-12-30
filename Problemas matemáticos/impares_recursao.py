def encontra_impares(lista, i=0, lista2=[]):
    if len(lista) < i+1:
        return None
    if lista[i] % 2 != 0:
        lista2.append(lista[i])
    encontra_impares(lista, i+1, lista2)
    return lista2
