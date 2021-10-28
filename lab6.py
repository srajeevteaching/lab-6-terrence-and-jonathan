# Programmers: Jonathan
# Lab 6
# October 28th, 2021
# CS 151
# Professor Dr.Rajeev
from graphics import *

def make_circle(x,y,r):
    circle = Circle(Point(x,y), r)
    circle.setFill("red")
    circle.setOutline("black")
    return circle

def find_x_coordinate(min,max,message):
    message_input = int(input(message))
    minimum = min
    maximum = max
    if message_input <= maximum and message_input >= minimum:
        return message_input
    elif message_input > maximum or message_input < minimum:
        return 50

def main():
    #starting_x_coordinate = find_x_coordinate(50,450,"What is your starting point? (50-450)")
    window = GraphWin("Lab 6", 500,500)
    circle = make_circle(50,20,10)
    circle.draw(window)
    for i in range(500):
        circle.move(.5,0)
    window.getMouse()
    window.close()


main()





