words = ["空", "秘密", "電柱", "ひらけごま", "海", "ギター"]
s = input("文字列を入力してください: ")

try:
    index = words.index(s)
    print(f'"{s}"のインデックスは{index}です')
except ValueError:
    print(f'"{s}"は見つかりませんでした')
    
if s in words:
    index = words.index(s)
    print(f'"{s}"のインデックスは{index}です')