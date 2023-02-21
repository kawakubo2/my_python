import random, time

def create_random_list(dict1):
    result = []
    for key, val in dict1.items():
        result += [key] * val
    random.shuffle(result)
    return result

country_dict = {"イギリス": 6, "スペイン": 8, "ドイツ": 3, "フランス": 9, "イタリア": 14}

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


def myfilter(filter, nums):
    for n in nums:
        if filter(n):
            yield n

def mymap(func, gen):
    for n in gen:
        yield func(n)

radius = [1, 2, 3, 4, 5, 6, 7, 8]

import math
circle_area_list = list(mymap(lambda r: r ** 2 * math.pi, myfilter(lambda n: n % 2 == 0, radius)))
print(circle_area_list)

circle_area_list2 = [r ** 2 * math.pi for r in radius if r % 2 == 0]
print(circle_area_list2)