import turtle
import datetime
from RandFunct import random_number
from RandFunct2 import random_number2
import random
#from tkinter import *

#this code retrieves the date and time from the computer, to create the timestamp

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

wn = turtle.Screen()

collst = ["black", "white", "blue", "red", "yellow", "pink", "brown", "silver", "gray", "purple", "gold", "green", "light blue", "light yellow", "light pink", "tan", "light gray", "lavender", "light green"]

tommy = turtle.Turtle()
tommy.shape("circle")
tommy.speed(1000)

turtle.bgcolor('white')

tommy.color('black')
    
segnum = random_number2(8, 16)

y1range = []

y2range = []

for ctr in range(segnum):

    val = random_number2(-300,300)

    y1range.append(val)

    val2 = random_number2(-300,300)

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

fillr = random_number(len(collst))

tommy.fillcolor(collst[fillr])

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

#ts = turtle.getscreen()

#filnm = "Turtle_" + tim + ".eps"

#ts.getcanvas().postscript(file=filnm)

turtle.exitonclick()