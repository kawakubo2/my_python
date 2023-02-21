data1 = ['ぱんだ', 'うさぎ', 'こあら', 'とら']
data2 = ['panda', 'rabbit', 'koala', 'tigger']

for d1, d2 in zip(data1, data2):
    print(d1, '=', d2)

upperbases = [1, 2, 3, 4, 5]
lowerbases = [2, 3, 4, 5, 6]
heights    = [3, 4, 5, 6, 7]

def trapezoid(u, l, h):
    if not (len(upperbases) == len(lowerbases) == len(heights)):
        raise Exception('引数の数が不一致')
    return (u + l) * h / 2

try:
    for u, l, h in zip(upperbases,lowerbases,heights):
        print(trapezoid(u, l, h))
except Exception as e:
    print(e)

scores = [
    [10, 20, 30, 40, 50],
    [30, 40, 150, 60, 70],
    [50, 60, 70, 80, 90]
]

for score in scores:
    if any([s < 0 or s > 100 for s in score]):
        print('点数に外れ値が存在する')
        continue
    print(score)
import math
radius = [1, 2, 3, 4, 5]

def get_area(r):
    return r**2*math.pi
# 高階関数(higher order function)
area = map(get_area, radius)
for a in area:
    print(a)