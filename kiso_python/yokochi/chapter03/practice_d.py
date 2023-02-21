import sys

try:
    age = int(input('年齢を入力してください: '))
except ValueError:
    print('年齢は整数で入力してください。')
    sys.exit()

if age <= 0:
    print('年齢は正の整数です')
elif age < 13:
    print('子供料金です')
else:
    print('大人料金です')