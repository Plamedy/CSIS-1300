"""
American Flag The width (w) of the official American flag is 1.9 times the height (h). The blue rectangular 
canton (referred to as the “union”) has width 25 w and height 713 h. Write a program that draws an American flag.

This code uses the Python Turtle module to draw the American flag.The draw_rectangle() function takes two 
parameters, length and height, which represent the length and height of the flag respectively. The function 
first sets the turtle to an "up" position, then calculates the values of C, D, and L, which are used later for 
drawing the stripes and stars. It sets the turtle's color to red and fills the rectangle by drawing four sides 
using the turtle.forward() and turtle.right() methods. After that, the function draws the stripes by looping 
through 13 times and using the modulus operator to determine whether the current stripe should be red or white. It then uses the same turtle.forward() and turtle.right() methods to draw each stripe.
Next, the function calculates the position of the stars rectangle, sets the turtle's color to blue, and fills 
the rectangle by drawing four sides using the same methods as before. It then calls the draw_star() function to 
draw the stars on top of the rectangle.The draw_star() function takes two parameters, l and h, which represent 
the length and height of the flag again. It then uses a loop to draw the rows of stars, with each row containing 
10 stars. It calls the draw_starrows() function to draw each row. The draw_starrows() function takes one 
parameter, row, which represents the y-coordinate of the row of stars. It uses a loop to draw 10 stars in the 
current row using the turtle.forward() and turtle.left() methods. Finally, the draw_flag() function sets the 
height of the flag, calls the draw_rectangle() function to draw the flag, sets the turtle's position to write 
my initials **CREATIVE ELEMENT** in yellow at the bottom of the flag, and then calls the turtle.bye() function 
to exit the Turtle module.
"""

import turtle
# 
def draw_rectangle(length, height):
    # Draws the rectangle
    turtle.up()
    x = -150
    y = 150
    C = height*(7/13)
    D = length*(2/5)
    L = float(round(height/13,1))
    turtle.color("red")
    turtle.begin_fill()
    turtle.setpos(x,y)
    turtle.down()
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(height)
    turtle.end_fill()
    ## Then draw the stripes.
    x1 = -150
    y1 = 150-L
    for z in range(13):
        if z%2 == 0:
            r=255
            s=t=0
        else:
            r=s=t=255
        turtle.up()
        turtle.speed(100)
        turtle.setpos(x1,y1)
        turtle.setheading(90)
        turtle.down()
        turtle.colormode(255)
        turtle.color(r,s,t)
        turtle.begin_fill()
        turtle.forward(L)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(L)
        turtle.right(90)
        turtle.forward(length)
        turtle.end_fill()
        y1 -= L
        ## Finally draw the stars rectangle overlapping the stripes, next is stars.
    x2 = -150+D
    y2 = 150.5-C

    turtle.up()
    turtle.setpos(x2,y2)
    turtle.down()
    turtle.color("blue")
    turtle.begin_fill()
    turtle.forward(D)
    turtle.right(90)
    turtle.forward(C)
    turtle.right(90)
    turtle.forward(D)
    turtle.right(90)
    turtle.forward(C)
    turtle.end_fill()
    turtle.up()
    turtle.bye

    draw_star(-length, height)

def draw_star(l, h):
    for z in range(50):
        if z < 7:
            row = 140
            draw_starrows(row)
        if z < 14:
            row = row - 20
            draw_starrows(row)
        if z < 21:
            row = row - 20
            draw_starrows(row)
        if z < 28:
            row = row - 20
            draw_starrows(row)
        if z < 35:
            row = row - 20
            draw_starrows(row)
            ## This gets the turtle pen out of the way at the very end.
            turtle.up()
            turtle.setpos(-180,100)
        break

def draw_starrows(row):
    x = -160
    for z in range(10):
        x += 15
        turtle.up()
        turtle.color("white")
        turtle.speed(100)
        turtle.setpos(x,row)
        turtle.begin_fill()
        turtle.down()
        turtle.forward(6.154)
        turtle.left(144)
        turtle.forward(6.154)
        turtle.left(144)
        turtle.forward(6.154)
        turtle.left(144)
        turtle.forward(6.154)
        turtle.left(144)
        turtle.forward(6.154)
        turtle.left(144)
        turtle.end_fill()
    turtle.bye

def draw_flag():
    A = 200
    height = int(A)
    draw_rectangle(height*1.9, height)
    draw_star(-height, height)
    turtle.up()
    turtle.setpos(-75, -height/2 - 10)
    turtle.color("yellow")
    # Writes in my intials at the bottom of the code.
    turtle.write("PMM", align="center", font=("Arial", 20, "bold"))
    turtle.bye
draw_flag()