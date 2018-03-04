import turtle
import math
from time import strftime
from random import *

### Setting up Osiris' Window

wn = turtle.Screen()
osiris = turtle.Turtle()
wn.screensize(10000, 10000)

### SCREENSHOT COMMAND ON 'A' KEYBOARD PRESS ###

def ihy():
    ts = osiris.getscreen()
    osiris.hideturtle()
    ts.getcanvas().postscript(file="horus - " +
                              strftime("%Y-%m-%d %H-%M-%S") +
                              ".eps", width=5000, height=5000)
    osiris.showturtle()
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
    X = math.degrees(math.acos((C * C + A * A - B * B)/(2.0 * C * A))) # bottom angle
    return X

'''
#############################################################
################## GEOMETRIC DEFINITIONS ####################
##################        START          ####################
#############################################################
'''

########################################################################
### Imhotep = Islamic-based tile, with zig zags and downward columns ###
### Architect, engineer, scribe                                      ###
########################################################################
### Developed using
###imhotep_y = 1,imhotep_width = 400,imhotep_height = 400,
###imhotep_spike_no = 1,imhotep_row_no = 2,
###imhotep_row_margin_percent = 10,imhotep_middle_buffer_percent=10,
###imhotep_row_buffer = 10, imhotep_downward_length=75,
###imhotep_downward_no=1, imhotep_downward_cols=1,
###imhotep_row_pensize = 2, imhotep_row_color = '#FF3300',
###imhotep_downward_pensize = 2, imhotep_downward_color = '#0033FF',
###imhotep_bounding_pensize = 2, imhotep_bounding_color = '#00FF33',
###imhotep_write_output=1):

