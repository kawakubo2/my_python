import turtle, math

screen = turtle.Screen()
screen.setup(1000, 1000)
screen.title('タートル')

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.shapesize(3)
my_turtle.speed(8)
my_turtle.pensize(4)
my_turtle.pencolor("green")

PYRAMID_HEIGHT = 10
SIZE = 40

def init():
    my_turtle.penup()
    my_turtle.back((math.floor(PYRAMID_HEIGHT * 2 - 1) / 2) * SIZE)
    my_turtle.right(90)
    my_turtle.forward(math.floor(PYRAMID_HEIGHT / 2) * SIZE)
    my_turtle.left(90)

def rect():
    my_turtle.pendown()
    for _ in range(4):
        my_turtle.forward(SIZE)
        my_turtle.left(90)
    
def create_floor(num):
    for _ in range(num):
        rect()
        my_turtle.forward(SIZE)

def up_floor(num):
    my_turtle.penup()
    my_turtle.left(90)
    my_turtle.forward(SIZE)
    my_turtle.left(90)
    my_turtle.forward(SIZE * (num - 1))
    my_turtle.left(180)

def pyramid(height):
    init()
    for _ in range(height):
        create_floor(height * 2 - 1)
        up_floor(height * 2 - 1)
        height -= 1

pyramid(PYRAMID_HEIGHT)

screen.mainloop()