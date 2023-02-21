import datetime
import os

with open(os.path.dirname(__file__) + '/access.log', 'a', encoding='UTF-8') as f:
    f.write(f"{datetime.datetime.now()}\n")

print('現在時刻をファイルに保存しました。')