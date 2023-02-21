from bs4 import BeautifulSoup
import os

source = os.path.join(os.path.dirname(__file__), 'fish.html')

with open(source, encoding='utf-8') as fp:
    html_str = fp.read()
soup = BeautifulSoup(html_str, 'html5lib')

for h2 in soup.find_all('h2'):
    if h2.string == 'ウナギ':
        for e in h2.next_siblings:
            if e.name == 'p':
                if e['class'][0] == 'price':
                    print(e.string)