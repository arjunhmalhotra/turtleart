'''
This program randomly draws 40 koch snowflakes. The koch function draws the
intital curve and the snowflakes function draws 40 snowflakes.
'''

import turtle
import random

def koch(tortoise, length, depth):
    '''
    The koch function draws the initial koch curve used to draw the 40 snowflakes.
    Parameters.
        tortoise: turtle graphic
        length: length of koch curve
        depth: intricacy of koch curve
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



def snowflakes(tortoise, length, depth):
    '''
    The snowflakes function randomly draws 40 snowflakes using the koch function.
    The borders of the snowflakes are cyan, while the interior is a random shade
    of blue.
    Parameters:
        tortoise: turtle graphic
        length: size of snowflake
        depth: intricacy of snowflake
    Return Value: none
    '''
    x = 0
    y = 0
    
    for i in range(40):
        r = random.randint(1,50)
        g = random.randint(50,100)
        b = random.randint(170,255)
        tortoise.pencolor("cyan")
        tortoise.fillcolor((r,g,b))
        tortoise.penup()
        tortoise.goto(x,y)
        tortoise.pendown()
        tortoise.begin_fill()
        for side in range(3):
            koch(tortoise, length, depth)
            tortoise.right(120)
        tortoise.end_fill()
        x = random.randint(-300,300)
        y = random.randint(-300,300)
    
   
  
def main():
    length = 60
    depth = 3
    franklin = turtle.Turtle()
    franklin.speed(0)
    franklin.hideturtle()
    screen = franklin.getscreen()
    screen.colormode(255)
    snowflakes(franklin, length, depth)

    


main()
