answer = ['イタリア', 'イギリス', 'イタリア', 'フランス', 'フランス', 'イタリア', 
         'フランス', 'イギリス', 'イギリス', 'ドイツ', 'イタリア', 'イタリア', 
         'ドイツ', 'イタリア', 'フランス', 'イタリア', 'イタリア', 'イタリア', 
         'フランス', 'スペイン', 'ドイツ', 'スペイン', 'イタリア', 'スペイン', 
         'スペイン', 'スペイン', 'スペイン', 'フランス', 'フランス', 'フランス', 
         'イギリス', 'イタリア', 'イタリア', 'イタリア', 'フランス', 'イタリア', 
         'スペイン', 'イギリス', 'スペイン', 'イギリス']

results = {}

for country in answer:
    if country in results:
        results[country] += 1
    else:
        results[country] = 1

for country, num in sorted(results.items(), key=lambda c: c[1], reverse=True):
    print('{}: {}'.format(country, num))