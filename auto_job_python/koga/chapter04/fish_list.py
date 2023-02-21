from bs4 import BeautifulSoup
import os, csv

with open(os.path.dirname(__file__) + "/fish.html", "r", encoding="UTF-8") as fp:
    html_str = fp.read()
    soup = BeautifulSoup(html_str, "html5lib")

    res = []
    div_list = soup.select('#fishes > div')
    for div in div_list:
        fish = div.h2.text
        desc = div.select('.desc')[0].text
        price = div.select('.price')[0].text
        res.append([fish, desc, price])
print(res)

with open(os.path.dirname(__file__) + "/fish.csv", "wt", encoding="sjis") as fp:
    csv.writer(fp).writerows(res)
