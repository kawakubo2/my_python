import math

data = [1, 2, 3, 4, 5]

def circle_area(radius):
    return radius ** 2 * math.pi

for area in map(circle_area, data):
    print(area)

areas = list(map(circle_area, data))
print(areas)