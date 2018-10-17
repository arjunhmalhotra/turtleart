'''

This program draws a fern in python.

'''
import turtle
def floor(x,y):
    '''
    This function defines the floor so the fern can be drawn.  If x is larger,
    it will be returned, otherwise y is returned.  This is passed into the
    fern function below.
    '''
    if x > y:
       return x
    return y

def draw_fern1(george,length1, angle1, length2, angle2, depth):
    '''
    This function is the recursive function that draws the fern.  This draws
    left side of the fern.
    '''
    
    flip = 1
    for i in range(0, length2):
        george.left(angle2)
        george.forward(length1)
        if depth > 1:
            george.left(angle1*flip)

            draw_fern1(george,floor((length1/3)-(i/2),1), angle1*flip,
                    floor((length2-i),1), angle2*flip, (depth-1))
            george.left(180-angle1*flip)
    flip=flip*-1

    george.left(180)


    for i in range(0,length2):
        george.forward(length1)
        george.right(angle2)

def draw_fern2(george,length1, angle1, length2, angle2, depth):
    '''
    This function draws the right side of the fern.
    '''
    
    flip = 1
    for i in range(0, length2):
        george.left(angle2)
        george.forward(length1)
        if depth > 1:
            george.left(angle1*flip)

            draw_fern2(george,floor((length1/3)-(i/2),1), angle1*flip,
                    floor((length2-i),1), angle2*flip, (depth-1))
            george.left(180-angle1*flip)
    flip=flip*-1

    george.left(180)


    for i in range(0,length2):
        george.forward(length1)
        george.right(angle2)
        
def main():
    
    george = turtle.Turtle()
    george.speed(0)
    george.pencolor('dark green')
    george.penup()
    george.goto(0,-250)
    george.pendown()
    george.left(90)
 
    george.hideturtle()
 
    draw_fern1(george,75,70,8,4,6)
    george.left(180)
    draw_fern2(george,75,270,8,4,6)
    george.left(180)


main()
