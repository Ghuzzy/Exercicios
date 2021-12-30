def menor_nome(nomes):
    nomes = [nome.strip() for nome in nomes]
    menornome = nomes[0]
    x = len(nomes)
    for i in range(x):
        if len(menornome) > len(nomes[i]):
            menornome = nomes[i]
    print(menornome.capitalize())
