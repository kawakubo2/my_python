import turtle
import math
screen = turtle.Screen()
screen.setup(800, 800)
screen.title('タートル')

my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
my_turtle.shapesize(2)
my_turtle.speed(3)
my_turtle.pensize(4)
my_turtle.pencolor('green')

radius = 36
sw = 1
start_pos = (-3 * radius * 2, -3 * radius * 2)
my_turtle.penup()
my_turtle.goto(start_pos)
my_turtle.pendown()

count = 7
while count > 0:
    for i in range(count):
        my_turtle.pendown()
        my_turtle.circle(radius)
        my_turtle.penup()
        if i < count - 1:
            my_turtle.forward(radius * 2)
    my_turtle.penup()
    if count == 1:
        break
    if sw == 1:
        my_turtle.left(sw * 90)
        my_turtle.forward(radius)
        my_turtle.left(sw * 30)
        my_turtle.forward(radius * 2)
        my_turtle.right(sw * 30)
        my_turtle.forward(radius)
        my_turtle.left(90)
    else:
        my_turtle.left(90)
        my_turtle.forward(radius)
        my_turtle.left(150)
        my_turtle.forward(radius * 2)
        my_turtle.right(150)
        my_turtle.forward(radius)
        my_turtle.left(90)
    sw = sw * (-1)
    count -= 1
screen.mainloop()