import math

class Circle:
    def __init__(self, radius, color="white"):
        self.__radius = radius
        self.__color = color
        
    def get_radius(self):
        return self.__radius
    def get_color(self):
        return self.__color

    radius = property(get_radius)
    color = property(get_color)

class NewCircle(Circle):
    def menseki(self):
        return self.radius ** 2 * math.pi
        
    menseki = property(menseki)
    
if __name__ == '__main__':
    c1 = NewCircle(10, "black")
    print(f"半径: {c1.radius}, 色: {c1.color} 面積: {c1.menseki:.2f}")