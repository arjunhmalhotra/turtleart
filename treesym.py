'''
This program draws a tree with arrowlike structures symmetric about the center.
'''


import turtle

#----------------------------- TREE FUNCTION -----------------

def treesym(tortoise,depth,length):
    '''
This function draws a tree.
Parameter:
tortoise:       drawing objects
depth:          level of treesym curve detail
length:         size of line segment

Return value: none
    '''
    
    angle = 25.7
    stack = []              #stack storing turtle state

    if depth == 0:
        tortoise.forward(length)
    else:
        treesym2(tortoise,depth-1, length)
        

        #remember branch
        stack.append(tortoise.xcor())
        stack.append(tortoise.ycor())
        stack.append(tortoise.heading())
        
        tortoise.left(angle)
        treesym(tortoise,depth-1, length)
        
        
        #recall branch
        tortoise.up()
        tortoise.setheading( stack.pop() )
        tortoise.sety( stack.pop() )
        tortoise.setx( stack.pop() )
        tortoise.down()

        #remember branch
        stack.append(tortoise.xcor())
        stack.append(tortoise.ycor())
        stack.append(tortoise.heading())

        tortoise.right(angle)
        treesym(tortoise,depth-1, length)

        #recall branch
        tortoise.up()
        tortoise.setheading( stack.pop() )
        tortoise.sety( stack.pop() )
        tortoise.setx( stack.pop() )
        tortoise.down()

        treesym2(tortoise,depth-1, length)
        treesym(tortoise,depth-1, length)

        
        
#------------------------ FUNCTION TWO --------------------------------
def treesym2(tortoise,depth,length):
    '''
This function draws a tree.
Parameter:
tortoise:       drawing objects
depth:          level of treesym curve detail
length:         size of line segment

Return value: none
    '''
    
    angle = 25.7
    stack = []              #stack storing turtle state

    if depth == 0:
        tortoise.forward(length)
    else:
        treesym2(tortoise,depth-1, length)
        treesym2(tortoise,depth-1, length)
        
#------------------------ MAIN --------------------------------

def main():
    fred = turtle.Turtle()
    fred.setheading(90)
    fred.speed(0)
    fred.up()
    fred.goto(-200,-300)
    fred.down()

    treesym(fred, 7, 2)
    

    


    screen = fred.getscreen()
    screen.exitonclick
#-----------------------------------------
main()
