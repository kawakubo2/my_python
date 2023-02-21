end = int(input('最後の数値を入力してください: '))

total = 0
for num in range(1, end+1):
    total += num

print(str(end) + 'までの総和: ' + str(total))

print(str(end) + 'までの総和: ' + str((1 + end) * (end // 2)))

list1 = list(range(1, 11))
print(list1)

list2 = list(range(0, 101, 10))
print(list2)