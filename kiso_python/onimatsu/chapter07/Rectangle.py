# -*- coding: utf-8 -*-

class Rectangle:
    """
    長方形を表すクラス
    x座標、y座業、幅、高さを持つ長方形クラス
    面積、対角線の長さ、原点から距離を求めることができる
    """
    def __init__(self, x, y, width, height):
        self.set_x(x)
        self.set_y(y)
        self.set_width(width)
        self.set_height(height)
        
    def get_x(self):
        return self.__x
    
    def set_x(self, x):
        self.__x = x
        
    def get_y(self):
        return self.__y
    
    def set_y(self, y):
        self.__y = y
        
    def get_width(self):
        return self.__width
    
    def set_width(self, width):
        if width <= 0:
            raise ValueError("幅が0以下")
        self.__width = width
        
    def get_height(self):
        return self.__height
    
    def set_height(self, height):
        if height <= 0:
            raise ValueError("高さが0以下")
        self.__height = height
        
    x = property(get_x, set_x)
    y = property(get_y, set_y)
    width = property(get_width, set_width)
    height = property(get_height, set_height)
        
    def area(self):
        """
        幅(width)と高さ(height)から面積を求め、その値を返すメソッド
        """
        return self.width * self.height
    
    def diagonal(self):
        """
        幅(width)と高さ(height)から対角線の長さを求め、その値を返すメソッド
        """
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def distance(self):
        """
        長方形の左上隅の座標(x, y)の原点からの距離を求め、その値を返すメソッド
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5

import sys
    
try:
    rec1 = Rectangle(6, 8, 3, 4)
    print('面積:{:.1f}'.format(rec1.area()))
    print('対角線の長さ:{:.1f}'.format(rec1.diagonal()))
    print('原点からの距離:{:.1f}'.format(rec1.distance()))
    
    rec1.background_color = 'yellow'
    
    print('背景色:{}'.format(rec1.background_color))
    
    rec1.width = 8
    rec1.height = 12
    print('面積:{:.1f}'.format(rec1.area()))
    print('対角線の長さ:{:.1f}'.format(rec1.diagonal()))
    print('原点からの距離:{:.1f}'.format(rec1.distance()))
except ValueError as ve:
    print(ve)
    sys.exit(-1)

   
    