import turtle

screen = turtle.Screen()
screen.setup(800, 800)
screen.title('タートル')

my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
my_turtle.shapesize(3)
my_turtle.speed(3)
my_turtle.pensize(4)
my_turtle.pencolor('green')
my_turtle.fillcolor('yellow')

my_turtle.goto(50, 50)

my_turtle.begin_fill()
my_turtle.right(90)
my_turtle.forward(250)
my_turtle.left(90)
my_turtle.forward(250)
my_turtle.left(90)
my_turtle.forward(250)
my_turtle.end_fill()

my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(300)

screen.mainloop()