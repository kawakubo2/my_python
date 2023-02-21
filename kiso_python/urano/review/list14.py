list13 = [8, 2, 1, 7, 12, 11, 9, 8, 5, 2, 1]

# 3で割ったあまり
# 0、1、2の合計：ｗ

total = {0: 0, 1: 0, 2: 0}
for n in list13:
    m = n % 3
    total[m] += n
    
for m, t in total.items():
    print(f"3で割ったあまりが{m}の合計は{t}")
