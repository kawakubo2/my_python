import math

def even_filter(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

def circle_area(gen):
    for r in gen:
        yield r ** 2 * math.pi

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for n in circle_area(even_filter(numbers)):
    print(n)

even_numbers = []
for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)

circle_area_list = []
for r in even_numbers:
    circle_area_list.append(r ** 2 * math.pi)

print(circle_area_list)