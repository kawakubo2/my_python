import random

name = ["山", "川", "池", "田", "鈴", "佐", "加", "大", "中", "小", "黒", "赤",
         "白", "青", "坂", "野", "町", "村", "丘", "岡", "塚", "金", "古", "近",
         "辺", "遠", "岩", "石", "木", "沼", "海", "天", "犬", "東", "西", "南", "北"]

def get_last_name(name):
    while True:
        n1 = name[random.randrange(0, len(name))]
        n2 = name[random.randrange(0, len(name))]
        if n1 == n2: continue
        return n1 + n2

for i in range(20):
    print(get_last_name(name))
    
