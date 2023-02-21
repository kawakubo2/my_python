import re

p = input('正規表現: ')

pattern = re.compile(p)

while True:
    s = input("対象文字列(終了はq): ")
    if s == "q" or s == "Q":
        break
    results = pattern.finditer(s)
    for result in results:
        print(result.group())