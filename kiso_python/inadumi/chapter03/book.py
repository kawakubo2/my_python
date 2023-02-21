# -*- coding: utf-8 -*-

class Book:
    def __init__(self, subject, authors, price):
        self.__subject = subject
        self.__authros = authors
        self.__price = price
        
    @property
    def subject(self):
        return self.__subject
    
    @property
    def authors(self):
        return self.__authros
    
    @property
    def price(self):
        return self.__price
    
    def __str__(self):
        return 'Book [subject = {}, authors = {}, price = {}円]'\
            .format(self.subject, self.authors, self.price)