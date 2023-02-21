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

positions = [(100, 100),(0, 0),(-100, -100), (-100, 100), (100, -100)]

for pos in positions:
    my_turtle.penup()
    my_turtle.goto(pos)
    my_turtle.pendown()
    my_turtle.circle(100)
    
screen.mainloop()