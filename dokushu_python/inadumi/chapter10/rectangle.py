import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_diagonal(self):
        return math.hypot(self.width, self.height)

    def get_perimeter(self):
        return (self.width + self.height) * 2

print(f'__name__={__name__}')
if __name__ == '__main__':
    rec = Rectangle(8, 6)
    print('長方形の面積: {}'.format(rec.get_area()))
    print('長方形の対角線: {}'.format(rec.get_diagonal()))
    print('長方形の外周: {}'.format(rec.get_perimeter()))