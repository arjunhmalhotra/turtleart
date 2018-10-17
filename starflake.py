'''
This program draws a magnificent starflake using turtle, recursion, and koch
curves. The koch function draws the inital curve and the starflake function
draws the starflake.
'''

import turtle


def koch(tortoise, length, depth):
    '''
    The koch function draws the inital koch curve used in the starflake function
    Parameters:
        tortoise: turtle graphic
        length: length of koch curve
        depth: level of intricacy of the koch curve
    Return Value: none 
    '''
    if depth == 0:
        tortoise.forward(length)
    else:
        koch(tortoise, length/3, depth-1)
        tortoise.left(60)
        koch(tortoise, length/3, depth-1)
        tortoise.right(120)
        koch(tortoise, length/3, depth-1)
        tortoise.left(60)
        koch(tortoise, length/3, depth-1)


def starflake(tortoise, length, depth):
    '''
    The starflake function recursively draws a starflake using the koch
    function.The borders of each sequential star flake are cyan, while the
    fill is a continuously lighter shade of blue.
    Parameters:
        tortoise: turtle graphic
        length: size of starflake
        depth: level of intricacy of starflake
    Return Value: none
    '''
    x = -250
    y = 130
    b = 50
    tortoise.penup()
    tortoise.goto(x,y)
    tortoise.pendown()
    tortoise.fillcolor((0,0,b))
    tortoise.begin_fill()
    for side in range(3):
        tortoise.pencolor("cyan")
        koch(tortoise, length, depth)
        tortoise.right(120)
    tortoise.end_fill()
    for i in range(8):
        length = length/1.5
        x = x/1.5
        y = y/1.5
        b = b+25
        tortoise.fillcolor((0,0,b))
        tortoise.penup()
        tortoise.goto(x,y)
        tortoise.pendown()
        tortoise.begin_fill()
        for side in range(3):
            koch(tortoise, length, depth)
            tortoise.right(120)
        tortoise.end_fill()

            
def main():
    length = 500
    depth = 5
    franklin = turtle.Turtle()
    franklin.speed(0)
    screen = franklin.getscreen()
    screen.colormode(255)
    franklin.hideturtle()
    starflake(franklin,length,depth)




main()
