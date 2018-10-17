'''
This program recursively draws a dream catcher using a pattern of triangles.
The drawTri function is used to draw the inital triangles, and the dreamCatcher
function uses the drawTri function to draw the dream catcher.
'''

import turtle


def drawTri(tortoise, length, width):
    '''
    The drawTri function draws a traingle with another triangle at each point of
    the initial triangle.
    Parameters:
        tortoise: turtle graphic
        length: length of triangle
        width: width of triangle
    Return Value: none 
    '''
    for i in range(3):
        tortoise.forward(length)
        tortoise.right(120)
        tortoise.forward(width)
        tortoise.right(120)
        tortoise.forward(length)
    tortoise.right(90)


def dreamCatcher(tortoise, length, width):
    '''
    The dreamCatcher function uses the drawTri function to recursively draw
    a dream catcher. The drawTri function is called a total of 8 times.
    Parameters:
        tortoise: turtle graphic
        length: length of triangle
        width: width of triangle
    Return Value: none
    '''
    for i in range(4):
        drawTri(tortoise, length, width)
    tortoise.setheading(45)
    tortoise.pencolor("red")
    for i in range(4):
        drawTri(tortoise, length, width)
    tortoise.setheading(22.5)
    tortoise.pencolor("black")
    for i in range(4):
        drawTri(tortoise, length, width)
    tortoise.setheading(67.5)
    tortoise.pencolor("red")
    for i in range(4):
        drawTri(tortoise, length, width)
    tortoise.setheading(78.75)
    tortoise.pencolor("black")
    for i in range(4):
        drawTri(tortoise, length, width)
    tortoise.setheading(11.25)
    tortoise.pencolor("red")
    for i in range(4):
        drawTri(tortoise, length, width)
    tortoise.setheading(56.25)
    tortoise.pencolor("black")
    for i in range(4):
        drawTri(tortoise, length, width)
    tortoise.setheading(33.75)
    tortoise.pencolor("red")
    for i in range(4):
        drawTri(tortoise, length, width)


def main():
    length = 200
    width = 100
    franklin = turtle.Turtle()
    franklin.hideturtle()
    screen = franklin.getscreen()
    franklin.speed(0)
    dreamCatcher(franklin, length, width)


main()
    
