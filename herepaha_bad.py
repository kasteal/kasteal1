import turtle as tl


def dra_squar(scale):
    if scale > 0:
        tl.up()
        tl.forward(5)
        tl.left(90)
        tl.forward(5)
        tl.down()
        tl.right(90)
        for i in range(4):
            tl.forward(scale)
            tl.left(90)
        dra_squar(scale-10)



scal = 400

dra_squar(scal)
tl.done()
