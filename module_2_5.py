def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        submatrix = []
        for k in range(m):
            submatrix.append([value])
        matrix.append(submatrix)
    print(matrix)
n =  int(input('Введите n: '))
m =  int(input('Введите m: '))
value = int(input('Введите value: '))
get_matrix(n,m,value)
