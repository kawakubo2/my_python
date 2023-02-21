
for time in range(-1, 25):
    print('---< ', time , '時 >---')
    print('--- 解法1 ---')
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

    print('--- 解法2 ---')
    if time < 0 or time > 23:
        print('時刻の範囲を超えています。')
    elif time >= 19:
        print('こんばんは。')
    elif time >= 13:
        print('こんにちは。')
    elif time == 12:
        print('お昼です。')
    else:
        print('おはようございます。')

    print('--- 解法3 ---')
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