import os

filepath = os.path.join(os.path.dirname(__file__), 'answer')

def create_random_list(item_dict):
    import random
    result = []
    for key, value in item_dict.items():
        result += [key] * value # ["イギリス", "イギリス", ...]
    random.shuffle(result)
    return result

answer = create_random_list({"イギリス": 6, "スペイン": 8, "ドイツ": 3, 
                             "フランス": 9, "イタリア": 14})

with open(filepath, "w", encoding="utf_8") as outf:
    outf.writelines([country + "\n" for country in answer])

results = {}
with open(filepath, "r", encoding="utf_8") as inf:
    for country in inf:
        country = country.rstrip("\n")
        if country in results:
            results[country] += 1
        else:
            results[country] = 1
        
for country, num in sorted(results.items(), key=lambda c: c[1], reverse=True):
    print(f"{country}: {num}")