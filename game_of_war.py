import math #подключаем библиотеку
import numpy #подключаем numpy
import matplotlib.pyplot as mpp #подключаем матлотлиб как мпп

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__': # оно будет работать, если главная штука
    arguments = numpy.arange(0, 200, 0.1) #создать массив из 200/01 переменных от 0 - 200
    mpp.plot( arguments, [math.sin(a) * math.sin(a/20.0) for a in arguments]) #сроим график
    mpp.show() #показываем график