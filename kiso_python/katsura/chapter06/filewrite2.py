import os

weekdays = ['日曜日', '月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日']

with open(os.path.dirname(__file__) + '/days.txt', 'w', encoding='utf_8') as f:
    f.writelines([w + '\n' for w in weekdays])