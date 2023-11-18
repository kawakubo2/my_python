season = ["春", "夏", "秋", "冬"]

print("--- iter(イテレータを使用した取り出し方) ---")
itr = iter(season)
while True:
    try:
       print(next(itr))
    except StopIteration:
        break

# 糖衣構文(Syntax Sugar)
print("--- iterを使わずに取り出す(内部ではiterが使用されている) ---")
for s in season:
    print(s)