def imhotep(imhotep_y = 1,imhotep_width = 400,imhotep_height = 400,
            imhotep_spike_no = 1,imhotep_row_no = 2,
            imhotep_row_margin_percent = 10,imhotep_middle_buffer_percent=10,
            imhotep_row_buffer = 10, imhotep_downward_length=75,
            imhotep_downward_no=1, imhotep_downward_cols=1,
            imhotep_row_pensize = 2, imhotep_row_color = '#FF3300',
            imhotep_downward_pensize = 2, imhotep_downward_color = '#0033FF',
            imhotep_bounding_pensize = 2, imhotep_bounding_color = '#00FF33',
            imhotep_write_output=1):
    if imhotep_y == 1:
        if (imhotep_downward_no*imhotep_downward_length) <= (imhotep_height):
            ### We need to work out the angles and lengths involved
            ### Essentially, we're building out a series of triangles
            ### So we need pythag and acos

            ### ~~~~~~~ ROW LOGIC ~~~~~~~~ ###
            imhotep_row_x_start = (imhotep_width / 2 )
            ### Margin at the bottom and top of the tile as a percent
            imhotep_row_margin = ((imhotep_width / 2 ) *
                                  (imhotep_row_margin_percent/100))
            ### Buffer between the top rows and bottom rows
            imhotep_middle_buffer = ((imhotep_width / 2 ) *
                                     (imhotep_middle_buffer_percent/100))
            ### How much space in each half of the tile, need to remove
            ### the margin, padding, buffers etc
            imhotep_working_space = (((imhotep_height/2)-imhotep_row_margin-
                                      (imhotep_middle_buffer/2))-
                                     (imhotep_row_buffer*(imhotep_row_no-1)))
            ### We can then use this working space to figure out how tall each spike is
            imhotep_spike_height = ((imhotep_working_space) / imhotep_row_no)
            ### We the space between each row - this is a constant
            imhotep_row_space = (imhotep_working_space / imhotep_row_no)
            ### How wide is each spike (we determine the spike to be both the up
            ### And the down as a whole)
            imhotep_spike_width = (imhotep_width/(imhotep_spike_no*2))
            ### This is the length of the spike line itself
            ### We use pythag here because we already worked out the height of the spike
            ### And the width of the spike
            imhotep_spike_length = pythag(imhotep_spike_width,imhotep_spike_height)
            imhotep_row_y_start = (imhotep_height / 2)
            ### We need to know how to move osiris, so we need ACOS to find out the
            ### bottom angle of the spike
            imhotep_spike_bottom_angle = (work_acos(imhotep_spike_width,
                                                    imhotep_spike_height,
                                                    imhotep_spike_length))
            ### Once we have the bottom angle, we also know that the spike is
            ### Essentially two right angle triangles, so we can do the math
            ### Of 180 (as all triangles have 180 degrees), minus the bottom angle
            ### to give us the top angle
            imhotep_spike_top_angle = (180 - 90) - imhotep_spike_bottom_angle

            ### ~~~~~~~ DOWNWARD COLUMNS LOGIC ~~~~~~~~ ###

            ### So we need to work out how wide each of the 'slopes' is
            ### on the downward columns. We do this by taking the width of the tile
            ### then dividing it by the both the number of downward 'hockey sticks'
            ### PLUS the number of downward columns. This bit works like a matrix,
            ### so it's a bit hard to contextulise in text, but as we want everything
            ### to stay within the tile, we know that (e.g.) if there are two columns
            ### the first downward column has to finish 'one downward slope' from the
            ### right hand edge, similarly, the second downward column has to start
            ### 'one downward slope' from the left hand edge
            imhotep_slope_width = (imhotep_width / (imhotep_downward_no+
                                                    imhotep_downward_cols))
            ### To work out the height of each slope, we just use the height,
            ### Take away the downward length (our input in the function) TIMES
            ### The number of downward sections (hockey sticks). We then have to
            ### divide all of this by the number of downward sections (hockey sticks)
            ### BUT we have to account for the first downward slope, which isn't a hockey stick
            ### so we have to add the one needed for this downward slope
            imhotep_slope_height = ((imhotep_height - (imhotep_downward_length *
                                                      imhotep_downward_no))/
                                    (imhotep_downward_no+1))
            ### As with the spikes, because we figured out the width and height of the
            ### downward slope, we can then use ACOS to work out the actual drawn length
            imhotep_slope_length = pythag(imhotep_slope_width,imhotep_slope_height)
            imhotep_slope_bottom_angle = (work_acos(imhotep_slope_width,imhotep_slope_height,
                                                    imhotep_slope_length))
            imhotep_slope_top_angle = (180 - 90) - imhotep_slope_bottom_angle

                                          
            ### Draws the bounding box for the tile ###
            osiris.penup()
            osiris.goto(imhotep_row_x_start,-imhotep_row_y_start)
            osiris.pendown()
            osiris.setheading(90)
            osiris.pensize(imhotep_bounding_pensize)
            osiris.pencolor(imhotep_bounding_color)
            for i in range(2):
                osiris.forward  (imhotep_height)
                osiris.left     (90)
                osiris.forward  (imhotep_width)
                osiris.left     (90)
            ### Draws the zig-zag rows ###
            osiris.penup()
            osiris.goto(0,0)
            osiris.setheading(90)
            osiris.goto(-imhotep_row_x_start,(0+(imhotep_middle_buffer/2)))
            osirisReturnX = osiris.xcor()
            osirisReturnY = osiris.ycor()
            osiris.pencolor(imhotep_row_color)
            osiris.pensize(imhotep_row_pensize)
            ### imhotep_f - 1 = top, 2 = bottom ##            
            for imhotep_f in range(1,3):           
                for imhotep_g in range(1, (imhotep_row_no+1)):
                    for imhotep_h in range(1, (imhotep_spike_no+1)):
                        if imhotep_f == 1:
                            osiris.setheading(90)
                            osiris.right(90-imhotep_spike_bottom_angle)
                        else:
                            osiris.setheading(270)
                            osiris.left(90-imhotep_spike_bottom_angle)
                        osiris.pendown()
                        osiris.forward(imhotep_spike_length)
                        osiris.penup()
                        if imhotep_f == 1:
                            osiris.right(180-(imhotep_spike_top_angle*2))
                        else:
                            osiris.left(180-(imhotep_spike_top_angle*2))
                        osiris.pendown()
                        osiris.forward(imhotep_spike_length)
                        osiris.penup()
                    osiris.goto(osirisReturnX,osirisReturnY)
                    if imhotep_f == 1:
                        osiris.setheading(270)
                    else:
                        osiris.setheading(90)
                    osiris.backward(imhotep_row_space+imhotep_row_buffer)
                    osirisReturnX = osiris.xcor()
                    osirisReturnY = osiris.ycor()
                osiris.goto(-imhotep_row_x_start,(0-(imhotep_middle_buffer/2)))
                osirisReturnX = osiris.xcor()
                osirisReturnY = osiris.ycor()
            ### Draws the downward lines ###
            osiris.pensize(imhotep_downward_pensize)
            osiris.pencolor(imhotep_downward_color)                
            for imhotep_m in range(1,3):
                osiris.goto(0,0)
                osiris.setheading(90)
                if imhotep_m == 1:
                    osiris.goto(-imhotep_row_x_start,imhotep_row_y_start)
                else:
                    osiris.goto(imhotep_row_x_start,imhotep_row_y_start)
                osirisReturnX = osiris.xcor()
                osirisReturnY = osiris.ycor()
                for imhotep_n in range(1, (imhotep_downward_cols+1)):
                    osiris.setheading(90)
                    if imhotep_m == 1:
                        osiris.right(180-imhotep_slope_top_angle)
                    else:
                        osiris.left(180-imhotep_slope_top_angle)
                    osiris.pendown()
                    osiris.forward(imhotep_slope_length)
                    for imhotep_o in range (1, (imhotep_downward_no+1)):
                        osiris.setheading(270)
                        osiris.forward(imhotep_downward_length)
                        osiris.setheading(90)
                        if imhotep_m == 1:
                            osiris.right(180-imhotep_slope_top_angle)
                        else:
                            osiris.left(180-imhotep_slope_top_angle)
                        osiris.pendown()
                        osiris.forward(imhotep_slope_length)
                    osiris.penup()
                    osiris.goto(osirisReturnX,osirisReturnY)
                    if imhotep_m == 1:
                        osiris.setheading(0)
                    else:
                        osiris.setheading(180)
                    osiris.forward(imhotep_slope_width)
                    osirisReturnX = osiris.xcor()
                    osirisReturnY = osiris.ycor()
            ### Outputs the input values for the tile ###                    
            if imhotep_write_output == 1:
                osiris.goto(-imhotep_row_x_start,-imhotep_row_y_start)
                for imhotep_write in ['imhotep_width','imhotep_height','imhotep_spike_no',
                                      'imhotep_row_no','imhotep_row_margin_percent',
                                      'imhotep_row_buffer',
                                      'imhotep_middle_buffer_percent','imhotep_downward_length',
                                      'imhotep_downward_no','imhotep_downward_cols']:
                    osiris.setheading(90)
                    osiris.backward(20)
                    osiris.write(imhotep_write)
                osiris.goto(-(imhotep_row_x_start-200),-imhotep_row_y_start)
                for imhotep_write in [imhotep_width,imhotep_height,imhotep_spike_no,
                                      imhotep_row_no,imhotep_row_margin_percent,
                                      imhotep_row_buffer,
                                      imhotep_middle_buffer_percent,imhotep_downward_length,
                                      imhotep_downward_no,imhotep_downward_cols]:
                    osiris.setheading(90)
                    osiris.backward(20)
                    osiris.write(imhotep_write)              
        else:
            print('Downward value too high, will draw outside of tile')
                                   

