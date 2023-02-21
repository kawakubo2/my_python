import turtle

screen = turtle.Screen()
screen.setup(800, 800)
screen.title('タートル')

my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
my_turtle.shapesize(2)
my_turtle.speed(8)
my_turtle.pensize(4)
my_turtle.pencolor('green')

radius = 36
for j in range(3, -4, -1):
    for i in range(-3, 4):
        my_turtle.penup()
        my_turtle.goto(i * radius * 2, j * radius * 2)
        my_turtle.pendown()
        my_turtle.circle(radius)

screen.mainloop()