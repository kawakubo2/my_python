# -*- coding: utf-8 -*-

class Book:
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.set_price(price)
        
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        if price < 0:
            raise ValueError('価格が負')
        self.__price = price
        
    def __eq__(self, other):
        if other is None:
            return False
        if other.title == self.title and other.author == self.author and other.price == self.price:
            return True
        else:
            return False
        
    def __str__(self):
        return "タイトル:{},作者:{},価格{}円".format(self.title, self.author, self.price)
        
    title = property(get_title)
    author = property(get_author)
    price = property(get_price, set_price)
    

# =============================================================================
# if __name__ == '__main__':
#     book1 = Book('坊っちゃん', '夏目漱石', 300)
#     book2 = Book('坊っちゃん', '夏目漱石', 300)
#     if book1 == book2:
#         print('等しい')
#     else:
#         print('等しくない')
# =============================================================================

class Bookshelf:
    def __init__(self, books):
        self.__books = books
        
    def search(self, query):
        result = []
        for book in self.__books:
            try:
                if book.title.index(query) >= 0:
                    result.append(book)
            except ValueError:
                pass
        return result
                
    def get_books(self):
        return self.__books
    
    books = property(get_books)
    
    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
    
    def print_books(self):
        for book in self.books:
            print(book)
            
if __name__ == '__main__':
    books = [
            Book('基礎Python', 'aaa', 100),
            Book('独習Python', 'bbb', 200),
            Book('独習Java', 'ccc', 300),
            Book('10日でおぼえるPython', 'aaa', 400),
            Book('はじめてのPython第2版', 'bbb', 500)
    ]
    bs = Bookshelf(books)
    bs.print_books()
    
    while True:
        sw = int(input('1.追加 2.削除 3:検索 9.終了 : '))
        if sw == 9:
            break
        if sw == 1:
            title = input('タイトル: ')
            author = input('作者: ')
            price = int(input('価格: '))
            bs.add_book(Book(title, author, price))
        elif sw == 2:
            title = input('タイトル: ')
            author = input('作者: ')
            price = int(input('価格: '))
            bs.remove_book(Book(title, author, price))
        elif sw == 3:
            query = input('検索: ')
            for b in bs.search(query):
                print(b)
        else:
            print('1,2,3,9から選択してください')
        bs.print_books()
            
