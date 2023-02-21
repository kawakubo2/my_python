secret = 'foo'

while True:
    word = input('秘密の言葉を入力して下さい: ')
    if word == secret:
        print('--正解です--')
        break
    else:
        print('--正しくありません--')