# Trapezoid

upperbases = [5, 3, 4, 3, 6, 2]
lowerbases = [4, 2, 8, 6, 7, 5]
heights    = [3, 8, 7, 8, 5, 4]

for upper, lower, height in zip(upperbases, lowerbases, heights):
    print((upper + lower) * height / 2)