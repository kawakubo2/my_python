words = ['旅行', '桜', 'NG', 'テレビ', '岸辺', 'NG', 'ラジオ']

for word in words:
    if word == 'NG':
        continue
    print(word)
for word in words:
    if word != 'NG':
        print(word)