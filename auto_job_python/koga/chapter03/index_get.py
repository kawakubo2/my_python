words = ["空", "秘密", "電柱", "ひらけごま", "海", "ギター"]

str = input('文字列: ')

try:
    index = words.index(str)
    print(f"{str}のインデックスは{index}です。")
except ValueError:
    print(f"{str}は見つかりませんでした。")

colors = {'赤': 'red', '緑': 'green', '黄色': 'yellow'}

key = '赤'
print(colors.get(key, 'なし'))
key = '黒'

print(colors.get(key, 'なし'))
