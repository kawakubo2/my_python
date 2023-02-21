import datetime

file = open('./dokushu_python/inadumi/chapter07/access.log', 'a', encoding='utf-8')
file.write(f'{datetime.datetime.now()}\n')
file.close()
print('現在時刻をファイルに保存しました。')