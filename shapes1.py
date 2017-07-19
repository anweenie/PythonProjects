from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(600,400)
#x_pos = -250
#y_pos = -150
#t.setposition(x_pos, y_pos)

### Write your code below:
pendown()
pencolor("goldenrod")
forward(90)
left(60)
back(90)
left(60)
forward(90)
pendown()

pendown()
left(45)
forward(90)
left(45)
forward(90)
left(45)
forward(90)
left(45)
forward(90)
left(45)
forward(90)
left(45)
forward(90)
left(45)
forward(90)
left(45)
forward(90)
# Close window on click.
exitonclick()


from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(600,400)
#x_pos = -250
#y_pos = -150
#t.setposition(x_pos, y_pos)

### Write your code below:
inp = int(input("How many sides?"))
#number = input("How many sides?")

def shape(num):
     for i in range(num):
        t.forward(100)
        t.right(360/num)

shape(inp)

#triangle():
#pendown()
#pencolor("goldenrod")
#forward(90)
#left(60)
#back(90)
#left(60)
#forward(90)
#pendown()

#pendown()
#left(45)
#forward(90)
#left(45)
#forward(90)
#left(45)
#forward(90)
#left(45)
#forward(90)
#left(45)
#forward(90)
#left(45)
#forward(90)
#left(45)
#forward(90)
#left(45)
#forward(90)

# Close window on click.
exitonclick()
