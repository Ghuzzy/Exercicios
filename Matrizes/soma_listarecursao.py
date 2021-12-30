def soma_lista(lista, i=0):

    if i+1 > len(lista):
        return 0
    else:
        return lista[i] + soma_lista(lista, i+1)
