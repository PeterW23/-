
from tkinter import *
from math import sin, cos, pi
import random
import numpy as np

root = Tk()

canvasWidth = 800
canvasHeight = 600
myCanvas = Canvas(root, width = canvasWidth, height = canvasHeight, bg = "black")

myCanvas.pack(pady = 20)


def createHeartShape():  # function to draw graph
    tValues = []  # list to contain numbers for t variable
    x = 0
    y = 0
    heartCoordinates1 = {}
    heartCoordinates2 = {}
    heartCoordinates3 = {}
    repetition = 0
    pointList = []
    for i in np.arange(0, 2*pi, 0.003):
        tValues.append(i)  # about 6000
    for t in tValues:
        x,y = heartShapeFunction(t)
        heartCoordinates1[x] = y

        if (45*pi/24 < t < 49*pi/24) and (0*pi/24 < t < 3*pi/24):
            heartCoordinates2[x] = y

# for x,y in heartCoordinates2.items():
#     myCanvas.create_rectangle(x, y, x + 5, y + 5, width=0, fill='#ff7171')
    for x,y in heartCoordinates1.items():

        myCanvas.create_rectangle(x, y, x+3, y+3, width = 0, fill = '#ff7171')

    while repetition <= 30:
        repetition += 1

        for n in range(1000):
            t = random.uniform(0, 2*pi)
            if not (45*pi/24 < t < 49*pi/24) and not (0*pi/24 < t < 3*pi/24):
                normalRandomNumber = abs(np.random.lognormal(mean=0, sigma=1.6, size=None))
                if normalRandomNumber < 100:
                    x, y = heartShapeFunction(t)
                    if x < canvasWidth/2:
                        x2 = x + normalRandomNumber
                    else:
                        x2 = x - normalRandomNumber
                    if y < canvasHeight/2:
                        y2 = y + normalRandomNumber
                    else:
                        y2 = y - normalRandomNumber
                    if not (abs(x - canvasWidth / 2) < 1):
                        heartCoordinates3[x2] = y2


    for x2,y2 in heartCoordinates3.items():
        myCanvas.create_rectangle(x2, y2, x2 + 1, y2 + 1, width=0, fill='#ff7171')


def heartShapeFunction(t):  # function to generate coordinates to draw out the heart
    x = 16 * (sin(t) ** 3) * 8 + canvasWidth/2
    y = -(13 * cos(t) - 5 * cos(2*t) - 2 * cos(3 * t) - cos(4*t)) * 8 + canvasHeight/2

    return x, y


def main():
    createHeartShape()

    root.mainloop()


main()