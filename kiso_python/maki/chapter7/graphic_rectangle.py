# -*- coding: utf-8 -*-

# graphic_rectangle.py

from rectangle1 import Rectangle

class GraphicRectangle(Rectangle):
    
    def __init__(self, width, height, x, y):
        self.__x = x
        self.__y = y
        super().__init__(width, height)
        
    def get_x(self):
        return self.__x
    
    def set_x(self, x):
        self.__x = x
        
    def get_y(self):
        return self.__y
    
    def set_y(self, y):
        self.__y = y
        
    def distance(self):
        return (self.__x ** 2 + self.__y ** 2) ** 0.5
        
    x = property(get_x, set_x)
    y = property(get_y, set_y)
    
if __name__ == "__main__":
    
    g_rec1 = GraphicRectangle(20, 30, 80, 60)
    
    print("幅: {:.2f} 高さ: {:.2f} X座標: {:.2f} Y座標: {:.2f} 原点からの距離: {:.2f}".format(
            g_rec1.width,  g_rec1.height, g_rec1.x, g_rec1.y, g_rec1.distance()))
    
    