import turtle

screen = turtle.Screen()
screen.setup(800, 800)
screen.title('タートル')

my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
my_turtle.shapesize(3)
my_turtle.speed(2)
my_turtle.pensize(4)
my_turtle.pencolor('green')

unit = 50
loop = 8
for i in range(loop * 2):
    my_turtle.forward(unit * (i + 1))
    my_turtle.left(90)
    my_turtle.forward(unit * (i + 1))
    my_turtle.left(90)

screen.mainloop()