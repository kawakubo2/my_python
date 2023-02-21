# -*- coding: utf-8 -*-

height = [180, 165, 159, 171, 155]

print(height[0]) # インデックス, 添え字
print(height[1])
print(height[2])
print(height[3])
print(height[4])

print(height[-1])
print(height[-2])
print(height[-3])
print(height[-4])
print(height[-5])

print(len(height))

print(height[len(height) - 1])
print(height[len(height) - 2])
print(height[len(height) - 3])
print(height[len(height) - 4])
print(height[len(height) - 5])

height[0] = 179
print(height)

height.append(162)
print(height)
