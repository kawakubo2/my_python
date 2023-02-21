end = int(input("正の整数を入力してください: "))

total = 0
counter = 0
while counter <= end:
    total += counter
    counter += 1
    
print(f"1～{end}までの総和: {total}")