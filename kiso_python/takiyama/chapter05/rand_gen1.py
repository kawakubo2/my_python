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
        
n = 100_000

start = time.time()
gen = random_gen(n)
for num in gen:
    pass
end = time.time()
print(f"処理時間: {end - start}")