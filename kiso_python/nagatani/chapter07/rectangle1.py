# rectangle1.py
import math

class Rectangle:
    """
    長方形を表すクラス
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 面積
    def get_area(self):
        """
        面積を返すメソッド
        """
        return self.width * self.height

    # 対角線
    def get_diagonal(self):
        """
        対角線の長さを返すメソッド
        """
        return math.sqrt(math.pow(self.width, 2) + math.pow(self.height, 2))
    # 外周
    def get_perimeter(self):
        """
        外周の長さを返すメソッド
        """
        return (self.width + self.height) * 2

rec1 = Rectangle(6, 8)
rec2 = Rectangle(4, 3)

print(f"rec1: 面積: {rec1.get_area()} 対角線: {rec1.get_diagonal()} 外周: {rec1.get_perimeter()}")
print(f"rec2: 面積: {rec2.get_area()} 対角線: {rec2.get_diagonal()} 外周: {rec2.get_perimeter()}")