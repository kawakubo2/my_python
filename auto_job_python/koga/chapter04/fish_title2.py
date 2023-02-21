from bs4 import BeautifulSoup
import os

with open(os.path.dirname(__file__) + "/fish.html", encoding="UTF-8") as fp:
    html_srt = fp.read()

soup = BeautifulSoup(html_srt, "html5lib")

title = soup.find("title")
print(title.text)
