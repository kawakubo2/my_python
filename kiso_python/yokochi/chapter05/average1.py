def average(init, *nums):
    sum = init
    for n in nums:
        sum += n
    return sum / (len(nums) + 1)

print(average(10))
print(average(10, 20))
print(average(10, 5, 15, 25, 40))