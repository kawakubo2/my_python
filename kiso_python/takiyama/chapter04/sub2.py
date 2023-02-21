import re

members = [
    "Taro Yamada,51,78,172",
    "Hanako Sato,32,55,160",
    "Ichiro Suzuki,43,78,179"
]

pattern = re.compile(r"^([a-zA-Z]+ [a-zA-Z]+),(\d{1,3}),(\d{1,3}),(\d{2,3})$")

for member in members:
    print(pattern.sub(r"\3,\4,\1,\2", member))