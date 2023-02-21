import turtle

screen = turtle.Screen()
screen.setup(1000, 1000)
screen.title('タートル')

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.shapesize(3)
my_turtle.pensize(4)
my_turtle.pencolor("green")

my_turtle.forward(200)
my_turtle.left(90)
my_turtle.forward(200)
my_turtle.left(90)
my_turtle.forward(200)
my_turtle.left(90)
my_turtle.forward(200)
my_turtle.left(90)

screen.mainloop()