# regexp_sub.py
import re

"""
名前,生年月日,身長,体重
         ↓
生年月日,体重,身長,名前
"""

members = [
    "Taro Yamada,1992-12-24,170,67",
    "Hanako Yokoyama,2000-01-15,160,52",
    "Ichiro Tanaka,1978-02-23,178,78"
]
pattern = r"^([a-zA-Z]+ [a-zA-Z]+),(\d{4}-\d{1,2}-\d{1,2}),(\d{2,3}),(\d{2,3})$"

for member in members:
    print(re.sub(pattern, r"\2,\4,\3,\1", member))