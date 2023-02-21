import math

class Rectangle:
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)

    def get_width(self):
        return self.__width

    def set_width(self, width):
        if type(width) != float and type(width) != int:
            raise ValueError("幅が数値ではありません。")
        if width <= 0:
            raise ValueError("幅が0以下です。")
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        if type(height) != float and type(height) != int:
            raise ValueError("高さが数値ではありません。")
        if height <= 0:
            raise ValueError("高さが0以下です。")
        self.__height = height

    def get_area(self):
        return self.__width * self.__height 

    def get_diagonal(self):
        return math.hypot(self.__width, self.__height)

    width = property(get_width)
    height = property(get_height)
    area = property(get_area)
    diagonal = property(get_diagonal)

if __name__ == "__main__":

    try:
        rec1 = Rectangle(8, 6)
        print(f"幅が{rec1.width}、高さが{rec1.height}の長方形の面積は{rec1.area}")
        rec2 = Rectangle(9, -7)
        print(f"幅が{rec2.width}、高さが{rec2.height}の長方形の面積は{rec2.area}")
    except Exception as e:
        print(e)