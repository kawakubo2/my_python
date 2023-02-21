import math
from functools import reduce

numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

area_total = reduce(lambda result, area: result + area, map(lambda r: r ** 2 * math.pi, filter(lambda n: n > 0 and n % 2 == 0, numbers)))

print('円の面積の合計:{}'.format(area_total))

print('---< listの内包表記 >---')
area_total2 = sum([r ** 2 * math.pi for r in numbers if r > 0 and r % 2 == 0])

print('円の面積の合計:{}'.format(area_total2))