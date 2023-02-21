import math

numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

def positive_even(nums):
    for n in nums:
        if n > 0 and n % 2 == 0:
            yield n

def circle_area(gen1):
    for r in gen1:
        yield math.pow(r, 2) * math.pi


for area in circle_area(positive_even(numbers)):
    print(area)