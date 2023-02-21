end = int(input('最後の数値を入力してください: '))
total = 0
counter = 0
while counter <= end:
    total = total + counter # total += counter
    counter += 1
    
print(str(end) + "までの総和: ", total)

print(sum([1, 2, 3]))