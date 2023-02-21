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

# 正方形を描く
def draw_square(length=200,angle=90):
    for _ in range(4):
        my_turtle.forward(length)
        my_turtle.left(angle)

def draw_pyramid(dansu, length=200):
    num = dansu * 2 - 1
    start_pos = (num // 2) * length
    my_turtle.left(180)
    my_turtle.penup()
    my_turtle.forward(start_pos)
    my_turtle.left(180)
    while True:
        my_turtle.pendown()
        for _ in range(num):
            draw_square(length, 90)
            my_turtle.forward(length)
        my_turtle.left(90)
        my_turtle.forward(length)
        my_turtle.left(90)
        my_turtle.forward(length*(num - 1))
        my_turtle.left(180)
        num -= 2
        if num <= 0:
            break
    
draw_pyramid(10, 30)
    
screen.mainloop()