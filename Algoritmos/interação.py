import time


def insertion(A):
    n = len(A)
    tempoinicial = time.time()
    for i in range(n):
        temp = A[i]
        j = i
        while (j > 0) and (temp < A[j-1]):
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1
        A[j] = temp
    tempofinal = time.time() - tempoinicial
    return A, tempofinal
