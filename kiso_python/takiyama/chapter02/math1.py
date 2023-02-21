from math import hypot, sqrt, pow

p1 = (3, 7)
p2 = (6, 3)

distance = sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))
print(f"2点間の距離は{distance}")

distance = hypot(p2[0] - p1[0], p2[1] - p1[1])
print(f"2点間の距離は{distance}")