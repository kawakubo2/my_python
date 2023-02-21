times = [-1, 24, 0, 7, 11, 12, 13, 15, 18, 19, 21, 23]
for time in times:
    print(f"\n======< 時刻: {time} >======")
    print("---小さい値から比較する場合---")
    if time < 0 or time > 23:
        print("時刻の範囲を超えています。")
    elif time <= 11:
        print("おはようございます。")
    elif time == 12:
        print("お昼です。")
    elif time <= 18:
        print("こんにちは。")
    else:
        print("こんばんは。")
        
    print("---大きい値から比較する場合---")
    if time < 0 or time > 23:
        print("時刻の範囲を超えています。")
    elif time >= 19:
        print("こんばんは。")
    elif time >= 13:
        print("こんにちは。")
    elif time == 12:
        print("お昼です。")
    else:
        print("おはようございます。")
        
    print("---範囲を指定する方法---")
    if 0 <= time <= 11:
        print("おはようございます。")
    elif time == 12:
        print("お昼です。")
    elif 13 <= time <= 18:
        print("こんにちは。")
    elif 19 <= time <= 23:
        print("こんばんは。")
    else:
        print("時刻の範囲を超えています。")