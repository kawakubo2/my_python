# practice_b.py
import sys

try:
    year = int(input('生まれた年を入力してください: '))
except:
    print('数値を入力してください')
else:
    if year >= 2001:
        print('21世紀生まれですね')
    else:
        print('21世紀生まれではありません')