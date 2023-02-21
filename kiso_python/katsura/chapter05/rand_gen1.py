import random, time

def random_gen(num):
    randoms = set()
    while True:
        rand_num = random.randrange(num)
        if rand_num not in randoms:
            randoms.add(rand_num)
            yield rand_num
        elif len(randoms) == num:
            break
        
num = 10000
start = time.time()
gen = random_gen(num)
for n in gen:
    pass
    # print(n)
end = time.time()
print(f'処理件数: {num}, 処理時間: {end - start}')