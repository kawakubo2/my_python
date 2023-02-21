import random
def make_random_list(item_dict):
    """
    この関数は引数の辞書からキーと値を取り出し、値で指定した個数を持ったキー
    のリストを作る。
    引数:
        item_dict dictionary: 国名をキー、個数を値とした辞書

    戻り値:
        キーの個数分のリストをすべて結合し、シャッフルしたリスト
    """
    result = []
    for item, num in item_dict.items():
        result += [item] * num
    random.shuffle(result)
    return result

if __name__ == '__main__':
    answer = make_random_list({"イギリス": 6, "スペイン": 8, "ドイツ": 3,
                            "フランス": 9, "イタリア": 14})

    country_ranking_dict = {}

    for country in answer:
        if country in country_ranking_dict:
            country_ranking_dict[country] += 1
        else:
            country_ranking_dict[country] = 1
    """
    for country, num in sorted(country_ranking_dict.items(), key=lambda t: t[1], reverse=True):
        print(f"{country}: {num}")
    """    
    for country, num in sorted(country_ranking_dict.items(), key=lambda t: t[1], reverse=True):
        print(f"{country}:{num}")

        