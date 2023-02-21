import random, math

NUM = 100_000_000
count = 0

for _ in range(NUM):
    x = random.random()
    y = random.random()
    if math.hypot(x, y) <= 1:
        count += 1
        
area = count / NUM * 4
print(area)