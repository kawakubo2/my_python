def filter(test, nums):
    for n in nums:
        if test(n):
            yield n
            
def map(func, gen):
    for n in gen:
        yield func(n)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

import math
for circle_area in map(lambda r: r ** 2 * math.pi, filter(lambda n: n % 2 != 0, numbers)):
    print(circle_area)