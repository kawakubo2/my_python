import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getarea(self):
        return self.width * self.height

    def diagonal(self):
        return math.hypot(self.width, self.height)

    def perimeter(self):
        return (self.width + self.height) * 2

rec1 = Rectangle(6, 8)
print('面積: ' + str(rec1.getarea()))
print('対角線: ' + str(rec1.diagonal()))
print('外周: ' + str(rec1.perimeter()))