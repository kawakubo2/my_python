import math

radius = [1, 2, 3, 4, 5]

circle_area = []
for r in radius:
    circle_area.append(r ** 2 * math.pi)

print(circle_area)

circle_area2 = [r ** 2 * math.pi for r in radius]
print(circle_area2)