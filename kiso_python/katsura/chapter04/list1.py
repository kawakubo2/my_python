numbers = [1, [2, 3, [4, 5], 6], [7, [8, 9], 10]]
print(numbers[0])
print(numbers[1][0])
print(numbers[1][1])
print(numbers[1][2][0])
print(numbers[1][2][1])
print(numbers[2][0])
print(numbers[2][1][0])
print(numbers[2][1][1])
print(numbers[2][2])

# 再帰関数(recursive function)
def list_sum(nums):
    total = 0
    for n in nums:
        if type(n) == list:
            total += list_sum(n)
        else:
            total += n
    return total

print(list_sum(numbers))