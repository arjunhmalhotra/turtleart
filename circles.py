'''
This program draws circles recursivley to create a cool pattern
'''

import turtle


def drawCircle(george,x, y, radius):
    '''
    This function uses recursive principals to draw hundreds of circles.
    To change the depth, change the radius size below.  Inputs are
    george the turtle, starting x coordinate, starting y coordinate, and radius
    of the circle.  Output is a turtle drawing.
    '''
    if radius > 10:
        george.up()
        george.goto(x,y)
        george.down()
        george.circle(radius)
        drawCircle(george,x+radius,y+radius/2,radius/2)
        george.up()
        george.goto(x,y)
        george.down()
        george.circle(radius)
        drawCircle(george,x-radius,y+radius/2,radius/2)
        george.up()
        george.goto(x,y)
        george.down()
        george.circle(radius)
        drawCircle(george,x,y+radius/2,radius/2)
        george.up()
        george.goto(x,y)
        george.down()
        george.circle(radius)
        drawCircle(george,x,y-radius/2,radius/2)
        george.up()
        george.goto(x,y)
        george.down()
        george.circle(radius)
        drawCircle(george,x,y+radius*(1.5),radius/2)
       

def main():
    george = turtle.Turtle()
    george.hideturtle()
    george.speed(0)
    george.pendown()
    radius = 200
    x = 0
    y = -200
    drawCircle(george,x, y, radius)



main()
