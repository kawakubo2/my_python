i = 1
sum = 0
while i <= 100:
    i += 1
    if i % 2 != 0:
        continue
    sum += i

print('1～100までの偶数の合計:{}'.format(sum))
