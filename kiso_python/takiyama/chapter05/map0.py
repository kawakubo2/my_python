import math

def my_map(func, it):
    for item in it:
        yield(func(item))

numbers = [1, 2, 3, 4, 5]

for s in my_map(math.sqrt, numbers):
    print(s)
    