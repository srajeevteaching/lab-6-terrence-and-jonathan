Lab 6


Problem:
Roll a ball and make it bounce around the sides of a window 4 times

Purpose:
This lab gives you practice with: * Designing, programming, and calling functions * Designing and programming while loops * Designing loop conditions * Re-using many of the other aspects of Python we've learned so far * Testing code

Details:
You need to design, write, and test a program that rolls a ball. The ball goes down and right, bounces against the right edge of the window, then goes down and left, bounces against the bottom edge, then goes up and left, bounces against the left edge, then goes up and right and stops when it hits the top edge.

Program Requirements:
When you plan your solution, you must take the following into account:

Your program should be designed using at least 1 function: it returns a value input by the user after checking that that value is between 2 values (a min and a max); you can assume that the user will enter integer values only: it accepts 3 parameters representing the min, max, and a message to pass to the user when asking the user to input a value
Your program should use that function to get user input for the starting x coordinate of the ball (the starting y coordinate is 20). Note that you can do that function at the very end (i..e you can start by hard coding a value for the starting x coordinate) Important note: Point ( 0, 0 ) is at the top left of the window.
Your program should make sure that the starting x coordinate is between 50 and 450 included (considering that the height and width of the window are set at 500 - see skeleton code provided); this will make sure that the ball hits the right edge first, then the bottom edge, then the left edge, and finally the top edge.
Steps:
Understand the problem
Write the first loop, moving the ball to the right and down; do not worry about the ball going through the wall of the window
Make your ball stop at the edge of the window
Write the 2nd, then 3rd, then 4th loop. Test your code after you have written each loop.
Rename Lab6Shell.py; name your file using your two last names as in Name1Name2Lab6.py. Place your code in that file. VERY IMPORTANT: Your code makes use of functions coded in the files graphics.py and graphicsCS151.py, i.e. these 2 files need to be in your project directory. The import statement is provided in the shell code. DO NOT modify graphics.py and graphicsCS151.py
Write your code following your algorithm and using good usability principles.
Properly comment your code with intro comments, function comments, and line comments
Since we have visual feedback and know what to expect, we are going to take a break from flowcharts and test cases for this lab.

Submit:
To GitHub and Moodle: Your Python file, be sure to include your two last names in the file name
