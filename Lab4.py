import numpy as np

def rzad_macierzy(A):
    rzad = len(A[0])
    for row in range(rzad):
        #A[0] - A[row-1] = 0
        #[row] != 0
        if A[row][row] != 0:
            for col in range(len(A)):
                if col != row:
                    mnoznik = (A[col][row]/A[row][row])
                    for i in range(rzad):
                        A[col][i] -= (mnoznik*A[row][i])
        else:
            redukowanie = True

            for i in range(row+1,len(A)):
                # w momencie natrafienia na element niezerowy, robimy podmiane rzedow
                if A[i][row] != 0:
                    swap(A,row, i, rzad)
                    redukowanie = False
                    break
            #sprawdzamy czy bedziemy redukowac kolumny (if)
            if redukowanie:
                rzad -= 1
                for i in range(len(A)):
                    A[i][row] = A[i][rzad]


            row -=1
    return rzad
def swap(A, rzad1, rzad2, col):
    for i in range(col):
        temp = A[rzad1][i]
        A[rzad1][i] = A[rzad2][i]
        A[rzad2][i] = temp

matryca = [[1, 2, 3],
            [1, 5, 3],
            [12, 3, 4]]
print("rzad numpyem")
print(np.linalg.matrix_rank(matryca))
moja = rzad_macierzy(matryca)
print(moja)
