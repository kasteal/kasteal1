import numpy
from numpy import array
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box


def gauss(a, b):
    a = a.copy()
    b = b.copy()
    zxczhuk = len(b)

    def forward():
        for i in range(zxczhuk-1):
            if a[i][i] == 0:
                for j in range(i+1, zxczhuk):
                    if a[j][i] != 0:
                        a[i], a[j] = a[j], a[i]
            for j in range(i+1, zxczhuk):
                zxczilba = -(a[j][i]/a[i][i])
                for k in range(i, zxczhuk):
                    a[j][k] += a[i][k]*zxczilba
                b[j] += b[i] * zxczilba

    def backward():
        for i in range(zxczhuk-1, -1, -1):
            for j in range(i-1, -1, -1):
                zxczilba = -(a[j][i] / a[i][i])
                a[j][i] = 0
                b[j] += b[i]*zxczilba
            b[i] /= a[i][i]

    forward()
    backward()

    return b

a = [
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4],
    [2.0, 1.0, 4.0, 3]
]

b = [5, 6, 7, 8]


oob_solution = solve_out_of_the_box(a, b)
solution = gauss(a, b)

print(solution)
print("Макс отклонение компоненты решения:", norm(solution-oob_solution, ord=1))