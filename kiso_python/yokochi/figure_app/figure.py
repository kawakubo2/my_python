from abc import ABC, abstractmethod
import math

class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width= width
        self.height = height
        
    def get_area(self):
        return self.width * self.height

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
        
    def get_area(self):
        return math.pow(self.radius, 2) * math.pi

class Triangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def get_area(self):
        return self.base * self.height / 2

class Square(Figure):
    def __init__(self, length):
        self.length = length
        
    def get_area(self):
        return math.pow(self.length, 2)

if __name__ == '__main__':
    
    figures1 = [ Rectangle(25, 8), Circle(5), Triangle(10, 20), 
                 Rectangle(20, 5), Square(5) ]
    figures2 = [ Circle(11), Triangle(10, 10), Rectangle(10, 10) ]
    
    def calc_total(figures):
        total = 0
        for f in figures:
            total += f.get_area()
        return total
    
    player1_area = calc_total(figures1)
    player2_area = calc_total(figures2)

    print(f"プレイヤー1の合計: {player1_area} プレイヤー2の合計: {player2_area}")
    if player1_area > player2_area:
        print("プレイヤー1の勝ち")
    elif player1_area < player2_area:
        print("プレイヤー2の勝ち")
    else:
        print("引き分け")
    