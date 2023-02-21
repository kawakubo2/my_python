# -*- coding: utf-8 -*-

import math
from mondai_c import Circle

class NewCircle(Circle):
    
    def get_menseki(self):
        return self.radius ** 2 * math.pi
    
    menseki = property(get_menseki)
    
if __name__ == '__main__':
    c1 = NewCircle(10, 'black')
    
    print('半径: {}, 色: {}, 面積: {:.2f}'.format(c1.radius, c1.color,
          c1.menseki))
        