import os

data = ["あいうえお", "かきくけこ", "さしすせそ"]

with open(os.path.dirname(__file__) + '/abc', 'w', encoding='UTF-8') as f:
    f.writelines([s + "\n" for s in data])
