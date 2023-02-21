import random

kuji = ['大吉', '中吉', '凶']

random.seed(123)
print(kuji[random.randrange(len(kuji))])

random.seed(456)
print(random.choice(kuji))

help(random)
