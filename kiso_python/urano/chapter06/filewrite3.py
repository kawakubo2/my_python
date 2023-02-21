import os, sys, random

if len(sys.argv) != 2:
    print('ファイルをひとつ指定してください。')
    sys.exit()

path = sys.argv[1]

if os.path.exists(os.path.dirname(__file__) + '/' + path):
    if input('上書きしますか?(y/n): ') != 'y':
        sys.exit()

kujis = ['大吉', '中吉', '凶']
with open(os.path.dirname(__file__) + '/' + path, 'w', encoding='utf_8') as f:
    f.write(kujis[random.randrange(len(kujis))] + '\n')