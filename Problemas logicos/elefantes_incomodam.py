def incomodam(n):
    if n <= 0:
        return ''
    else:
        return 'incomodam ' + str(incomodam(n-1))

def elefantes(n, x = 1):
    if n <= 1 or x > n:
        return ''
    else:
        if x == 1:
            return 'Um elefante incomoda muita gente \n' + str(elefantes(n, x+1))
        else:
            if x == n:
                return str(x)+' elefantes '+str(incomodam(x))+'muito mais\n'
            else:
                return str(x)+' elefantes '+str(incomodam(x))+'muito mais\n'+str(x)+' elefantes incomodam muita gente\n'+str(elefantes(n,x+1))

print(elefantes(5))