import re

# Taro Yamada,28,78,172 ---> 78,172,Taro Yamada,28
pattern = r"^([a-zA-Z]+ [a-zA-Z]+),(\d{1,3}),(\d{2,3}),(\d{2,3})$"
reg = re.compile(pattern)
members = [
    "Taro Yamada,28,78,172",
    "Ichiro Tanaka,52,82,178",
    "Hanako Yokoyama,33,60,158"
]

for member in members:
    print(reg.sub(r"\3,\4,\1,\2", member))
