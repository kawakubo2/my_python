upperbases = [2, 4, 3, 5, 2, 3]
lowerbases = [5, 4, 3, 2, 3, 4]
heights    = [3, 2, 4, 4, 5, 3]

for upper, lower, height in zip(upperbases, lowerbases, heights):
    print((upper + lower) * height / 2)
    
    