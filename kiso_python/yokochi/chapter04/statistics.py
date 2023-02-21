# statistics.py

prices = [ 3200, 4300, 2800, 2200, 3800, 2600, 3000, 2900, 3100, 3400]
distance = [ 10, 3, 12, 20, 5, 18, 11, 13, 13, 8]

def avg(nums):
    return sum(nums) / len(nums)

def variant(nums):
    average = avg(nums)
    return sum([(num - average) ** 2 for num in nums]) / len(nums)

def coef(nums1, nums2):
    avg1 = avg(nums1)
    avg2 = avg(nums2)
    return (sum([(num1 - avg1) * (num2 - avg2) for num1, num2 in zip(nums1, nums2)]) / len(nums1)) \
      / (variant(nums1) ** 0.5 * variant(nums2) ** 0.5)

price_distance_coef = coef(prices, distance)
print(f"マンション価格と駅からの徒歩時間(分)の相関係数: {price_distance_coef}")