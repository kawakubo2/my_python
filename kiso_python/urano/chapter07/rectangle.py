# rectangle.py

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height
    def set_width(self, width):
        if width <= 0:
            raise Exception('幅が0以下')
        self.__width = width
    def set_height(self, height):
        if height <= 0:
            raise Exception('高さが0以下')
        self.__height = height
    def get_area(self):
        return self.width * self.height
    width = property(get_width, set_width)
    height = property(get_height, set_height)
    area = property(get_area)

class CoordinateRectangle(Rectangle):
    def __init__(self, width, height, x, y):
        self.__x = x
        self.__y = y
        super().__init__(width, height)
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def set_x(self, x):
        self.__x = x
    def set_y(self, y):
        self.__y = y
    def get_distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    x = property(get_x, set_x)
    y = property(get_y, set_y)
    distance = property(get_distance)

if __name__ == '__main__':
    rec1 = Rectangle(8, 5)
    print(f'幅:{rec1.width}, 高さ:{rec1.height}, 面積:{rec1.area}')
    rec1.height = 10
    print(f'幅:{rec1.width}, 高さ:{rec1.height}, 面積:{rec1.area}')
    try:
        rec1.width = -5
        print(f'幅:{rec1.width}, 高さ:{rec1.height}, 面積:{rec1.area}')
    except Exception as e:
        print(e)

    coord_rec1 = CoordinateRectangle(3, 4, 6, 8)
    area = coord_rec1.area
    distance = coord_rec1.distance
    print(f"幅が{coord_rec1.width}、高さが{coord_rec1.height}の長方形の面積は{area}")
    print(f"X座標が{coord_rec1.x}、Y座標が{coord_rec1.y}の長方形の原点からの距離は{distance}")