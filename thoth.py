import turtle
import math
from time import strftime
from random import *

### Setting up Osiris' Window

wn = turtle.Screen()
osiris = turtle.Turtle()
wn.screensize(1000, 1000)


### SCREENSHOT COMMAND ON 'A' KEYBOARD PRESS ###

def ihy():
    ts = osiris.getscreen()
    osiris.hideturtle()
    ts.getcanvas().postscript(file="thoth/thoth - " + djet +
                              ".eps", width=1000, height=1000)
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

### MATH DEFINITIONS ###

def pythag(sidea, sideb):
    csquare = (sidea ** 2) + (sideb ** 2)
    sidec = math.sqrt(csquare)
    return sidec

def work_acos(A,B,C):
    X = math.degrees(math.acos(((C ** 2) + (A ** 2) - (B ** 2))/(2.0 * C * A))) # bottom angle
    return X


'''
#############################################################
################## GEOMETRIC DEFINITIONS ####################
##################        START          ####################
#############################################################
'''

#######################################################
### Thoth = Randomly generated tile                 ###
### God of Knowledge, the Moon, Measurement, Wisdom ###
#######################################################
########### Developed using
##thoth_y=1,thoth_height=500,thoth_ray_no_min = 1,
##thoth_ray_no_max = 4,thoth_ray_reverse_no_min = 1,
##thoth_ray_reverse_no_max = 4,thoth_stripe_no_min = 1,
##thoth_stripe_no_max = 4,thoth_stripe_reverse_no_min = 1,
##thoth_stripe_reverse_no_max = 4,thoth_halo_no_min = 1,
##thoth_halo_no_max = 4,thoth_circle_no_min = 1,
##thoth_circle_no_max = 4, 
##thoth_ray_pensize = 2,thoth_ray_color = '#990000',
##thoth_ray_reverse_pensize = 2,thoth_ray_reverse_color = '#990000',
##thoth_stripe_pensize = 2,thoth_stripe_color = '#990000',
##thoth_stripe_reverse_pensize = 2,thoth_stripe_reverse_color = '#990000',
##thoth_halo_pensize = 2,thoth_halo_color = '#990000',
##thoth_circle_pensize = 2,thoth_circle_color = '#990000' 

