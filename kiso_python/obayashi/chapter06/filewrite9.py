import os, random

def get_random_list(dic):
    result = []
    for item, num in dic.items():
        result += [item] * num
    random.shuffle(result)
    return result

country_dic = { "イタリア": 13, "イギリス": 10, "ドイツ": 8, "スペイン": 7, "フランス": 4}

country_list = get_random_list(country_dic)

with open(os.path.dirname(__file__) + "/answer.txt", "w", encoding="UTF-8") as f:
    f.writelines([country + "\n" for country in country_list])

