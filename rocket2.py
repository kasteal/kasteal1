import math
import matplotlib.pyplot as mpp

MODEL_DT = 0.001
MODEL_G = 9.81


class Body:
    def __init__(self, x, y, vx, vy, t):
        self.x = x
        self.y = y
        self.t = t
        self.vx = vx
        self.vy = vy
        self.sx = []
        self.sy = []

    def advance(self):
        self.t += MODEL_DT
        if self.y > 0:
            self.sx.append(self.x)
            self.sy.append(self.y)
            self.x += self.vx * MODEL_DT
            self.y += self.vy * MODEL_DT
            self.vy -= MODEL_G * MODEL_DT



class Rocket(Body):
    def __init__(self, x, y, vx, vy, u, m, dm, t):
        super().__init__(x, y, vx, vy, t)
        self.m0 = m
        self.m = m
        self.u = u
        self.dm = dm

    def advance(self):
        super().advance()
        if self.m > 0 and 2 > self.t > 1:
            self.vy -= self.u * MODEL_DT
            self.m -= self.dm * MODEL_DT
        elif self.m > 0:
            self.vy += self.u * MODEL_DT
            self.m -= self.dm * MODEL_DT

a = Rocket(200, 11, 10, 20, 40, 20, 5, 0)
b = Body(200, 1, 10, 90, 0)

while a.t < 20:
    a.advance()
    b.advance()
    print(a.t)

mpp.plot(a.sx, a.sy)
mpp.plot(b.sx, b.sy)
mpp.show()
