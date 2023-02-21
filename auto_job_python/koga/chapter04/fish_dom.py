from bs4 import BeautifulSoup
import os

with open(os.path.dirname(__file__) + '/fish.html', 'r', encoding='UTF-8') as fp:
    html_str = fp.read()
    soup = BeautifulSoup(html_str, 'html5lib')
    e = soup.find('head')
    # 親要素
    print(f"親要素: {e.parent.name}")
    # 子要素の一覧 改行もテキストノードとみなされる
    # したがって、0,2,4,6はNoneが返される(nameがないから)
    for i, child in enumerate(e.children):
        print(f"{i}: {child.name}")

    # 要素名を使う
    print(f"{e.title.name}")

    child = list(e.children)[0]
    while True:
        if child == None:
            break
        print(child, end="")
        child = child.next_sibling

    print(f"2つ前の兄弟: {e.title.previous_sibling.previous_sibling}")
    print(f"2つ次の兄弟: {e.title.next_sibling.next_sibling}")
         