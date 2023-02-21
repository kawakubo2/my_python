import random, math

"""
num = 100
minus_1_counter = 0
plus_1_counter = 0
for _ in range(10000):
    x = -1 + (random.randrange(0, num * 2 + 1) / num)
    if x < -1 or x > 1:
        print('不正な値が発生')
        break
    if x == -1:
        minus_1_counter += 1
    if x == 1:
        plus_1_counter += 1

print(f"-1の発生回数: {minus_1_counter}")
print(f"+1の発生回数: {plus_1_counter}")
"""

# 乱数を発生させる回数
def calc_circle_area_with_probability(radius, num):
    square_area = (radius * 2) * 2
    circle_counter = 0
    for _ in range(num):
        x = -1 + (random.randrange(0, num * 2 + 1) / num)
        y = -1 + (random.randrange(0, num * 2 + 1) / num)
        if (x ** 2 + y ** 2) <= radius ** 2:
            circle_counter += 1
    return square_area * (circle_counter / num)

num = 10000
for _ in range(6):
    area = calc_circle_area_with_probability(1, num)
    print(f"円の面積: {area}")
    num *= 4