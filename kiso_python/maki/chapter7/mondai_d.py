# -*- coding: utf-8 -*-

from mondai_b import Circle
import math

class NewCircle(Circle):
    def menseki(self):
        return self.radius ** 2 * math.pi
    
    
if __name__ == "__main__":
    c1 = NewCircle(10, "black")
    print("半径: {}, 色: {}, 面積: {:.2f}".format(
            c1.radius, c1.color, c1.menseki()))