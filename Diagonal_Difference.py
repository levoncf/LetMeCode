

#11 2 4
#4 5 6
#10 8 -12


def diagonalDifference(a):
    # Complete this function
    # rows = len(a)
    # cols = len(a[0])
    n = 3
    Sum_primaryDiag = 0
    Sum_SecondDiag = 0
    # primary Diag
    for i in range(n):
        Sum_primaryDiag = Sum_primaryDiag + a[i][i]
    print (Sum_primaryDiag)
    # Secondary Diag
    for j in range(n):
            Sum_SecondDiag = Sum_SecondDiag + a[j][ n - 1 - j]
            #print (i,"  ", j)
    print (Sum_SecondDiag)

    return abs(Sum_primaryDiag - Sum_SecondDiag)


a = [[11,2,4],[4,5,6],[10,8,-12]]
result = diagonalDifference(a)
print(result)
