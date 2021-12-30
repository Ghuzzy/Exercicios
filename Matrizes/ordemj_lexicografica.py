def primeiro_lex(lista):
    x = lista[0]
    for i in range(len(lista)):
        if x > lista[i]:
            x = lista[i]
    print(x)
