# -*- coding: utf-8 -*-

# trapezoid.py

upperbases = [ 2.2343, 5.8671, 3.1777, 6.7319, 3.716695]
lowerbases = [ 5.23555, 4.8771, 2.598284, 4.179523, 2.1874]
heights    = [ 3.57194, 3.7749, 4.0713, 3.9891, 4.00731]

for u, l, h in zip(upperbases, lowerbases, heights):
    print('{:.2f}'.format((u + h) * h / 2))