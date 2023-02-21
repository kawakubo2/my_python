import os, sys, random

base_dir = os.path.dirname(__file__)

if len(sys.argv) != 2:
    print("ファイル名をひとつ指定してください")
    sys.exit()
    
path = os.path.join(base_dir, sys.argv[1])
if os.path.exists(path):
    if input('上書きしますか?(y/n): ') != 'y':
        sys.exit()
        
kujis = ['大吉', '中吉', '凶']
with open(path, "w", encoding="utf_8") as f:
    f.write(kujis[random.randrange(len(kujis))] + "\n")