import re

members = [
    "Taro Yamada,38,178,78,Tokyo",
    "Hanako Yokoyama,24,160,57,Osaka",
    "Ichiro Suzuki,55,178,82,Fukuoka"
]

pattern = r"^([a-zA-Z]+ [a-zA-Z]+),(\d+),(\d{2,3}),(\d{2,3}),([a-zA-Z]+)$"

for member in members:
    # print(re.sub(pattern, r"\g<5>,\g<1>,\g<2>", member))
    print(re.sub(pattern, r"\5,\1,\2", member))