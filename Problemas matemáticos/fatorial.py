def main(m, n):
    combinacao = ""
    if m < n:
        print("O valor de M tem de ser maior ou igual a N")
    else:
        combinacao = fatorial(m)/(fatorial(m-n)*fatorial(n))
        return combinacao


def fatorial(n):
    k_fat = 1
    if n == 0:
        print("1")
    else:
        while n >= 1:
            k_fat = k_fat*(n)
            n = n-1
    return k_fat
