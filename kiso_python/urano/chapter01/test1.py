print(10 + 20)
print(10 - 5)
print(3 * 5)
print(12 / 5) # 小数点まで計算する
print(12 // 5) # 小数点を切り捨て計算する
print(12 % 5) # 余りを求める
print(2 ** 3)
print(2 ** 8)

bmi = 46 / (160 / 100) ** 2
print(bmi)

bmi = 88 / (180 / 100) ** 2
print(bmi)

print(2021, 9, 3, sep='/')

print("こんにちは、", "Python")

print("Python" * 5)
print("*" * 20)

DANSU = 5 
for i in range(1, DANSU + 1):
    print(' ' * (DANSU - i), end='')
    print('*' * (i * 2 - 1), end='')
    print(' ' * (DANSU - i))

print(str(2021) + "年")

print("鈴木さんは" + str(23) + "歳です。")

print("西暦" + str(1988 + 32) + "年") 