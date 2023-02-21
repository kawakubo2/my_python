season = ["春", "夏", "秋", "冬"]

itr = iter(season)

try:
    while True:
        print(next(itr))
except StopIteration:
    pass

# 難しい！！
# 糖衣構文(Syntax Sugar)
for s in season:
    print(s)
