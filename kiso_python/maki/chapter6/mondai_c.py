# python3 mondai_c.py abc def xyz
# abc
# def
# xyz

import sys

# 引数があることを確認する
if len(sys.argv) < 2:
    print('引数を指定してください')
    sys.exit()

with open("out.txt", "w", encoding="utf_8") as f:
    for i in sys.argv:
        f.write(i + "\n")

        