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

#######################################
### Anhur = Forward Facing Chevrons ###
### Sky god and god of war          ###
#######################################

def anhur(anhur_y=1,anhur_start=50,anhur_no=6,
          anhur_size=100,anhur_spacing=15,
          anhur_pensize=1,anhur_color='#FF4444'):
    if anhur_y == 1:
        osiris.pensize(anhur_pensize)
        osiris.color(anhur_color)
        osirisTemporaryX = osiris.xcor() 
        osirisTemporaryY = osiris.ycor()
        for anhur_c in range(anhur_no):
            osiris.penup()
            osiris.goto(osirisTemporaryX, osirisTemporaryY)   
            osiris.setheading(osirisHeadingStart)
            osiris.forward((anhur_start) + (anhur_spacing * anhur_c))
            # This is marked here as it will mark the top chevron
            osirisCurrentX = osiris.xcor() 
            osirisCurrentY = osiris.ycor() 
            osiris.right(135)
            osiris.pendown()
            osiris.pensize(2)
            anhur_calsize = ((anhur_size) -
                             ((anhur_size/anhur_no) * anhur_c))
            osiris.forward(anhur_calsize)
            osiris.backward(anhur_calsize)
            osiris.right(90)
            osiris.forward(anhur_calsize)
        osiris.penup()
        osiris.goto(osirisCurrentX, osirisCurrentY)    
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

################
#ROTATE SECTION#
################

### SHU         ### CONTROLS THE AMOUNT OF ROTATIONS

shu = 6

# if you want these on different diagonals - remember to divide it by SHU.
# EG.   First round = 90 when shu = 6
#       Second round = 60 when shu = 6
osiris.setheading(90)
for shu_a in range(shu):
    osiris.penup()             
    osiris.goto(0,0)
    osiris.forward(150)   
    osirisHeadingStart = osiris.heading()  
    osirisStartingX = osiris.xcor()
    osirisStartingY = osiris.ycor()

### ANHUR       ### FORWARD FACING CHEVONS
    anhur(anhur_y=1,anhur_start=50,anhur_no=6,
          anhur_size=100,anhur_spacing=15,
          anhur_pensize=1,anhur_color='#FF4444')
    
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
