# -*- coding: utf-8 -*-

end = int(input('最後の整数を入力してください : '))

sum = 0

for num in range(1, end + 1):
    # print(str(num) + ' ', end='')
    sum += num
    
print('')
print(str(end) + 'までの総和: ', sum)

print(sum[1, 2, 3, 4, 5])