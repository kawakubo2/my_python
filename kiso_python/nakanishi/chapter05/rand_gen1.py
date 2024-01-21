import random
import time

def random_gen(num):
    randoms = set() 
    while True:
        rand_num = random.randrange(num)
        if rand_num not in randoms:
            randoms.add(rand_num)
            yield rand_num
        elif len(randoms) == num:
            break

num = 1_000_000        
start = time.time()
gen = random_gen(num)
end = time.time()
randoms1 = set([n for n in range(num)]) # 検証用のset
randoms2 = set([n for n in gen]) # ジェネレータ関数で作ったset
randoms3 = randoms2 - randoms1 # 差集合を求めたら空集合になるはず
print(f"処理時間: {end - start}")
# print(randoms2)
print(f"件数: {len(randoms2)}")
print(f"0～{num - 1}までのセットとの差を求める: {randoms3}")
   