def ordenada(lista):
    for i in range(len(lista)):

        if i+1 < len(lista):
            if lista[i] > lista[i+1]:
                return False
    return True


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [9, 8, 7, 6, 5, 43, 2, 1]
