upper_bases = [2.2, 3.8, 3.9, 2.0, 5.1]
lower_bases = [7.8, 6.2, 6.1, 8.0, 4.9]
heights     = [10, 20, 30, 40, 50]

for upper, lower, height in zip(upper_bases, lower_bases, heights):
    print((upper + lower) * height / 2)

