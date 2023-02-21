end = int(input('最後の数値を入力してください: '))

sum = 0
for num in range(1, end + 1):
    sum += num # sum = sum + num

print(str(end) + "までの総和: " + str(sum))

nums = [1, 5, 8, 12, 7, 2, 4]

sum = 0
for n in nums:
    sum += n
print('合計=' + str(sum))