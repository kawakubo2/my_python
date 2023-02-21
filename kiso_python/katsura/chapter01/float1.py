x = 0.2
y = 0.6

print(x * 3)
# 結合則 四則演算 左結合
if x * 3 * 10 == y * 10:
    print('等しい')
else:
    print('等しくない')

EPSILON = 1.0e-9


if abs(x * 3 - y) < EPSILON:
    print('等しい')
else:
    print('等しくない')