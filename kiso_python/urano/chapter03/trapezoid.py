# trapezoid.py

upperbases = [2.4, 3.6, 2.0, 4.3, 1.7]
lowerbases = [3.6, 2.4, 5.0, 2.7, 5.3]
heights    = [3.0, 4.0, 3.0, 2.0, 3.0]

for u, l, h in zip(upperbases, lowerbases, heights):
    print((u + l) * h / 2)