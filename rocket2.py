import math
import matplotlib.pyplot as mpp

MODEL_DT = 0.001
MODEL_G = 9.81

class Rocket:
    def __init__(self, x, y, m, u, vx):
        self.x = x
        self.y = y
        self.sx = []
        self.sy = []
        self.m0 = m
        self.m = m
        self.vx = vx
        self.vy = 4
        self.u = u

    def up(self):

        self.sx.append(self.x)
        self.sy.append(self.y)
        self.x += self.vx * MODEL_DT
        self.vy += self.u * math.log(self.m0/self.m)
        self.y += self.vy
        self.m -= self.m0 * (1 / 2000)
        if self.m <= 0:
            self.padaem()


    def padaem(self):
        while self.y > 0:
            self.x += self.vx * MODEL_DT
            self.vy -= MODEL_G * MODEL_DT
            self.y += self.vy
            if self.y < 0:
                self.y = 0
            self.sy.append(self.y)
            self.sx.append(self.x)


a = Rocket(100, 10, 15, 0.001, 50)
while a.m > 0:
    a.up()

mpp.plot(a.sx, a.sy)
mpp.show()
