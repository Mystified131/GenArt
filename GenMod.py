import turtle
import datetime
from RandFunct import random_number
from RandFunct2 import random_number2
import random
#from tkinter import *

wn = turtle.Screen()

cirlst = ["yellow", "gold", "palegoldenrod", "deeppink"]

collst = [  "green", "tan", "lightgreen", "peru", "sienna", "lightseagreen", "lime", "mediumaquamarine", "dodgerblue", "turquoise", "darkorchid", "mediumorchid"]

tommy = turtle.Turtle()

tommy.hideturtle()

tommy.shape("circle")
tommy.shapesize(.1)

tommy.speed(1000)

#turtle.bgcolor('white')

#tommy.color('black')

for tur in range(10):

    right_now = datetime.datetime.now().isoformat()
    list = []

    for i in right_now:
        if i.isnumeric():
            list.append(i)

    tim = ("".join(list))

    turtle.clearscreen()

    turtle.bgcolor('white')

    tommy.color('black')
        
    segnum = random_number2(8, 16)

    y1range = []

    y2range = []

    for ctr in range(segnum):

        val = random_number2(-300,60)

        y1range.append(val)

        val2 = random_number2(-300,60)

        y2range.append(val2) 

    y1range.sort()

    y2range.sort()

    print(y1range)

    print(y2range)

    for subfl in range(segnum-1):

        fillr = random_number(len(collst))

        tommy.fillcolor(collst[fillr])

        tommy.penup()
        tommy.goto(-400, y1range[subfl])
        tommy.begin_fill()

        tommy.pendown()
        tommy.goto(400, y2range[subfl])

        tommy.goto(400, y2range[subfl+1])

        tommy.goto(-400, y1range[subfl+1])

        tommy.goto(-400, y1range[subfl])

        tommy.end_fill()

        tommy.penup()

    #############Top Fill

    fillr = random_number(len(collst))

    tommy.fillcolor(collst[fillr])

    tommy.penup()
    tommy.goto(-400, -400)
    tommy.begin_fill()

    tommy.pendown()
    tommy.goto(400, -400)

    tommy.goto(400, y2range[0])

    tommy.goto(-400, y1range[0])

    tommy.goto(-400, -400)

    tommy.end_fill()

    tommy.penup()

    #############Bass Fill

    #fillr = random_number(len(collst))

    tommy.fillcolor("lightskyblue")

    tommy.penup()
    tommy.goto(-400, 400)
    tommy.begin_fill()

    tommy.pendown()
    tommy.goto(400, 400)

    tommy.goto(400, y2range[segnum-1])

    tommy.goto(-400, y1range[segnum-1])

    tommy.goto(-400, -400)

    tommy.end_fill()

    tommy.penup()

    ###################Circle

    tommy.penup()

    tommy.hideturtle()

    fgr = random_number(len(cirlst))

    fore = cirlst[fgr]

    tommy.color(fore)

    xco = random_number2(-200, 200)

    yco = random_number2( 80, 120)

    csiz = random_number2(80, 100)

    tommy.goto(xco, yco)

    tommy.begin_fill()

    tommy.circle(csiz)

    tommy.end_fill()

    tommy.goto(-400,-400)

    ts = turtle.getscreen()

    turtle.clearstamp(-1)

    #turtle.Screen.clear()

    filnm = "Turtle_" + tim + ".eps"

    ts.getcanvas().postscript(file=filnm)

turtle.exitonclick()