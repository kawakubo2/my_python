import turtle

# スクリーンの取得
screen = turtle.Screen()
screen.setup(800, 800)
screen.title('タートル')

# タートルの生成
my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
my_turtle.shapesize(1)
my_turtle.pensize(4)
my_turtle.speed(8)
my_turtle.pencolor('green')

# 多角形を描く
def draw_polygon(length,num):
    angle = 360 / num
    for _ in range(num):
        my_turtle.forward(length)
        my_turtle.left(angle)

draw_polygon(20, 64)

screen.mainloop()