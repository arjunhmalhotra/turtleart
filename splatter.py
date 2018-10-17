"""

This program draws a paint splatter.

"""

import turtle

#----------------------------------------
def koch(tortoise,depth,length):
    '''
This function draws the patterns curves.
Parameter:
tortoise:       drawing objects
depth:          level of Koch curve detail
length:         length of line segment

Return value: none


    
    '''

    angle = 45
    
    if depth == 0:
        tortoise.forward(length)
    else:
        koch(tortoise,depth-1, length)
        tortoise.left(angle)
        tortoise.up()
        koch2(tortoise,depth-1, length)
        tortoise.down()
        tortoise.right(angle)
        koch(tortoise,depth-1, length)
        koch(tortoise,depth-1, length)
        tortoise.left(angle)
        koch(tortoise,depth-1, length)
        tortoise.left(angle)
        koch(tortoise,depth-1, length)
        koch(tortoise,depth-1, length)
        tortoise.left(angle)
        koch(tortoise,depth-1, length)
        tortoise.up()
        koch2(tortoise,depth-1, length)
        tortoise.down()
        tortoise.left(angle)
        koch(tortoise,depth-1, length)
        koch(tortoise,depth-1, length)
        tortoise.right(angle)
        tortoise.up()
        koch2(tortoise,depth-1, length)
        tortoise.down()
        tortoise.left(angle)
        koch(tortoise,depth-1, length)
        koch(tortoise,depth-1, length)
        tortoise.right(angle)
        koch(tortoise,depth-1, length)
        tortoise.right(angle)
        koch(tortoise,depth-1, length)
        koch(tortoise,depth-1, length)
        tortoise.right(angle)
        koch(tortoise,depth-1, length)
        tortoise.up()
        koch2(tortoise,depth-1, length)
        tortoise.down()
        tortoise.right(angle)
        koch(tortoise,depth-1, length)
        koch(tortoise,depth-1, length)
        koch(tortoise,depth-1, length)
        
        
#----------------------------------------
def koch2(tortoise,depth,length):
    '''
This function draws second recursive function to move forward without drawing a line.
Parameter:
tortoise:       drawing objects
depth:          level of Koch curve detail
length:         length of line segment

Return value: none
    '''

    if depth == 0:
        tortoise.forward(length)
    else:
        tortoise.up()
        koch(tortoise,depth-1, length)
        tortoise.down()
        tortoise.up()
        koch(tortoise,depth-1, length)
        tortoise.down()
        tortoise.up()
        koch(tortoise,depth-1, length)
        tortoise.down()
        tortoise.up()
        koch(tortoise,depth-1, length)
        tortoise.down()
        tortoise.up()
        koch(tortoise,depth-1, length)
        tortoise.down()
        tortoise.up()
        koch(tortoise,depth-1, length)
        tortoise.down()
        
        
        
        
#----------------------------------------

def main():
    fred = turtle.Turtle()
    fred.speed(0)
    fred.hideturtle()
    fred.up()
    fred.goto(100,-200)
    fred.down()
    
    koch(fred, 2, 2)
    fred.left(90)
    koch(fred, 2, 2)
    fred.left(90)
    koch(fred, 2, 2)
    fred.left(90)
    koch(fred, 2, 2)


    screen = fred.getscreen()
    screen.exitonclick
#-----------------------------------------
main()
