import os, sys, random

# 引数が1つであることを確認
if len(sys.argv) != 2:
    print('ファイル名をひとつ指定してください')
    sys.exit()

# パスが存在するか確認し、存在すればユーザに上書きするか判断を求める
path = sys.argv[1]
if os.path.exists(path):
    if input('上書きしますか?(y/n): ') != 'y':
        sys.exit()

kujis = ['大吉', '中吉', '凶']

with open(path, 'w', encoding='shift_jis') as f:
    f.write(kujis[random.randrange(len(kujis))] + '\n')
