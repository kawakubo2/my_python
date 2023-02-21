numbers = [1, [2, 3, [4, 5], 6, 7], [8, 9], 10]

# 再帰関数
def array_sum(nums):
    total = 0
    for n in nums:
        if type(n) == list:
            total += array_sum(n)
        else:
            total += n
    return total

print(array_sum(numbers))