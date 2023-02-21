import os, sys, random

if len(sys.argv) != 2:
    print("ファイル名をひとつ指定して下さい")
    sys.exit()

path = sys.argv[1]
if os.path.exists(path):
    if input("上書きしますか?(y/n): ") != "y":
        sys.exit()

kujis = ['大吉', '中吉', '凶']
with open(path, 'w', encoding='utf_8') as f:
    f.write(kujis[random.randrange(len(kujis))] + "\n")