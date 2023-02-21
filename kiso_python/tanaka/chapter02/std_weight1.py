"""
bmi = 体重(kg) / (身長(m) * 身長(m))
integer ---> 整数
int
"""
name = input('名前を入力してください: ')
print(name + 'さん、こんにちは！')

age = int(input('年齢を入力してください: '))
print(str(age) + '歳ですね。')

height = float(input('身長(cm)を入力してください: '))
bmi = 22
std_weight = bmi * (height/100) ** 2
print("身長: " + str(height) + "cm → ", end = "")
print("標準体重: " + str(std_weight) + "kg")