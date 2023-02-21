import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_width(self):
        return self.__width
    def set_width(self, width):
        if width <= 0:
            raise Exception('幅が負数')
        self.__width = width
    def get_height(self):
        return self.__height
    def set_height(self, height):
        if height <= 0:
            raise Exception('高さが負数')
        self.__height = height

    width = property(get_width, set_width)
    height = property(get_height, set_height)

    def get_area(self):
        return self.width * self.height
    def get_diagonal(self):
        return math.hypot(self.width, self.height)
    def get_perimeter(self):
        return (self.width + self.height) * 2

    area = property(get_area)
    diagonal = property(get_diagonal)
    perimeter = property(get_perimeter)

class VisualRectangle(Rectangle):
    def __init__(self, width, height, x, y, color):
        super().__init__(width, height)
        self.x = x
        self.y = y
        self.color = color

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

    def get_distance(self):
        return math.hypot(self.x, self.y)

    distance = property(get_distance)

    def move(self, x, y):
        self.x += x
        self.y += y

if __name__ == '__main__':
    w = 8
    h = 6
    r1 = Rectangle(w, h)
    print('幅が{}, 高さが{}の長方形'.format(r1.width, r1.height))
    print('面積: {:.2f}'.format(r1.area))
    print('対角線: {:.2f}'.format(r1.diagonal))
    print('周りの長さ: {:.2f}'.format(r1.perimeter))

    w = 10
    h = 8
    x = 6
    y = 8
    color = 'white'

    r2 = VisualRectangle(w, h, x, y, color)
    print('幅が{}, 高さが{}の長方形'.format(r2.width, r2.height))
    print('面積: {:.2f}'.format(r2.area))
    print('対角線: {:.2f}'.format(r2.diagonal))
    print('周りの長さ: {:.2f}'.format(r2.perimeter))
    print('原点からの距離: {:.2f}'.format(r2.distance))

    r2.move(4, 2)
    print('新しい座標: x={:.2f} y={:.2f}'.format(r2.x, r2.y))
    print('原点からの距離: {:.2f}'.format(r2.distance))