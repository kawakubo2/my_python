# hour = int(input('0から23の整数を入力してください'))

for hour in range(-1, 25):
    print('===< ' + str(hour) + '時 >===')
    print('---< 小さい順に並べる >---')
    if hour < 0 or hour > 23:
        print('時刻の範囲を超えています。')
    elif hour <= 11:
        print('おはようございます。')
    elif hour == 12:
        print('お昼です。')
    elif hour <= 18:
        print('こんにちは。')
    else:
        print('こんばんは。')

    print('---< 大きい順に並べる >---')
    if hour < 0 or hour > 23:
        print('時刻の範囲を超えています。')
    elif hour >= 19:
        print('こんばんは。')
    elif hour >= 13:
        print('こんにちは。')
    elif hour == 12:
        print('お昼です。')
    else:
        print('おはようございます。')

    print('---< 範囲を指定する >---')
    if  0 <= hour <= 11:
        print('おはようございます。')
    elif hour == 12:
        print('お昼です。')
    elif 13 <= hour <= 18:
        print('こんにちは。')
    elif 19 <= hour <= 23:
        print('こんばんは。')
    else:
        print('時刻の範囲を超えています。')
