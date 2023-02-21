numbers = [1, 2, 3, 4, 5]

# グローバル変数はsum変数は使用しないこと
# 使用するとsum関数が壊れる
sum = 0

print("合計: " + str(sum(numbers)))