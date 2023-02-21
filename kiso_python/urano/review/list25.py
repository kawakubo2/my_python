list25 = ['abc.py', 'bcd.java', 'cde.py', 'def.js', 'efg.py']

# 上記リストからPythonファイル(.py)だけを表示したい
for lang in list25:
    if lang[-3:] == '.py':
        print(lang)