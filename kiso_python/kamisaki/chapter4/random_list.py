import random, time

def random_list(dic):
    result = []
    for key, num in dic.items():
        result += [key] * num
    random.shuffle(result)
    return result

countries = random_list({"イギリス": 151638, "スペイン": 38988, "ドイツ": 27933, "フランス": 94233, "イタリア": 143239})

# print(countries)

start = time.time()

results = {}

for country in countries:
    if country in results:
        results[country] += 1 # results[country] = results[country] + 1
    else:
        results[country] = 1

end = time.time()

for country, num in results.items():
    print(f"{country}: {num}")

print(f"処理時間: {end - start}")