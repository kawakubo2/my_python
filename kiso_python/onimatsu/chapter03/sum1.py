# -*- coding: utf-8 -*-

end = int(input('最後の数値を入力してください: '))


sum = 0
for num in range(1, end + 1):
    sum += num
    
print(str(end) + 'までの総和: ', sum)

print('1から100までに存在する3の倍数の合計を計算')

sum = 0
for num in range(3, 101, 3):
    sum += num
    
print('答え=', sum)