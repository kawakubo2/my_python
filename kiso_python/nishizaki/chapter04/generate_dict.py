import random

answer = ['イタリア', 'スペイン', 'イタリア', 'イタリア', 'イタリア', 'フランス', 
          'フランス', 'イタリア', 'フランス', 'イギリス', 'イタリア', 'イタリア', 
          'スペイン', 'ドイツ', 'イタリア', 'イギリス', 'フランス', 'スペイン', 
          'イギリス', 'イタリア', 'スペイン', 'スペイン', 'フランス', 'スペイン', 
          'ド イツ', 'フランス', 'フランス', 'イタリア', 'イギリス', 'ドイツ', 
          'スペイン', 'スペイン', 'イタリ ア', 'イギリス', 'イギリス', 'イタリア', 
          'フランス', 'イタリア', 'フランス', 'イタリア']

# 集計用の空の辞書を準備
results = {}

for country in answer:
    # 辞書のキーとして存在する場合
    if country in results:
        results[country] += 1 # results[country] = results[country] + 1
    # 辞書のキーとして存在しない場合
    else:
        results[country] = 1

for country, num in results.items():
    print(f"{country}: {num}")
        
        