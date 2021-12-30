def conta_letras(frase, contar="vogais"):
    contador = 0
    frase = frase.lower()
    if contar == "vogais":
        for caractere in frase:
            if (ord(caractere) == 97) or (ord(caractere) == 101) or (ord(caractere) == 105) or (ord(caractere) == 111)or (ord(caractere) == 117):
                contador +=1

    elif contar == "consoantes":
        for caractere in frase:          
            if (ord(caractere) != 97)and(ord(caractere) != 101)and(ord(caractere) != 105)and(ord(caractere) != 111)and(ord(caractere) != 117) and (ord(caractere)>97 and ord(caractere)<=121):
                contador +=1

    return contador


print(conta_letras('programamos em python', 'consoantes'))      