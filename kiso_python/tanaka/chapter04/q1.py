fruits = ["バナナ", "リンゴ", "オレンジ", "リンゴ", "イチゴ", "バナナ", "バナナ"]

counter = {}
for f in fruits:
    if f in counter:
        counter[f] = counter[f] + 1
    else:
        counter[f] = 1
        
"""
{ "バナナ" : 3, "リンゴ": 2, "オレンジ": 1, "イチゴ": 1 }
"""

for fruit, count in counter.items():
    print(f"{fruit}: {count}")

amap = {}
amap["バナナ"] = 1
print(amap)