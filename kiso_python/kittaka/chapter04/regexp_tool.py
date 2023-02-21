# regexp_tool.py
import re

while True:
    pattern = input("正規表現(終了時はXXX): ")
    if pattern == "XXX":
        break
    regexp = re.compile(pattern)
    while True:
        target = input("対象文字列(正規表現に戻るYYY):")
        if target == "YYY":
            break
        result = regexp.search(target)
        if result:
            print("○")
        else:
            print("×")
    