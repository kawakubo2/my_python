from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    p = pos()
    print(help(p))
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()