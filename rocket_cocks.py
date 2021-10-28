import math
import matplotlib.pyplot as mpp

MODEL_G = 9.81
MODEL_DT = 0.001


class Raketa:
    def __init__(self, x, y, m, vy, vx):
        self.x = x
        self.y = y
        self.s_x = []
        self.s_y = []
        self.m0 = m
        self.m = m
        self.vx = vx
        self.vy = vy

    def polet(self):

        self.s_x.append(self.x)
        self.s_y.append(self.y)
        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT
        self.m -= self.m0*(1/2000)
        if self.m <= 0:
            self.toplivo_conec()

    def toplivo_conec(self):  # закончилось топливо
        while self.y > 0:
            self.x += self.vx * MODEL_DT
            self.vy -= MODEL_G * MODEL_DT
            self.y += self.vy * MODEL_DT
            self.s_y.append(self.y)
            self.s_x.append(self.x)



a = Raketa(500, 300, 10, 100, 100)
while a.m > 0:
    a.polet()
    print(a.y)


mpp.plot(a.s_x, a.s_y)
mpp.show()
