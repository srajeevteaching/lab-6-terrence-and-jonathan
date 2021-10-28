from graphics import *

# This function accepts 3 parameters:
# title, a string
# width, the width of the window being created
# height, the height of the window being created
# The function returns a window "object" (a variable) representing a window
# whose title is title, whose width is width, and whose height is height
# When called, the window is created and shows
def make_window( title, width, height ):
    win = GraphWin( title, width, height )
    return win

# This function creates a circle "object" and returns it
# A circle is defined by its center ( x, y ) and its radius, the 3 parameters of this function
# This function creates a circle but does not draw it
def make_circle( x, y, radius ):
    return Circle( Point( x, y ), radius )

# This function accepts 2 parameters:
# circle, a circle
# color, a color represented by a string such "red", "yellow", ...
# When called, it colors circle using color and draws it inside window
def color_circle(circle, color ):
    circle.setFill( color )
    circle.setOutline( color )

# This function accepts 3 parameters:
# window, a window
# circle, a circle
# color, a color represented by a string such "red", "yellow", ...
# When called, it colors circle using color and draws it inside window
def draw_and_color_circle( window, circle, color ):
    circle.setFill( color )
    circle.setOutline( color )
    circle.draw( window )

# This function accepts 3 parameters:
# circle, a circle "object"
# moveX, the number of pixels to move along the x axis
# moveY, the number of pixels to move along the y axis
# When called, it moves the position of circle by moveX and moveY pixels
def move( circle, moveX, moveY ):
    circle.move( moveX, moveY  )

# This function accepts 2 parameters:
# window, a window
# title, a string
# When called, it changes the title of window to title
def change_title( window,title ):
    window.master.title( title )

# This function accepts 1 parameter:
# ms, a number of milliseconds
# When called, it stops the program for ms milliseconds
def sleep( ms):
    time.sleep( ms / 1000 )
