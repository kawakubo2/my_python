import math

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x ** 2 + self.y ** 2 == other.x ** 2 + other.y ** 2

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.x ** 2 + self.y ** 2 < other.x ** 2 + other.y ** 2

    def __le__(self, other):
        return self.x ** 2 + self.y ** 2 <= other.x ** 2 + other.y ** 2

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __add__(self, other):
        if isinstance(other, Coordinate):
            return Coordinate(
                self.x + other.x,
                self.y + other.y
            )
        elif isinstance(other, int):
            return Coordinate(
                self.x + other, 
                self.y + other
            )
        else:
            raise TypeError('type must be Coordinate or int')

    def __radd__(self, other):
        if isinstance(other, Coordinate):
            return Coordinate(
                other.x + self.x, 
                other.y + self.y)
        elif isinstance(other, int):
            return Coordinate(
                other + self.x,
                other + self.y
            ) 
        else:
            raise TypeError('type must be Coordinate or int')

    def __iadd__(self, other):
        """
        複合代入演算子の場合、otherはCoordinateインスタンスのみとする
        self.x += other.x
        self.y += other.y
        return self
        """
        self.x += other.x
        self.y += other.y
        return Coordinate(
            self.x, 
            self.y)
        
    def __str__(self):
        return f'({self.x},{self.y})'

    def __int__(self):
        return int(self.__float__())

    def __float__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __bool__(self):
        print('__bool__')
        return self.x != 0 or self.y != 0

    def __len__(self):
        print('__len__')
        return int(math.sqrt(self.x ** 2 + self.y ** 2))

if __name__ == '__main__':
    c1 = Coordinate(10, 20)
    c2 = Coordinate(15, 25)
    print(c1 + 10)
    print(c1 + c2)
    print(c1)
    print(c2)
    c1 += c2 # c1 = c1 + c2
    print(c1)
    print(c2)
    print(10 + c1)

    c3 = Coordinate(1, 2)
    c4 = Coordinate(15, 25)
    c5 = Coordinate(2, 1)
    c6 = Coordinate(6, 8)
    c7 = Coordinate(0, 10)
    print(c3 < c4) # True
    print(c3 <= c5) # True
    print(c3 <= c4) # True
    print(c3 > c4) # False
    print(c6 == c7)
    print(c6 != c7)

    c8 = Coordinate(1, 2)
    print(float(c8))
    print(int(c8))

    list1 = list()
    print(list1 == False)
    
    c9 = Coordinate(0, 0)
    if c9:
        print('c9はTrueです。')
    else:
        print('c9はFalseです。')