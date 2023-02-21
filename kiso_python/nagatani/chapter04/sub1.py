import re

members = [
    "Taro Yamada,1988-12-23,180,88",
    "Hanako Yokoyama,2000-02-03,170,72",
    "Ichiro Tanaka,1972-10-23,185,90"
]

"""
名前,生年月日,身長,体重
        ↓
身長,体重,生年月日,名前
"""

pattern = "([a-zA-Z]+ [a-zA-Z]+),(\d{4}-\d{1,2}-\d{1,2}),(\d{2,3}),(\d{2,3})"
regexp = re.compile(pattern)
for member in members:
    print(regexp.sub(r"\3,\4,\2,\1", member))