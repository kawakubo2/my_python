# -*- coding: utf-8 -*-

widths  = [1, 2, 3, 4, 5]
heights = [6, 5, 4, 3, 2]

rect_areas = [width * height for width, height in zip(widths, heights)] 

print(rect_areas)

print('合計面積:{}'.\
      format(sum([width * height for width, height in zip(widths, heights)])))