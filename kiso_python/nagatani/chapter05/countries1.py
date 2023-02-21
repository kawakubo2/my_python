import make_random_list

answer = make_random_list.make_random_list({'イギリス':6,'スペイン':8,'ドイツ':3,'フランス':9,'イタリア':14})

results = {}

for country in answer:
    if country in results:
        results[country] += 1
    else:
        results[country] = 1

for country, count in sorted(results.items(), reverse=True, key=lambda n:n[1]):
    print(f"{country}: {count}")

