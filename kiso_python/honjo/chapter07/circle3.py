# -*- coding: utf-8 -*-

from circle2 import Circle

class NewCircle(Circle):
    def __init__(self, radius, color):
        super().__init__(radius, color)
        
    def menseki(self):
        import math
        return self.radius ** 2 * math.pi
    
if __name__ == '__main__':
    c1 = NewCircle(10, 'blue')
    print("半径:{} 色:{} 面積:{}"
          .format(c1.radius, c1.color, c1.menseki()))