# -*- coding: utf-8 -*-

words = ['旅行', '桜', 'テレビ', 'NG', '岸辺', 'NG', 'ラジオ', '五月雨']

for word in words:
    if word == 'NG':
        continue
    print(word)
    
files = ['hello.py', 'first.java', 'world.py', 'foo.php']
for file in files:
    if not file.endswith('.py'):
        continue
    print(file)