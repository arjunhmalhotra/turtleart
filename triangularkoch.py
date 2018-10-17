"""

This function draws a koch curve as a triangular series of spaces.

"""


import turtle

#=============== FUNCTION ONE ===========================

def triangle(tortoise,depth,length):
    '''
This function draws triangle curves.
Parameter:
tortoise:  drawing objects
depth:          level of triangle curve detail
length:         size of line segment

Return value: none
    '''

    angle = 60

    if depth == 0:
        tortoise.forward(length)
    else:
        triangle1(tortoise,depth-1, length)
        tortoise.left(angle)
        triangle(tortoise,depth-1, length)
        tortoise.left(angle)
        triangle1(tortoise,depth-1, length)


#========================= FUNCTION TWO =====================


def triangle1(tortoise,depth,length):
    '''
This function draws triangle curves.
Parameter:
tortoise:  drawing objects
depth:          level of triangle curve detail
length:         size of line segment

Return value: none
    '''

    angle = 60

    if depth == 0:
        tortoise.forward(length)
    else:
        triangle(tortoise,depth-1, length)
        tortoise.right(angle)
        triangle1(tortoise,depth-1, length)
        tortoise.right(angle)
        triangle(tortoise,depth-1, length)
        

#=========================== MAIN =================
        
        
def main():
    fred = turtle.Turtle()
    fred.speed(0)
    fred.up()
    fred.goto(-100,-100)
    fred.down()

    triangle1(fred, 6, 5)
    

    


    screen = fred.getscreen()
    screen.exitonclick
#-----------------------------------------
main()
