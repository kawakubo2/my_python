import math
from rectangle2 import Rectangle

class CoordinatedRectangle(Rectangle):
    def __init__(self, width, height, x, y):
        self.set_x(x)
        self.set_y(y)
        super().__init__(width, height)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if type(x) != float and type(x) != int:
            raise ValueError("x座標が数値でない。")
        self.__x = x
    
    def get_y(self):
        return self.__y

    def set_y(self, y):
        if type(y) != float and type(y) != int:
            raise ValueError("y座標が数値でない")
        self.__y = y

    def get_distance(self):
        return math.hypot(self.__x, self.__y)

    x = property(get_x)
    y = property(get_y)
    distance = property(get_distance)

if __name__ == "__main__":
    rec = CoordinatedRectangle(10, 20, 6, 8)
    print(f"面積: {rec.area} 原点からの距離: {rec.distance}")