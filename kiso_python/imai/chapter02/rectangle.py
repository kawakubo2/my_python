# -*- coding: utf-8 -*-

class Rectangle:
    # 初期化メソッド, コンストラクタ
    def __init__(self, width, height):
        self.width = width
        self.height = height
      
    def area(self):
        """
        幅と高さから面積を求めるメソッド
        """
        return self.width * self.height
    
    
    def diagonal(self):
        """
        幅と高さから対角線を求めるメソッド
        """
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def circumference(self):
        """
        幅と高さから外周を求めるメソッド
        """
        return (self.width + self.height) * 2
    
help(Rectangle)
rec1 = Rectangle(8, 6)

print("面積:{:.1f}".format(rec1.area()))
print("対角線:{:.1f}".format(rec1.diagonal()))
print("外周:{:.1f}".format(rec1.circumference()))