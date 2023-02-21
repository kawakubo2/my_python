"""
3の倍数、Fizz
5の倍数、Buzz
3の倍数かつ5の倍数、FizzBuzz
上記以外はそのまま数字を表示する
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
"""
for i in range(1, 31): # 1～30までの整数が発生する
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)