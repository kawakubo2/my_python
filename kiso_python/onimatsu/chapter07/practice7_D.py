# -*- coding: utf-8 -*-

import math

from practice7_B import Circle
    
class NewCircle(Circle):
    def menseki(self):
        return math.pow(self.radius, 2) * math.pi 
    
    menseki = property(menseki)
     
if __name__ == '__main__':
    c1 = NewCircle(10, 'black')
    print('半径:{} 色:{} 面積:{}'.format\
          (c1.radius, c1.color, c1.menseki))