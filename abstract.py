
import turtle


def drawDot(george,x, y, radius):
    '''
    This function uses recursive principals to draw hundreds of hexagons.
    To change the depth, change the radius size below.  Inputs are
    george the turtle, starting x coordinate, starting y coordinate, and radius
    of the circle.  Output is a turtle drawing.
    '''
    if radius >10:
        george.up()
        george.goto(x,y)
        george.down()
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        drawDot(george,x+radius,y+radius/2,radius/2)

        george.up()
        george.goto(x,y)
        george.down()
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        drawDot(george,x-radius,y+radius/2,radius/2)
        
        george.up()
        george.goto(x,y)
        george.down()
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        drawDot(george,x,y+radius/2,radius/2)
        
        george.up()
        george.goto(x,y)
        george.down()
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        drawDot(george,x,y-radius/2,radius/2)
        
        george.up()
        george.goto(x,y)
        george.down()
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        george.right(60)
        george.forward(radius)
        drawDot(george,x,y+radius*(1.5),radius/2)
        
        

def main():
    george = turtle.Turtle()
    george.hideturtle()
    george.speed(0)
    george.pendown()
    radius = 100
    x = 0
    y = 000
    drawDot(george,x, y, radius)



main()
