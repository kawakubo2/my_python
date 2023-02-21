from figure import Figure
from rectangle2 import Rectangle
from circle import Circle
from triangle import Triangle

player1 = [Rectangle(20, 20), Rectangle(10, 10), Circle(5), Triangle(25, 8)]
player2 = [Triangle(20, 10), Rectangle(15, 10), Circle(10)]

total1 = 0
for f in player1:
    print(f)
    total1 += f.getArea()

total2 = 0
for f in player2:
    print(f)
    total2 += f.getArea()

print("player1の合計: {:.2f}".format(total1))
print("player2の合計: {:.2f}".format(total2))