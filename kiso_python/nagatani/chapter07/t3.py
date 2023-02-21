import turtle

screen = turtle.Screen()
screen.setup(1000, 1000)
screen.title('タートル')

my_turtle = turtle.Turtle()
my_turtle.speed(1)
my_turtle.shape("turtle")
my_turtle.shapesize(2)
my_turtle.pensize(4)
my_turtle.pencolor("green")

sw = 1
count = 10
length = 20
edge = 40
for _ in range(count):
    my_turtle.forward(edge)
    my_turtle.left(90 * sw)
    my_turtle.forward(edge)
    my_turtle.left(90 * sw)
    my_turtle.forward(edge)
    my_turtle.left(90 * sw)
    my_turtle.forward(edge)
    my_turtle.penup()
    my_turtle.forward(length)
    my_turtle.right(90 * sw)
    my_turtle.forward(length)
    my_turtle.right(90 * sw)
    edge += (length * 2) 
    my_turtle.pendown()
    sw = sw * -1

screen.mainloop()