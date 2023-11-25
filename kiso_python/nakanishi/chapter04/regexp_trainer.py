import re

while True:
    pattern = input("正規表現(終了時はxxx): ")
    if pattern == "xxx":
        break
    while True:
        target = input("対象文字列(次の正規表現yyy): ")
        if target == "yyy":
            break
        m = re.search(pattern, target)
        if m:
            print("○")
        else:
            print("×")