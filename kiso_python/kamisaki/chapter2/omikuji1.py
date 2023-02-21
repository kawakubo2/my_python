import random

kuji = ['大吉', '中吉', '吉', '凶']

# print(kuji[random.randrange(len(kuji))])

for i in range(20):
    print(kuji[i % len(kuji)])
    
lot = 18479871

if lot % 10000 == 9871:
    print('3等10万円です')