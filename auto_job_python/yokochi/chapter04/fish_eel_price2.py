from bs4 import BeautifulSoup
import os

base_dir = os.path.dirname(__file__)
with open(os.path.join(base_dir, 'fish.html'), encoding='utf-8') as fp:
    html_str = fp.read()
    
soup = BeautifulSoup(html_str, 'html5lib')
p = soup.select('div#eel > p.price')
print(p[0].string)