from bs4 import BeautifulSoup
import os

source = os.path.join(os.path.dirname(__file__), 'fish.html')

with open(source, encoding='utf-8') as fp:
    html_str = fp.read()
    
soup = BeautifulSoup(html_str, 'html5lib')

title = soup.find('title')
print(title) 