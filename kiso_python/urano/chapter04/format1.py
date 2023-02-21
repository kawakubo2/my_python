# format1.py

name = '山田太郎'
age = 28
weight = 70
height = 178

print(name + 'さんの年齢は' + str(age) + '歳で、BMI値は' + str(weight / (height / 100) ** 2) + 'です。')
print("{}さんの年齢は{}歳で、BMI値は{:.1f}です。".format(name, age, weight / (height / 100) ** 2))

name1 = '田中'
name2 = '鈴木'

print("{1}さん、私は{0}です。・・・あれ？{1}さんですよね？".format(name1, name2))