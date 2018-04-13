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
### Amun = Central Spikes            ###        
### Creator God, Associated With Ra  ###        
########################################        

### Developed Using These Integars              
### (1,10,0,360,40,100,4,'#BFDDE1')               

def amun(amun_y=1,amun_no=10,amun_angle_a=0,amun_angle_b=360,
         amun_forward_a=40,amun_forward_b=100,
         amun_pensize=4,amun_color='#BFDDE1'):
    if amun_y == 1:
        for amun_a in range(amun_no):
            osiris.penup()
            osiris.pencolor(amun_color)
            osiris.pensize(amun_pensize)
            osiris.goto(0,0)				
            osiris.right(randint(amun_angle_a,amun_angle_b))
            osiris.pendown()
            osiris.forward(randint(amun_forward_a,amun_forward_b))
        osiris.penup()


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


### AMUN        ### RANDOM SPIKES ###
amun(amun_y=1,amun_no=18,amun_angle_a=0,amun_angle_b=360,
     amun_forward_a=40,amun_forward_b=600,
     amun_pensize=2,amun_color='#FF0000')


'''
##################################
##################################
################END###############
##################################
##################################
'''

turtle.done()