def thoth(
    thoth_y=1,thoth_height=600,
    thoth_ray_no_min = 1,thoth_ray_no_max = 5,
    thoth_ray_reverse_no_min = 1,thoth_ray_reverse_no_max = 5,
    thoth_stripe_no_min = 1,thoth_stripe_no_max = 5,
    thoth_stripe_reverse_no_min = 1,thoth_stripe_reverse_no_max = 5,
    thoth_halo_no_min = 1,thoth_halo_no_max = 5,
    thoth_circle_no_min = 1,thoth_circle_no_max = 5, 
    thoth_ray_pensize = 2,thoth_ray_color = '#990000',
    thoth_ray_reverse_pensize = 2,thoth_ray_reverse_color = '#990000',
    thoth_stripe_pensize = 2,thoth_stripe_color = '#990000',
    thoth_stripe_reverse_pensize = 2,thoth_stripe_reverse_color = '#990000',
    thoth_halo_pensize = 2,thoth_halo_color = '#990000',
    thoth_circle_pensize = 2,thoth_circle_color = '#990000' 
    ):
    if thoth_y == 1:
        thoth_ray_y = (randint(0,1))    
        thoth_ray_reverse_y = (randint(0,1))    
        thoth_stripe_y = (randint(0,1))    
        thoth_stripe_reverse_y = (randint(0,1))
        thoth_halo_y = (randint(0,1))    
        thoth_circle_y = (randint(0,1))
        thoth_ray_no = (randint(thoth_ray_no_min,thoth_ray_no_max))
        thoth_ray_reverse_no = (randint(thoth_ray_reverse_no_min,thoth_ray_reverse_no_max))
        thoth_stripe_no = (randint(thoth_stripe_no_min,thoth_stripe_no_max))
        thoth_stripe_reverse_no = (randint(thoth_stripe_reverse_no_min,thoth_stripe_reverse_no_max))
        thoth_halo_no = (randint(thoth_halo_no_min,thoth_halo_no_max))
        thoth_circle_no = (randint(thoth_circle_no_min,thoth_circle_no_max))
        thoth_cell_height = thoth_height / 2
        thoth_ray_height = thoth_cell_height / thoth_ray_no
        thoth_ray_reverse_height = thoth_cell_height / thoth_ray_reverse_no     
        thoth_stripe_height = thoth_cell_height / thoth_stripe_no
        thoth_stripe_reverse_height = thoth_cell_height / thoth_stripe_reverse_no        
        thoth_halo_size = thoth_cell_height / thoth_halo_no
        thoth_circle_size = thoth_cell_height / thoth_circle_no
        # Outer Stroke
        osiris.goto(-thoth_cell_height,thoth_cell_height)
        osiris.setheading(270)
        osiris.pensize(thoth_circle_pensize)
        osiris.color(thoth_circle_color)
        for thoth_box_range in range(1,5):
            osiris.pendown()
            osiris.forward(thoth_height)
            osiris.left(90)
            osiris.penup()
        ### Inner Circles            
        if thoth_circle_y == 1:
            osiris.pensize(thoth_circle_pensize)
            osiris.color(thoth_circle_color)
            for thoth_circle_a in range(1,(thoth_circle_no+1)):
                osiris.goto(0,0)
                osiris.setheading(90)
                osiris.forward(thoth_circle_size*thoth_circle_a)
                osiris.left(90)
                thoth_circle_on_off = (randint(0,1))
                if thoth_circle_on_off == 1:
                    osiris.pendown()
                    osiris.circle((thoth_circle_size*thoth_circle_a),360)
                    osiris.penup()
        ### Outer Circles
        if thoth_halo_y == 1:
            osiris.pensize(thoth_halo_pensize)
            osiris.color(thoth_halo_color)            
            for thoth_halo_range in range(1,(thoth_halo_no+1)):
                thoth_halo_on_off = (randint(0,1))
                thoth_halo_start_heading = 0
                for thoth_halo_a in [(-thoth_cell_height,thoth_cell_height),
                                     (-thoth_cell_height,-thoth_cell_height),
                                     (thoth_cell_height,-thoth_cell_height),
                                     (thoth_cell_height,thoth_cell_height)
                                     ]:
                    osiris.goto(thoth_halo_a)
                    osiris.setheading(thoth_halo_start_heading)
                    osiris.forward(thoth_halo_size*thoth_halo_range)
                    osiris.right(90)
                    if thoth_halo_on_off == 1:
                        osiris.pendown()
                        osiris.circle(-(thoth_halo_size*thoth_halo_range),90)
                        osiris.penup()
                    thoth_halo_start_heading = thoth_halo_start_heading + 90
        ### RAYS FROM THE CENTRE ###
        if thoth_ray_y == 1:
            osiris.pensize(thoth_ray_pensize)
            osiris.color(thoth_ray_color)            
            osiris.goto(0,0)
            osiris.setheading(90)
            for thoth_ray_range in range(0,(thoth_ray_no+1)):
                thoth_ray_on_off = (randint(0,1))        
                for thoth_ray_a in range(1,5):
                    thoth_C = pythag(thoth_cell_height,(thoth_ray_height
                                                        *thoth_ray_range))
                    thoth_M = (work_acos(thoth_cell_height,
                                         (thoth_ray_height*
                                          thoth_ray_range),thoth_C))
                    osiris.left(thoth_M)
                    if thoth_ray_on_off == 1:
                        osiris.pendown()
                        osiris.forward(thoth_C)
                        osiris.penup()
                    osiris.goto(0,0)
                    osiris.left(90-(thoth_M*2)) # We're getting him to turn from the current line to the next liine
                    if thoth_ray_on_off == 1:
                        if 1 <= thoth_ray_range <= (thoth_ray_no-1):
                            osiris.pendown()
                            osiris.forward(thoth_C)
                            osiris.penup()
                            osiris.goto(0,0)
                    osiris.left(thoth_M)
        ### RAYS FROM THE CORNER ###
        if thoth_ray_reverse_y == 1:
            osiris.pensize(thoth_ray_reverse_pensize)
            osiris.color(thoth_ray_reverse_color)
            for thoth_reverse_ray_range in range(0,(thoth_ray_reverse_no+1)):
                thoth_heading = 0
                thoth_reverse_ray_on_off = (randint(0,1))   
                for thoth_x in [(-thoth_cell_height,thoth_cell_height),
                                (-thoth_cell_height,-thoth_cell_height),
                                (thoth_cell_height,-thoth_cell_height),
                                (thoth_cell_height,thoth_cell_height)
                                ]:
                    osiris.goto(thoth_x)
                    osiris.setheading(thoth_heading)           
                    thoth_Q = pythag(thoth_cell_height,(thoth_ray_reverse_height*
                                                        thoth_reverse_ray_range))
                    thoth_P = work_acos(thoth_cell_height,
                                        (thoth_ray_reverse_height*
                                         thoth_reverse_ray_range),thoth_Q)
                    osiris.right(thoth_P)
                    if thoth_reverse_ray_on_off == 1:
                        osiris.pendown()
                        osiris.forward(thoth_Q)
                        osiris.penup()
                    osiris.goto(thoth_x)
                    osiris.right(90-(thoth_P*2))
                    if thoth_reverse_ray_on_off == 1:
                        if thoth_reverse_ray_range <= (thoth_ray_reverse_no-1):
                            osiris.pendown()
                            osiris.forward(thoth_Q)
                            osiris.penup()
                    thoth_heading = thoth_heading + 90
        ### STRIPE FROM THE CENTRE ###
        if thoth_stripe_y == 1:
            osiris.pensize(thoth_stripe_pensize)
            osiris.color(thoth_stripe_color)
            osiris.goto(0,0)
            osiris.setheading(90)
            for thoth_stripe_range in range(1,(thoth_stripe_no+1)):
                thoth_stripe_on_off_1 = (randint(0,1))
                for thoth_zz in range(1,5):
                    thoth_D_working = thoth_stripe_height * thoth_stripe_range
                    thoth_F = pythag(thoth_D_working,thoth_D_working)
                    osiris.forward(thoth_cell_height-thoth_D_working)
                    osiris.left(45)
                    if thoth_stripe_on_off_1 == 1:            
                        osiris.pendown()
                        osiris.forward(thoth_F)
                        osiris.penup()
                    osiris.goto(0,0)
                    osiris.left(45)
                    osiris.forward(thoth_cell_height-thoth_D_working)
                    osiris.right(45)
                    if thoth_stripe_on_off_1 == 1:
                        if thoth_stripe_range <= (thoth_stripe_no-1):
                            osiris.pendown()
                            osiris.forward(thoth_F)
                            osiris.penup()
                    osiris.goto(0,0)
                    osiris.left(45)
        ### STRIPE FROM THE CORNER ###                    
        if thoth_stripe_reverse_y == 1:
            osiris.pensize(thoth_stripe_reverse_pensize)
            osiris.color(thoth_stripe_reverse_color)
            osiris.goto(0,0)
            thoth_heading = 180
            for thoth_stripe_reverse_range in range(1,(thoth_stripe_reverse_no+1)):
                thoth_stripe_on_off_1 = (randint(0,1))
                thoth_stripe_on_off_2 = (randint(0,1))               
                for thoth_z in [(0,thoth_cell_height),
                                (-thoth_cell_height,0),
                                (0,-thoth_cell_height),
                                (thoth_cell_height,0)
                                ]:
                    thoth_E_working = (thoth_stripe_reverse_height
                                       * thoth_stripe_reverse_range)
                    thoth_R = pythag(thoth_E_working,thoth_E_working)
                    osiris.goto(thoth_z)
                    osiris.setheading(thoth_heading)  
                    osiris.forward(thoth_cell_height-thoth_E_working)
                    osiris.left(45)
                    if thoth_stripe_on_off_1 == 1:            
                        osiris.pendown()
                        osiris.forward(thoth_R)
                        osiris.penup()
                    if thoth_stripe_reverse_range <= (thoth_stripe_reverse_no-1):
                        osiris.goto(0,0)
                        osiris.setheading(thoth_heading)  
                        osiris.forward(thoth_E_working)
                        osiris.right(135)
                        if thoth_stripe_on_off_2 == 1:            
                            osiris.pendown()
                            osiris.forward(thoth_R)
                            osiris.penup()            
                    thoth_heading = thoth_heading + 90


        ### Outputs the input values for the tile ###
        osiris.goto(-thoth_cell_height,-thoth_cell_height)
        osiris.setheading(90)
        osiris.backward(20)
        osiris.write(djet,font=('Arial',8,'normal'))        
   
        for thoth_write in ['thoth_ray_y','thoth_ray_no',
                            'thoth_ray_reverse_y','thoth_ray_reverse_no',
                            'thoth_halo_y','thoth_halo_no'
                            ]:
            osiris.setheading(90)
            osiris.backward(20)
            osiris.write(thoth_write,font=('Arial',8,'normal'))
        osiris.goto(-thoth_cell_height+200,-thoth_cell_height)
        osiris.setheading(90)
        osiris.backward(20)        
        for thoth_write in [thoth_ray_y,thoth_ray_no,
                            thoth_ray_reverse_y,thoth_ray_reverse_no,
                            thoth_halo_y,thoth_halo_no
                            ]:           
            osiris.setheading(90)
            osiris.backward(20)
            osiris.write(thoth_write) 
        osiris.goto(-thoth_cell_height+300,-thoth_cell_height)
        osiris.setheading(90)
        osiris.backward(20)      
        for thoth_write in ['thoth_stripe_y','thoth_stripe_no',
                            'thoth_stripe_reverse_y','thoth_stripe_reverse_no',                            
                            'thoth_circle_y','thoth_circle_no'
                            
                            ]:
            osiris.setheading(90)
            osiris.backward(20)
            osiris.write(thoth_write,font=('Arial',8,'normal'))
        osiris.goto(-thoth_cell_height+500,-thoth_cell_height)
        osiris.setheading(90)
        osiris.backward(20)        
        for thoth_write in [thoth_stripe_y,thoth_stripe_no,
                            thoth_stripe_reverse_y,thoth_stripe_reverse_no,
                            thoth_circle_y,thoth_circle_no                            
                            ]:            
            osiris.setheading(90)
            osiris.backward(20)
            osiris.write(thoth_write,font=('Arial',8,'normal')) 





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

osiris.speed(0)
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

#####################
#BASE SHAPES SECTION#
#####################

for i in range(1200):
    djet = strftime("%Y-%m-%d %H-%M-%S")
    thoth()
    yam()
    ihy()
    osiris.clear()

'''
##################################
##################################
################END###############
##################################
##################################
'''
	
turtle.done()
