import random, math

COUNT = 10_000_000
NUM = 1_000_000
counter = 0
for i in range(COUNT):
    x = random.randrange(NUM) / NUM
    y = random.randrange(NUM) / NUM
    d = math.hypot(x, y)
    if d <= 1:
        counter += 1
        
area = counter / COUNT * 4
print(area)
    
