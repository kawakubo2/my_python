def getRandomList(seeddic):
    """
    引数で受け取ったキーと値は、新しく生成するリストの要素とその個数となる
    ["バナナ": 3, "リンゴ": 2, "ブドウ": 5] --->
    ["リンゴ", "バナナ", "ブドウ", "ブドウ", "ブドウ", 
     "バナナ", "バナナ", "ブドウ", "リンゴ", "ブドウ"]
    Args:
        seeddic (dict): 新しく生成される要素の値をキー、要素数を値とした辞書
    """
    import random
    result = []
    for item, cnt in seeddic.items():
        result += [item] * cnt
    random.shuffle(result)
    return result

answer = getRandomList({"イギリス": 6, "スペイン": 8, "ドイツ": 3, "フランス": 9, "イタリア": 14})

results = {}

for country in answer:
    if country in results:
        results[country] += 1
    else:
        results[country] = 1

for country, cnt in results.items():
    print(f"{country}: {cnt}")
        