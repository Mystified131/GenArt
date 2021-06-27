import turtle
import datetime
import random
import string
from unidecode import unidecode
from RandFunct import random_number
from RandFunct2 import random_number2
import os
#from tkinter import *

#this code retrieves the date and time from the computer, to create the timestamp

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

fillst = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\GenArt'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".txt"):
            fillst.append(str(filepath))

totlst = []

for elem in fillst:

    infile = open(elem, "r")

    plist = infile.readline()

    while plist:
        subl = plist.split()
        for elem in subl:
            if len(elem) > 3:
                elem = elem.strip('"')
                elem = elem.strip(',')
                elem = elem.strip('.')
                elem = elem.strip(':')
                elem = elem.strip(';')
                elem = elem.strip('!')
                elem = elem.strip('?')
                elem = elem.lower()
                elem = unidecode(elem)
  
                totlst.append(elem)
        plist = infile.readline()

    infile.close()

totlen = len(totlst)

wn = turtle.Screen()

collst = ["black", "silver"]

#bcollst = ["light blue", "tan", "white"]

bcollst = ["white", "white", "white"]

stllst = ["normal", "bold", "italic", "underline"]

tommy = turtle.Turtle()
tommy.speed(1000)

bkgr = random_number(len(bcollst))

back = bcollst[bkgr]

turtle.bgcolor(back)

#turtle.bgcolor("white")

#collst.remove(bcollst[bkgr])

shnum = random_number2(90, 115)

for ctr in range(shnum):

    fgr = random_number(len(collst))

    fore = collst[fgr]

    tommy.color(fore)

    N = random.randrange(12)

    stnum = random_number(totlen)

    stx = totlst[stnum]

    #stx = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

    xco = random_number2(-340, 240)

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