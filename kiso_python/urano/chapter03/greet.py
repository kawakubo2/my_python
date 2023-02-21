# greet.py
"""
午前( 0-11) ---> おはようございます。
お昼(12   ) ---> お昼です。
午後(13-18) ---> こんにちは。
夜  (19-23)  --> こんばんは。

上記以外は   ---> 時刻の範囲を超えています。 
"""

time = int(input('時刻を入力してください: '))

print('===< ' + str(time) + '時 >===')
print('---< 解法1 >---')
if 0 <= time <= 11:
    print('おはようございます。')
elif time == 12:
    print('お昼です。')
elif 13 <= time <= 18:
    print('こんにちは。')
elif 19 <= time <= 23:
    print('こんばんは。')
else:
    print('時刻の範囲を超えています。')

print('---< 解法2 >---')
if time < 0 or time > 23:
    print('時刻の範囲を超えています。')
elif time <= 11:
    print('おはようございます。')
elif time == 12:
    print('お昼です。')
elif time <= 18:
    print('こんにちは。')
else:
    print('こんばんは。')