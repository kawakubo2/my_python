names = ["山田", "井上", "太田", "田中", "山田"]

name = "山田"
while name in names:
    names.remove(name)

print(names)

weekdays = ["日", "月", "火", "水", "木", "金", "土"]
# 元のリストを反転させたくない場合
weekdays2 = weekdays[::-1]
print(weekdays)
print(weekdays2)
# 元のリストを反転させてもいい場合
weekdays.reverse()
print(weekdays)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"合計: {sum(numbers)}")
print(f"平均: {sum(numbers)/len(numbers):.1f}")
print(f"最大: {max(numbers)}")
print(f"最小: {min(numbers)}")

numbers2 = [1, [2, 3, [4, 5], [6,7]], [8, 9, [10]]]

print(type(numbers2))
if type(numbers2) == list:
    print("numbers2はリストである")

def list_sum(nums):
    total = 0
    for n in nums:
        if type(n) == list:
            total += list_sum(n)
        else:
            total += n
    return total

print(f"合計: {list_sum(numbers2)}")

numbers3 = [8, -1, 5, 4, 12, 7, -3, 2, 11]

numbers4 = sorted(numbers3)
print(numbers3)
print(numbers4)

numbers3.sort()
print(numbers3)