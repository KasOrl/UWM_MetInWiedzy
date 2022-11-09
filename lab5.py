import numpy as np


def wyznacznik_macierzy(A):
    wynik = 0

    if czy2n2(A):
        print(A)
        return ((A[0][0]* A[1][1]) - (A[1][0] * A[0][1]))
    else:
        for ind in range(len(A)):
            Ac = A.copy()
            Ac = A[1:len(Ac)]
            print("po usunieciu wiersza")
            print(Ac)
            height = len(Ac)

            for i in range(height):
                Ac[i] = np.delete(Ac[i], ind)

            print("po usunieciu kolumny")
            print(Ac)
            znak = (-1) ** (ind % 2)

            podmacierz = wyznacznik_macierzy(Ac)
            wynik += znak * podmacierz * A[0][ind]
    return wynik


def czy2n2(matryca):
    m = matryca.copy()
    h = len(m)
    w = len(m[0])
    print(m)
    if h == 2 and w == 2:
        print("jest 2x2")
        return 1
    else:
        print("jest wieksza")
        return 0


matryca2 = [[1, 2, 3], [1, 5, 3], [12, 3, 4]]
matryca = [[1, 3], [6, 5]]
m1 = [[-2,2,-3],[-1,5,3],[2,0,-1]]

moja = wyznacznik_macierzy(m1)
print("Numpyowy: ")
print(np.linalg.det(m1))
print("moja: ")
print(moja)