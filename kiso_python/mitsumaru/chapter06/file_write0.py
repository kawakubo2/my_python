import random
import os

answer = []
countries = {"イタリア": 14, "イギリス": 10, "ドイツ": 8, "スペイン": 7, "フランス": 4}
for country, num in countries.items():
    answer += [country] * num

random.shuffle(answer)

with open(os.path.dirname(__file__) + "/answer.txt", "w", encoding="UTF-8") as f:
    f.writelines([c + "\n" for c in answer])