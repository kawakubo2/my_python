words = ["空", "秘密", "電柱", "ひらけごま", "海", "ギター"]

str = input("文字列を入力してください: ")

# 例外処理
try:
    index = words.index(str)
    # print(f'"{str}"のインデックスは{index}です。')
    print('"' + str + '"のインデックスは' + str(index) + 'です。')
except ValueError:
    print(f'"{str}"は見つかりません。')