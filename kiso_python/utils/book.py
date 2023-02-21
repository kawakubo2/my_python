class Book:
    def __init__(self, isbn, title, price):
        self.isbn = isbn
        self.title = title
        self.price = price

    def __str__(self):
        return f"isbn: {self.isbn} title: {self.title} price: {self.price}"
