import turtle

screen = turtle.Screen()
screen.setup(800, 800)
screen.title("タートル")

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.shapesize(3)
my_turtle.pensize(4)
my_turtle.pencolor("green")
my_turtle.speed(1)

for _ in range(4):
    my_turtle.forward(200)
    my_turtle.left(90)
    
screen.mainloop()