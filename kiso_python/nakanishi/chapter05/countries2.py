countries = [
     'スペイン', 'イギリス', 'イギリス', 'フランス', 'イタリア', 'イタリア', 
     'スペイン', 'イギリス', 'ドイツ', 'イタリア', 'イタリア', 'イタリア', 
     'スペイン', 'イタリア', 'イタリア', 'スペイン', 'イギリス', 'ドイツ', 
     'スペイン', 'イタリア', 'フランス', 'フランス', 'イタリア', 'イタリア', 
     'スペイン', 'フランス', 'スペイン', 'イタリア', 'スペイン', 'ドイツ', 
     'イタリア', 'イタリア', 'フランス', 'フランス', 'フランス', 'フランス', 
     'イギリス', 'イタリア', 'フランス', 'イギリス', 'ルクセンブルク'
]

max_str_length = max([len(country) for country in countries])
result = {}

for c in countries:
    if c in result:
        result[c] += 1 # result[c] = result[c] + 1
    else:
        result[c] = 1 # result[c] = 1 ---> { "スペイン": 1 }

# { "スペイン": 2, "イギリス": 3, "フランス": 1, "イタリア": 2}
        
for index, (country, num) in enumerate(sorted(result.items(), key=lambda c: c[1], reverse=True)):
    print(f"{index + 1}.{country}{'　' * (max_str_length - len(country))}: {num:3d}")