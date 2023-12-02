week = ["日", "月", "火", "水", "木", "金", "土"]

print(week[::2])
print(week[1::2])

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(numbers[::3])
print(numbers[1::3])
print(numbers[2::3])

list1 = ["A", "B", "C", "D", "E", "F", "G", "H"]
# C, Dを削除して、削除したところをX, Y, Zで置き換えたい
list1[2:4] = ["X", "Y", "Z"]
print(list1)

# C, Dを削除したい
list1 = ["A", "B", "C", "D", "E", "F", "G", "H"]
list1[2:4] = []
print(list1)

list1 = ["A", "B", "C", "D", "E", "F", "G", "H"]
# BとCの間にX, Y, Zを挿入したい
list1[2:2] = ["X", "Y", "Z"]
print(list1)

season1 = ["春"]
season2 = ["夏", "秋", "冬"]
season1[1:1] = season2
print(season1)
