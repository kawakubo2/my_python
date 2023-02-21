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

positions = [(100, 0), (0, -100), (-100, -200), (-100, 0), (100, -200)]

def square():
    for _ in range(4):
        my_turtle.forward(200)
        my_turtle.left(90)

rec_pos = [(-200, 0), (0, 0), (-200, -200), (0, -200)]
for pos in rec_pos:
    my_turtle.penup()
    my_turtle.goto(pos)
    my_turtle.pendown()
    square()
    my_turtle.penup()

for pos in positions:
    my_turtle.penup()
    my_turtle.goto(pos)
    my_turtle.pendown()
    my_turtle.circle(100)

screen.mainloop()