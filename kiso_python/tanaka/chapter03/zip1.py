import random

weekday1 = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
weekday2 = ['日', '月', '火', '水', '木', '金', '土']

for en, ja in zip(weekday1, weekday2):
    print(f"{en}: {ja}")

lastnames = ['山田', '横山', '田中', '鈴木', '山本', '星山', '佐藤']
firstnames = ['太郎', '花子', '一郎', '次郎', '久美子', '裕子', '勝男']

random.shuffle(lastnames)
random.shuffle(lastnames)

for lastname, firstname in zip(lastnames, firstnames):
    print(f"{lastname}{firstname}")