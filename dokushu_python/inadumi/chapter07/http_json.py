import requests

res = requests.get('https://wings.msn.to/tmp/books.json')
bs = res.json()

for book in bs['books']:
    print('-----------------------------------------')
    print(f"ISBN: {book['isbn']}")
    print(f"題名: {book['title']}")
    print(f"著者: {book['author']}")
    print(f"出版社: {book['published']}")
    print(f"刊行日: {book['publishDate']}")