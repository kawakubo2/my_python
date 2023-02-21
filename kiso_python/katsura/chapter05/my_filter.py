numbers = [1, 2, 3, 4, -2, 5, 6, 7, -4, 8, 9, 10]

def my_filter(nums):
    for n in nums:
        if n >= 0:
            yield n

def my_filter2(nums):
    result = []
    for n in nums:
        if n >= 0:
            result.append(n)
    return result
            
for n in my_filter(numbers):
    print(n)

def my_map(gen):
    for n in gen:
        yield n ** 2

def my_map2(gen):
    result = []
    for n in gen:
        result.append(n ** 2)
    return result

for n in my_map(my_filter(numbers)):
    print(n)