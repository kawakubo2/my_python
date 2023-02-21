numbers = [78, 88, 90, 82, 80, 69, 95, 83, 91, 85]
"""
((78 - avg) ** 2 + (88 - avg) ** 2 ... (85 - avg) ** 2) / len(numbers)

"""

def variance(nums):
    avg = sum(nums) / len(nums)
    return sum([(n - avg) ** 2 for n in nums]) / len(nums)

var = variance(numbers)

print(f"平均: {sum(numbers) / len(numbers):.1f}")
print(f"分散: {var:.1f}")
print(f"標準偏差: {var ** 0.5:.1f}")
