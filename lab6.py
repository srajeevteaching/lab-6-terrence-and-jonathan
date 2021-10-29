# Programmers: Jonathan
# Lab 6
# October 28th, 2021
# CS 151
# Professor Dr.Rajeev

# Importing necessary libraries
from graphics import *
import random


# Defining function to make the circle
def make_circle(x, y, r):
    circle = Circle(Point(x, y), r)
    circle.setFill("red")
    circle.setOutline("black")
    return circle


# Defining the function to get user input
def find_x_coordinate(min, max, message):
    # Getting user input and validating if input entered is integer
    message_input = input(message)
    while message_input.isdigit() != True and message_input.isdecimal() != True:
        message_input = input(message)
    message_input = int(message_input)

    # Checking to see if the user input is allowed depending on the max and min of the window
    if message_input <= max and message_input >= min:
        return message_input
    elif message_input > max or message_input < min:
        # Recursively calls itself if the input does not match the range of inputs
        find_x_coordinate(min, max, message_input)
    return message_input


# Defining the function used to get a random color value used to change color of ball
def random_color():
    # Storing random values between 0-255 into their proper variables
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    # Storing random rgb values into rgb array
    rgb = [red, green, blue]
    # Storing the rgb value as a string into a variable
    random_color_string = color_rgb(rgb[0], rgb[1], rgb[2])
    return random_color_string


def main():
    # User input to find the beginning x coordinate
    starting_x_coordinate = find_x_coordinate(50, 450, "What is your starting point? (50-450, 250 is for diamond shape): ")

    # Initializing starting values
    height = 500
    width = 500
    radius = 10
    x_movement = 1
    y_movement = 1

    # Making the window for the program using graphics library
    window = GraphWin("Lab 6", width, height)
    window.setBackground("gray")

    # Setting the values for the limits where the ball can reach
    left_border = window.getWidth() - radius
    right_border = radius
    bottom_border = radius
    top_border = window.getHeight() - radius

    # Creating and showing the window with the circle in it
    circle = make_circle(starting_x_coordinate, radius, radius)
    circle.draw(window)

    # Will begin moving the circle once the program begins to run
    while window.checkMouse() == None:
        while True:
            # Begins moving the circle to the right and down by the starting values (1)
            circle.move(x_movement,y_movement)

            # When the ball is touching the top or bottom border it will change to the inverse of the y movement value
            if circle.getCenter().getY() <= bottom_border or circle.getCenter().getY() >= top_border:
                y_movement = -y_movement
                # Changes the color of the ball when it touches one of the borders
                circle.setFill(random_color())

            # When the ball is touching the left or right border it will change to the inverse of the x movement value
            elif circle.getCenter().getX() <= right_border or circle.getCenter().getX() >= left_border:
                x_movement = -x_movement
                # Changes the color of the ball when it touches one of the borders
                circle.setFill(random_color())

    window.getMouse()
    window.close()


main()


