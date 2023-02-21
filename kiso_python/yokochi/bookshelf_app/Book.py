import os

class Book:
    def __init__(self, title, price, publisher):
        self.__title = title
        self.__price = price
        self.__publisher = publisher
        
    def get_title(self):
        return self.__title
    def get_price(self):
        return self.__price
    def get_publisher(self):
        return self.__publisher
    
    title = property(get_title)
    price = property(get_price)
    publisher = property(get_publisher)

class Bookshelf:
    def __init__(self, books):
        """
        Booksインスタンスのリストを受け取り、self.booksインスタンス変数に格納する初期化メソッド
        Args:
            books ([list]): [Bookインスタンスのリスト]
        """
        self.books = books
        
    def add(self, book):
        """
        引数で受け取ったBookインスタンスを書棚(self.books)に追加するメソッド
        Args:
            book ([Book]): [Bookインスタンス]
        """
        self.books.append(book)
    
    def remove_by_title(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
        
    def get_by_title(self, title):
        """
        引数のタイトルを持ったBookインスタンスを
        新しいリストに格納し返すメソッド
        Args:
            title ([string]): [書籍タイトル]
        Returns:
            [Book[]]: [Bookインスタンスのメソッド]
        return self.books
        """
        result = []
        for book in self.books:
            if title in book.title:
                result.append(book)
        return result

    def get_all(self):
        """
        書棚(self.books)を返すメソッド
        Returns:
            [Book[]]: [Bookインスタンスのメソッド]
        """
        return self.books

class BookViewer:
    def view_book(self, book):
        print(f"{book.title} {book.publisher} {book.price}円")
        
    def view_books(self, books):
        for book in books:
            self.view_book(book)

class BookFileService:
    def __init__(self, file_path):
        self.file_path = file_path

    def create_books(self):
        books = []
        with open(self.file_path, 'r', encoding='utf_8') as f:
            for line in f:
                item = line.rstrip("\n").split(",")
                books.append(Book(item[0], int(item[1]), item[2]))
        return books

    def save_books(self, books):
        with open(self.file_path, 'w', encoding='utf_8') as f:
            for book in books:
                f.write(f"{book.title},")
                f.write(f"{book.price},")
                f.write(f"{book.title}\n")
                
if __name__ == '__main__':

    bookservice = BookFileService(os.path.dirname(__file__) + '/books.txt')
    books = bookservice.create_books()
    
    bookshelf = Bookshelf(books)
    viewer = BookViewer()
    viewer.view_books(bookshelf.get_all())
    
    while True:
        sw = input("1.追加 2.タイトルによる削除 3.タイトルによる検索 0.終了: ")
        if sw == "0":
            sw = input("保存しますか(y/n): ")
            if sw in ('y', 'Y', 'yes', 'YES'):
                bookservice.save_books(books)
            break
        if sw == "1":
            book = Book(input("タイトル: "), int(input("価格: ")), input("出版社: "))
            bookshelf.add(book)
            viewer.view_books(bookshelf.get_all())
        elif sw == "2":
            title = input("タイトル: ")
            bookshelf.remove_by_title(title)
            viewer.view_books(bookshelf.get_all())
        elif sw == "3":
            title = input("タイトル: ")
            searched_books = bookshelf.get_by_title(title)                
            viewer.view_books(searched_books)
        else:
            print("1～3を選択してください")
            