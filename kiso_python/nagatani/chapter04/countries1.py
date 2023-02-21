import make_random_list

answer = make_random_list.make_random_list({'イギリス':6,'スペイン':8,'ドイツ':3,'フランス':9,'イタリア':14})

results = {}

for country in answer:
    if country in results:
        results[country] += 1
    else:
        results[country] = 1

for country, count in results.items():
    print(f"{country}: {count}")


def intersect(set1, set2):
    result = set()
    for item in set1:
        if item in set2:
            result.add(item)
    return result

def minus(set1, set2):
    result = set()
    for item in set1:
        if item not in set2:
            result.add(item)
    return result

set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {1, 2, 4, 8, 16, 32}

set3 = intersect(set1, set2)
print(set3)
set4 = minus(set1, set2)
print(set4)