import random

kuji = ['大吉', '中吉', '凶', '大凶']
print("要素数: " + str(len(kuji)))
print("乱数: " + str(random.randrange(len(kuji))))
print(kuji[random.randrange(len(kuji))])

for i in range(100):
    r = random.randrange(len(kuji))
    if 0 <= r < len(kuji):
        print(r)
    else:
        print('?????????')
        break