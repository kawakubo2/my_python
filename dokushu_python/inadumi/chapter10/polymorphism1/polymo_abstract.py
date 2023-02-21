import math
from abc import abstractmethod, ABC

class Figure(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle class: width={self.width}, height={self.height}"

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * math.pi

    def __str__(self):
        return f"Circle class: radius={self.radius}"

class Triangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return self.base * self.height / 2

    def __str__(self):
        return f"Triangle class: base={self.base}, height={self.height}"

class Trapezoid(Figure):
    def __init__(self, upperbase, lowerbase, height):
        self.upperbase = upperbase
        self.lowerbase = lowerbase
        self.height = height

    def get_area(self):
        return (self.upperbase + self.lowerbase) * self.height / 2

    def __str__(self):
        return f"Trapezoid class: upperbase={self.upperbase}, lowerbase={self.lowerbase}, height={self.height}"

class Diamond(Figure):
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def get_area(self):
        return self.diagonal1 * self.diagonal2 / 2

    def __str__(self):
        return f"Diamond class: diagonal1={self.diagonal1}, diagonal2={self.diagonal2}"

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name}はワンワンなく")

if __name__ == '__main__':
    player1_figures = [Rectangle(20, 5), Triangle(10, 20), Circle(5), Rectangle(10, 10)]
    player2_figures = [Triangle(25, 16), Triangle(10, 10), Triangle(30, 5), 
                       Trapezoid(10, 10, 5), Diamond(10, 8), Dog("ポチ")]

    def get_total_area(figures):
        total = 0
        for figure in figures:
            if isinstance(figure, Figure):
                print(figure)
                total += figure.get_area()
        return total

    player1_total = get_total_area(player1_figures)
    player2_total = get_total_area(player2_figures)

    print(f"プレイヤー1の合計面積: {player1_total}")
    print(f"プレイヤー2の合計面積: {player2_total}")