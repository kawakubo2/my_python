import re

s1 = "井上花子:21:東京"

s2 = re.sub(r"(\d+):(\w+)", r"\2:\1", s1)
print(s2)

result = re.sub(r"<div>(.+)</div>", r"<p>\1</p>", "<div>Pythonは1991年生まれの言語です。</div>")
print(result)

name = "佐藤 チャーリー"

name2 = re.sub(r"(\w+) (\w+)", r"\2・\1は私のペンネームです。", name)
print(name2)

