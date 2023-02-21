nums = [99, 3, -5, 0, 100, 14, 18, 14]
nums.sort()
print(nums)

nums = [99, 3, -5, 0, 100, 14, 18, 14]
nums.sort(reverse=True)
print(nums)

nums = [99, 3, -5, 0, 100, 14, 18, 14]
nums2 = sorted(nums)
print(nums2)
print(nums)

members = [
    {"name": "山田太郎", "weight": 70, "height": 175},
    {"name": "田中一郎", "weight": 70, "height": 168},
    {"name": "鈴木次郎", "weight": 70, "height": 180},
    {"name": "佐藤勝男", "weight": 70, "height": 172},
]

def bmi(weight, height):
    return weight / (height / 100) ** 2
import pprint
members.sort(key=lambda m: bmi(m['weight'], m['height']))
pprint.pprint(members)