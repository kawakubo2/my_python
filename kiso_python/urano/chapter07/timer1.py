import turtle

screen = turtle.Screen()
screen.setup(1000, 300)
# チラつき防止
screen.tracer(0)

news_turtle = turtle.Turtle()
news_turtle.penup()
news_turtle.hideturtle()
news_turtle.goto(-400, 0)

i = 0
s = "      【天気】上空の寒気と冬型の気圧配置の影響で、27日の朝は各地で今シーズン一番の冷え込みとなりました。日本海側を中心に大気の状態が不安定になり雪や雨が降っていて、大雪のほか、落雷や突風、急な強い雨などに十分な注意が必要です。"
def news_reader():
    global i
    if i + 20 > len(s):
        i = 0
    news_turtle.clear()
    news_turtle.write(s[i: i+20], font=("helvetica", 28))
    i += 1
    screen.ontimer(news_reader, 300)
    
news_reader()

screen.mainloop()
        