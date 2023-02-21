import math
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.__width

    def set_width(self, width):
        if width <= 0:
            raise Exception('幅が0以下')
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        if height <= 0:
            raise Exception('高さが0以下')
        self.__height = height

    width = property(get_width, set_width)
    height = property(get_height, set_height)

    def area(self):
        return self.width * self.height        

    def diagonal(self):
        return math.hypot(self.width, self.height) # widthの2乗とheightの2乗の平方根

class DrawableRectangle(Rectangle):
    def __init__(self, width, height, x, y, color):
        self.__x = x
        self.__y = y
        self.__color = color
        super().__init__(width, height)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    x = property(get_x, set_x)
    y = property(get_y, set_y)
    color = property(get_color, set_color)

    def distance(self):
        return math.hypot(self.x, self.y)

if __name__ == '__main__':
    r1 = DrawableRectangle(3, 4, 8, 6, 'white')
    print('原点からの距離:{:.2f}'.format(r1.distance()))