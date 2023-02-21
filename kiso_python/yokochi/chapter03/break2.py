secret = "foo"

while True:
    word = input('秘密の言葉を入力してください: ')
    if word == "foo":
        print('--正解です---')
        break
    else:
        print('--正しくありません--')


total = 0
count = 0
for n in range(1001):
    count += 1
    total += n
    if (total > 1000):
        break

print(f"{count}回目で1000を超えました。値: {total}")