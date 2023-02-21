# rectangle1.py

class Rectangle:

    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)
        
    def get_width(self):
        return self.__width
    
    def set_width(self, width):
        if width <=  0:
            raise ValueError('幅が0以下')
        self.__width = width
        
    def get_height(self):
        return self.__height

    def set_height(self, height):
        if height <= 0:
            raise ValueError('高さが0以下')
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def diagonal(self):
        return (self.__width ** 2 + self.__height ** 2) ** 0.5
    
    width = property(get_width, set_width)
    height = property(get_height, set_height)

if __name__ == "__main__":
    r1 = Rectangle(3, 4)
    r2 = Rectangle(8, 6)
    
    print("r1の面積は{}、対角線の長さは{}です。".format(r1.area(), r1.diagonal()))
    print("r2の面積は{}、対角線の長さは{}です。".format(r2.area(), r2.diagonal()))
    
    r2.width = 10
    r2.height = -10
    print("r2の面積は{}、対角線の長さは{}です。".format(r2.area(), r2.diagonal()))
