from bs4 import BeautifulSoup
import os

with open(os.path.dirname(__file__) + "/fish.html", "r", encoding="UTF-8") as fp:
    html_str = fp.read()
    soup = BeautifulSoup(html_str, "html5lib")

    h2_list = soup.find_all("h2")
    for h2 in h2_list:
        print(h2.text)