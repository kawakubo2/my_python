from book import Book

class Bookshelf:

    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def remove(self, title):
        result = None
        for book in self.books:
            if book.subject == title:
                result = book
                self.books.remove(book)
                break
        return result

    def search(self, title):
        result = []
        for book in self.books:
            if title in book.subject:
                result.append(book)

        return result

    def printBooks(self):
        for book in self.books:
            print(book)

