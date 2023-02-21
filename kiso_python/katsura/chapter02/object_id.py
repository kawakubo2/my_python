a = 123
print(id(a))

color = '赤'
print(id('赤'))

def mul(x, y):
    result = x * y
    return result

print(mul(20, 10))

import math
class Rectangle:
    """
    長方形を表すクラス
    プロパティ
        width:幅(float)
        height:高さ(float)
    メソッド
        get_area:面積を求める
        get_diaglnal:対角線を求める
    """
    def __init__(self, width,height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def get_area(self):
        """
        面積を求めるためのメソッド
        """
        return self.width * self.height
    def get_diagonal(self):
        """
        対角線の長さを求めるメソッド
        """
        return math.hypot(self.width, self.height)

rec1 = Rectangle(3, 4)
rec2 = Rectangle(6, 8)

print(help(Rectangle))

print(f"幅が{rec1.get_width()}, 高さが{rec1.get_height()}の長方形の面積は{rec1.get_area()}")
print(f"幅が{rec2.get_width()}, 高さが{rec2.get_height()}の長方形の面積は{rec2.get_area()}")

print(f"幅が{rec1.get_width()}, 高さが{rec1.get_height()}の長方形の対角線は{rec1.get_diagonal()}")
print(f"幅が{rec2.get_width()}, 高さが{rec2.get_height()}の長方形の対角線は{rec2.get_diagonal()}")

import calendar

cal = calendar.TextCalendar(6)
cal.prmonth(2021, 10)