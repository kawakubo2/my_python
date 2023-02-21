# book.py

class Book:
    def __init__(self, title, price, publisher):
        self.title = title
        self.price = price
        self.publisher = publisher
    def __str__(self):
        return f"Book class: タイトル:{self.title} 価格:{self.price} 出版社:{self.publisher}"

class Bookshelf:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def search_book_by_title(self, keyword):
        result = []
        for book in self.books:
            if keyword in book.title:
                result.append(book)
        return result

    def __str__(self):
        result = ''
        for book in self.books:
            result += str(book) + "\n"
        return result
bs = Bookshelf()
bs.add_book(Book('基礎Pyhotn', 2500, 'インプレス'))
bs.add_book(Book('明解C言語入門', 2300, 'SBクリエイティブ'))
bs.add_book(Book('独習Python', 3500, '翔泳社'))
bs.add_book(Book('JavaScript本格入門', 3200, '技術評論社'))

while True:
    sw = int(input("1.追加 2.検索 3.表示 9.終了: "))

    if sw == 9:
        break
    if sw == 1:
        title = input('タイトル: ')
        price = int(input('価格: '))
        publisher = input('出版社: ')
        bs.add_book(Book(title, price, publisher))
        print(bs)
    elif sw == 2:
        title = input('タイトル: ')
        result = bs.search_book_by_title(title)
        for book in result:
            print(book)
    elif sw == 3:
        print(bs)
    else:
        print('1～3を選択してください。')
    
