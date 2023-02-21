from bs4 import BeautifulSoup
import os

source = os.path.join(os.path.dirname(__file__), 'fish.html')

with open(source, encoding='utf-8') as fp:
    html_str = fp.read()
soup = BeautifulSoup(html_str, 'html5lib')

for h2 in soup.select('#fruits h2'):
    print(f"魚名: {h2.string}")
    next = h2.next_sibling
    while next:
        if next.name == 'p':
            if next['class'][0] == 'desc':
                print(f"説明: {next.string}")
            elif next['class'][0] == 'price':
                print(f"価格: {next.string}")
        next = next.next_sibling