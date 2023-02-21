# -*- coding: utf-8 -*-

end = int(input('最後の整数を入力してください : '))
while end <= 0:
    print("1以上の整数値を入力してください")
    end = int(input('最後の整数を入力してください : '))

sum = 0
counter = 1
while counter <= end:
    sum += counter
    counter += 1

print(str(end) + "までの総和:", sum)
