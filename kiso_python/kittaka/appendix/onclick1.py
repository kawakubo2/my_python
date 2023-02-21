import turtle, random

def draw_circle(x, y):
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.begin_fill()
    my_turtle.circle(random.randint(50, 150))
    my_turtle.end_fill()
    my_turtle.penup()
    
screen = turtle.Screen()
screen.setup(800, 800)
screen.title('タートル')

my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
my_turtle.shapesize(3)
my_turtle.speed(2)
my_turtle.pensize(4)
my_turtle.pencolor('green')
my_turtle.fillcolor("yellow")
my_turtle.penup()

screen.onscreenclick(draw_circle)

screen.mainloop()