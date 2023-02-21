# -*- coding: utf-8 -*-

from . import figure

def get_area():
    print(f'三角形の面積: {figure.get_triangle_area(8, 5)}')
    print(f'円の面積: {figure.get_circle_area(5)}')