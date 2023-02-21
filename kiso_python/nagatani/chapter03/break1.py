words = ['旅行', '桜', 'テレビ',  '岸辺', 'ラジオ']

complete_flag = True
for word in words:
    if word == '終了':
        print('*ループが中断しました')
        complete_flag = False
        break
    print(word)

if complete_flag:
    print('*ループが完了しました。')

for word in words:
    if word == '終了':
        print('*ループが中断しました')
        break
    print(word)
else:
    print('*ループが完了しました。')