# except0.py

while True:
    try:
        score = int(input('点数を入力してください: '))
        if score < 0 or score > 100:
            print('点数は0～100の範囲で入力してください。')
            continue
        break
    except ValueError:
        print('数値の形式に誤りがあります。整数値を入力してください。')