# product

import itertools

# デカルト積
print('テスト1')
for i, n in enumerate(itertools.product(['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'])):
    print("{:3d}:{}".format(i+1, n))

print('テスト2')
for i, n in enumerate(itertools.product(('A', 'B', 'C'),(1, 2, 3),('X', 'Y', 'Z'))):
    print("{:3d}:{}".format(i+1, n))