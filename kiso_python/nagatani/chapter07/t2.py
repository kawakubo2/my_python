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

pi2 = 360
poly = 128 
edge = 10 
for _ in range(poly):
    my_turtle.forward(edge)
    my_turtle.left(pi2 / poly)

screen.mainloop()