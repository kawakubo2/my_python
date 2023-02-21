import re

members = [
    "山田太郎,1995-12-23,58,170",
    "横山花子,1989-05-05,52,155",
    "田中一郎,1972-09-23,80,173"
]

s = r"(\w+),((\d{4})-(\d{1,2})-(\d{1,2})),(\d{2,3}),(\d{2,3})";
pattern = re.compile(s)

for member in members:
    print(pattern.sub(r"\6,\7,\1,\3年\4月\5日", member))