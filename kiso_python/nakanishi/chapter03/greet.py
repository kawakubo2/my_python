for hour in range(-1, 25): # -1から24までの整数値を生成
    print(f"------< {hour}時 >------")
    print("===[範囲を指定する方法]===")
    if hour >= 0 and hour <= 11:
        print("おはようございます。")
    elif hour == 12:
        print("お昼です")
    elif hour >= 13 and hour <= 18:
        print("こんにちは")
    elif hour >= 19 and hour <= 23:
        print("こんばんは")
    else:
        print("時刻の範囲を超えています。")

    print("\n===[小さい順に並べる方法]===")
    if hour < 0 or hour > 23:
        print("時刻の範囲を超えています。")
    elif hour <= 11:
        print("おはようございます。")
    elif hour == 12:
        print("お昼です。")
    elif hour <= 18:
        print("こんにちは。")
    else:
        print("こんばんは。")

    print("\n===[in演算子を使用する方法]===")
    if hour in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11): 
        print("おはようございます。")
    elif hour == 12:
        print("お昼です。")
    elif hour in (13, 14, 15, 16, 17, 18):
        print("こんにちは。")
    elif hour in (19, 20, 21, 22, 23):
        print("こんばんは。")
    else:
        print("時刻の範囲を超えています。")
    
    