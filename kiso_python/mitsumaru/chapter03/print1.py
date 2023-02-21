numbers = [3, 1, 9, 8, 5, 7, 2, 4, 6, 10]

total = 0
for num in numbers:
    total += num

print('合計:', total)

numbers = [3, 1, [9, 8, [5, 7], 2], [4, 6], 10]
numbers2 = [
    [
        [ 1, 2, 3],
        [ 4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]

def array_sum(nums):
    total = 0
    for n in nums:
        if (type(n) == int):
            total += n
        else:
            total += array_sum(n)
    return total

print(array_sum(numbers))   