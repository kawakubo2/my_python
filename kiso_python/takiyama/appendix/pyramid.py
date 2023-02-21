import math
import turtle

screen = turtle.Screen()
screen.setup(1000, 1000)
screen.title("タートル")

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.shapesize(3)
my_turtle.pensize(4)
my_turtle.pencolor("green")
my_turtle.speed(8)

DANSU = 10
NB_BLOCK = DANSU * 2 - 1
FORWARD = 30 

def init():
    my_turtle.penup()
    my_turtle.left(180)
    my_turtle.forward(math.floor(FORWARD * NB_BLOCK / 2))
    my_turtle.left(90)
    my_turtle.forward(math.floor(FORWARD * NB_BLOCK / 2))
    my_turtle.left(90)

def square():
    for k in range(4):
        my_turtle.forward(FORWARD)
        my_turtle.left(90)

def move_upper_stage(i):
    my_turtle.left(90)
    my_turtle.forward(FORWARD)
    my_turtle.left(90)
    my_turtle.forward((i - 1) * FORWARD)
    my_turtle.left(180)
            
def draw_pyramid():
    init()
    for i in range(NB_BLOCK, 0, -2):
        my_turtle.penup()
        for j in range(i):
            my_turtle.pendown()
            square()
            my_turtle.penup()
            my_turtle.forward(FORWARD)
        move_upper_stage(i)

draw_pyramid()
    
screen.mainloop()