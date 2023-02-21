import turtle
import datetime

screen = turtle.Screen()
screen.setup(600, 300)
# チラつき防止
screen.tracer(0)

time_turtle = turtle.Turtle()
time_turtle.penup()
time_turtle.hideturtle()
time_turtle.goto(-200, 0)

def clock():
    now = datetime.datetime.now()
    time = f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}"
    time_turtle.clear()
    time_turtle.write(time, font=("helvetica", 80))
    # 100ミリ秒ごとに自分自身を呼び出す
    screen.ontimer(clock, 100)

clock()    

screen.mainloop()