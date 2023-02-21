def positive_gen(nums):
    for n in nums:
        if n > 0:
            yield n

def circle_area(gen):
    import math
    for radius in gen:
        yield radius ** 2 * math.pi

numbers = [3, 1, 2, 0, 4, -2, 1, 2, 10, 3, 4, 3, 4]

# gen = positive_gen(numbers)
# try:
#     print(next(gen))
#     print(next(gen))
# except StopIteration:
#     pass

# シンタックスシュガー(糖衣構文)
for n in circle_area(positive_gen(numbers)):
    print(n)