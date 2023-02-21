# -*- coding: utf-8 -*-

import rectangle

r1 = rectangle.Rectangle(5.2, 7.31, 50.24, 79.88)
print("面積:{}".format(r1.area()))
print("外周:{}".format(r1.circumference()))
print("原点からの距離:{}".format(r1.distance()))