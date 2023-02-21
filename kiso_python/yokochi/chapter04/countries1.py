import random, time

def create_random_list(dict1):
    result = []
    for key, val in dict1.items():
        result += [key] * val
    random.shuffle(result)
    return result

country_dict = {"イギリス": 100000, "スペイン": 120000, "ドイツ": 180000, "フランス": 200000, "イタリア": 400000}

answer = create_random_list(country_dict)
# print(answer)

start = time.time()
results = {}

for country in answer:
    if country in results:
        results[country] += 1
    else:
        results[country] = 1
end = time.time()
print(f"処理時間: {end - start}")

for country, num in sorted(results.items(), key=lambda item:item[1], reverse=True):
    print(f"{country}: {num}")
