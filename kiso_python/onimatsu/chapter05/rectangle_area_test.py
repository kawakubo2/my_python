# -*- coding: utf-8 -*-

def rectangle_area(width=10, height=10):
    return width * height;

a = 100
b = 200

print("幅が{}cm、高さが{}cmの長方形の面積は{}平方cmです"
      .format(a, b, rectangle_area(a, b)))

print("幅が{}cm、高さが{}cmの長方形の面積は{}平方cmです"
      .format(a, b, 
              rectangle_area(height=b, width=a)))

print("長方形の面積は{}平方cmです"
      .format(rectangle_area()))