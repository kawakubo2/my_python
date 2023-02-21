def average(*nums):
    if len(nums) == 0:
        raise Exception('引数なし')
    sum = 0
    for n in nums:
        sum += n
    return sum / len(nums)

print(average(1, 10, 100))

try:
    average()
except Exception as e:
    print(e)