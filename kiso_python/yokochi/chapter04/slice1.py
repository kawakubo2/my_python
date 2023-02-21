num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six']

print(num[2:5]) # [開始:終了]
print(num[::2])
print(num[-1::-1])

# 要素の置換
num[2:5] = ["a", "b", "c", "d"]
print(num)

# 要素の追加
num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six']
num[2:2] = ["x", "y", "z"]
print(num)

# 要素の削除
num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six']
num[2:5] = []
print(num)

num2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(num2[::3])
print(num2[1::3])
print(num2[2::3])
