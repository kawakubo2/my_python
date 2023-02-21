def average(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum / len(nums)

# 引数の数が変えられる
print(average(1, 10, 100))
print(average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(average(1.2, 2.3, 3.4, 4.5))