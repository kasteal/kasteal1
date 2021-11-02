import math
import matplotlib.pyplot as mpp

MODEL_DT = 0.001
MODEL_G = 9.81


class Body:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.sx = []
        self.sy = []

    def advance(self):
        self.sx.append(self.x)
        self.sy.append(self.y)

        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT
        self.vy -= MODEL_G * MODEL_DT




class Rocket(Body):
    def __init__(self, x, y, m, u, vx):
        super().__init__(x, y, vx, 20)
        self.m0 = m
        self.m = m
        self.u = u
    def advance(self):
        super().advance()
        self.vy += self.u * MODEL_DT
        self.m -= self.m0 * MODEL_DT
        if self.m <= 0:
            self.padaem()


    def padaem(self):
        while self.y > 0:
            if self.y < 0:
                self.y = 0
            super().advance()


a = Rocket(200, 0, 15, 40, 50)
b = Body(200, 100, 1, 2)

while a.m > 0:
    a.advance()
while b.y > 0:
    b.advance()

mpp.plot(a.sx, a.sy)
mpp.show()
mpp.plot(b.sx, b.sy)
mpp.show()
