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


def mx(a,b):
    if a > b:
        return a
    return b

