from bs4 import BeautifulSoup
import os

with open(os.path.dirname(__file__) + "/fish.html", "r", encoding="UTF-8") as fp:
    html_str = fp.read()

    soup = BeautifulSoup(html_str, "html5lib")

    p = soup.select("div#eel > p.price")
    print(p[0].string)