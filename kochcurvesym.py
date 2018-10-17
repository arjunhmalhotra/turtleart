"""
This program draws a variation of a Koch curve symmetric about the cartesian plane.

"""

import turtle

#----------------------------------------
def koch(tortoise,depth,length):
    '''
This function draws Koch curves.
Parameter:
tortoise:  drawing objects
depth:          level of Koch curve detail
length:         size of line segment

Return value: none
    '''

    angle = 90

    if depth == 0:
        tortoise.forward(length)
    else:
        koch(tortoise,depth-1, length)
        tortoise.left(angle)
        koch(tortoise,depth-1, length)
        tortoise.right(angle)
        koch(tortoise,depth-1, length)
        tortoise.right(angle)
        koch(tortoise,depth-1, length)
        tortoise.left(angle)
        koch(tortoise,depth-1, length)
        
        
        
        
        
        
#----------------------------------------

def main():
    fred = turtle.Turtle()
    fred.speed(0)
    fred.up()
    fred.goto(-100,-100)
    fred.down()

    for i in range(2):              #the for loop makes the recursive call symmetric
                                    #about the x axis
        koch(fred, 4, 5)
        fred.right(180)

    


    screen = fred.getscreen()
    screen.exitonclick
#-----------------------------------------
main()
