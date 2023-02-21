from bs4 import BeautifulSoup
import os

# HTMLファイルを読む
with open(os.path.dirname(__file__) + '/fish.html', 'r', encoding='UTF-8') as fp:
    html_str = fp.read()

# Beautiful Soupのオブジェクトを作成
soup = BeautifulSoup(html_str, 'html5lib')

# title要素を探して表示
title = soup.find('title')
print(title)