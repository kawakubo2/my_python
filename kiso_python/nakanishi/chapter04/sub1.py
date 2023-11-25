import re

members = [
    "Taro Yamada,39,170,83,Osaka",
    "Hanako Yokoyama,29,159,58,Nagoya",
    "Ichiro Tanaka,55,179,84,Fukuoka",
    "Kumiko Yamamoto,33,162,62,Tokyo"
]

for m in members:
    print(re.sub("^([a-zA-Z]+ [a-zA-Z]+),(\d{2,3}),(\d{2,3}),(\d{2,3}),([a-zA-Z]+)$", r"\5,\1,\2", m))
