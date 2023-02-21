from random_util import make_random_list
import os

answers = make_random_list({"イタリア": 13, "イギリス": 10, "ドイツ": 8, "スペイン": 7, "フランス": 4})
# print(answer)

base_dir = os.path.dirname(__file__)
out_filepath = os.path.join(base_dir, "answer.txt")
with open(out_filepath, "w", encoding="utf_8") as out_f:
    out_f.writelines([line + "\r" for answer in answers])


