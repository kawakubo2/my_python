import math
from figure import Figure

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return self.radius ** 2 * math.pi

    def __str__(self):
        return "Circle class: radius = {}".format(self.radius)