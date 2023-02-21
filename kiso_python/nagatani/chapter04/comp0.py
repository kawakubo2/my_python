import math

day_of_week = [w + '曜日' for w in "日月火水木金土"]
print(day_of_week)

day_of_week2 = []
for w in "日月火水木金土":
    day_of_week2.append(w + "曜日")

print(day_of_week2)

nums = [-3, 4, 2, 1, 5, 7, 6, 4]

circle_area_list = []

for n in nums:
    if n > 0 and n % 2 == 0:
        circle_area_list.append(n ** 2 * math.pi)

print(circle_area_list)

circle_area_list2 = [r ** 2 * math.pi for r in nums if r > 0 and r % 2 == 0]
print(circle_area_list2)

scores = [77, 68, 90, 82, 80, 78, 92, 55, 65, 70, 72 ]
avg = sum(scores) / len(scores)

def variant(nums):
    avg = sum(nums) / len(nums)
    return sum([(n - avg) ** 2 for n in nums]) / len(nums)

v1 = variant(scores)
print(f"分散: {v1}")
print(f"標準偏差: {v1 ** 0.5}")

price = [3200, 3800, 4000, 2800, 5000, 4200, 2900, 3500, 3000, 4300]
distance = [10, 12, 8, 15, 5, 8, 20, 14, 8,  6]

avg1 = sum(price) / len(price)
avg2 = sum(distance) / len(distance)

temp = sum([(avg1 - p)*(avg2 - d) for p, d in zip(price, distance)]) / len(price)
coef = temp / (variant(price) ** 0.5 * variant(distance) ** 0.5)
print(coef)


