def mysum(*nums):
    print(type(nums))
    total = 0
    for n in nums:
        total += n
    return total

print(mysum())
print(mysum(1))
print(mysum(1, 2))
print(mysum(1, 2, 3, 4, 5, 6))

print(1, 'abc', True, lambda x: x** 2)
print()
print('xyz')

def average(num, *nums):
    total = num
    for n in nums:
        total += n
    return total / (len(nums) + 1)

print(average(5))
print(average(1, 10, 100))

print('{0}さんの年齢は{1}歳です。'.format('山田', 38))

import re
def printf(format, *args):
    for i in range(len(args)):
        format = re.sub('\\{' + str(i) + '\\}', \
            str(args[i]) if type(args[i]) != str else args[i] , format)
    print(format)

printf('{0}さんの年齢は{1}歳です。{0}さんは私の上司です。', '田中', 43)
