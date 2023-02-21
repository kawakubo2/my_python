end = int(input('最後の数値を入力してください: '))
total = 0
counter = 1
while counter <= end:
    total += counter
    counter += 1

print(str(end) + 'までの総和: ' + str(total))