import math
from abc import abstractmethod, ABC

class Figure(ABC):
    @abstractmethod
    def getArea(self):
        pass
    
class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def getArea(self):
        return self.width * self.height

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
    def getArea(self):
        return self.radius ** 2 * math.pi

class Triangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def getArea(self):
        return self.base * self.height / 2

class Trapezoid(Figure):
    def __init__(self, upperbase, lowerbase, height):
        self.upperbase = upperbase
        self.lowerbase = lowerbase
        self.height    = height
    def getArea(self):
        return (self.upperbase + self.lowerbase) * self.height / 2
        

player1 = [Rectangle(10, 20), Triangle(10, 10), Circle(5), Rectangle(5, 10)]
player2 = [Rectangle(20, 15), Triangle(20, 5), Trapezoid(6, 4, 10)]

def calc_total_area(figures):
    total = 0
    for fig in figures:
        total += fig.getArea()
    return total

print("player1 total", calc_total_area(player1))
print("player2 total", calc_total_area(player2))