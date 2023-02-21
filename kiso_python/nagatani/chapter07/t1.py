import turtle

screen = turtle.Screen()
screen.setup(1000, 1000)
screen.title('タートル')

my_turtle = turtle.Turtle()
my_turtle.sety(300)
my_turtle.speed(3)
my_turtle.shape("turtle")
my_turtle.shapesize(2)
my_turtle.pensize(4)
my_turtle.pencolor("green")

my_turtle.left(270)
unit = 40
size = 17 
for i in range(size):
    my_turtle.forward(unit * (size - i))
    my_turtle.left(90)
    my_turtle.forward(unit * (i + 1))
    my_turtle.left(90)

cnt = size // 2 + 1
for i in range(cnt):
    my_turtle.forward(unit)
    my_turtle.left(90)
    my_turtle.forward(unit)
    my_turtle.right(90)

screen.mainloop()