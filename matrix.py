# matrix multiplication

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
c = []
sum = 0
for i in range(len(a)):
    c.append([])
    sum = 0
    for k in range(len(b)):
        sum = 0
        for j in range(len(b)):
            sum = sum+(a[i][j]*b[j][k])
        c[i].append(sum)

print(c)

# doint the same using functions

'''initialize c to 0
consider two matrices A and b
find dot product of two lists
pick ith row and jth col in a matrix
'''


def initialize_mat(dim):
    c = []
    for i in range(dim):
        c.append([])
    for j in range(dim):
        for k in range(dim):
            c[j].append(0)
    return c


def dot_product(u, v):
    sum = 0
    for i in range(len(u)):
        sum = sum+(u[i]*v[i])
    return sum


def row(M, i):
    dim = len(M)
    row_val = []
    for k in range(dim):
        row_val.append(M[i][k])
    return row_val


def col(M, i):
    dim = len(M)
    column = []
    for k in range(dim):
        column.append(M[k][i])
    return column


result = initialize_mat(3)
for i in range(len(result)):
    for j in range(len(result)):
        result[i][j] = dot_product(row(a, i), col(b, j))

print(result)
