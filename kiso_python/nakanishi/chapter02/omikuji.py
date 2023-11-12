import random
kuji = ["大吉", "中吉", "凶"]

print(kuji[random.randrange(len(kuji))])
print(random.choice(kuji))

"""
print(kuji[random.randrange(len(kuji))])
print(kuji[random.randrange(3)])
print(kuji[0])またはprint(kuji[1])またはprint(kuji[2])
"""