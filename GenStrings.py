import turtle
import datetime
import random
import string
from RandFunct import random_number
from RandFunct2 import random_number2
#from tkinter import *

#this code retrieves the date and time from the computer, to create the timestamp

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

wn = turtle.Screen()

collst = ["black", "silver"]

bcollst = ["light blue", "tan", "white"]

stllst = ["normal", "bold", "italic", "underline"]

tommy = turtle.Turtle()
tommy.speed(1000)

bkgr = random_number(len(bcollst))

back = bcollst[bkgr]

turtle.bgcolor(back)

#collst.remove(bcollst[bkgr])

shnum = random_number2(200, 325)

for ctr in range(shnum):

    fgr = random_number(len(collst))

    fore = collst[fgr]

    tommy.color(fore)

    N = random.randrange(12)

    stx = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

    xco = random_number2(-320, 280)

    yco = random_number2(-300, 300)

    sz = random_number2(12,56)

    stlen = len(stllst)

    styl = random_number(stlen)

    styll = stllst[styl]

    tommy.penup()

    tommy.goto(xco, yco)

    tommy.write(stx, font=("Courier", sz, styll))

#ts = turtle.getscreen()

#filnm = "Turtle_" + tim + ".eps"

#ts.getcanvas().postscript(file=filnm)

turtle.exitonclick()