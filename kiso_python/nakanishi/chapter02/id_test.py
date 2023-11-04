def first_value(nums):
    result = []
    for n in nums:
        result.append(n)
    result[0] *= 2
    return result

numbers = [1, 2, 3]
numbers2 = first_value(numbers);
print(numbers)
print(id(numbers))
print(numbers2)
print(id(numbers2))

