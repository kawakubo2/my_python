word_list = [
    ['あ', 'い', '終了', 'う', 'え', 'お'],
    [1, 2, 3, 4, '終了', 5, 6, 7, 8],
    ['田中', '山田', '終了', '山本', '横山']
]


for words in word_list:
    for word in words:
        if word == '終了':
            break
        print(word)
    print()