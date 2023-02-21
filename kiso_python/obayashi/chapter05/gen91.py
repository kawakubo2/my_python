import math

def positive_even_filter(nums):
    for n in nums:
        if n > 0 and n % 2 == 0:
            yield n

numbers = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

for n in positive_even_filter(numbers):
    print(n)

def circle_area(my_filter):
    for n in my_filter:
        yield n ** 2 * math.pi

for area in circle_area(positive_even_filter(numbers)):
    print(area)