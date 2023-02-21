class Book:
    def __init__(self, subject, author, price):
        self.__subject = subject
        self.__author = author
        self.__price = price

    def get_subject(self):
        return self.__subject

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

    subject = property(get_subject)
    author = property(get_author)
    price = property(get_price)

    def __str__(self):
        return "Book: subject={}, author={}, price={}".format(self.subject, self.author, self.price)