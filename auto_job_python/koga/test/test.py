import math

wod = '日月火水木金土'

for c in wod:
    print(c + '曜日')

wod_list = [c + '曜日' for c in wod]
print(wod_list)

radius = [1, 2, 3, 4, -5, 6, 7, 8];
circle_area = [r ** 2 * math.pi for r in radius if r > 0]
print(circle_area)