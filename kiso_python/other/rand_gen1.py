import random

def rand_gen(num):
    # 生成済みの乱数を格納するリスト
    randoms = []
    
    while True:
        rand_num = random.randrange(num)
        if rand_num not in randoms:
            randoms.append(rand_num)
            yield rand_num
        elif len(randoms) >= num:
            break;

for n in rand_gen(20):
    print(n)
