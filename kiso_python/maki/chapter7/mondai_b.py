# -*- coding: utf-8 -*-

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
        
if __name__ == "__main__":
    c1 = Circle(10, "black")
    print("半径: {}, 色: {}".format(c1.radius, c1.color))