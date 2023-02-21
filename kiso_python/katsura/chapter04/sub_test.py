import re

members = [
    "Taro Yamada,1990-12-31,87,175",
    "Hanako Yokoyama,1998-07-07,49,154",
    "Ichiro Tanaka,1978-06-23,72,171",
    "Yuko Hoshiyama,1995-04-08,55,165"
]

pattern = r"^([a-zA-Z]+ [a-zA-Z]+),([0-9]{4}-[0-9]{1,2}-[0-9]{1,2}),([0-9]{2,3}),([0-9]{2,3})$"

reg = re.compile(pattern)

for member in members:
    print(reg.sub(r'\3,\4,\1,\2', member))

help(re)
