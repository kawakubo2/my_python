import math

class Rectangle:
    def __init__(self, x, y, width, height):
        self.set_x(x)
        self.set_y(y)
        self.set_width(width)
        self.set_height(height)

    def get_x(self):
        return self.__x
    def set_x(self, x):
        self.__x = x
    def get_y(self):
        return self.__y
    def set_y(self, y):
        self.__y = y
    def get_width(self):
        return self.__width
    def set_width(self, width):
        if width <= 10:
            raise Exception("幅が10以下")
        self.__width = width
    def get_height(self):
        return self.__height 
    def set_height(self, height):
        if height <= 10:
            raise Exception("高さが10以下")
        self.__height = height

    x = property(get_x, set_x)
    y = property(get_y, set_y)
    width = property(get_width, set_width)
    height = property(get_height, set_height)

    # 面積
    def get_area(self):
        return self.width * self.height

    # 対角線の長さ
    def get_diagonal(self):
        return math.hypot(self.width, self.height)

    # 原点からの距離
    def get_distance(self):
        return math.hypot(self.x, self.y)

    area = property(get_area)
    diagonal = property(get_diagonal)
    distance = property(get_distance)

if __name__ == "__main__":

    r1 = Rectangle(3, 4, 12, 18)
    r2 = Rectangle(5, 5, 15, 13)

    print(f"r1: 面積: {r1.area} 対角線の長さ: {r1.diagonal:.2f} 原点からの距離: {r1.distance:.2f}")
    print(f"r2: 面積: {r2.area} 対角線の長さ: {r2.diagonal:.2f} 原点からの距離: {r2.distance:.2f}")
    
    