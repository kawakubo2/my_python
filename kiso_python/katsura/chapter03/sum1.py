end = int(input('最後の数値を入力してください'))

total = 0
for num in range(1, end + 1):
    total += num

print(f"{end}までの総和: {total}")
