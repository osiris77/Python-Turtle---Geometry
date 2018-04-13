import turtle
import math
from time import strftime
from random import *

### Setting up Osiris' Window

wn = turtle.Screen()
osiris = turtle.Turtle()
wn.screensize(10000, 10000)
djet = strftime("%Y-%m-%d %H-%M-%S")

### SCREENSHOT COMMAND ON 'A' KEYBOARD PRESS ###

def ihy():
    ts = osiris.getscreen()
    osiris.hideturtle()
    ts.getcanvas().postscript(file="horus - " + djet +
                              ".eps", width=5000, height=5000)
    osiris.showturtle()
    print ('screenshot taken')
turtle.onkey(ihy,"a")
turtle.listen()

### CENTRE DOT COMMAND ON 'D' KEYBOARD PRESS ###

def yam():
    osiris.penup()
    osiris.goto(0,0)
    osiris.dot(3,'#0000FF')
    
turtle.onkey(yam,"d")
turtle.listen()

'''
#############################################################
################## GEOMETRIC DEFINITIONS ####################
##################        START          ####################
#############################################################
'''

########################################
### Aker = Outward facing lines      ###        
### God of the horizon               ###        
########################################        
### Developed Using These Integars              
### (aker_y=1,aker_span=10,aker_start=-50,
### aker_start_increase = 15,aker_no=5,aker_length=300,
### aker_length_increase=-30,aker_angle=12,aker_angle_increase=5,
### aker_gap=10,aker_gap_increase=2,aker_pensize=3,aker_color='#F09900')

def aker(aker_y=1,aker_span=10,aker_start=-50,
         aker_start_increase = 15,aker_no=5,aker_length=300,
         aker_length_increase=-30,aker_angle=12,aker_angle_increase=5,
         aker_gap=10,aker_gap_increase=2,aker_pensize=3,aker_color='#F09900'):
    if aker_y == 1:
        osiris.penup()
        osiris.pencolor(aker_color)
        osiris.pensize(aker_pensize)
        osiris.setheading(osirisHeadingStart)
        osiris.forward(aker_start)
        osirisCurrentX = osiris.xcor()
        osirisCurrentY = osiris.ycor()
        for aker_d in range(1,3):
            osiris.setheading(osirisHeadingStart)
            if aker_d == 1:
                osiris.right(90)
            else:
                osiris.left(90)
            osiris.forward(aker_span)
            osiris.dot(2)
            osirisTemporaryX = osiris.xcor()
            osirisTemporaryY = osiris.ycor()
            for aker_e in range(1,(aker_no+1)):
                osiris.setheading(osirisHeadingStart)
                if aker_d == 1:
                    osiris.right(aker_angle+(aker_e*aker_angle_increase))
                else:
                    osiris.left(aker_angle+(aker_e*aker_angle_increase))
                osiris.pendown()
                osiris.forward(aker_length+(aker_e*aker_length_increase))
                osiris.penup()
                osiris.goto(osirisTemporaryX,osirisTemporaryY)                    
                osiris.setheading(osirisHeadingStart)
                osiris.forward(aker_e*aker_start_increase)
                if aker_d == 1:
                    osiris.right(90)
                else:
                    osiris.left(90)
                osiris.forward(aker_gap*(aker_e*aker_gap_increase))
            osiris.goto(osirisCurrentX,osirisCurrentY)
        osiris.setheading(osirisHeadingStart)

'''
##############################################
##############################################
##################START#######################
##############################################
##############################################
'''
    
	#####################
	#CONFIGURING OSIRIS##
	#####################

osiris.speed(2)
def osirisslow():
    osiris.speed(1)
def osirismid():
    osiris.speed(4)
def osirisquick():
    osiris.speed(0)
turtle.onkey(osirisquick,"0")
turtle.onkey(osirismid,"4")
turtle.onkey(osirisslow,"1")
turtle.listen()
osiris.penup()
osiris.setheading(90)
osirisHeadingStart = osiris.heading()
osiris.goto(0,0)

#################
#GEOMETRIC TILES#
#################

################
#ROTATE SECTION#
################

### SHU         ### CONTROLS THE AMOUNT OF ROTATIONS

shu = 6

osiris.setheading(90)
for shu_a in range(shu):
    osiris.penup()             
    osiris.goto(0,0)
    osiris.forward(0)   
    osirisHeadingStart = osiris.heading()  
    osirisStartingX = osiris.xcor()
    osirisStartingY = osiris.ycor()

### AKER        ### OUTWARD FACING LINES
    aker(aker_y=1,aker_span=-10,aker_start=150,
         aker_start_increase = 8,aker_no=6,aker_length=550,
         aker_length_increase=-30,aker_angle=12,aker_angle_increase=5,
         aker_gap=5,aker_gap_increase=3,aker_pensize=2,aker_color='#0FC200')
    
###################
#COMMAND TO ROTATE#
###################

    osiris.setheading(osirisHeadingStart)
    osirisHeadingStart = osirisHeadingStart + (360/shu)
    osiris.setheading(osirisHeadingStart)


'''
##################################
##################################
################END###############
##################################
##################################
'''
	
turtle.done()
