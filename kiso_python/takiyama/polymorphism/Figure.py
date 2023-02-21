import math
from abc import abstractmethod, ABC

# ポリモーフィズム(polymorphism)
class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass
    
class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def get_area(self):
        return self.width * self.height
    
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        return self.radius ** 2 * math.pi

class Triangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def get_area(self):
        return self.base * self.height

class Trapezoid(Figure):
    def __init__(self, upperbase, lowerbase, height):
        self.upperbase = upperbase
        self.lowerbase = lowerbase
        self.height = height
        
    def get_area(self):
        return (self.upperbase + self.lowerbase) * self.height / 2

if __name__ == '__main__':
    
    player1 = [ Rectangle(20, 10), Circle(5), Triangle(10, 10), Rectangle(10, 10)]
    player2 = [ Triangle(10, 10), Circle(10), Rectangle(5, 10), Trapezoid(5, 5, 10)]
    
    def calc_total(figures):
        total = 0
        for f in figures:
            if isinstance(f, Figure):
                total += f.get_area()
            else:
                raise TypeError("Figureを継承したクラスではありません。")
        return total
    
    player1Total = calc_total(player1)
    player2Total = calc_total(player2)

    print(f"プレイヤー1: {player1Total}  プレイヤー2: {player2Total}")
    if player1Total > player2Total:
        print("プレイヤー1の勝ち")
    elif player1Total < player2Total:
        print("プレイヤー2の勝ち")
    else:
        print("引き分け")