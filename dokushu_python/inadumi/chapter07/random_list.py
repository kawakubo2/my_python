import random

countries = {"イタリア": 13, "イギリス": 10, "ドイツ": 8, "スペイン": 7, "フランス": 4}

def random_list(dic):
    result = []
    for key, num in dic.items():
        result += [key] * num
    random.shuffle(result)
    return result

random_countries = random_list(countries)
print(random_countries)

fav_countries = {}
for country in random_countries:
    if country in fav_countries:
        fav_countries[country] += 1
    else:
        fav_countries[country] = 1

for country, num in sorted(fav_countries.items(), key=lambda c: c[1], reverse=True):
    print(f"{country}: {num}")