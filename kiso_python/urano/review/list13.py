list13 = [8, 2, 1, 7, 12, 11, 9, 8, 5, 2, 1]

# 3で割ったあまり
# 0、1、2の個数
counter0 = 0
counter1 = 0
counter2 = 0
for n in list13:
    m = n % 3
    if m == 0:
        counter0 += 1
    elif m == 1:
        counter1 += 1
    else:
        counter2 += 1
        
print(f'3で割ったあまりが0の個数は{counter0}')
print(f'3で割ったあまりが1の個数は{counter1}')
print(f'3で割ったあまりが2の個数は{counter2}')
      
