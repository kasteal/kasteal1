def gcdupd(a, b):
    if b == 0:
        return 1, 0, a
    x, y, d = gcdupd(b, a % b)
    return [y, x-y*(a//b), d]


a,b = map(int, input('Введите числа a,b: ').split())
x, y, d = gcdupd(a,b)
print('%d * %d + %d * %d = %d' % (x,a,y,b,d))