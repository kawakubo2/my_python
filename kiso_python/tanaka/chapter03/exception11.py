name = input('名前: ')

while True:
    try:
        age = int(input('年齢: '))
        break
    except:
        print('年齢は正の整数値を入力してください。')

print(f"{name}さんの年齢は{age}歳です。")

numbers = [1, 2, 3, 4]

print(numbers[4])


