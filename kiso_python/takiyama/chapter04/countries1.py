def create_random_list(item_dict):
    import random
    result = []
    for key, value in item_dict.items():
        result += [key] * value # ["イギリス", "イギリス", ...]
    random.shuffle(result)
    return result

answer = create_random_list({"イギリス": 6, "スペイン": 8, "ドイツ": 3, 
                             "フランス": 9, "イタリア": 14})

print(answer)

results = {}
for country in answer:
    if country in results:
        results[country] += 1
    else:
        results[country] = 1
        
for country, num in results.items():
    print(f"{country}: {num}")