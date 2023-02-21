# -*- coding: utf-8 -*-

end = int(input('最後の整数を入力してください : '))

sum = 0
for num in range(1, end + 1):
    sum += num
    
print('{}までの総和: {}'.format(end, sum))


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

sum = 0
for num in nums:
    sum += num
    
print(sum)