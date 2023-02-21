numbers = [ 88, 77, 58, 68, 90, 80, 85, 92, 65, 70, 73, 85, 98, 69 ]
avg = sum(numbers) / len(numbers)

def  variance(nums, avg):
    return sum([(n - avg) ** 2 for n in nums]) / len(nums)

print(f"分散: {variance(numbers, avg)}")
    