#####################################
### Wadjwer = End bounding box    ###
### Sea and other lakes           ###
#####################################


def wadjwer(wadjwer_y):
    if wadjwer_y == 1:
        osiris.pencolor         ('#FF0000')
        osiris.penup            ()
        osiris.goto             (4000,-4000)
        osiris.pendown          ()
        osiris.setheading       (90)
        for i in range(4):
                osiris.forward  (8000)
                osiris.left     (90)


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
##def osirissuper():
##    osiris.speed(7)
def osirisquick():
    osiris.speed(0)
turtle.onkey(osirisquick,"0")
##turtle.onkey(osirissuper,"7")
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

### IMHOTEP      ### ISLAMIC-INSPIRED TILE 
imhotep(imhotep_y = 1,imhotep_width = 400,imhotep_height = 400,
        imhotep_spike_no = 3,imhotep_row_no = 3,
        imhotep_row_margin_percent = 10,imhotep_middle_buffer_percent=10,
        imhotep_row_buffer = 10, imhotep_downward_length=75,
        imhotep_downward_no=3, imhotep_downward_cols=3,
        imhotep_row_pensize = 2, imhotep_row_color = '#FF3300',
        imhotep_downward_pensize = 2, imhotep_downward_color = '#0033FF',
        imhotep_bounding_pensize = 2, imhotep_bounding_color = '#00FF33',
        imhotep_write_output=1)                                     

'''
##################################
##################################
################END###############
##################################
##################################
'''
	
### WADJWER     ### END BOUNDING BOX
### wadjwer_y
wadjwer(0)

turtle.done()
