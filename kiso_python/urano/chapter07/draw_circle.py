import turtle
import random
def draw_circle(x, y):
    colors = ['lavender', 'lightgray', 'lightyellow', 'floralwhite', 'lightpink']
    my_turtle.fillcolor(random.choice(colors))
    my_turtle.begin_fill()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.circle(random.randint(20, 150))
    my_turtle.penup()
    my_turtle.end_fill()
    
screen = turtle.Screen()
screen.setup(1000, 1000)
screen.title('クリックした位置に円を描く')
my_turtle = turtle.Turtle()
my_turtle.speed(10)
my_turtle.pensize(1)
my_turtle.shapesize(2)
my_turtle.shape('turtle')
my_turtle.penup()

for _ in range(50):
    x = random.randint(-450, 450)
    y = random.randint(-450, 450)
    draw_circle(x, y)


screen.mainloop()