# -*- coding: utf-8 -*-

end = int(input('最後の整数を入力してください:'))

sum = 0

print('---< 解法1 >---')
for num in range(1, end+1):
    if num % 2 == 0:
        sum += num
        
print(str(end) + 'までの偶数の総和:' + str(sum))

print('---< 解法2 >---')
sum = 0

for num in range(0, end+1, 2):
    sum += num
print(str(end) + 'までの偶数の総和:' + str(sum))
    
    
