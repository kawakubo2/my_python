lst = []
lst += ['春']
lst += ['夏', '秋', '冬']
print(lst)

numbers = [1, [2, 3, [4, 5], 6], [7, [8, 9]], 10]

def my_sum(nums):
    total = 0
    for n in nums:
        if type(n) == list:
            total += my_sum(n)
        else:
            total += n
    return total

print('合計 =', my_sum(numbers))

names = ['山田', '横山', '田中', '山田', '山本', '鈴木', '星山', '山田']

name = '山田'

while name in names:
    names.remove(name)

print(names)

import numpy as np

nums = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

npnum = np.array(nums)
print(npnum)

npnum2 = npnum[1:3, 1:3]
print(npnum2)

numbers2 = [1, 2, 3, 4, 5, 6, 7]

numbers3 = numbers2[::-1]
print(numbers3)